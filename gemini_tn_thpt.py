#!/usr/bin/env python3
"""
Thực nghiệm giải đề thi TN THPT môn Toán bằng Gemini (Chương 3 – ĐACN).

Quy trình: PDF chuẩn -> LaTeX/JSON (convert) -> kiểm định thủ công -> gửi prompt từng câu (solve)
           -> chấm điểm, thống kê theo câu / dạng bài / đề / mạch kiến thức + vẽ biểu đồ (score).

Cài đặt:   pip install google-genai pymupdf matplotlib
API key:   lấy miễn phí tại https://aistudio.google.com/apikey rồi
           Windows (PowerShell):  $env:GEMINI_API_KEY="..."      Linux/macOS:  export GEMINI_API_KEY=...

Cấu trúc thư mục (tạo sẵn bên cạnh file này):
  de_thi/<MA>.pdf      file PDF chuẩn của đề (MA = D25-MH, D25-G1..G4, D26-G1..G4)
  data/<MA>.json       đề đã chuyển sang LaTeX/JSON (do lệnh convert tạo, NHÓM PHẢI KIỂM TRA LẠI)
  dap_an/<MA>.json     đáp án chính thức (nhóm tự nhập, KHÔNG gửi cho mô hình)
  responses/<MA>.jsonl phản hồi gốc của Gemini (do lệnh solve tạo)
  ket_qua/             bảng số liệu + biểu đồ (do lệnh score tạo)
  nhan_loi.csv         (tùy chọn) nhãn lỗi E1–E9 cho các câu sai, nhóm tự điền

Lệnh:
  python gemini_tn_thpt.py convert D25-G1          # chuyển 1 đề PDF -> data/D25-G1.json
  python gemini_tn_thpt.py template D25-G1         # tạo file đáp án trống dap_an/D25-G1.json
  python gemini_tn_thpt.py solve D25-G1            # cho Gemini giải từng câu (chạy lại sẽ bỏ qua câu đã có)
  python gemini_tn_thpt.py solve all               # giải lần lượt cả 9 đề
  python gemini_tn_thpt.py score                   # chấm + xuất ket_qua/
"""
import argparse, csv, json, os, re, sys, time
from datetime import datetime
from decimal import Decimal, InvalidOperation
from pathlib import Path

ROOT = Path(__file__).resolve().parent
EXAMS = ["D25-MH", "D25-G1", "D25-G2", "D25-G3", "D25-G4", "D26-G1", "D26-G2", "D26-G3", "D26-G4"]
QIDS = [f"I.{i}" for i in range(1, 13)] + [f"II.{i}" for i in range(1, 5)] + [f"III.{i}" for i in range(1, 7)]
FORMAT_OF = {"I": "mcq", "II": "tf", "III": "short"}
TOPICS = {"dai_so_giai_tich": "Đại số và Giải tích", "hinh_hoc_do_luong": "Hình học và Đo lường",
          "thong_ke_xac_suat": "Thống kê và Xác suất"}
TF_POINTS = {0: Decimal("0"), 1: Decimal("0.1"), 2: Decimal("0.25"), 3: Decimal("0.5"), 4: Decimal("1")}
PROMPT_VERSION = "P1.0"  # mã phiên bản prompt (mục 1.2.3); đổi khi sửa prompt
DEFAULT_MODEL = os.environ.get("GEMINI_MODEL", "gemini-flash-latest")

# ----------------------------------------------------------------- prompt (mục 3.1.4)
SYSTEM_PROMPT = (
    "Bạn là trợ lý giải toán THPT. Chỉ sử dụng dữ kiện được cung cấp trong đề. Không tự bổ sung số liệu "
    "hoặc giả thiết. Kiểm tra điều kiện xác định, đơn vị và yêu cầu làm tròn. Nếu dữ kiện hoặc hình ảnh "
    "không đủ rõ, hãy ghi nhận tình trạng đó. Trả kết quả dưới dạng JSON gồm hai trường \"answer\" và "
    "\"solution_summary\"."
)
RULES = {
    "mcq": 'Đây là câu trắc nghiệm nhiều lựa chọn. Chọn đúng một phương án trong A, B, C, D. '
           'Trường "answer" là một chữ cái: "A", "B", "C" hoặc "D".',
    "tf": 'Đây là câu trắc nghiệm Đúng/Sai gồm bốn mệnh đề a, b, c, d. Xét lần lượt từng mệnh đề và kết luận độc lập. '
          'Trường "answer" là object {"a": true/false, "b": true/false, "c": true/false, "d": true/false}.',
    "short": 'Đây là câu trả lời ngắn. Đáp án là một số, tối đa 4 ký tự (kể cả dấu "-" và dấu ","), '
             'làm tròn theo yêu cầu của đề. Trường "answer" là chuỗi số, ví dụ "12,5".',
}

