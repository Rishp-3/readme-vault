#!/usr/bin/env python3
"""build.py - deterministic generator for the whole github-profile-designs repo.

Produces, for each of the 20 designs:
  designs/NN-slug/assets/*.svg        (template, placeholder text)
  designs/NN-slug/demo/README.md      (Rishp-3 personalised)
  designs/NN-slug/demo/assets/*.svg   (filled with Rishp-3 data)
  designs/NN-slug/README.md, setup.md, svg-prompt.md, colors.md, variants/, workflow/
  designs/NN-slug/preview.png         (banner + about card render, 1200px wide)
Plus shared/, docs/ (incl. gallery.png), root README.md and helper files.

Usage: python3 build.py [--only NN] [--no-png]
"""
import argparse
import json
import math
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)

import design_defs as DD  # noqa: E402
import svg_builders_a as A  # noqa: E402
import svg_builders_b as B  # noqa: E402
from svgkit import STACK_ICONS, SOCIAL_ICONS  # noqa: E402

DATA_PATH = os.path.join(HERE, "data", "rishp-3.json")
with open(DATA_PATH, encoding="utf-8") as f:
    DATA = json.load(f)

BUILDER = {**{f"d{d['num']}": getattr(A, f"d{d['num']}") for d in DD.DESIGNS[:11]},
           **{f"d{d['num']}": getattr(B, f"d{d['num']}") for d in DD.DESIGNS[11:]}}

# ---------------------------------------------------------------- context
def base_ctx(design):
    return dict(
        palette=design["palette"],
        name="YOUR_NAME", role="YOUR_ROLE", tagline="YOUR_TAGLINE",
        status="YOUR_STATUS", username="YOUR_USERNAME", username_l="your-username",
        initial="Y", initial2="YN", initials="YOUR_INITIALS", pill="Open to collaborate", loc_line="YOUR_LOCATION",
        open_to="open to collaborations", os="Linux", role_short="YOUR_ROLE",
        stack_inline="A · B · C",
        stack_icons=STACK_ICONS,
        stack_labels=["HTML", "CSS", "JS", "React", "Tailwind", "Bootstrap", "Node", "Git",
                      "GitHub", "Netlify", "C", "Java"],
        stack_ext=["index.html", "style.css", "app.js", "App.jsx", "tw.config.js",
                   "ui.css", "server.js", ".gitconfig"],
        stack_arr="React, JavaScript, Tailwind",
        phrases=["Hi, I'm YOUR_NAME", "YOUR_ROLE", "React · Tailwind · JavaScript",
                 "Open to collaborations"],
        sub="self-taught · building for the web",
        about_lines=["> YOUR_ROLE", "> YOUR_STACK_1 · YOUR_STACK_2", "> open to collaborate"],
        footer="thanks for visiting", section="Featured Projects",
        facts=["YOUR_SKILL_1", "YOUR_SKILL_2", "Open to work"],
        value="YOUR_VALUE_STATEMENT", value_short="YOUR_VALUE_SHORT",
        contact_line="YOUR_CONTACT",
        skill_groups=[("FRONTEND", ["YOUR_STACK_1", "YOUR_STACK_2", "YOUR_STACK_3"]),
                      ("BACKEND", ["YOUR_STACK_4", "YOUR_STACK_5"]),
                      ("TOOLS", ["YOUR_TOOL_1", "YOUR_TOOL_2"])],
    )


def demo_ctx(design):
    c = base_ctx(design)
    stack3 = DATA.get("stack", [])  # Issue 5: person's stack, never top_languages
    initials = "".join(w[:1] for w in DATA["name"].split()[:2]).upper() or "Y"
    c.update(
        name=DATA["name"], role=DATA["role"], tagline=DATA["tagline"],
        status=DATA["status"], username=DATA["login"], username_l=DATA["login"].lower(),
        initial=DATA["name"][:1].upper(), initial2="R3", initials=initials,
        loc_line="Arch Linux", open_to="open to collaborations & open source",
        os=DATA["os"], role_short="Frontend Dev",
        stack_inline="React · JS · Tailwind",
        stack_arr=", ".join(f'"{s}"' for s in stack3[:3]),
        phrases=["Hi, I'm Rishabh", "Frontend Developer", "React · Tailwind · JavaScript",
                 "Open to collaborations"],
        sub="self-taught since 2023 · goal: full stack",
        about_lines=["> frontend developer", "> react · tailwind · js", "> open to collaborate"],
        footer="built with SVG · thanks for scrolling",
        facts=["React", "Responsive UI", "Open to work"],
        value="Self-taught frontend developer building clean, responsive UIs with React.",
        value_short="Self-taught · React focus · coding since 2023",
        contact_line="github.com/Rishp-3",
        skill_groups=[("FRONTEND", ["React", "Tailwind CSS", "JavaScript", "HTML5 / CSS3"]),
                      ("BACKEND", ["Node.js", "Express.js"]),
                      ("TOOLS", ["Git", "GitHub", "Netlify"])],
    )
    return c


def build_files(design, ctx):
    fn = BUILDER[f"d{design['num']}"]
    return fn(ctx)


# ---------------------------------------------------------------- READMEs
STATS_BASE = "https://github-readme-stats.vercel.app/api"
STREAK = "https://github-readme-streak-stats.herokuapp.com"


def featured_repo_rows(user, theme):
    rows = []
    for r in DATA["featured_repos"]:
        rows.append(f'<img src="{STATS_BASE}/pin/?username={user}&repo={r}&show_owner=true&{theme}" width="400" alt="{r} pinned repo card"/>')
    return "\n".join(rows)


def stats_row(user, theme, extra=""):
    return (f'<img src="{STATS_BASE}?username={user}&hide_border=true&count_private=true&{theme}" width="400" alt="GitHub stats"/>\n'
            f'<img src="{STATS_BASE}/top-langs/?username={user}&layout=compact&hide_border=true&{theme}" width="400" alt="Top languages"/>\n'
            f'{extra}'
            f'<img src="{STREAK}?username={user}&hide_border=true&{theme}" width="400" alt="GitHub streak stats"/>')


SOCIAL_LINKS = [
    ("LinkedIn", "linkedin", "/in/rishp3"),
    ("X", "x", ""),
    ("Instagram", "instagram", ""),
    ("YouTube", "youtube", ""),
    ("CodePen", "codepen", ""),
    ("Medium", "medium", ""),
    ("LeetCode", "leetcode", ""),
    ("GeeksforGeeks", "gfg", ""),
    ("Stack Overflow", "stackoverflow", ""),
]


def socials_demo():
    L = DATA["links"]
    return "\n".join([
        f'<a href="{L["linkedin"]}"><img src="https://img.shields.io/badge/LinkedIn-0A66C2?style=flat-square&logo=linkedin&logoColor=white" alt="LinkedIn"/></a>',
        f'<a href="{L["x"]}"><img src="https://img.shields.io/badge/X-111111?style=flat-square&logo=x&logoColor=white" alt="X"/></a>',
        f'<a href="{L["instagram"]}"><img src="https://img.shields.io/badge/Instagram-E4405F?style=flat-square&logo=instagram&logoColor=white" alt="Instagram"/></a>',
        f'<a href="{L["youtube"]}"><img src="https://img.shields.io/badge/YouTube-FF0000?style=flat-square&logo=youtube&logoColor=white" alt="YouTube"/></a>',
        f'<a href="{L["codepen"]}"><img src="https://img.shields.io/badge/CodePen-181717?style=flat-square&logo=codepen&logoColor=white" alt="CodePen"/></a>',
        f'<a href="{L["medium"]}"><img src="https://img.shields.io/badge/Medium-12100E?style=flat-square&logo=medium&logoColor=white" alt="Medium"/></a>',
        f'<a href="{L["leetcode"]}"><img src="https://img.shields.io/badge/LeetCode-FFA116?style=flat-square&logo=leetcode&logoColor=black" alt="LeetCode"/></a>',
        f'<a href="{L["gfg"]}"><img src="https://img.shields.io/badge/GeeksforGeeks-2F8D46?style=flat-square&logo=geeksforgeeks&logoColor=white" alt="GeeksforGeeks"/></a>',
        f'<a href="{L["stackoverflow"]}"><img src="https://img.shields.io/badge/StackOverflow-F58025?style=flat-square&logo=stackoverflow&logoColor=white" alt="Stack Overflow"/></a>',
    ])


