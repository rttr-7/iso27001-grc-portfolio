"""Build the interactive dashboard from the case-study data.

Reads the Statement of Applicability CSV and the formal ISMS documents
(00-09 Markdown files), injects them into dashboard/template.html, and writes
the finished site to docs/index.html, which GitHub Pages serves.

Usage:
  python3 dashboard/build.py                     build docs/index.html
  python3 dashboard/build.py --body-only PATH    also write the page body alone
                                                 (for hosts that add their own <html> wrapper)
"""
import argparse
import csv
import json
import re
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
CASE = ROOT / "01-iso27001-isms-implementation"
SITE = ROOT / "docs"

with open(CASE / "data" / "statement-of-applicability.csv", newline="") as f:
    rows = list(csv.reader(f))[1:]
assert len(rows) == 93, f"expected 93 Annex A controls, found {len(rows)}"

# Short titles and clause references for the document list
SHORT = {
    "00-case-study-brief": ("Case study brief", "Problem statement, objectives, approach and results"),
    "01-company-profile": ("Company profile", "Organization and ISMS governance"),
    "02-implementation-roadmap": ("Implementation roadmap", "Program plan · all clauses"),
    "03-isms-scope": ("ISMS scope", "Clause 4.3"),
    "04-context-and-interested-parties": ("Context and interested parties", "Clauses 4.1, 4.2"),
    "05-risk-assessment-methodology": ("Risk assessment methodology", "Clause 6.1.2"),
    "06-risk-register-and-treatment-plan": ("Risk register and treatment plan", "Clauses 6.1.3, 8.2, 8.3"),
    "07-statement-of-applicability": ("Statement of Applicability", "Clause 6.1.3 d · Annex A"),
    "08-internal-audit-checklist": ("Internal audit checklist and report", "Clause 9.2"),
    "09-management-review-report": ("Management review report", "Clause 9.3"),
}
docs = []
for path in sorted(CASE.glob("0[0-9]-*.md")):
    md = path.read_text()
    first = next((l for l in md.splitlines() if l.startswith("# ")), path.stem)
    title = re.sub(r"^#\s*\d+\s*-\s*", "", first).strip("# ").strip()
    short, clause = SHORT.get(path.stem, (title, ""))
    docs.append({"id": path.stem, "num": path.stem[:2], "title": title, "short": short, "clause": clause, "md": md})
assert len(docs) == 10, f"expected 10 documents, found {len(docs)}"


def js(value):
    # Keep "</" out of the inline script so document text can never close the tag
    return json.dumps(value, ensure_ascii=False).replace("</", "<\\/")


parser = argparse.ArgumentParser()
parser.add_argument("--body-only", type=Path, help="also write the page without its <html> wrapper to this path")
args = parser.parse_args()

body = (HERE / "template.html").read_text().replace("__SOA_DATA__", js(rows)).replace("__DOCS_DATA__", js(docs))
head, rest = body.split("</style>", 1)
SITE.mkdir(exist_ok=True)
(SITE / "index.html").write_text(
    '<!doctype html>\n<html lang="en">\n<head>\n<meta charset="utf-8">\n'
    '<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">\n'
    "<style>[hidden]{display:none!important} body{margin:0} img{max-width:100%}</style>\n"
    + head + "</style>\n</head>\n<body>\n" + rest + "\n</body>\n</html>\n"
)
if args.body_only:
    args.body_only.write_text(body)
print(f"Built docs/index.html with {len(rows)} controls and {len(docs)} documents")