CONVERT_PROMPT = """Chép lại CHÍNH XÁC đề thi Toán trong file PDF đính kèm sang JSON. KHÔNG giải, KHÔNG thêm đáp án.
Trả về một JSON array gồm đúng 22 phần tử theo thứ tự đề, mỗi phần tử có dạng:
{
 "id": "I.1".."I.12" | "II.1".."II.4" | "III.1".."III.6",
 "part": "I" | "II" | "III",
 "content_latex": "phần dẫn/đề bài, mọi công thức viết bằng LaTeX trong $...$",
 "options": {"A": "...", "B": "...", "C": "...", "D": "..."}   (chỉ Phần I, các phần khác để null),
 "statements": {"a": "...", "b": "...", "c": "...", "d": "..."} (chỉ Phần II, các phần khác để null),
 "has_figure": true/false   (câu có hình vẽ, đồ thị, bảng biến thiên hay không),
 "page": số trang PDF (bắt đầu từ 1) chứa hình của câu, null nếu không có hình,
 "topic": "dai_so_giai_tich" | "hinh_hoc_do_luong" | "thong_ke_xac_suat"
}
Bảng (không phải hình) thì chép bằng LaTeX tabular hoặc Markdown. Giữ nguyên dấu phẩy thập phân, đơn vị và yêu cầu làm tròn."""


def client():
    try:
        from google import genai
    except ImportError:
        sys.exit("Thiếu thư viện: pip install google-genai pymupdf matplotlib")
    if not os.environ.get("GEMINI_API_KEY") and not os.environ.get("GOOGLE_API_KEY"):
        sys.exit("Chưa đặt biến môi trường GEMINI_API_KEY (lấy tại https://aistudio.google.com/apikey).")
    return genai.Client()


def call(cl, model, contents, system=None, retries=4, wait=20):
    from google.genai import types
    cfg = types.GenerateContentConfig(system_instruction=system, response_mime_type="application/json")
    for attempt in range(retries + 1):
        try:
            return cl.models.generate_content(model=model, contents=contents, config=cfg)
        except Exception as e:  # lỗi mạng / giới hạn tần suất -> thử lại (mục 2.2.3)
            if attempt == retries:
                raise
            print(f"   lỗi API ({str(e)[:120]}), thử lại sau {wait * (attempt + 1)} giây...")
            time.sleep(wait * (attempt + 1))


def parse_json(text):
    text = (text or "").strip()
    text = re.sub(r"^```(?:json)?\s*|\s*```$", "", text)
    return json.loads(text)