SOCIALS_TPL = """<a href="https://linkedin.com/in/YOUR_LINKEDIN"><img src="https://img.shields.io/badge/LinkedIn-0A66C2?style=flat-square&logo=linkedin&logoColor=white" alt="LinkedIn"/></a>
<a href="https://x.com/YOUR_X"><img src="https://img.shields.io/badge/X-111111?style=flat-square&logo=x&logoColor=white" alt="X"/></a>
<a href="https://instagram.com/YOUR_INSTAGRAM"><img src="https://img.shields.io/badge/Instagram-E4405F?style=flat-square&logo=instagram&logoColor=white" alt="Instagram"/></a>
<a href="https://youtube.com/@YOUR_YOUTUBE"><img src="https://img.shields.io/badge/YouTube-FF0000?style=flat-square&logo=youtube&logoColor=white" alt="YouTube"/></a>
<a href="mailto:YOUR_EMAIL"><img src="https://img.shields.io/badge/Email-D14836?style=flat-square&logo=gmail&logoColor=white" alt="Email"/></a>"""


def per_design_readme(design, demo=False):
    num, slug = design["num"], design["slug"]
    theme = DD.stats_params(design)
    user = DATA["login"] if demo else "YOUR_USERNAME"
    assets = "assets" if demo else "assets"
    name = DATA["name"] if demo else "YOUR_NAME"
    role = DATA["role"] if demo else "YOUR_ROLE"
    tagline = DATA["tagline"] if demo else "YOUR_TAGLINE"
    status = DATA["status"] if demo else "YOUR_STATUS"
    prefix = "" if demo else ""
    L = []
    L.append('<div align="center">')
    L.append("")
    L.append(f'<img src="{prefix}assets/banner.svg" width="100%" alt="{name} profile banner"/>')
    L.append("")
    if num == "09":
        L.append("*The banner above types four lines — no JavaScript needed.*")
        L.append("")
    if num == "20":
        summary = ("Self-taught Frontend Developer specialising in React. I build clean, responsive "
                   "user interfaces and I am progressing toward full stack development." if demo
                   else "One-line professional summary: what you do, your specialisation, your goal.")
        L.append(f"### {summary}")
        L.append("")
    L.append("</div>")
    L.append("")
    # short about
    if num != "20":
        L.append("## About")
        L.append("")
        if demo:
            L.append(f"- 🔭 I'm **{role}** — {tagline.lower()}")
            L.append("- 🌱 Currently learning: **full stack development** (journey started 2023, self-taught)")
            L.append(f"- ⚡ Status: **{status}** — open to collaborations and open source")
            L.append("- 💻 Daily OS: **Arch Linux**")
        else:
            L.append("- 🔭 I'm **YOUR_ROLE** — YOUR_TAGLINE")
            L.append("- 🌱 Currently learning: YOUR_CURRENT_LEARNING")
            L.append("- ⚡ Status: YOUR_STATUS — open to collaborations")
            L.append("- 💻 Daily OS: YOUR_OS")
        L.append("")
    L.append('<div align="center">')
    L.append("")
    L.append(f'<img src="{prefix}assets/about-card.svg" width="480" alt="About me card"/>')
    L.append("")
    L.append("</div>")
    L.append("")
    if num == "02":
        L.append('<div align="center"><img src="assets/section-header.svg" width="100%" alt="Skills section header"/></div>')
        L.append("")
    L.append("## Skills")
    L.append("")
    L.append('<div align="center">')
    L.append("")
    L.append(f'<img src="{prefix}assets/skills.svg" width="100%" alt="Tech stack icons"/>')
    L.append("")
    if num == "01":
        stack = " · ".join(DATA["stack"]) if demo else "YOUR_STACK_1 · YOUR_STACK_2 · YOUR_STACK_3 · …"
        L.append(stack)
        L.append("")
    L.append("</div>")
    L.append("")
    if num == "05":
        L.append('<div align="center"><img src="assets/tabs.svg" width="100%" alt="Section tabs"/></div>')
        L.append("")
    L.append("## Featured Projects")
    L.append("")
    L.append('<div align="center">')
    L.append("")
    L.append(featured_repo_rows(user, theme))
    L.append("")
    L.append("</div>")
    L.append("")
    # design-specific extras
    if num == "10":
        L.append("## Snake")
        L.append("")
        L.append('<div align="center">')
        L.append("")
        L.append("<picture>")
        L.append('  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/{}/{}/output/github-contribution-grid-snake-dark.svg"/>'.format(user, user))
        L.append('  <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/{}/{}/output/github-contribution-grid-snake.svg"/>'.format(user, user))
        L.append('  <img alt="github contribution grid snake animation" src="https://raw.githubusercontent.com/{}/{}/output/github-contribution-grid-snake.svg"/>'.format(user, user))
        L.append("</picture>")
        L.append("")
        L.append("</div>")
        L.append("")
    if num == "08":
        L.append(f'<div align="center"><img src="{prefix}assets/wave-footer.svg" width="100%" alt="Wave footer"/></div>')
        L.append("")
    if num == "04":
        L.append(f'<div align="center"><img src="{prefix}assets/prompt-footer.svg" width="100%" alt="Terminal footer"/></div>')
        L.append("")
    if num == "05":
        L.append(f'<div align="center"><img src="{prefix}assets/status-bar.svg" width="100%" alt="Status bar footer"/></div>')
        L.append("")
    if num == "07":
        L.append(f'<div align="center"><img src="{prefix}assets/hud-frame.svg" width="480" alt="HUD frame decoration"/></div>')
        L.append("")
    # stats row
    L.append("## GitHub Stats")
    L.append("")
    L.append('<div align="center">')
    L.append("")
    summary_card = ""
    if num in ("02", "20"):
        summary_card = (f'<img src="https://github-profile-summary-cards.vercel.app/api/cards/profile-details?username={user}&theme={"github_dark" if design["themes"] != "both" else "github"}" width="600" alt="Profile summary card"/>\n\n')
    L.append(stats_row(user, theme, extra=summary_card))
    L.append("")
    L.append("</div>")
    L.append("")
    L.append(f'<div align="center"><img src="{prefix}assets/divider.svg" width="100%" alt="divider"/></div>')
    L.append("")
    L.append("## Connect")
    L.append("")
    L.append('<div align="center">')
    L.append("")
    L.append(socials_demo() if demo else SOCIALS_TPL)
    L.append("")
    L.append("</div>")
    L.append("")
    foot = (f"Design `{num}-{slug}` from **github-profile-designs** · made with self-contained SVG"
            if demo else "Footer line — e.g. \"This design is from github-profile-designs\".")
    L.append(f'<div align="center"><sub>{foot}</sub></div>')
    L.append("")
    return "\n".join(L)


# ---------------------------------------------------------------- docs md
def colors_md(design):
    p = design["palette"]
    def lum(hex_s):
        hex_s = hex_s.lstrip("#")
        if len(hex_s) == 8:
            hex_s = hex_s[:6]
        r, g, b = (int(hex_s[i:i + 2], 16) / 255 for i in (0, 2, 4))
        f = lambda v: v / 12.92 if v <= 0.03928 else ((v + 0.055) / 1.055) ** 2.4
        return 0.2126 * f(r) + 0.7152 * f(g) + 0.0722 * f(b)
    def ratio(a, b):
        la, lb = lum(a), lum(b)
        hi, lo = max(la, lb), min(la, lb)
        return (hi + 0.05) / (lo + 0.05)
    bg = p.get("bg") or p.get("bg1") or "#000000"
    txt = p.get("text") or p.get("foam") or p.get("white") or "#FFFFFF"
    r = ratio(bg, txt)
    rows = "\n".join(f"| `{v}` | {k} |" for k, v in p.items())
    dark_only = design["themes"] == "dark-only"
    note = ("\n\n**This design is dark-only.** No light variant is provided because the palette "
            "depends on a dark background for contrast and glow effects.\n" if dark_only else "")
    return (f"# Colors — {design['num']} {design['name']}\n\n"
            f"| Hex | Role |\n|---|---|\n{rows}\n\n"
            f"**Contrast:** text `{txt}` on background `{bg}` = **{r:.2f}:1** "
            f"({'passes' if r >= 4.5 else 'below'} WCAG AA 4.5:1 target).\n"
            f"{note}\n"
            f"## Ready-to-paste stats-card parameters\n\n```\n{DD.stats_params(design)}\n```\n\n"
            f"Paste after any `github-readme-stats` / `streak-stats` URL, e.g.\n\n```\n"
            f"https://github-readme-stats.vercel.app/api?username=YOUR_USERNAME&{DD.stats_params(design)}\n```\n")


