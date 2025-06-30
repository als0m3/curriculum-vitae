"""Build the public profile using only the Python standard library."""
import json
from html import escape
from pathlib import Path
from urllib.parse import urlsplit

ROOT = Path(__file__).resolve().parents[1]

def link(url, label):
    if urlsplit(url).scheme not in {"https", "http"}:
        raise ValueError("Profile links must use HTTP or HTTPS")
    return f'<a href="{escape(url, quote=True)}">{escape(label)}</a>'

def render(data):
    basics = data["basics"]
    links = " · ".join(link(p["url"], p["network"]) for p in basics.get("profiles", []))
    projects = "".join(f'<article><h3>{link(p["url"], p["name"])}</h3><p>{escape(p["description"])}</p></article>' for p in data.get("projects", []))
    skills = "".join(f'<li><strong>{escape(s["name"])}</strong> — {escape(", ".join(s["keywords"]))}</li>' for s in data.get("skills", []))
    return """<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>""" + escape(basics["name"]) + """ · Technical profile</title>
<meta name="description" content=""" + '"' + escape(basics["summary"], quote=True) + '"' + """>
<style>
:root{color-scheme:light dark;font-family:system-ui,sans-serif;line-height:1.65;background:#0d1725;color:#e6edf7}
body{max-width:850px;margin:0 auto;padding:64px 24px}header{border-bottom:1px solid #34465c;padding-bottom:32px}h1{font-size:clamp(2.4rem,6vw,4rem);letter-spacing:-.05em;line-height:1.1;margin:16px 0}h2{margin-top:48px;font-size:1.35rem}h3{margin:0;font-size:1.15rem}p{max-width:68ch}a{color:#7dd3fc;text-underline-offset:4px}a:hover{color:#fff}.label{color:#b7c9e0}.eyebrow{text-transform:uppercase;letter-spacing:.15em;font-size:.8rem;color:#5eead4}article{padding:24px;border:1px solid #34465c;border-radius:12px;margin:16px 0}article p{margin-bottom:0}ul{padding-left:20px}li{margin:12px 0}footer{border-top:1px solid #34465c;margin-top:48px;padding-top:24px;font-size:.9rem;color:#b7c9e0}
@media print{:root{color-scheme:light;background:white;color:#111}body{padding:0;font-size:11pt}a{color:#164e63}article{break-inside:avoid}h1{font-size:30pt}h2{margin-top:24px}.eyebrow,.label,footer{color:#334155}}
</style></head><body><header><div class="eyebrow">Build · Automate · Share</div><h1>""" + escape(basics["name"]) + """</h1><p class="label">""" + escape(basics["label"]) + """</p><p>""" + escape(basics["summary"]) + """</p><nav aria-label="Social profiles">""" + links + """</nav></header><main><h2>Selected projects</h2>""" + projects + """<h2>Toolkit</h2><ul>""" + skills + """</ul><h2>Let's talk</h2><p>Technical conversations and collaboration welcome. Échanges bienvenus en français ou en anglais.</p><p>""" + escape(basics["email"]) + """</p></main><footer>Use your browser's Print → Save as PDF for a printable copy.</footer></body></html>
"""

if __name__ == "__main__":
    target = ROOT / "docs"
    target.mkdir(exist_ok=True)
    (target / "index.html").write_text(render(json.loads((ROOT / "resume.json").read_text())), encoding="utf-8")
    (target / ".nojekyll").touch()