# ----------------------------------------------------------------- convert: PDF -> JSON
def cmd_convert(a):
    pdf = ROOT / "de_thi" / f"{a.exam}.pdf"
    if not pdf.exists():
        sys.exit(f"Không thấy {pdf}")
    cl = client()
    print(f"Tải {pdf.name} lên Gemini và chuyển sang LaTeX/JSON...")
    f = cl.files.upload(file=str(pdf))
    resp = call(cl, a.model, [f, CONVERT_PROMPT])
    items = parse_json(resp.text)
    ids = [q.get("id") for q in items]
    if ids != QIDS:
        print(f"!! CẢNH BÁO: danh sách câu không khớp 22 câu chuẩn: {ids}")
    for q in items:
        q["format"] = FORMAT_OF.get(q.get("part"), "?")
    out = ROOT / "data" / f"{a.exam}.json"
    out.parent.mkdir(exist_ok=True)
    out.write_text(json.dumps({"exam_id": a.exam, "source_pdf": pdf.name, "verified": False, "questions": items},
                              ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"Đã ghi {out}. HÃY ĐỐI CHIẾU VỚI PDF GỐC, sửa lỗi chép đề rồi đặt \"verified\": true trước khi solve.")


def cmd_template(a):
    out = ROOT / "dap_an" / f"{a.exam}.json"
    out.parent.mkdir(exist_ok=True)
    if out.exists():
        sys.exit(f"{out} đã tồn tại.")
    tpl = {q: ("" if not q.startswith("II.") else {"a": None, "b": None, "c": None, "d": None}) for q in QIDS}
    out.write_text(json.dumps(tpl, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"Đã tạo {out}: điền A/B/C/D cho Phần I, true/false cho Phần II, số (vd \"12,5\") cho Phần III.")


# ----------------------------------------------------------------- solve: gửi prompt từng câu
def question_text(q):
    s = q["content_latex"]
    if q.get("options"):
        s += "\n" + "\n".join(f"{k}. {v}" for k, v in q["options"].items())
    if q.get("statements"):
        s += "\n" + "\n".join(f"{k}) {v}" for k, v in q["statements"].items())
    return s


def page_png(pdf, page, cache={}):
    import fitz  # pymupdf
    key = (str(pdf), page)
    if key not in cache:
        doc = fitz.open(str(pdf))
        cache[key] = doc[page - 1].get_pixmap(dpi=150).tobytes("png")
    return cache[key]


def cmd_solve(a):
    from google.genai import types
    exams = EXAMS if a.exam == "all" else [a.exam]
    cl = client()
    for ex in exams:
        dpath = ROOT / "data" / f"{ex}.json"
        if not dpath.exists():
            print(f"[{ex}] bỏ qua: chưa có {dpath.name}"); continue
        data = json.loads(dpath.read_text(encoding="utf-8"))
        if not data.get("verified") and not a.force:
            print(f"[{ex}] bỏ qua: file JSON chưa được kiểm định (verified=false). Dùng --force nếu chắc chắn."); continue
        rpath = ROOT / "responses" / f"{ex}.jsonl"
        rpath.parent.mkdir(exist_ok=True)
        done = set()
        if rpath.exists():
            done = {json.loads(l)["id"] for l in rpath.read_text(encoding="utf-8").splitlines() if l.strip()}
        pdf = ROOT / "de_thi" / f"{ex}.pdf"
        print(f"[{ex}] nạp đề: {len(data['questions'])} câu, đã có {len(done)}")
        for q in data["questions"]:
            if q["id"] in done:
                continue
            fmt = FORMAT_OF[q["part"]]
            parts = [RULES[fmt] + "\n\nĐề bài:\n" + question_text(q)]
            if q.get("has_figure") and q.get("page") and pdf.exists():
                parts.append(types.Part.from_bytes(data=page_png(pdf, int(q["page"])), mime_type="image/png"))
                parts[0] += f"\n\n(Ảnh đính kèm là trang đề chứa hình của câu {q['id']}; chỉ dùng hình của câu này.)"
            rec = {"exam": ex, "id": q["id"], "time": datetime.now().isoformat(timespec="seconds"), "model": a.model,
                   "prompt_version": PROMPT_VERSION}
            t0 = time.time()
            try:
                resp = call(cl, a.model, parts, system=SYSTEM_PROMPT)
                rec.update(raw=resp.text, model_version=getattr(resp, "model_version", None),
                           latency_s=round(time.time() - t0, 1))
                um = getattr(resp, "usage_metadata", None)
                if um:
                    rec["tokens_in"], rec["tokens_out"] = um.prompt_token_count, um.candidates_token_count
            except Exception as e:
                rec.update(raw=None, api_error=str(e)[:500])
            with rpath.open("a", encoding="utf-8") as fh:
                fh.write(json.dumps(rec, ensure_ascii=False) + "\n")
            print(f"   {q['id']:6s} xong ({rec.get('latency_s', '-')} s)")
            time.sleep(a.sleep)


# ----------------------------------------------------------------- score
def norm_mcq(x):
    s = str(x or "").strip().upper()
    if s in ("A", "B", "C", "D"):
        return s
    m = re.search(r"\b([ABCD])\b", s)
    return m.group(1) if m else None


def to_bool(v):
    if isinstance(v, bool):
        return v
    s = str(v).strip().lower()
    if s in ("true", "đúng", "dung", "đ", "d", "1", "t"):
        return True
    if s in ("false", "sai", "s", "0", "f"):
        return False
    return None


def norm_num(x):
    s = str(x if x is not None else "").strip().replace(" ", "").replace(",", ".")
    try:
        return Decimal(s)
    except InvalidOperation:
        return None


def grade(fmt, pred, key):
    """Trả về (đúng_trọn_câu, số_mệnh_đề_đúng, điểm)."""
    if fmt == "mcq":
        ok = norm_mcq(pred) is not None and norm_mcq(pred) == norm_mcq(key)
        return ok, None, Decimal("0.25") if ok else Decimal("0")
    if fmt == "short":
        p, k = norm_num(pred), norm_num(key)
        ok = p is not None and k is not None and p == k
        return ok, None, Decimal("0.5") if ok else Decimal("0")
    pred = pred if isinstance(pred, dict) else {}
    k = sum(1 for lab in "abcd" if to_bool(pred.get(lab)) is not None and to_bool(pred.get(lab)) == to_bool(key[lab]))
    return k == 4, k, TF_POINTS[k]


def vn(x, nd=1):
    return f"{x:.{nd}f}".replace(".", ",")


def md_table(header, rows):
    out = ["| " + " | ".join(header) + " |", "|" + "---|" * len(header)]
    out += ["| " + " | ".join(str(c) for c in r) + " |" for r in rows]
    return "\n".join(out)


def cmd_score(a):
    labels = {}
    lp = ROOT / "nhan_loi.csv"
    if lp.exists():
        with lp.open(encoding="utf-8-sig") as fh:
            for r in csv.DictReader(fh):
                if r.get("ma_loi"):
                    labels[(r["exam"], r["id"])] = r["ma_loi"].strip().upper()
    rows, models = [], set()
    for ex in EXAMS:
        dp, kp, rp = (ROOT / "data" / f"{ex}.json", ROOT / "dap_an" / f"{ex}.json", ROOT / "responses" / f"{ex}.jsonl")
        if not (dp.exists() and kp.exists() and rp.exists()):
            print(f"[{ex}] bỏ qua (thiếu data/dap_an/responses)"); continue
        qs = {q["id"]: q for q in json.loads(dp.read_text(encoding="utf-8"))["questions"]}
        key = json.loads(kp.read_text(encoding="utf-8"))
        resp = {}
        for l in rp.read_text(encoding="utf-8").splitlines():
            if l.strip():
                r = json.loads(l); resp[r["id"]] = r  # lấy lượt cuối nếu có trùng
        for qid in QIDS:
            q = qs.get(qid, {"part": qid.split(".")[0]})
            fmt = FORMAT_OF[qid.split(".")[0]]
            r = resp.get(qid)
            err, pred, summary = None, None, ""
            if r is None:
                err = "CHUA_CHAY"
            elif r.get("api_error") or not r.get("raw"):
                err = "E9"
            else:
                models.add(r.get("model_version") or r.get("model"))
                try:
                    obj = parse_json(r["raw"])
                    if isinstance(obj, list):
                        obj = obj[0]
                    pred, summary = obj.get("answer"), obj.get("solution_summary", "")
                except Exception:
                    err = "E8"
            ok, k, pts = grade(fmt, pred, key[qid]) if err is None else (False, 0 if fmt == "tf" else None, Decimal(0))
            if err is None and fmt == "tf" and not isinstance(pred, dict):
                err = "E8"
            rows.append(dict(exam=ex, id=qid, format=fmt, topic=q.get("topic", ""), has_figure=bool(q.get("has_figure")),
                             pred=json.dumps(pred, ensure_ascii=False), key=json.dumps(key[qid], ensure_ascii=False),
                             correct=ok, tf_k=k, points=pts,
                             ma_loi=labels.get((ex, qid), err or ""), summary=summary,
                             latency=(r or {}).get("latency_s"), tok_in=(r or {}).get("tokens_in"),
                             tok_out=(r or {}).get("tokens_out")))
    if not rows:
        sys.exit("Chưa có dữ liệu để chấm.")
    out = ROOT / "ket_qua"; out.mkdir(exist_ok=True)
    with (out / "chi_tiet_tung_cau.csv").open("w", encoding="utf-8-sig", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=list(rows[0].keys())); w.writeheader(); w.writerows(rows)
    wrong = [r for r in rows if not r["correct"]]
    if not lp.exists():
        with lp.open("w", encoding="utf-8-sig", newline="") as fh:
            w = csv.writer(fh); w.writerow(["exam", "id", "ma_loi", "ghi_chu"])
            for r in wrong:
                w.writerow([r["exam"], r["id"], r["ma_loi"], ""])
        print(f"Đã tạo {lp.name}: điền mã lỗi E1–E9 cho {len(wrong)} câu sai rồi chạy lại score.")

    exams = [e for e in EXAMS if any(r["exam"] == e for r in rows)]
    N = len(rows)
    sel = lambda **kw: [r for r in rows if all(r[k] == v for k, v in kw.items())]
    pct = lambda n, d: 100 * n / d if d else 0
    per_exam = {}
    for e in exams:
        rs = sel(exam=e)
        per_exam[e] = dict(mcq=sum(r["correct"] for r in rs if r["format"] == "mcq"),
                           tfk=sum(r["tf_k"] or 0 for r in rs if r["format"] == "tf"),
                           tf=sum(r["correct"] for r in rs if r["format"] == "tf"),
                           sa=sum(r["correct"] for r in rs if r["format"] == "short"),
                           tot=sum(r["correct"] for r in rs), pts=float(sum(r["points"] for r in rs)))
    n_ok = sum(r["correct"] for r in rows)
    tf_rows = sel(format="tf")
    tfk = sum(r["tf_k"] or 0 for r in tf_rows)
    scores = {e: v["pts"] for e, v in per_exam.items()}
    best, worst = max(scores, key=scores.get), min(scores, key=scores.get)
    md = [f"# Kết quả thực nghiệm Gemini – {datetime.now():%d/%m/%Y %H:%M}",
          f"Mô hình ghi nhận trong phản hồi: {', '.join(sorted(m for m in models if m)) or '?'}", ""]
    md += ["## Bảng 3.14. Kết quả tổng hợp", md_table(["Chỉ số", "Kết quả"], [
        ["Số câu đúng / tổng số câu", f"{n_ok} / {N}"],
        ["Tỷ lệ đúng trên tổng số câu (3.1)", f"{vn(pct(n_ok, N))} %"],
        ["Số mệnh đề Đúng/Sai xác định đúng", f"{tfk} / {4 * len(tf_rows)}"],
        ["Điểm trung bình (thang 10)", vn(sum(scores.values()) / len(scores), 2)],
        ["Điểm cao nhất (mã đề)", f"{vn(scores[best], 2)} ({best})"],
        ["Điểm thấp nhất (mã đề)", f"{vn(scores[worst], 2)} ({worst})"],
        ["Số phản hồi lỗi định dạng hoặc kỹ thuật (E8, E9)", sum(r["ma_loi"] in ("E8", "E9") for r in rows)],
    ]), ""]
    ne = len(exams)
    fmt_rows = []
    by_fmt = {}
    for name, fmt, maxp in [("Nhiều lựa chọn", "mcq", "3,0"), ("Đúng/Sai (trọn câu)", "tf", "4,0"), ("Trả lời ngắn", "short", "3,0")]:
        rs = sel(format=fmt); ok = sum(r["correct"] for r in rs)
        by_fmt[name] = pct(ok, len(rs))
        fmt_rows.append([name, "câu", len(rs), ok, vn(pct(ok, len(rs))), vn(float(sum(r["points"] for r in rs)) / ne, 2), maxp])
        if fmt == "tf":
            by_fmt["Đúng/Sai (theo mệnh đề)"] = pct(tfk, 4 * len(rs))
            fmt_rows.append(["Đúng/Sai (theo mệnh đề)", "mệnh đề", 4 * len(rs), tfk, vn(pct(tfk, 4 * len(rs))), "–", "–"])
    fmt_rows.append(["Tổng (theo câu)", "câu", N, n_ok, vn(pct(n_ok, N)), vn(sum(scores.values()) / ne, 2), "10,0"])
    md += ["## Bảng 3.15. Tỷ lệ đúng theo dạng bài",
           md_table(["Dạng bài", "Đơn vị", "Tổng số", "Số đúng", "Tỷ lệ đúng (%)", "Điểm TB/đề", "Điểm tối đa/đề"], fmt_rows), ""]
    ex_rows = [[e, v["mcq"], v["tfk"], v["tf"], v["sa"], v["tot"], vn(pct(v["tot"], 22)), vn(v["pts"], 2)] for e, v in per_exam.items()]
    for lab, pre in [("TB 2025", "D25"), ("TB 2026", "D26"), ("TB 9 đề", "D")]:
        vs = [v for e, v in per_exam.items() if e.startswith(pre)]
        if vs:
            m = lambda k: sum(v[k] for v in vs) / len(vs)
            ex_rows.append([lab, vn(m("mcq")), vn(m("tfk")), vn(m("tf")), vn(m("sa")), vn(m("tot")), vn(pct(m("tot"), 22)), vn(m("pts"), 2)])
    md += ["## Bảng 3.17. Kết quả chi tiết theo từng đề", md_table(
        ["Mã dữ liệu", "Nhiều lựa chọn (/12)", "Đ/S mệnh đề (/16)", "Đ/S trọn câu (/4)", "Trả lời ngắn (/6)",
         "Tổng câu đúng (/22)", "Tỷ lệ đúng (%)", "Điểm (/10)"], ex_rows), ""]
    # Bảng 3.16: phân bố số mệnh đề đúng k trong câu Đúng/Sai
    kd = [[k, sum(1 for r in tf_rows if (r["tf_k"] or 0) == k), vn(pct(sum(1 for r in tf_rows if (r["tf_k"] or 0) == k), len(tf_rows))),
           vn(float(TF_POINTS[k]), 2)] for k in range(5)]
    md += ["## Bảng 3.16. Phân bố số mệnh đề xác định đúng trong mỗi câu Đúng/Sai",
           md_table(["Số mệnh đề đúng k", "Số câu", "Tỷ lệ (%)", "Điểm g(k)"], kd), ""]
    # Bảng 3.18: theo năm và loại đề
    yr = []
    for lab, ids in [("Đề minh họa 2025", ["D25-MH"]), ("Đề gốc 2025", ["D25-G1", "D25-G2", "D25-G3", "D25-G4"]),
                     ("Đề gốc 2026", ["D26-G1", "D26-G2", "D26-G3", "D26-G4"])]:
        vs = [per_exam[e] for e in ids if e in per_exam]
        if vs:
            p = [v["pts"] for v in vs]
            yr.append([lab, len(vs), 22 * len(vs), sum(v["tot"] for v in vs), vn(pct(sum(v["tot"] for v in vs), 22 * len(vs))),
                       vn(sum(p) / len(p), 2), vn(min(p), 2), vn(max(p), 2)])
    md += ["## Bảng 3.18. So sánh kết quả theo năm và loại đề",
           md_table(["Nhóm đề", "Số đề", "Số câu", "Số câu đúng", "Tỷ lệ đúng (%)", "Điểm TB", "Thấp nhất", "Cao nhất"], yr), ""]
    tp_rows = []
    for k, name in TOPICS.items():
        rs = sel(topic=k); ok = sum(r["correct"] for r in rs)
        tp_rows.append([name, len(rs), ok, vn(pct(ok, len(rs)))])
    tp_rows.append(["Tổng", N, n_ok, vn(pct(n_ok, N))])
    for lab, hf in [("Trong đó: câu có hình vẽ", True), ("Trong đó: câu không có hình vẽ", False)]:
        rs = sel(has_figure=hf); ok = sum(r["correct"] for r in rs)
        tp_rows.append([lab, len(rs), ok, vn(pct(ok, len(rs)))])
    md += ["## Bảng 3.19. Tỷ lệ đúng theo mạch kiến thức", md_table(["Mạch kiến thức", "Số câu", "Số đúng", "Tỷ lệ đúng (%)"], tp_rows), ""]
    # Bảng 3.20: tài nguyên
    lat = [r["latency"] for r in rows if r["latency"] is not None]
    ti = [r["tok_in"] for r in rows if r["tok_in"] is not None]
    to = [r["tok_out"] for r in rows if r["tok_out"] is not None]
    avg = lambda xs: vn(sum(xs) / len(xs)) if xs else "–"
    md += ["## Bảng 3.20. Thời gian xử lý và tài nguyên sử dụng", md_table(["Chỉ số", "Giá trị"], [
        ["Tổng số yêu cầu đã gửi", N], ["Số yêu cầu lỗi API (E9)", sum(r["ma_loi"] == "E9" for r in rows)],
        ["Thời gian phản hồi trung bình (giây/câu)", avg(lat)], ["Thời gian phản hồi lớn nhất (giây)", vn(max(lat)) if lat else "–"],
        ["Token đầu vào trung bình/câu", avg(ti)], ["Token đầu ra trung bình/câu", avg(to)],
        ["Tổng thời gian chạy 9 đề (phút)", vn(sum(lat) / 60) if lat else "–"]]), ""]
    err_names = ["Đọc dữ kiện", "Đọc hình", "Mô hình hóa", "Kiến thức", "Suy luận", "Tính toán", "Kết luận", "Đầu ra", "Kỹ thuật"]
    unl = sum(1 for r in wrong if not r["ma_loi"])
    er = [[f"E{i}", n, sum(r["ma_loi"] == f"E{i}" for r in wrong), vn(pct(sum(r["ma_loi"] == f"E{i}" for r in wrong), len(wrong)))]
          for i, n in enumerate(err_names, 1)]
    er.append(["", "Tổng", len(wrong), "100"])
    md += ["## Bảng 3.21. Phân bố nhóm lỗi chính trong các câu trả lời sai", md_table(["Mã", "Nhóm lỗi", "Số câu", "Tỷ lệ trên tổng câu sai (%)"], er)]
    fm = [("Nhiều lựa chọn", "mcq"), ("Đúng/Sai", "tf"), ("Trả lời ngắn", "short")]
    cross = [[f"E{i}"] + [sum(1 for r in wrong if r["ma_loi"] == f"E{i}" and r["format"] == f) for _, f in fm]
             + [sum(1 for r in wrong if r["ma_loi"] == f"E{i}")] for i in range(1, 10)]
    cross.append(["Tổng"] + [sum(1 for r in wrong if r["format"] == f) for _, f in fm] + [len(wrong)])
    md += ["", "## Bảng 3.22. Phân bố nhóm lỗi theo dạng bài", md_table(["Mã lỗi"] + [n for n, _ in fm] + ["Tổng"], cross)]
    # Phụ lục C: chi tiết từng câu
    fmt_vn = {"mcq": "NLC", "tf": "Đ/S", "short": "TLN"}
    tp_vn = {"dai_so_giai_tich": "ĐS-GT", "hinh_hoc_do_luong": "HH-ĐL", "thong_ke_xac_suat": "TK-XS"}
    show = lambda v: v.replace('"', "").replace("true", "Đ").replace("false", "S").replace("null", "–")
    for j, e in enumerate(exams, 1):
        md += ["", f"## Bảng C.{j}. Kết quả chi tiết từng câu – đề {e}", md_table(
            ["Câu", "Dạng", "Mạch", "Hình", "Đáp án chính thức", "Trả lời của Gemini", "Kết quả", "Điểm", "Mã lỗi"],
            [[r["id"], fmt_vn[r["format"]], tp_vn.get(r["topic"], ""), "x" if r["has_figure"] else "",
              show(r["key"]), show(r["pred"]), ("Đúng" if r["correct"] else (f"{r['tf_k']}/4" if r["format"] == "tf" else "Sai")),
              vn(float(r["points"]), 2), r["ma_loi"]] for r in sel(exam=e)])]
    if unl:
        md.append(f"\n> Còn {unl} câu sai chưa gán nhãn lỗi – điền vào nhan_loi.csv rồi chạy lại.")
    (out / "ket_qua.md").write_text("\n".join(md), encoding="utf-8")

    # ---- biểu đồ (Hình 3.2, 3.3)
    import matplotlib; matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    plt.rcParams["font.family"] = "Times New Roman" if os.name == "nt" else "DejaVu Serif"
    fig, ax = plt.subplots(figsize=(7, 3.6), dpi=200)
    names = list(by_fmt.keys()); vals = list(by_fmt.values())
    b = ax.bar(names, vals, color="#4C72B0", width=0.55)
    ax.bar_label(b, labels=[vn(v) + "%" for v in vals], padding=2, fontsize=9)
    ax.set_ylim(0, 105); ax.set_ylabel("Tỷ lệ đúng (%)"); ax.spines[["top", "right"]].set_visible(False)
    plt.xticks(fontsize=9); plt.tight_layout(); plt.savefig(out / "fig_3_2_theo_dang.png"); plt.close()
    fig, ax1 = plt.subplots(figsize=(7.5, 3.6), dpi=200)
    xs = list(per_exam.keys())
    b = ax1.bar(xs, [pct(v["tot"], 22) for v in per_exam.values()], color="#4C72B0", width=0.55, label="Tỷ lệ đúng (%)")
    ax1.set_ylim(0, 105); ax1.set_ylabel("Tỷ lệ đúng (%)"); ax1.spines[["top"]].set_visible(False)
    ax2 = ax1.twinx(); ax2.plot(xs, [v["pts"] for v in per_exam.values()], "o-", color="#DD8452", label="Điểm (/10)")
    ax2.set_ylim(0, 10.5); ax2.set_ylabel("Điểm (thang 10)"); ax2.spines[["top"]].set_visible(False)
    fig.legend(loc="lower center", ncol=2, fontsize=9, frameon=False, bbox_to_anchor=(0.5, -0.02))
    plt.xticks(fontsize=9); plt.tight_layout(rect=(0, 0.06, 1, 1)); plt.savefig(out / "fig_3_4_theo_de.png"); plt.close()
    fig, ax = plt.subplots(figsize=(6.5, 3.4), dpi=200)
    b = ax.bar([str(r[0]) for r in kd], [r[1] for r in kd], color="#4C72B0", width=0.55)
    ax.bar_label(b, padding=2, fontsize=9); ax.set_xlabel("Số mệnh đề xác định đúng trong câu (k)"); ax.set_ylabel("Số câu")
    ax.spines[["top", "right"]].set_visible(False); plt.tight_layout(); plt.savefig(out / "fig_3_3_phan_bo_dung_sai.png"); plt.close()
    fig, ax = plt.subplots(figsize=(6.5, 3.4), dpi=200)
    ev = [sum(1 for r in wrong if r["ma_loi"] == f"E{i}") for i in range(1, 10)]
    b = ax.bar([f"E{i}" for i in range(1, 10)], ev, color="#C44E52", width=0.55)
    ax.bar_label(b, padding=2, fontsize=9); ax.set_ylabel("Số câu sai"); ax.spines[["top", "right"]].set_visible(False)
    plt.tight_layout(); plt.savefig(out / "fig_3_5_nhom_loi.png"); plt.close()
    print(f"Xong. Xem {out / 'ket_qua.md'} và 2 biểu đồ trong {out}.")


def main():
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--model", default=DEFAULT_MODEL, help=f"mã mô hình Gemini (mặc định {DEFAULT_MODEL})")
    sp = p.add_subparsers(dest="cmd", required=True)
    s = sp.add_parser("convert"); s.add_argument("exam", choices=EXAMS); s.set_defaults(f=cmd_convert)
    s = sp.add_parser("template"); s.add_argument("exam", choices=EXAMS); s.set_defaults(f=cmd_template)
    s = sp.add_parser("solve"); s.add_argument("exam", choices=EXAMS + ["all"])
    s.add_argument("--sleep", type=float, default=6.0, help="nghỉ giữa 2 câu (giây) để không vượt hạn mức gói miễn phí")
    s.add_argument("--force", action="store_true"); s.set_defaults(f=cmd_solve)
    s = sp.add_parser("score"); s.set_defaults(f=cmd_score)
    a = p.parse_args(); a.f(a)


if __name__ == "__main__":
    main()