def setup_md(design):
    num = design["num"]
    extra_steps = ""
    if num == "10":
        extra_steps = """
7. **Snake workflow**: copy `workflow/snake.yml` into `.github/workflows/snake.yml` of your profile repo.
8. Create an empty branch named `output` (`git checkout --orphan output && git commit --allow-empty -m "init" && git push origin output`).
9. Run the workflow once from Actions → "Contribute Graph Snake" → Run workflow. The snake SVGs appear in `dist/` on the `output` branch.
"""
    return f"""# Setup — {design['num']} {design['name']}

1. Create a repository named exactly `YOUR_USERNAME` (same as your GitHub account name). GitHub renders its README on your profile page.
2. Copy this folder's `README.md` and the entire `assets/` directory into that repo (keep the relative paths).
3. Replace every placeholder listed in `../../shared/placeholders.md` (`YOUR_NAME`, `YOUR_USERNAME`, `YOUR_ROLE`, `YOUR_TAGLINE`, socials, stack items).
4. Edit the SVG text directly: open the file in any editor and change the `<text>` elements —
   - `assets/banner.svg`: ids `banner-name`, `banner-role`, `banner-tagline`
   - `assets/about-card.svg`: ids `card-name`, `card-role`, `card-status`, `card-user`
   - `assets/skills.svg`: icon groups (swap `icon(...)` blocks; see `../../shared/icons/`)
5. Change colors by find-and-replacing the hex values from `colors.md` inside the SVGs.
6. Commit and push, then open `https://github.com/YOUR_USERNAME` to check the profile.
{extra_steps}
## Troubleshooting

- **Image not loading** — path typos are the usual cause; GitHub serves images from camo, which needs the exact relative path and committed files.
- **Animation not playing** — some browsers only animate SVG when opened directly; in the README it animates in Chrome/Firefox/Safari. If nothing moves, your OS "reduce motion" setting disables it (by design — every SVG respects `prefers-reduced-motion`).
- **Stale image after editing** — camo caches aggressively; append `?v=2` to the `src` or wait a few minutes.
- **Text overflow** — keep replaced names under ~14 characters at the current font size, or lower `font-size` in the `<text>` element.
"""


def svg_prompt_md(design):
    p = design["palette"]
    pal = "\n".join(f"- {k}: `{v}`" for k, v in p.items())
    extras = {"02": "- section-header.svg (1000x56): rounded card title with accent bar",
              "03": "- frame.svg (480x220): double white/black frame used around the about card",
              "04": "- prompt-footer.svg (1000x40): `$ echo \"thanks for visiting\"` prompt line",
              "05": "- status-bar.svg (1000x32): blue VS Code style status bar; tabs.svg (1000x40): three file tabs",
              "07": "- hud-frame.svg (480x220): cut-corner bracket frame overlay",
              "08": "- wave-footer.svg (1000x60): mirrored waves for the bottom of the page",
              }.get(design["num"], "- (no extra files)")
    anim_desc = ANIM_TEXT[design["num"]]
    layout = LAYOUT_TEXT[design["num"]]
    return f"""# AI prompt — recreate {design['num']} {design['name']}

Copy everything below into an AI that outputs SVG code.

---

Create SVG files for a GitHub profile README, design "{design['num']}-{design['slug']}".

**Constraints:** fully self-contained; no `<script>`, no `foreignObject`, no external fonts/images/href URLs (only xmlns); `viewBox` set plus explicit `width`/`height`; one `<title>` and one `<desc>` per file; system font stacks only (`ui-monospace, SFMono-Regular, Menlo, Consolas, monospace` and `-apple-system, "Segoe UI", Helvetica, Arial, sans-serif`); each file under 150 KB; animation via SMIL (`animate`, `animateTransform`, `animateMotion`, `set`) or CSS `@keyframes` inside `<style>` in the SVG only; include `@media (prefers-reduced-motion: reduce){{*{{animation:none !important;}}}}`; valid XML.

**Files:**
- banner.svg (1000x300)
- divider.svg (1000x24)
- about-card.svg (480x220)
- skills.svg (1000x120)
{extras}

**Palette:**
{pal}

**Typography:** headings in the sans stack, small labels/terminal text in the mono stack; banner name 40–46 px bold, tagline 15–18 px, card name 19–22 px.

**Layout:**
{layout}

**Animation:**
{anim_desc}

**Text content:** placeholders `YOUR_NAME`, `YOUR_ROLE`, `YOUR_TAGLINE`, `YOUR_STATUS`. Banner shows only name/tagline/role (no design name). No email addresses in SVG.

**Output:** only the SVG code per file, each in its own fenced block labelled with the file name.
"""


ANIM_TEXT = {
 "01": "Name fades in 0→1 over 0.8 s, tagline delayed 0.2 s, role delayed 0.4 s (CSS keyframes with staggered animation-delay). Reduced-motion off-switch included.",
 "02": "Card rises (translateY 10→0, opacity) 0.7 s ease-out once on load. Nothing else animates.",
 "03": "White 2 px scan-line rect (opacity .15) translates x −200→1200 over 6 s, linear, indefinite loop.",
 "04": "Four terminal lines revealed sequentially with clipPath rect width 0→full, 0.9 s each, starting at 0.6 s, spaced 1.1 s apart, calcMode linear, fill freeze. Block cursor blinks 1 s (discrete 0.5 duty).",
 "05": "Each code line group fades 0→1 in 0.3 s, delayed 0.4 s per line. Caret rect blinks 0.9 s discrete.",
 "06": "40 glyph columns, each a `<use>` of one of 8 predefined columns, animateTransform translate y −330→330, durations 4–9 s random, negative random begin delays, indefinite.",
 "07": "Three stacked name layers (pink/cyan/white); pink+cyan offset ±3 px constantly; glitch burst every 4 s for ~120 ms via animateTransform translate keyTimes 0.92–1. Divider dot travels 0→1000 in 2.6 s.",
 "08": "Three sine-wave bands drawn twice as wide as the canvas, animateTransform translate 0→−1000 seamless loops at 8 s, 12 s, 18 s. Divider mini-wave 6 s.",
 "09": "One `<text>` per phrase clipped by an animated rect width (0→w→w→0) within a 16 s cycle split across 4 phrases; caret rect steps x between phrase ends (discrete) and blinks 0.9 s.",
 "10": "No SVG animation required (the snake itself is a generated GIF/SVG from the Action). Grid cells static.",
 "11": "Three concentric circles animate r (+10) and opacity over 3 s, staggered 0.5 s, ease-in-out keySplines 0.42 0 0.58 1. Name glow pulses opacity 0.85→1→0.85 over 4 s. Divider pulse dot travels left→right 3 s. Skill icons scale 1→1.06→1 staggered 0.15 s.",
 "12": "Pixel stars blink with discrete opacity step animations (2–4 s, random begin). XP bar fills width 0→372 once over 2.5 s (fill=freeze). shape-rendering crispEdges everywhere.",
 "13": "Four blurred pastel blobs translate along a slow there-and-back path (10–14 s). Eight sparkles fade 0.2→1→0.2 randomly. All ease.",
 "14": "Sun group translates y +14→−14→+14 over 12 s. Three birds follow animateMotion straight paths 20–28 s with negative begins for staggering.",
 "15": "One letter of the name flickers like a faulty sign: tspan opacity discrete values 1;0.15;1;0.3;1;0.1;1 with irregular keyTimes on a 7 s loop. Card border stroke cycles cyan→green→magenta over 12 s (discrete).",
 "16": "80 stars twinkle opacity 0.3→1→0.3 over 2–5 s random. Galaxy group rotates 0→360 over 120 s. Shooting star uses animateMotion across the banner every 9 s with fading opacity. Skills icons sit on two orbit rings rotating ±360 over 60/80 s.",
 "17": "Four foam wave bands translate 0→−1000 seamlessly at 9/13/17/21 s. Ten bubbles animateMotion upward with opacity fade. Fish silhouette crosses on animateMotion 24 s. Skill bubbles bob 3 px over 3 s staggered.",
 "18": "Three pine layers sway rotate −1°→+1°→−1° about their trunk base at 5/7/9 s (parallax feel). Nine fireflies drift (small translate) and blink (irregular opacity). Mist band translates x 0→60→0 over 16 s.",
 "19": "Two/three large blurred blobs drift slowly (10–14 s) behind static glass panels. Nothing else animates — the illusion must read even frozen.",
 "20": "Single 1 s fade-in (opacity 0→1) applied to name, role, value line and chips. No looping animation.",
}

