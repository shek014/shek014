"""Generate assets/languages.svg and assets/activity.svg from the GitHub GraphQL API."""
import datetime as dt
import json
import os
import urllib.request

USER = os.environ.get("GH_USER", "shek014")
TOKEN = os.environ["GH_TOKEN"]
ACCENT = "#C0504D"
MUTED = "#8b949e"
FONT = "-apple-system,BlinkMacSystemFont,Segoe UI,Helvetica,Arial,sans-serif"
SKIP = {"Jupyter Notebook", "TEX", "Batchfile", "Shell", "PowerShell"}
COLORS = ["#C0504D", "#D9826F", "#E8B4A0", "#8C6B66", "#5E4A47", "#B7A9A6", "#6E7681", "#A5ADB8"]


def gql(query, **variables):
    req = urllib.request.Request(
        "https://api.github.com/graphql",
        data=json.dumps({"query": query, "variables": variables}).encode(),
        headers={"Authorization": f"bearer {TOKEN}", "Content-Type": "application/json"},
    )
    with urllib.request.urlopen(req) as r:
        out = json.load(r)
    if "errors" in out:
        raise SystemExit(out["errors"])
    return out["data"]


def languages():
    data = gql("""query($u:String!){user(login:$u){repositories(first:100,ownerAffiliations:OWNER,isFork:false){
      nodes{languages(first:10,orderBy:{field:SIZE,direction:DESC}){edges{size node{name}}}}}}}""", u=USER)
    totals = {}
    for repo in data["user"]["repositories"]["nodes"]:
        for e in repo["languages"]["edges"]:
            name = e["node"]["name"]
            if name not in SKIP:
                totals[name] = totals.get(name, 0) + e["size"]
    top = sorted(totals.items(), key=lambda kv: -kv[1])[:6]
    total = sum(s for _, s in top) or 1
    return [(n, s / total) for n, s in top]


def activity():
    data = gql("""query($u:String!){user(login:$u){contributionsCollection{contributionCalendar{
      weeks{contributionDays{contributionCount date}}}}}}""", u=USER)
    weeks = data["user"]["contributionsCollection"]["contributionCalendar"]["weeks"]
    return [(w["contributionDays"][0]["date"], sum(d["contributionCount"] for d in w["contributionDays"])) for w in weeks]


def languages_svg(langs, w=840):
    h = 64 + 28 * ((len(langs) + 2) // 3)
    parts, x = [], 0.0
    for i, (_, frac) in enumerate(langs):
        bw = frac * w
        parts.append(f'<rect x="{x:.1f}" y="0" width="{max(bw - 2, 1):.1f}" height="10" fill="{COLORS[i]}"/>')
        x += bw
    for i, (name, frac) in enumerate(langs):
        cx, cy = (i % 3) * (w / 3), 44 + (i // 3) * 28
        parts.append(f'<circle cx="{cx + 5}" cy="{cy - 4}" r="5" fill="{COLORS[i]}"/>'
                     f'<text x="{cx + 18}" y="{cy}" fill="{MUTED}" font-size="14">{name} <tspan opacity=".7">{frac * 100:.1f}%</tspan></text>')
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="100%" font-family="{FONT}">'
            f'<clipPath id="c"><rect width="{w}" height="10" rx="5"/></clipPath><g clip-path="url(#c)">{parts[0] if parts else ""}'
            + "".join(parts[1:len(langs)]) + "</g>" + "".join(parts[len(langs):]) + "</svg>")


def activity_svg(weeks, w=840, h=180):
    pad_l, pad_b, top = 28, 26, 10
    peak = max((c for _, c in weeks), default=0) or 1
    n = len(weeks)
    step = (w - pad_l) / max(n, 1)
    ch = h - pad_b - top
    bars, pts, labels = [], [], []
    for i, (date, c) in enumerate(weeks):
        x = pad_l + i * step
        bh = c / peak * ch
        bars.append(f'<rect x="{x + 1:.1f}" y="{top + ch - bh:.1f}" width="{max(step - 2, 1):.1f}" height="{bh:.1f}" fill="{ACCENT}" opacity=".35" rx="1"/>')
        pts.append(f"{x + step / 2:.1f},{top + ch - bh:.1f}")
        d = dt.date.fromisoformat(date)
        if d.day <= 7:
            labels.append(f'<text x="{x:.1f}" y="{h - 8}" fill="{MUTED}" font-size="11">{d.strftime("%b")}</text>')
    grid = "".join(f'<line x1="{pad_l}" x2="{w}" y1="{top + ch * f:.1f}" y2="{top + ch * f:.1f}" stroke="{MUTED}" stroke-opacity=".2"/>' for f in (0, .5, 1))
    total = sum(c for _, c in weeks)
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h + 22}" width="100%" font-family="{FONT}">'
            f'<text x="{pad_l}" y="14" fill="{MUTED}" font-size="13">{total} contributions in the last year</text>'
            f'<g transform="translate(0,22)">{grid}'
            f'<text x="0" y="{top + 4}" fill="{MUTED}" font-size="11">{peak}</text>'
            f'<text x="0" y="{top + ch}" fill="{MUTED}" font-size="11">0</text>'
            + "".join(bars)
            + f'<polyline points="{" ".join(pts)}" fill="none" stroke="{ACCENT}" stroke-width="2" stroke-linejoin="round"/>'
            + "".join(labels) + "</g></svg>")


if __name__ == "__main__":
    os.makedirs("assets", exist_ok=True)
    with open("assets/languages.svg", "w") as f:
        f.write(languages_svg(languages()))
    with open("assets/activity.svg", "w") as f:
        f.write(activity_svg(activity()))