LAYOUT_TEXT = {
 "01": "Banner: name at x=60 y=130 (44 px weight 300), tagline x=60 y=172 (18 px muted), role x=60 y=204, hairline rule y=232 from x=60 to 940. Divider: centered 1 px line 60 % width. About card: avatar circle outline left (cx 70 cy 70 r 34), name/role right, status dot + text, thin rule, @username mono. Skills: 12 monochrome 40 px icons, 40 px gaps, no labels.",
 "02": "Banner: bg full-bleed, rounded 16 px card (40,60,920x180) with feDropShadow; name 34 px at 76,138, role below; accent pill 260x44 rx 22 right side. Section header: 1000x56, accent bar 6x28 at x=24, card rect behind title. About card: rounded card 448x188 with avatar ring (stroke accent 3 px). Skills: 8 tiles per row 108x46 rx 10, icon left + label.",
 "03": "Banner: black bg, inset 1 px white frame at 12 px margin, uppercase name 64 px letter-spacing 6 centered y=150, role 16 px dim y=196, scan line on top. Divider: dashed 4 6. About card: dark inner panel with double frame, initial-circle avatar, uppercase mono text. Skills: grayscale icons 88 px pitch.",
 "04": "Banner: terminal title bar 940x40 rx 8 at (30,24) with 3 traffic dots, mono title centered; 4 typed lines start x=56, y=100/140/180/220, 20 px mono; blinking block cursor after last line; CRT scanline pattern overlay 6 % opacity. About card: neofetch block — 3-line ASCII logo left column, key/value pairs right (OS/Shell/Role/Stack/Status). Skills: `$ ls ./stack` header + 8 file rows with tiny icons. Footer: prompt echo line.",
 "05": "Banner: sidebar strip top 34 px (#252526) with active tab `about.js`; line numbers gutter x≈60; 7 code lines at y=54+30·i, 15 px mono, tokens colored keyword/string/comment/number; minimap column x=930 w=70 with gray bars; status bar 32 px #569CD6 bottom. About card: package.json tab + JSON lines. Skills: explorer tree `▾ stack/` with 8 file rows. Extras: status bar, tabs.",
 "06": "Banner: pure black, 40 rain columns at 25 px pitch built from 8 reusable column defs (`<use>`), 14 glyphs each 18 px mono; center dark rounded rect 500x130 at (250,90) opacity .92 holding name 34 px + tagline 15 px. Divider: single glyph row. About card: black card, green 1 px border, mono lines `> identify --user`, name, role, [status], user_. Skills: green icons 72 px pitch.",
 "07": "Banner: vertical gradient #140A28→#0A0A1F; perspective floor: 13 converging lines + 4 horizontals near bottom (y 240–300); main cut-corner octagon panel inset 30 px; HUD labels in corners; name 46 px triple-stack centered y=150; role 16 px cyan letterspaced; tagline 13 px pink. Divider: pink neon line + glowing traveling dot. About card: cut-corner card, `// STATUS: ONLINE`, name, role, @user, `// open to …`. Skills: neon icons with duplicated blurred copy for glow.",
 "08": "Banner: bg #0F172A; three filled sine bands (amp 14/18/10, wavelengths 250/330/200, baselines 235/250/265) closing to y=300, gradient fills at 50/55/85 % opacity; name 44 px centered y=120, tagline y=158, role mono y=190. Divider: 500-wide mini wave translated seamlessly. About card: #111c33 rounded 14 with 5 px gradient top bar. Skills: gradient-outline pills auto-width. Footer: 1000x60 mirrored bands.",
 "09": "Banner: bg #0D1117; phrases 30 px mono at x=60 baseline y=160, each clipped by a rect animated in a 16 s type/hold/erase cycle; caret 12x34 follows phrase end; sub line 15 px muted y=210. Divider: dotted line + accent rect filling 0→800 once. About card: three typed lines 15 px mono in a #161B22 rounded card. Skills: static accent-colored icon row.",
 "10": "Banner: GitHub dark bg; name 40 px centered y=80, tagline mono y=112; static 52x7 contribution grid starting (20,150), 16 px cells rx 3 in five greens, six-cell blue snake sitting on the grid. Divider: one row of 52 cells. About card: #161B22 rounded card like 09. Skills: green icon row.",
 "11": "Banner: bg #0B0B1A; orb at (500,150): radial-gradient core circle r 26 blurred stdDev 12 + three pulsing rings r 34/52/72; name 34 px y=250 with feDropShadow violet glow; tagline violet y=285. Divider: faint violet line + blurred pink dot crossing every 3 s. About card: #131328 rounded 14, violet border whose stroke-opacity pulses 5 s plus blurred halo copy. Skills: icons wrapped in groups scaling 1→1.06 staggered.",
 "12": "Banner: flat #2B2D42 night sky; 26 square pixel stars (4 px); stepped pixel mountain silhouettes along the bottom (two grays); original pixel character (head/cap/body/arms rects) at a desk with monitor left third; title rendered from a 5x7 bitmap font in yellow 6 px pixels centered y=60; role subtitle 3 px pixels white. Divider: repeating pixel hearts red/yellow/green. About card: RPG dialog box double-bordered white, `PLAYER 1` yellow bitmap text, HP bar static, XP bar fills once. Skills: 64 px bordered tiles with icons + 2 px bitmap labels.",
 "13": "Banner: light pink bg; four blurred pastel blobs (stdDev 22) drifting; eight 4-point sparkles twinkling; name 40 px centered y=150 with soft lilac drop shadow; tagline y=192; role lilac y=224. Divider: three 5 px dots pink/blue/lilac centered. About card: 24 px rounded card with pastel gradient wash, dashed avatar ring. Skills: 60 px round pastel tiles alternating colors.",
 "14": "Banner: vertical gradient orange→coral→purple→deep; half sun (r 70 radial + blurred halo) rising/falling ±14 px 12 s behind hills; three hill silhouettes (paths) in darkening purples at bottom; three simple bird strokes crossing via animateMotion; name white 44 px y=120, tagline y=156. Divider: gradient horizon line + sun dot. About card: gradient bg with translucent white inner card (18 % white, 1 px white border). Skills: white icons on translucent circular pills.",
 "15": "Banner: pure dark #0A0A0A; rounded rect 18 px around name: solid cyan stroke 2 px + blurred duplicate 3 px 55 %; name 46 px white centered with middle letter in a flickering tspan; role green mono letterspaced y=226; tagline magenta y=254. Divider: cyan line with 4x12 end caps. About card: cycling-border card (stroke values cyan;green;magenta discrete 12 s) + blurred halo copy. Skills: icons with matching neon underline bars.",
 "16": "Banner: deep space #05051A; 80 stars (r 1/1.5/2.5) twinkling; spiral galaxy left-of-center: bright radial core + four rotated ellipse arms, whole group rotating 120 s; ringed planet right (indigo disc + tilted pink ring); shooting star crossing every 9 s; name 40 px weight 300 letter-spacing 4 centered y=150. Divider: faint line + 20 tiny stars. About card: #0A0A24 rounded card, star-dust dots along top/bottom edges. Skills: 12 icons on two concentric orbit rings counter-rotating 60/80 s.",
 "17": "Banner: vertical gradient light blue→deep navy; four foam wave bands (amp 10→22, speed 9→21 s) anchored to bottom; ten outlined bubbles rising with animateMotion + fade; small fish silhouette crossing leftwards 24 s; name foam-white 44 px y=100, tagline y=134. Divider: single 4 px-amplitude foam wave stroke. About card: mid-blue rounded card with animated low-opacity caustic curves. Skills: icons inside 30 px bubble circles bobbing 3 px staggered.",
 "18": "Banner: forest bg #0F3D22; moon top-right with blurred halo; three depth layers of triangle pines (far 8 trees darker/smaller, mid 7, near 5 tallest) each swaying ±1° about trunk base at different speeds; drifting blurred mist band y≈200; nine fireflies (2.5 px warm-yellow) blinking/drifting; name #DCFCE7 42 px y=100. Divider: baseline with 10 tiny tree triangles. About card: wooden-sign — brown outer rounded rect, grain curves, dark green inset with tan border. Skills: leaf-shaped tiles (rounded, one pointed corner) alternating greens.",
 "19": "Banner: diagonal indigo→sky gradient; three big blurred blobs (stdDev 30, pink + sky-blue) drifting behind; central frosted panel 700x160 rx 20: white 18 % fill + 1 px white 40 % stroke + inner top highlight gradient; name 40 px white on panel y=140, tagline y=176, role mono y=206. Divider: 400x20 glass pill. About card: gradient card with two blobs peeking under a smaller glass panel. Skills: 72x80 glass tiles in a row. Note: real backdrop blur is impossible in SVG — this imitates it.",
 "20": "Banner: white (dark: #0B1220) with 8 px navy/blue left accent stripe; name 40 px semibold x=60 y=120; role 19 px blue y=158; value statement 15 px slate y=190; three fact chips (navy fill, white text, rx 17) y=210. Divider: thin slate line x 60→940. About card: subtle gray inner card, navy initials circle avatar, name/role/value/contact. Skills: three labeled columns FRONTEND / BACKEND / TOOLS with square bullets.",
}


def variants_md(design):
    num = design["num"]
    if design["themes"] == "both":
        return None  # written separately
    return (f"# Variants\n\n`{design['num']}-{design['slug']}` is **single-theme ({design['themes']})**.\n\n"
            "The composition relies on its background (glow, neon, rain, depth) so a light variant would "
            "break contrast. Use it on both GitHub themes as-is — GitHub READMEs have no automatic theme "
            "switch unless you add a `<picture>` yourself, which is not recommended here.\n")


def light_picture_snippet(design):
    return (f'<picture>\n'
            f'  <source media="(prefers-color-scheme: dark)" srcset="assets/banner-dark.svg"/>\n'
            f'  <img alt="{design["name"]} banner" src="assets/banner.svg"/>\n'
            f'</picture>')


# ---------------------------------------------------------------- shared
def shared_icons_svg(name, color):
    from svgkit import icon
    body = icon(name, 0, 0, color=color, size=48)
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="48" height="48" viewBox="0 0 48 48" role="img">
<title>{name} icon</title><desc>Original generic {name} glyph, 48x48.</desc>
{body}
</svg>
'''


def write_shared():
    sd = os.path.join(ROOT, "shared")
    os.makedirs(os.path.join(sd, "icons"), exist_ok=True)
    os.makedirs(os.path.join(sd, "dividers"), exist_ok=True)
    allnames = sorted(set(STACK_ICONS + SOCIAL_ICONS))
    for n in allnames:
        with open(os.path.join(sd, "icons", f"{n}-mono.svg"), "w") as f:
            f.write(shared_icons_svg(n, "#8892A0"))
        with open(os.path.join(sd, "icons", f"{n}-color.svg"), "w") as f:
            f.write(shared_icons_svg(n, "#3B82F6"))
    dividers = {
        "dots.svg": '<circle cx="470" cy="12" r="3" fill="#8A8A8A"/><circle cx="500" cy="12" r="3" fill="#8A8A8A"/><circle cx="530" cy="12" r="3" fill="#8A8A8A"/>',
        "line.svg": '<line x1="200" y1="12" x2="800" y2="12" stroke="#8A8A8A" stroke-width="1"/>',
        "dashed.svg": '<line x1="100" y1="12" x2="900" y2="12" stroke="#8A8A8A" stroke-width="1" stroke-dasharray="4 6"/>',
        "wave.svg": '<path d="M250 12 q 25 -8 50 0 t 50 0 t 50 0 t 50 0 t 50 0 t 50 0 t 50 0 t 50 0 t 50 0 t 50 0" fill="none" stroke="#8A8A8A" stroke-width="2"/>',
        "gradient-bar.svg": '<defs><linearGradient id="gb" x1="0" x2="1"><stop offset="0" stop-color="#06B6D4"/><stop offset="1" stop-color="#8B5CF6"/></linearGradient></defs><rect x="300" y="9" width="400" height="6" rx="3" fill="url(#gb)"/>',
        "ascii.svg": '<text x="500" y="17" text-anchor="middle" font-family="ui-monospace, Menlo, Consolas, monospace" font-size="14" fill="#8A8A8A">- - - ✦ - - -</text>',
    }
    for fname, body in dividers.items():
        with open(os.path.join(sd, "dividers", fname), "w") as f:
            f.write(f'<svg xmlns="http://www.w3.org/2000/svg" width="1000" height="24" viewBox="0 0 1000 24" role="img"><title>Generic divider</title><desc>Reusable 1000x24 divider.</desc>{body}</svg>\n')
    with open(os.path.join(sd, "badges.md"), "w") as f:
        f.write(BADGES_MD)
    with open(os.path.join(sd, "placeholders.md"), "w") as f:
        f.write(PLACEHOLDERS_MD)


BADGES_MD = """# Copy-paste badge snippets (shields.io)

All badges use `style=flat-square` by default — swap for `flat`, `for-the-badge`, `plastic`, `social`.

## Socials

```md
[![LinkedIn](https://img.shields.io/badge/LinkedIn-0A66C2?style=flat-square&logo=linkedin&logoColor=white)](https://linkedin.com/in/YOUR_LINKEDIN)
[![X](https://img.shields.io/badge/X-111111?style=flat-square&logo=x&logoColor=white)](https://x.com/YOUR_X)
[![Instagram](https://img.shields.io/badge/Instagram-E4405F?style=flat-square&logo=instagram&logoColor=white)](https://instagram.com/YOUR_INSTAGRAM)
[![YouTube](https://img.shields.io/badge/YouTube-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://youtube.com/@YOUR_YOUTUBE)
[![CodePen](https://img.shields.io/badge/CodePen-181717?style=flat-square&logo=codepen&logoColor=white)](https://codepen.io/YOUR_USERNAME)
[![Medium](https://img.shields.io/badge/Medium-12100E?style=flat-square&logo=medium&logoColor=white)](https://medium.com/@YOUR_MEDIUM)
[![LeetCode](https://img.shields.io/badge/LeetCode-FFA116?style=flat-square&logo=leetcode&logoColor=black)](https://leetcode.com/u/YOUR_LEETCODE)
[![StackOverflow](https://img.shields.io/badge/StackOverflow-F58025?style=flat-square&logo=stackoverflow&logoColor=white)](https://stackoverflow.com/users/YOUR_SO_ID)
[![Email](https://img.shields.io/badge/Email-D14836?style=flat-square&logo=gmail&logoColor=white)](mailto:YOUR_EMAIL)
```

## Status

```md
![Online](https://img.shields.io/badge/status-online--%26--operational-39D353?style=flat-square)
![Open to work](https://img.shields.io/badge/open%20to-collaborations-2563EB?style=flat-square)
![Learning](https://img.shields.io/badge/learning-full%20stack-8B5CF6?style=flat-square)
```

## Stack

```md
![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=flat-square&logo=html5&logoColor=white)
![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=flat-square&logo=css3&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=flat-square&logo=javascript&logoColor=black)
![React](https://img.shields.io/badge/React-61DAFB?style=flat-square&logo=react&logoColor=black)
![Tailwind](https://img.shields.io/badge/Tailwind-38BDF8?style=flat-square&logo=tailwindcss&logoColor=black)
![Bootstrap](https://img.shields.io/badge/Bootstrap-7952B3?style=flat-square&logo=bootstrap&logoColor=white)
![Node.js](https://img.shields.io/badge/Node.js-339933?style=flat-square&logo=nodedotjs&logoColor=white)
![Express](https://img.shields.io/badge/Express-000000?style=flat-square&logo=express&logoColor=white)
![Git](https://img.shields.io/badge/Git-F05032?style=flat-square&logo=git&logoColor=white)
![Netlify](https://img.shields.io/badge/Netlify-00C7B7?style=flat-square&logo=netlify&logoColor=white)
![C](https://img.shields.io/badge/C-A8B9CC?style=flat-square&logo=c&logoColor=black)
![Java](https://img.shields.io/badge/Java-ED8B00?style=flat-square&logo=openjdk&logoColor=black)
![Arch](https://img.shields.io/badge/Arch%20Linux-1793D1?style=flat-square&logo=archlinux&logoColor=white)
```

Monochrome variant (design 03): append `&color=000000&labelColor=111111` to any badge URL above.
"""

PLACEHOLDERS_MD = """# Placeholder reference

Every template README/SVG uses these tokens. Replace all of them before publishing.

| Placeholder | Meaning | Example |
|---|---|---|
| `YOUR_NAME` | Display name shown in banner/card | `Rishabh` |
| `YOUR_USERNAME` | GitHub login (also the profile repo name) | `Rishp-3` |
| `YOUR_TAGLINE` | One-line hook under the name | `Building clean and responsive UIs` |
| `YOUR_ROLE` | Job title / focus | `Frontend Developer` |
| `YOUR_STATUS` | Availability line | `Online & Operational` |
| `YOUR_LOCATION` / `YOUR_OS` | Extra card line | `India` / `Arch Linux` |
| `YOUR_LINKEDIN` | LinkedIn slug | `rishp3` |
| `YOUR_X` | X handle without `@` | `rishp_3` |
| `YOUR_INSTAGRAM` | Instagram handle | `rishp_3` |
| `YOUR_YOUTUBE` | YouTube handle | `rishp3` |
| `YOUR_EMAIL` | Contact email (README text only — never in SVGs) | `you@example.com` |
| `YOUR_STACK_1..N` | Tech names in skills lists/strips | `React`, `Tailwind CSS` |
| `YOUR_TOOL_1..2` | Tooling names (design 20) | `Git`, `Netlify` |
| `YOUR_SKILL_1..2` | Fact-chip labels (design 20) | `Responsive UI` |
| `YOUR_VALUE_STATEMENT` | One-sentence recruiter summary (design 20) | `Self-taught dev focused on React` |
| `YOUR_CURRENT_LEARNING` | About bullet | `full stack development` |

Tip: run `python3 tools/replace-placeholders.py --design 05-code-editor --name "..." --username "..."` to fill a design automatically.
"""


# ---------------------------------------------------------------- previews
def render_png(svg_path, png_path, width):
    import cairosvg
    cairosvg.svg2png(url=svg_path, write_to=png_path, output_width=width)
    return png_path


def make_preview(design, tmpdir):
    """preview.png 1200 wide: banner scaled + about card scaled side-by-side."""
    import cairosvg
    from PIL import Image
    banner = os.path.join(tmpdir, "banner.svg")
    card = os.path.join(tmpdir, "about-card.svg")
    bp = os.path.join(tmpdir, "banner.png")
    cp = os.path.join(tmpdir, "card.png")
    cairosvg.svg2png(url=banner, write_to=bp, output_width=1200)
    cairosvg.svg2png(url=card, write_to=cp, output_width=520)
    bi, ci = Image.open(bp).convert("RGBA"), Image.open(cp).convert("RGBA")
    pad = 40
    H = bi.height + ci.height + pad * 3
    canvas = Image.new("RGBA", (1200, H), (13, 17, 23, 255))
    canvas.paste(bi, (0, pad), bi)
    canvas.paste(ci, (pad, pad * 2 + bi.height), ci)
    out = os.path.join(ROOT, "designs", f"{design['num']}-{design['slug']}", "preview.png")
    canvas.convert("RGB").save(out)
    return out


def make_gallery(pairs):
    import cairosvg
    from PIL import Image
    cols, rows = 4, 5
    cw, chh, cap = 300, 130, 30
    W, H = cols * cw + (cols + 1) * 20, rows * (chh + cap) + (rows + 1) * 20
    canvas = Image.new("RGB", (W, H), (8, 10, 16))
    for i, (num, slug, banner_png) in enumerate(pairs):
        img = Image.open(banner_png).convert("RGB")
        img.thumbnail((cw, chh))
        x = 20 + (i % cols) * (cw + 20) + (cw - img.width) // 2
        y = 20 + (i // cols) * (chh + cap + 20)
        canvas.paste(img, (x, y))
        from PIL import ImageDraw, ImageFont
        d = ImageDraw.Draw(canvas)
        try:
            font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf", 16)
        except Exception:
            font = ImageFont.load_default()
        d.text((x, y + img.height + 4), f"{num} · {slug}", fill=(200, 210, 225), font=font)
    os.makedirs(os.path.join(ROOT, "docs", "images"), exist_ok=True)
    canvas.save(os.path.join(ROOT, "docs", "images", "gallery.png"))


# ---------------------------------------------------------------- root readme
def root_readme():
    rows = []
    for d in DD.DESIGNS:
        slug = f"{d['num']}-{d['slug']}"
        light = "light + dark" if d["themes"] == "both" else "dark only"
        rows.append(f"| {d['num']} | [{d['name']}](designs/{slug}/) | {d['category']} | {d['vibe']} "
                    f"| {'yes' if d['animated'] else 'no'} | {light} "
                    f"| <img src=\"designs/{slug}/preview.png\" width=\"220\" alt=\"{slug} preview\"/> |")
    table = "\n".join(rows)
    return f"""<div align="center">

# github-profile-designs

**20 copy-paste-ready GitHub profile README designs — SVG-first, animated, no JavaScript.**

<img src="docs/images/gallery.png" width="100%" alt="Gallery of all 20 designs"/>

![License](https://img.shields.io/badge/license-MIT-22C55E?style=flat-square)
![Designs](https://img.shields.io/badge/designs-20-2563EB?style=flat-square)
![PRs](https://img.shields.io/badge/PRs-welcome-F59E0B?style=flat-square)

</div>

## How to use in 4 steps

1. Create a repo named **exactly your GitHub username** (e.g. `octocat/octocat`). Its README becomes your profile page.
2. Pick a design below, open its folder, and copy its `README.md` and the whole `assets/` folder into your profile repo. (Each folder also has a `demo/` — the same design already filled with real public data of [`Rishp-3`](https://github.com/Rishp-3) — so you can see it working.)
3. Replace the placeholders (see [`shared/placeholders.md`](shared/placeholders.md)) — or run `python3 tools/replace-placeholders.py --design 05-code-editor --name "..." --username "..."` to do it in one shot.
4. Commit, push, open your profile. Done.

## The 20 designs

| # | Design | Category | Vibe | Animated | Themes | Preview | Folder |
|---|---|---|---|---|---|---|---|
{table.replace(" | <img", " | <img")}

## FAQ

**Why SVG?** GitHub strips `<style>` and `<script>` from Markdown, but it *does* render `.svg` files placed in the repo via `<img>`. An SVG carries its own styles and animations, so it survives the sandbox while anything HTML/CSS-based would not.

**Why are animations inside the SVG?** Because CSS/JS in Markdown is removed. Inside the SVG we can use SMIL (`<animate>`, `<animateTransform>`, `<animateMotion>`) and CSS `@keyframes` — and every design ships a `prefers-reduced-motion` off-switch.

**How do I switch dark/light?** For designs 01, 02, 13, 14 and 20 use the `<picture>` pattern shown in their `variants/` files: GitHub renders the correct source based on the visitor's theme. Other designs are intentionally dark-only (see each `colors.md`).

**How do I add the contribution snake?** Only design 10 ships it: copy `designs/10-snake-game/workflow/snake.yml` into your profile repo's `.github/workflows/`, create an empty `output` branch, run the workflow once. Full steps in `designs/10-snake-game/setup.md`.

## Credits & License

Built with a single deterministic generator ([`tools/build.py`](tools/build.py)). Icons are original geometric marks, not trademarked logos. Demo data comes from the public GitHub API snapshot in [`tools/data/rishp-3.json`](tools/data/rishp-3.json).

MIT © 2026 Rishp-3
"""


DOCS_CUSTOM = """# Customization guide

## Change the colors
Every SVG stores colors inline. Open the file, find-and-replace the hex values from the design's `colors.md`.
Watch the contrast: text must stay ≥ 4.5:1 against the background (each `colors.md` lists the computed ratio).

## Change the text
SVG text lives in `<text>` elements with stable ids documented in each `setup.md`
(e.g. `banner-name`, `card-role`). Keep replacement strings short — measure roughly
`chars × font-size × 0.6` (monospace) and stay inside the box, or lower the `font-size` attribute.

## Change sizes
Scale by editing `width`/`height` (keep `viewBox` untouched and the drawing scales perfectly).
Standard sizes: banner 1000×300, divider 1000×24, section header 1000×56, about card 480×220, skills 1000×120.

## Swap icons
Original 48×48 glyphs are in `shared/icons/` (mono + colored). Each icon is a `<g transform="translate(x,y) scale(k)">…</g>`
block — copy it into any SVG and change its `fill`/`stroke` color. To use official brand logos instead, link shields.io badge images from the README instead of embedding SVGs.

## Dark/light `<picture>` switching
```html
<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/banner-dark.svg"/>
  <img alt="banner" src="assets/banner.svg"/>
</picture>
```
Keep both files identical except palette. Designs 01/02 ship `banner-dark.svg` in `assets/`; 13/14/20 explain their variants in `variants/`.
"""

DOCS_SVG_GUIDE = """# SVG guide — using `svg-prompt.md` with an AI

Each design folder contains `svg-prompt.md`: a complete, self-contained brief that regenerates that design's SVGs without seeing this repo. Paste it into any capable model and ask for one file at a time (banner first, then card, skills, divider).

## What GitHub allows (and what kills your SVG)
- ✅ Self-contained SVG files committed to the repo, referenced with `<img src="...">` (works in READMEs; SVGs from URLs are blocked by camo).
- ✅ SMIL animations (`animate`, `animateTransform`, `animateMotion`, `set`) and CSS `@keyframes` inside a `<style>` element in the SVG.
- ✅ Filters: `feGaussianBlur`, `feDropShadow`, patterns, gradients, clipPaths, masks.
- ❌ `<script>` — stripped/inert. Never rely on JS.
- ❌ `foreignObject` — GitHub sanitizes it away.
- ❌ Web fonts (`@import`, external `.woff2`) — only system stacks render: `ui-monospace, SFMono-Regular, Menlo, Consolas, monospace` and `-apple-system, "Segoe UI", Helvetica, Arial, sans-serif`.
- ❌ External images/hrefs inside the SVG (`<image href="http…">`) — blocked.
- ⚠️ Keep files small (< 150 KB hard ceiling, aim < 60 KB) and always validate with `xmllint --noout`.

## Checklist after AI generation
1. `xmllint --noout file.svg` passes.
2. `viewBox` + `width`/`height` present; `<title>`/`<desc>` added.
3. No banned constructs above (`grep -E 'script|foreignObject|href="http'`).
4. `prefers-reduced-motion` block exists.
5. Open it in a browser, then in the README preview — animations behave the same.
"""


def write_static_files():
    gh = os.path.join(ROOT, ".github")
    for sub in ("ISSUE_TEMPLATE", "workflows"):
        os.makedirs(os.path.join(gh, sub), exist_ok=True)
    with open(os.path.join(ROOT, "LICENSE"), "w") as f:
        f.write(MIT_LICENSE)
    with open(os.path.join(ROOT, "CONTRIBUTING.md"), "w") as f:
        f.write(CONTRIBUTING)
    with open(os.path.join(ROOT, "CODE_OF_CONDUCT.md"), "w") as f:
        f.write(COC)
    with open(os.path.join(ROOT, "CHANGELOG.md"), "w") as f:
        f.write(CHANGELOG)
    with open(os.path.join(ROOT, ".gitignore"), "w") as f:
        f.write("__pycache__/\n*.pyc\nout/\nnode_modules/\n.DS_Store\n")
    with open(os.path.join(gh, "ISSUE_TEMPLATE", "design-request.md"), "w") as f:
        f.write(DESIGN_REQUEST)
    with open(os.path.join(gh, "ISSUE_TEMPLATE", "bug-report.md"), "w") as f:
        f.write(BUG_REPORT)
    with open(os.path.join(gh, "PULL_REQUEST_TEMPLATE.md"), "w") as f:
        f.write(PR_TEMPLATE)
    with open(os.path.join(gh, "workflows", "link-check.yml"), "w") as f:
        f.write(LINK_CHECK)
    os.makedirs(os.path.join(ROOT, "docs"), exist_ok=True)
    with open(os.path.join(ROOT, "docs", "CUSTOMIZATION.md"), "w") as f:
        f.write(DOCS_CUSTOM)
    with open(os.path.join(ROOT, "docs", "SVG-GUIDE.md"), "w") as f:
        f.write(DOCS_SVG_GUIDE)
    with open(os.path.join(ROOT, "README.md"), "w") as f:
        f.write(root_readme())


MIT_LICENSE = """MIT License

Copyright (c) 2026 Rishp-3

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

CONTRIBUTING = """# Contributing

Thanks for interest in improving **github-profile-designs**!

## Adding or fixing a design
1. Everything is generated from `tools/build.py` + `tools/design_defs.py` + the SVG builders. **Do not hand-edit generated files** — edit the generator and re-run `python3 tools/build.py`.
2. Add your design config to `DESIGNS` and a builder function; keep the naming scheme `NN-slug`.
3. Run the quality gates: `python3 tools/check.py`, `xmllint --noout` on every new SVG.
4. Preview PNGs are regenerated automatically (cairosvg renders the first frame of SMIL animations — that is expected).

## Conventions
- SVGs must stay self-contained (see `docs/SVG-GUIDE.md`): no scripts, no external refs, system fonts only, reduced-motion respected.
- Templates use only placeholders from `shared/placeholders.md`; personal data appears only in `demo/` folders.
- Text contrast ≥ 4.5:1 on backgrounds.

Open an issue first for big changes. PRs should describe *what* changed and show a screenshot.
"""

COC = """# Contributor Covenant Code of Conduct (short form)

**Our pledge:** be respectful and inclusive. Harassment, personal attacks, and discriminatory language are not tolerated.

**Standards:** use welcoming language, assume good intent, give and gracefully accept constructive feedback, focus on what is best for the community.

**Enforcement:** report issues to the maintainers via a private GitHub issue or the profile contact links of `Rishp-3`. All complaints are reviewed and investigated promptly and fairly; maintainers who fail to uphold the standard face temporary or permanent removal.

**Attribution:** adapted from the Contributor Covenant, version 2.1, https://www.contributor-covenant.org/version/2/1/code_of_conduct.html
"""

CHANGELOG = """# Changelog

All notable changes to this project are documented here, format based on
[Keep a Changelog](https://keepachangelog.com/en/1.1.0/), versioning per
[Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.0.0] - 2026-10-13

### Added
- 20 GitHub profile README designs (`01-minimal` … `20-portfolio-pro`), each with:
  - copy-paste template README + self-contained animated SVG assets
  - a demo README personalised with public data of GitHub user `Rishp-3`
  - `setup.md`, `svg-prompt.md`, `colors.md`, `preview.png`, `variants/`
- Deterministic generator `tools/build.py`, live data fetcher `tools/fetch-data.py`
  (with manual fallback snapshot), CLI filler `tools/replace-placeholders.py`,
  validator `tools/check.py`.
- Shared icon set (original 48×48 glyphs, mono + colored), 6 generic dividers,
  `badges.md`, `placeholders.md`.
- Docs: `CUSTOMIZATION.md`, `SVG-GUIDE.md`, 4×5 `gallery.png`.
- CI: weekly + per-push link check (lychee), design validation workflow.
- Issue templates, PR template, MIT license, code of conduct.
"""

DESIGN_REQUEST = """---
name: Design request
about: Suggest a new profile README design
title: "[design] "
labels: design-request
---

**Describe the vibe**
Colors, mood, references (screenshots welcome).

**Should it animate?**
What moves and how (typing, waves, glow, rain, ...)?

**Light/dark?**
Which GitHub theme(s) should it support?

**Would you like to build it?**
Yes / No — if yes, mention it here so we can assign it.
"""

BUG_REPORT = """---
name: Bug report
about: Something renders wrong or breaks
title: "[bug] "
labels: bug
---

**Design**
e.g. `07-cyberpunk`

**What happens vs what should happen**

**Where**
Browser + OS, GitHub theme (dark/light), README snippet or screenshot.

**SVG checks**
- [ ] `xmllint --noout file.svg` passes
- [ ] File < 150 KB
- [ ] No `<script>` / `foreignObject` / external hrefs
"""

PR_TEMPLATE = """## What does this PR do?

## Which designs are affected?

## Checklist
- [ ] Regenerated with `python3 tools/build.py` (no hand-edited generated files)
- [ ] `python3 tools/check.py` passes
- [ ] Every new/changed SVG passes `xmllint --noout`, is < 150 KB, has `<title>`/`<desc>`
- [ ] Animations respect `prefers-reduced-motion`
- [ ] Screenshots/previews updated
- [ ] No personal data outside `demo/` folders; no email in SVGs
"""

LINK_CHECK = """name: Link Check
on:
  push:
    paths:
      - "**.md"
  pull_request:
  schedule:
    - cron: "0 6 * * 1"   # weekly, Monday 06:00 UTC
permissions:
  contents: read
jobs:
  lychee:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Link-check this repository only
        uses: lycheeverse/lychee-action@v2
        with:
          args: >-
            --verbose --no-progress --max-redirects 5
            --exclude-mail
            --exclude "YOUR_USERNAME|YOUR_|example\\.com|your-username"
            --exclude-path .git
            "*.md" "designs/**/*.md" "docs/**/*.md" "shared/**/*.md" ".github/**/*.md"
          fail: true
        env:
          GITHUB_TOKEN: ${'{'}{ secrets.GITHUB_TOKEN }{'}'}
"""

SNAKE_YML = """name: Contribute Graph Snake
on:
  schedule:
    - cron: "0 */12 * * *"   # every 12 hours
  workflow_dispatch:
  push:
    branches: [main]
permissions:
  contents: write
jobs:
  snake:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: Platane/snk/svg-only@v3
        with:
          github_user_name: ${'{'}{ github.repository_owner }{'}'}
          outputs: |
            dist/github-contribution-grid-snake.svg
            dist/github-contribution-grid-snake-dark.svg?palette=github-dark
      - uses: crazy-max/ghaction-github-pages@v4
        with:
          target_branch: output
          build_dir: dist
          keep_history: true
        env:
          GITHUB_TOKEN: ${'{'}{ secrets.GITHUB_TOKEN }{'}'}
"""


# ---------------------------------------------------------------- main
def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--only")
    ap.add_argument("--no-png", action="store_true")
    args = ap.parse_args()

    write_static_files()
    write_shared()

    import tempfile
    gallery_pairs = []
    for design in DD.DESIGNS:
        if args.only and design["num"] != args.only:
            continue
        slug = f"{design['num']}-{design['slug']}"
        ddir = os.path.join(ROOT, "designs", slug)
        os.makedirs(os.path.join(ddir, "assets"), exist_ok=True)
        os.makedirs(os.path.join(ddir, "demo", "assets"), exist_ok=True)
        os.makedirs(os.path.join(ddir, "variants"), exist_ok=True)

        tpl_files = build_files(design, base_ctx(design))
        demo_files = build_files(design, demo_ctx(design))
        for fname, content in tpl_files.items():
            with open(os.path.join(ddir, "assets", fname), "w") as f:
                f.write(content)
        for fname, content in demo_files.items():
            with open(os.path.join(ddir, "demo", fname.replace("assets/", ""), ) if False else
                      os.path.join(ddir, "demo", "assets", fname), "w") as f:
                f.write(content)

        with open(os.path.join(ddir, "README.md"), "w") as f:
            f.write(per_design_readme(design, demo=False))
        with open(os.path.join(ddir, "demo", "README.md"), "w") as f:
            f.write(per_design_readme(design, demo=True))
        with open(os.path.join(ddir, "setup.md"), "w") as f:
            f.write(setup_md(design))
        with open(os.path.join(ddir, "svg-prompt.md"), "w") as f:
            f.write(svg_prompt_md(design))
        with open(os.path.join(ddir, "colors.md"), "w") as f:
            f.write(colors_md(design))

        if design["themes"] == "both":
            dark_ctx = base_ctx(design); dark_ctx["dark"] = True
            lctx = demo_ctx(design)
            with open(os.path.join(ddir, "variants", "light.md"), "w") as f:
                f.write(f"# Light variant\n\nThe default `assets/` SVGs are the light variant for this design. "
                        f"Reference them normally:\n\n```\n<img src=\"assets/banner.svg\" width=\"100%\" alt=\"banner\"/>\n```\n")
            with open(os.path.join(ddir, "variants", "dark.md"), "w") as f:
                f.write(f"# Dark variant\n\nUse `<picture>` so GitHub picks the SVG by visitor theme:\n\n"
                        f"```html\n{light_picture_snippet(design)}\n```\n\n"
                        f"`assets/banner-dark.svg` is generated for this design"
                        + (" (demo copy in `demo/assets/banner-dark.svg`)." if design["num"] in ("01", "02") else ". "
                           "For 13/14/20 the default palettes already read well on both GitHub themes; "
                           "the dark file is optional — regenerate it with `python3 tools/build.py --only "
                           + design["num"] + "` if you need tweaks.") + "\n")
            if design["num"] in ("01", "02"):
                dfiles = build_files(design, dark_ctx)
                with open(os.path.join(ddir, "assets", "banner-dark.svg"), "w") as f:
                    f.write(dfiles["banner.svg"])
                df2 = build_files(design, {**demo_ctx(design), "dark": True})
                with open(os.path.join(ddir, "demo", "assets", "banner-dark.svg"), "w") as f:
                    f.write(df2["banner.svg"])
        else:
            with open(os.path.join(ddir, "variants", "README.md"), "w") as f:
                f.write(variants_md(design))

        if design["num"] == "10":
            wd = os.path.join(ddir, "workflow")
            os.makedirs(wd, exist_ok=True)
            with open(os.path.join(wd, "snake.yml"), "w") as f:
                f.write(SNAKE_YML)

        if not args.no_png:
            td = tempfile.mkdtemp()
            bpath = os.path.join(td, "banner.svg")
            with open(bpath, "w") as f:
                f.write(demo_files["banner.svg"])
            apath = os.path.join(td, "about-card.svg")
            with open(apath, "w") as f:
                f.write(demo_files["about-card.svg"])
            make_preview(design, td)
            gpath = os.path.join(td, "g.png")
            render_png(bpath, gpath, 300)
            gallery_pairs.append((design["num"], design["slug"], gpath))
            import shutil
            shutil.rmtree(td, ignore_errors=True)
        print(f"[build] {slug} done")

    if not args.no_png and len(gallery_pairs) == 20:
        make_gallery(gallery_pairs)
        print("[build] gallery.png done")


if __name__ == "__main__":
    main()
