#!/usr/bin/env python3
"""SVG asset builders for all 20 designs.

Every builder returns {filename: svg_string}. Template mode uses placeholders
(YOUR_NAME, YOUR_ROLE, YOUR_TAGLINE); demo mode passes real Rishp-3 values.
Sizes: banner 1000x300 (hero 1000x340 allowed), divider 1000x24,
about-card 480x220, skills 1000x120.
"""
import math
import random
from svgkit import *  # noqa: F401,F403
import svgkit as K

TPL = dict(name="YOUR_NAME", role="YOUR_ROLE", tagline="YOUR_TAGLINE", status="YOUR_STATUS")


def _status_dot(x, y, color="#39D353"):
    return (circle(x, y, 5, fill=color) +
            animate_on(circle(x, y, 8, fill="none", stroke=color, sw=1.5, opacity=0.6),
                       anim("r", "7;11;7", "2.4s"), anim("opacity", "0.6;0;0.6", "2.4s")))


# =====================================================================
# 01 minimal
# =====================================================================
def d01(ctx):
    p = ctx["palette"]
    dark = ctx.get("dark", False)
    bg = p["bg_dark"] if dark else "none"
    text_c = p["text_dark"] if dark else p["text"]
    muted = p["muted"]
    line_c = p["line"]
    name, role, tag = ctx["name"], ctx["role"], ctx["tagline"]
    banner = rect(0, 0, 1000, 300, fill=bg)
    # Issue 15: base state fully visible; animation only starts from hidden via `from`.
    css = REDUCED + ".fade{animation:fin .8s ease backwards}\n@keyframes fin{from{opacity:0}to{opacity:1}}\n"
    body = [banner]
    t1 = text(60, 130, name, size=44, fill=text_c, weight="300", tid="banner-name")
    t2 = text(60, 172, tag, size=18, fill=muted, tid="banner-tagline")
    t3 = text(60, 204, role, size=16, fill=muted, tid="banner-role")
    rule = line(60, 232, 940, 232, stroke=line_c, sw=1)
    body.append(g(t1, cls="fade"))
    body.append(g(t2, cls="fade"))
    body.append(g(t3, cls="fade"))
    body.append(rule)
    bsvg = svg_doc(1000, 300, style_block(css) + "".join(body),
                   f"{name} - minimal banner", "Minimal white-space profile banner.",
                   extra_defs="")
    divider = svg_doc(1000, 24, line(200, 12, 800, 12, stroke=line, sw=1),
                      "Divider", "Centered thin rule.", "")
    card = (rect(0, 0, 480, 220, fill=bg) +
            circle(70, 70, 34, fill="none", stroke=line_c, sw=1) +
            text(70, 78, (name[:1] if name != TPL["name"] else "Y"), size=28, fill=muted, anchor="middle", family=K.MONO, tid="card-initial") +
            text(130, 62, name, size=22, fill=text_c, weight="600", tid="card-name") +
            text(130, 90, role, size=14, fill=muted, tid="card-role") +
            (_status_dot(136, 128) if not dark else circle(136, 128, 5, fill="#39D353")) +
            text(150, 133, ctx["status"], size=13, fill=muted, tid="card-status") +
            line(60, 160, 420, 160, stroke=line_c, sw=1) +
            text(60, 188, "@@" + ctx["username"], size=13, fill=muted, family=K.MONO, tid="card-user"))
    cardsvg = svg_doc(480, 220, card, f"{name} about card", "Minimal about card.", "")
    icons = []
    x = 60
    for ic in ctx["stack_icons"]:
        icons.append(icon(ic, x, 36, color=text_c, size=48, scale=0.8))
        x += 40 + 48
    skillsvg = svg_doc(1000, 120, rect(0, 0, 1000, 120, fill=bg) + "".join(icons),
                       "Skills", "Monochrome tech icons row.", "")
    files = {"banner.svg": bsvg, "divider.svg": dividers_common(p, line_c), "about-card.svg": cardsvg, "skills.svg": skillsvg}
    files["banner.svg"] = bsvg
    if dark:
        pass
    return files


def dividers_common(p, line_c):
    return svg_doc(1000, 24, line(200, 12, 800, 12, stroke=line_c, sw=1), "Divider", "Thin rule.", "")


# =====================================================================
# 02 clean-card
# =====================================================================
def d02(ctx):
    p = ctx["palette"]
    dark = ctx.get("dark", False)
    bg = p["bg_dark"] if dark else p["bg"]
    card = p["card_dark"] if dark else p["card"]
    text_c = p["text_dark"] if dark else p["text"]
    acc, brd = p["accent"], p["border"]
    name, role = ctx["name"], ctx["role"]
    D = defs(fe_drop_shadow("sh", 0, 6, 12, "#0F172A", 0.18))
    css = REDUCED + ".rise{animation:rise .7s ease-out backwards}\n@keyframes rise{from{opacity:0;transform:translateY(10px)}to{opacity:1;transform:translateY(0)}}\n"
    banner_body = (rect(0, 0, 1000, 300, fill=bg) +
        g(rect(40, 60, 920, 180, fill=card, rx=16, stroke=brd, sw=1, blur="sh"), cls="rise") +
        text(76, 138, name, size=34, fill=text_c, weight="700", tid="banner-name", cls="rise") +
        text(76, 172, role, size=17, fill="#64748B" if not dark else "#94A3B8", tid="banner-role") +
        rect(660, 122, 260, 44, fill=acc, rx=22) +
        text(790, 150, ctx["pill"], size=15, fill="#FFFFFF", anchor="middle", weight="600", tid="banner-pill"))
    bsvg = svg_doc(1000, 300, D + style_block(css) + banner_body, f"{name} banner", "Card-style banner with accent pill.")
    divider = svg_doc(1000, 24, rect(300, 10, 400, 4, fill=brd, rx=2) + rect(470, 8, 60, 8, fill=acc, rx=4),
                      "Divider", "Accent-ticked rule.")
    cardb = (rect(0, 0, 480, 220, fill=bg) +
             rect(16, 16, 448, 188, fill=card, rx=16, stroke=brd, sw=1, blur="sh") +
             circle(76, 88, 32, fill=bg, stroke=acc, sw=3) +
             text(76, 96, ctx["initial"], size=24, fill=acc, anchor="middle", weight="700", tid="card-initial") +
             text(128, 80, name, size=21, fill=text_c, weight="700", tid="card-name") +
             text(128, 104, role, size=14, fill="#64748B" if not dark else "#94A3B8", tid="card-role") +
             _status_dot(44, 158) +
             text(58, 163, ctx["status"], size=13, fill=text_c, tid="card-status") +
             line(40, 182, 440, 182, stroke=brd, sw=1) +
             text(40, 197, "@" + ctx["username"] + " · " + ctx["loc_line"], size=12,
                  fill="#64748B" if not dark else "#94A3B8", tid="card-sub"))
    csvg = svg_doc(480, 220, D + cardb, f"{name} about card", "Rounded about card with avatar ring.")
    tiles = ""
    labels = ctx["stack_labels"]
    for i, ic in enumerate(ctx["stack_icons"]):
        tx = 24 + (i % 8) * 120
        ty = 10 + (i // 8) * 55
        tiles += rect(tx, ty, 108, 46, fill=card, rx=10, stroke=brd, sw=1) + \
                 icon(ic, tx + 6, ty + 5, color=acc, size=36) + \
                 text(tx + 48, ty + 29, labels[i], size=12, fill=text_c, tid=f"skill-{i}")
    ssvg = svg_doc(1000, 120, rect(0, 0, 1000, 120, fill=bg) + tiles, "Skills grid", "Icon tiles, 8 per row.")
    shdr = (rect(0, 0, 1000, 56, fill=bg) + rect(24, 14, 6, 28, fill=acc, rx=3) +
            rect(40, 8, 300, 40, fill=card, rx=10, stroke=brd, sw=1) +
            text(60, 33, ctx.get("section", "Section title"), size=16, fill=text_c, weight="600", tid="section-title"))
    hsvg = svg_doc(1000, 56, shdr, "Section header", "Card-style section header with accent bar.")
    return {"banner.svg": bsvg, "divider.svg": divider, "about-card.svg": csvg,
            "skills.svg": ssvg, "section-header.svg": hsvg}


# =====================================================================
# 03 monochrome
# =====================================================================
def d03(ctx):
    p = ctx["palette"]
    name_u = ctx["name"].upper()
    scan = animate_on(rect(-200, 0, 200, 300, fill="#FFFFFF", opacity=0.15, rid="scanline"),
                      anim_transform_translate("-200,0;1200,0", "6s"))
    banner = svg_doc(1000, 300,
        rect(0, 0, 1000, 300, fill=p["bg"]) +
        rect(12, 12, 976, 276, fill="none", stroke=p["text"], sw=1) +
        text(500, 150, name_u, size=min(64, max(24, int(900 / max(1, K.tw(name_u, 1, mono=False))))),
             fill=p["text"], anchor="middle", weight="700", spacing=6, tid="banner-name") +
        text(500, 196, ctx["role"].upper(), size=16, fill=p["dim"], anchor="middle", spacing=4, tid="banner-role") +
        scan, "Monochrome banner", "Uppercase name inside a thin frame with a slow scan line.")
    divider = svg_doc(1000, 24, line(100, 12, 900, 12, stroke=p["text"], sw=1, dash="4 6"),
                      "Divider", "Dashed rule.")
    frame = svg_doc(480, 220, rect(6, 6, 468, 208, fill=p["black2"], stroke=p["text"], sw=1) +
                    rect(14, 14, 452, 192, fill="none", stroke=p["frame"], sw=1),
                    "Frame", "Double frame used around the about card.")
    card = svg_doc(480, 220,
        rect(0, 0, 480, 220, fill=p["black2"]) +
        rect(10, 10, 460, 200, fill="none", stroke=p["frame"], sw=1) +
        circle(70, 78, 30, fill="none", stroke=p["text"], sw=1) +
        text(70, 88, ctx["initial"], size=26, fill=p["text"], anchor="middle", family=K.MONO, tid="card-initial") +
        text(124, 70, ctx["name"].upper(), size=20, fill=p["text"], weight="700", spacing=3, tid="card-name") +
        text(124, 96, ctx["role"].upper(), size=13, fill=p["dim"], spacing=2, tid="card-role") +
        line(40, 130, 440, 130, stroke=p["frame"], sw=1, dash="4 6") +
        circle(48, 156, 5, fill=p["text"]) +
        text(62, 161, ctx["status"].upper(), size=12, fill=p["dim"], family=K.MONO, tid="card-status") +
        text(40, 192, "@" + ctx["username"], size=12, fill=p["dim"], family=K.MONO, tid="card-user"),
        "About card", "Black and white identity card.")
    icons = ""
    x = 60
    for ic in ctx["stack_icons"]:
        icons += icon(ic, x, 36, color=p["text"], size=48, scale=0.8)
        x += 88
    skills = svg_doc(1000, 120, rect(0, 0, 1000, 120, fill=p["black2"]) + icons,
                     "Skills", "Grayscale tech icons.")
    return {"banner.svg": banner, "divider.svg": divider, "about-card.svg": card,
            "skills.svg": skills, "frame.svg": frame}


# =====================================================================
# 04 hacker-terminal
# =====================================================================
def d04(ctx):
    p = ctx["palette"]
    lines = ["$ whoami", ctx["name"], "$ cat role.txt", ctx["role"]]
    widths = [K.tw(l, 20) for l in lines]
    body = [rect(0, 0, 1000, 300, fill=p["bg"]),
            rect(30, 24, 940, 40, fill=p["bar"], rx=8),
            circle(54, 44, 7, fill="#FF5F56"), circle(78, 44, 7, fill=p["warn"]), circle(102, 44, 7, fill="#27C93F"),
            text(500, 50, f"{ctx['username_l']}@host: ~", size=15, fill=p["dim"], family=K.MONO, anchor="middle", tid="term-title")]
    css = REDUCED
    y = 100
    for i, (l, w) in enumerate(zip(lines, widths)):
        col = p["text"] if i % 2 == 0 else "#E8FFE8"
        clip_id = f"clipL{i}"
        # Issue 15: base clip width is FULL so the text shows statically / under reduced motion;
        # SMIL animates from 0 to full when motion is allowed.
        reveal = anim("width", f"0;{int(w)+6}", "0.9s", begin=f"{0.6 + i * 1.1}s", repeat="0", calc="linear", fill="freeze")
        cp = defs(f'<clipPath id="{clip_id}"><rect x="52" y="{y - 22}" width="{int(w)+6}" height="30">' + reveal + "</rect></clipPath>")
        body.append(cp)
        body.append(g(text(56, y, l, size=20, fill=col, family=K.MONO, tid=f"term-line-{i}"), clip=clip_id))
        y += 40
    cursor = animate_on(rect(56 + widths[3] + 10, y - 58, 11, 22, fill=p["text"]),
                        anim("opacity", "1;1;0;0", "1s", repeat="indefinite", calc="discrete", keytimes="0;0.5;0.5;1"))
    body.append(cursor)
    pat = '<pattern id="crt" width="4" height="4" patternUnits="userSpaceOnUse"><rect width="4" height="2" fill="#33FF66"/></pattern>'
    bsvg = svg_doc(1000, 300, defs(pat) + style_block(css) + "".join(body),
                   "Terminal banner", "Green terminal that types whoami and role.", "")
    divider = svg_doc(1000, 24, text(500, 16, "-----[ ✓ ]-----", size=14, fill=p["dim"], family=K.MONO, anchor="middle"),
                      "Divider", "ASCII divider.")
    ascii_logo = "\n".join(["   /\\ ",  "  /  \\ ", " / /\\ \\ ", "/_/  \\_\\ "])
    nb = [rect(0, 0, 480, 220, fill="#020502", stroke=p["dim"], sw=1, rx=6)]
    logo_lines = ["  ▄▄  ", " █▀█ ", " ▀▀  "]
    ly = 60
    for ll in logo_lines:
        nb.append(text(30, ly, ll, size=18, fill=p["text"], family=K.MONO, tid="nf-logo"))
        ly += 24
    # Issue 6/12: terminal-framed initials avatar (no photo anywhere).
    nb.append(circle(430, 42, 22, fill="none", stroke=p["text"], sw=2))
    nb.append(text(430, 50, ctx["initials"], size=17, fill=p["text"], anchor="middle",
                   family=K.MONO, weight="700", tid="card-initials"))
    # Issue 4: values are rendered directly (the old code embedded a literal "<text>" string).
    # Issue 3 rule: no invented facts -> the "Shell: zsh" line was removed.
    kv = [("user", "@" + ctx["username"]), ("role", ctx["role_short"]), ("os", ctx["os"]),
          ("stack", ctx["stack_inline"]), ("status", ctx["status"])]
    ky = 52
    for k, v in kv:
        nb.append(text(150, ky, f"{k}:", size=13, fill=p["dim"], family=K.MONO, tid=f"nf-{k}"))
        nb.append(text(150, ky + 15, str(v)[:34], size=13, fill=p["text"], family=K.MONO, tid=f"nv-{k}"))
        ky += 34
    nsvg = svg_doc(480, 220, "".join(nb), "Neofetch card", "Terminal identity block.")
    rows = ""
    ry = 20
    for i, ic in enumerate(ctx["stack_icons"][:8]):
        lbl = ctx["stack_labels"][i].lower().replace(" ", "-")
        col = 0 if i < 4 else 1
        yy = 20 + (i % 4) * 26
        xx = 40 + col * 480
        rows += icon(ic, xx, yy - 18, color=p["dim"], size=20) + \
                text(xx + 28, yy, f"-rw-r--r--  1  user  stack/{lbl}", size=14, fill=p["text"], family=K.MONO, tid=f"ls-{i}")
    head = text(40, 16, "$ ls ./stack", size=14, fill=p["warn"], family=K.MONO, tid="ls-head")
    ssvg = svg_doc(1000, 120, rect(0, 0, 1000, 120, fill="#020502") + head + rows, "Skills listing", "ls output of stack files.")
    footer = svg_doc(1000, 40, rect(0, 0, 1000, 40, fill=p["bg"]) +
                     text(40, 26, '$ echo "thanks for visiting"', size=16, fill=p["text"], family=K.MONO, tid="foot-cmd"),
                     "Footer prompt", "Terminal footer echo.")
    return {"banner.svg": bsvg, "divider.svg": divider, "about-card.svg": nsvg,
            "skills.svg": ssvg, "prompt-footer.svg": footer}


# =====================================================================
# 05 code-editor
# =====================================================================
def d05(ctx):
    p = ctx["palette"]
    code = [
        [("comment", "// profile.config")],
        [("keyword", "const"), ("plain", " developer "), ("plain", "= {")],
        [("prop", "  name"), ("plain", ": "), ("string", f'"{ctx["name"]}"'), ("plain", ",")],
        [("prop", "  role"), ("plain", ": "), ("string", f'"{ctx["role"]}"'), ("plain", ",")],
        [("prop", "  stack"), ("plain", ": ["), ("string", f'"{ctx["stack_arr"]}"'), ("plain", "],")],
        [("prop", "  openToWork"), ("plain", ": "), ("keyword", "true"), ("plain", ",")],
        [("plain", "};")],
    ]
    body = [rect(0, 0, 1000, 300, fill=p["bg"]),
            rect(0, 0, 1000, 34, fill=p["sidebar"]),
            rect(20, 6, 130, 28, fill=p["bg"], rx=4),
            text(35, 25, "about.js", size=13, fill=p["text"], family=K.MONO, tid="tab-name"),
            circle(135, 20, 4, fill=p["comment"])]
    lh = 30
    top = 54
    for li, toks in enumerate(code):
        delay = 0.3 + li * 0.4
        seg = ""
        xoff = 90
        for kind, txt in toks:
            col = {"comment": p["comment"], "keyword": p["keyword"], "string": p["string"],
                   "fn": p["fn"], "number": p["number"], "prop": p["cyan"] if "cyan" in p else "#9CDCFE",
                   "plain": p["text"]}[kind]
            seg += text(xoff, top + li * lh, txt, size=15, fill=col, family=K.MONO, tid=f"code-t{li}")
            xoff += K.tw(txt, 15) + 2
        reveal = g(seg, tid=f"code-line-{li}")
        body.append(animate_on(reveal, anim("opacity", "0;1", "0.3s", begin=f"{delay}s", repeat="0", fill="freeze")))
        body.append(rect(40, top + li * lh - 15, 30, 20, fill="none"))
        body.append(text(60, top + li * lh, str(li + 1), size=12, fill="#5A5A5A", family=K.MONO, anchor="end", tid=f"ln-{li}"))
    caret = animate_on(rect(90 + K.tw(code[-1][0][1], 15) + 6, top + 6 * lh - 15, 9, 20, fill=p["text"]),
                       anim("opacity", "1;1;0;0", "0.9s", repeat="indefinite", calc="discrete", keytimes="0;0.5;0.5;1"))
    body.append(caret)
    mm = ""
    rnd = random.Random(5)
    for i in range(26):
        mm += rect(940, 40 + i * 9, rnd.randint(10, 45), 5, fill="#3C3C3C", opacity=rnd.choice([0.5, 0.8]))
    body.append(rect(930, 34, 70, 246, fill="#252526"))
    body.append(mm)
    body.append(rect(0, 268, 1000, 32, fill=p["keyword"]))
    body.append(text(20, 289, " main ", size=13, fill="#1E1E1E", family=K.MONO, tid="sb-branch"))
    body.append(text(880, 289, "UTF-8   JavaScript", size=13, fill="#1E1E1E", family=K.MONO, tid="sb-enc"))
    bsvg = svg_doc(1000, 300, "".join(body), "Code editor banner", "Editor window showing a developer object literal.")
    divider = svg_doc(1000, 24, line(100, 12, 900, 12, stroke=p["sidebar"], sw=2) +
                      rect(480, 6, 40, 12, fill=p["keyword"], rx=3), "Divider", "Editor-colored rule.")
    pkg = [rect(0, 0, 480, 220, fill=p["bg"], stroke=p["sidebar"], sw=1),
           rect(0, 0, 480, 30, fill=p["sidebar"]),
           text(14, 20, "package.json", size=12, fill=p["text"], family=K.MONO, tid="pk-tab")]
    # Issue 5: stack comes from the person's `stack` list (not top_languages).
    # Issue 6/12: initials avatar chip in the tab bar. No fake facts (no version/private fields).
    pkg.append(rect(404, 5, 66, 20, fill=p["tab"], rx=10))
    pkg.append(text(437, 19, ctx["initials"], size=12, fill=p["string"], anchor="middle",
                    family=K.MONO, weight="700", tid="card-initials"))
    s1, s2, s3 = ctx["stack"][:3]
    plines = ['{', f'  "name": "{ctx["username_l"]}",', f'  "author": "{ctx["name"]}",',
              f'  "role": "{ctx["role"]}",', f'  "os": "{ctx["os"]}",',
              f'  "stack": ["{s1}", "{s2}", "{s3}"],',
              f'  "learning": "Full Stack",', '  "since": 2023,',
              f'  "openSource": true', '}']
    py = 46
    for i, pl in enumerate(plines):
        col = p["string"] if ":" in pl else p["text"]
        pkg.append(text(16, py, pl[:44], size=11.5, fill=col, family=K.MONO, tid=f"pk-{i}"))
        py += 17
    psvg = svg_doc(480, 220, "".join(pkg), "package.json card", "Identity as a package manifest.")
    tree = [rect(0, 0, 1000, 120, fill=p["sidebar"]),
            text(20, 22, "EXPLORER", size=11, fill="#9D9D9D", family=K.MONO, tid="ex-head"),
            text(20, 46, "▾ stack/", size=13, fill=p["text"], family=K.MONO, tid="ex-folder")]
    for i, ic in enumerate(ctx["stack_icons"][:8]):
        cx = 40 + (i % 4) * 240
        cy = 66 + (i // 4) * 26
        ext = ctx["stack_ext"][i]
        tree.append(icon(ic, cx, cy - 14, color=p["fn"], size=16))
        tree.append(text(cx + 20, cy, ext, size=12, fill=p["text"], family=K.MONO, tid=f"ex-{i}"))
    ssvg = svg_doc(1000, 120, "".join(tree), "File explorer skills", "Stack as files in a tree.")
    status = svg_doc(1000, 32, rect(0, 0, 1000, 32, fill=p["keyword"]) +
                     text(16, 21, "⎇ main", size=13, fill="#1E1E1E", family=K.MONO, tid="st-branch") +
                     text(900, 21, "UTF-8 · JavaScript · Ln 7", size=13, fill="#1E1E1E", family=K.MONO, tid="st-info"),
                     "Status bar", "Editor status bar footer.")
    tabs = svg_doc(1000, 40, rect(0, 0, 1000, 40, fill=p["sidebar"]) +
                   rect(10, 6, 150, 34, fill=p["bg"], rx=4) + text(24, 28, "about.js", size=13, fill=p["text"], family=K.MONO, tid="tb-1") +
                   rect(170, 6, 170, 34, fill=p["tab"], rx=4) + text(184, 28, "projects.jsx", size=13, fill="#8f8f8f", family=K.MONO, tid="tb-2") +
                   rect(350, 6, 150, 34, fill=p["tab"], rx=4) + text(364, 28, "stats.ts", size=13, fill="#8f8f8f", family=K.MONO, tid="tb-3"),
                   "Tabs", "Section switcher visual.")
    return {"banner.svg": bsvg, "divider.svg": divider, "about-card.svg": psvg,
            "skills.svg": ssvg, "status-bar.svg": status, "tabs.svg": tabs}


# =====================================================================
# 06 matrix rain
# =====================================================================
def d06(ctx):
    p = ctx["palette"]
    rnd = random.Random(66)
    glyphs = "01$#@{}<>"
    col_defs = ""
    for ci in range(8):
        chars = "".join(rnd.choice(glyphs) for _ in range(14))
        tspans = "".join(f'<tspan x="0" dy="22">{esc(ch)}</tspan>' for ch in chars)
        shade = [p["bright"], p["mid"], p["dim"]][ci % 3]
        col_defs += (f'<g id="mc{ci}"><text font-family="{K.MONO}" font-size="18" fill="{shade}" xml:space="preserve">'
                     f'{tspans}</text></g>')
    cols = ""
    for c in range(40):
        x = 8 + c * 25
        dur = rnd.uniform(4, 9)
        delay = rnd.uniform(0, 6)
        use = f'<use href="#mc{c % 8}" x="{x}" y="-330"/>'
        mv = f'<animateTransform attributeName="transform" type="translate" values="0,-330;0,330" dur="{dur:.1f}s" begin="-{delay:.1f}s" repeatCount="indefinite"/>'
        if use.endswith("/>"):
            use = use[:-2] + ">" + mv + "</use>"
        cols += use
    panel = (rect(250, 90, 500, 130, fill="#000000", rx=12, opacity=0.92, stroke=p["mid"], sw=1) +
             text(500, 145, ctx["name"], size=34, fill=p["head"], anchor="middle", family=K.MONO, weight="700", tid="banner-name") +
             text(500, 182, ctx["tagline"], size=15, fill=p["bright"], anchor="middle", family=K.MONO, tid="banner-tagline"))
    bsvg = svg_doc(1000, 300, defs(col_defs) + rect(0, 0, 1000, 300, fill=p["bg"]) + cols + panel,
                   "Matrix rain banner", "Falling glyph columns behind a readable panel.")
    divider = svg_doc(1000, 24, "".join(
        text(20 + i * 25, 18, rnd.choice(glyphs), size=14, fill=[p["bright"], p["mid"], p["dim"]][i % 3], family=K.MONO)
        for i in range(40)), "Divider", "Row of falling glyphs.")
    card = svg_doc(480, 220,
        rect(0, 0, 480, 220, fill="#000000", stroke=p["mid"], sw=1, rx=8) +
        # Issue 6/12: initials avatar in the design's own terminal frame.
        rect(392, 24, 64, 64, fill="none", stroke=p["bright"], sw=2, rx=4) +
        text(424, 65, ctx["initials"], size=22, fill=p["bright"], anchor="middle",
             family=K.MONO, weight="700", tid="card-initials") +
        text(30, 50, "> identify --user", size=14, fill=p["dim"], family=K.MONO, tid="card-cmd") +
        text(30, 88, ctx["name"], size=24, fill=p["bright"], family=K.MONO, weight="700", tid="card-name") +
        text(30, 118, ctx["role"], size=14, fill=p["head"], family=K.MONO, tid="card-role") +
        text(30, 148, "[" + ctx["status"] + "]", size=13, fill=p["mid"], family=K.MONO, tid="card-status") +
        text(30, 190, "@" + ctx["username"] + "_", size=13, fill=p["bright"], family=K.MONO, tid="card-user"),
        "Matrix about card", "Green-on-black identity terminal card.")
    icons = ""
    x = 100
    for ic in ctx["stack_icons"]:
        icons += icon(ic, x, 36, color=p["bright"], size=48, scale=0.75)
        x += 72
    ssvg = svg_doc(1000, 120, rect(0, 0, 1000, 120, fill="#000000") + icons, "Matrix skills", "Green monochrome icons.")
    return {"banner.svg": bsvg, "divider.svg": divider, "about-card.svg": card, "skills.svg": ssvg}


# =====================================================================
# 07 cyberpunk
# =====================================================================
def cut_panel(x, y, w, h, c, fill=None, sw=2):
    cc = 22
    pts = f"{x + cc},{y} {x + w - cc},{y} {x + w},{y + cc} {x + w},{y + h - cc} {x + w - cc},{y + h} {x + cc},{y + h} {x},{y + h - cc} {x},{y + cc}"
    return polygon(pts, fill=fill or "none", stroke=c, sw=sw)


def d07(ctx):
    p = ctx["palette"]
    bggrad = defs(linear_gradient("cbg", [("0%", p["bg1"]), ("100%", p["bg2"])], x1="0%", y1="0%", x2="0%", y2="100%") +
                  fe_gaussian_blur("glow", 4))
    grid = ""
    for i in range(13):
        gx = 500 + (i - 6) * 160
        grid += line(500, 240, gx, 300, stroke=p["cyan"], sw=1, opacity=0.25)
    for j in range(4):
        gy = 245 + j * j * 3.5 + j * 4
        grid += line(0, gy, 1000, gy, stroke=p["pink"], sw=1, opacity=0.22)
    glitch_anim = lambda off: anim("transform", f"translate({off},0);translate({off},0);translate({off + 6},0);translate({off - 5},0);translate({off},0);translate({off},0)",
                                   "4s", repeat="indefinite", calc="linear", keytimes="0;0.94;0.955;0.97;0.985;1")
    name_x = 500
    layers = (
        g(text(name_x, 150, ctx["name"], size=46, fill=p["pink"], anchor="middle", weight="800", spacing=2, tid="gl-pink"), transform="translate(-3,0)") +
        g(text(name_x, 150, ctx["name"], size=46, fill=p["cyan"], anchor="middle", weight="800", spacing=2, tid="gl-cyan"), transform="translate(3,1)") +
        text(name_x, 150, ctx["name"], size=46, fill="#FFFFFF", anchor="middle", weight="800", spacing=2, tid="banner-name"))
    # apply glitch via animateTransform on wrapper groups
    lp = g(layers, tid="name-stack")
    glitch = (f'<g><animateTransform attributeName="transform" type="translate" values="0,0;0,0;4,-2;-3,2;0,0;0,0" keyTimes="0;0.92;0.94;0.97;0.99;1" dur="4s" repeatCount="indefinite"/>')
    hud = (cut_panel(30, 30, 940, 240, p["cyan"], fill="#16093A", sw=2) +
           text(60, 70, "[ SYS.ONLINE ]", size=12, fill=p["yellow"], family=K.MONO, tid="hud-tl") +
           text(940, 70, "[ NAV.OK ]", size=12, fill=p["yellow"], family=K.MONO, anchor="end", tid="hud-tr") +
           text(60, 250, "[ LINK.STABLE ]", size=12, fill=p["cyan"], family=K.MONO, opacity=0.8, tid="hud-bl"))
    body = [rect(0, 0, 1000, 300, fill="url(#cbg)"), grid, hud,
            glitch + text(500, 150, ctx["name"], size=46, fill=p["pink"], anchor="middle", weight="800", spacing=2, opacity=0.85, tid="banner-name-pink") + "</g>",
            text(500, 150, ctx["name"], size=46, fill="#FFFFFF", anchor="middle", weight="800", spacing=2, tid="banner-name"),
            text(500, 192, ctx["role"].upper(), size=16, fill=p["cyan"], anchor="middle", spacing=6, family=K.MONO, tid="banner-role"),
            text(500, 218, ctx["tagline"], size=13, fill=p["pink"], anchor="middle", family=K.MONO, tid="banner-tagline")]
    bsvg = svg_doc(1000, 300, bggrad + "".join(body), "Cyberpunk banner", "Neon HUD panel with glitching name.")
    dot = animate_on(circle(0, 12, 5, fill=p["cyan"], blur="glow"),
                     anim_transform_translate("0,12;1000,12", "2.6s"))
    divider = svg_doc(1000, 24, line(0, 12, 1000, 12, stroke=p["pink"], sw=2, opacity=0.7) + dot,
                      "Divider", "Neon line with traveling dot.")
    card = svg_doc(480, 220,
        rect(0, 0, 480, 220, fill="#0d0620") +
        cut_panel(12, 12, 456, 196, p["cyan"], fill="#1B0B3A", sw=2) +
        # Issue 6/12: initials avatar in a neon octagon frame.
        cut_panel(388, 30, 62, 62, p["pink"], fill="#0d0620", sw=2) +
        text(419, 70, ctx["initials"], size=22, fill=p["yellow"], anchor="middle",
             family=K.MONO, weight="700", tid="card-initials") +
        text(40, 52, "// STATUS: ONLINE", size=13, fill=p["green"] if "green" in p else p["cyan"], family=K.MONO, tid="card-status") +
        text(40, 96, ctx["name"], size=26, fill="#FFFFFF", weight="700", tid="card-name") +
        text(40, 126, ctx["role"], size=14, fill=p["pink"], family=K.MONO, tid="card-role") +
        text(40, 156, "@" + ctx["username"], size=13, fill=p["cyan"], family=K.MONO, tid="card-user") +
        text(40, 186, "// " + ctx["open_to"], size=12, fill=p["yellow"], family=K.MONO, tid="card-open"),
        "Cyberpunk about card", "Cut-corner identity card.")
    glowf = defs(fe_gaussian_blur("nglow", 2.5))
    icons = ""
    x = 60
    for ic in ctx["stack_icons"]:
        col = [p["pink"], p["cyan"], p["yellow"]][(x // 88) % 3]
        icons += f'<g filter="url(#nglow)">{icon(ic, x, 34, color=col, size=52, scale=0.8)}</g>'
        icons += icon(ic, x, 34, color=col, size=52, scale=0.8)
        x += 88
    ssvg = svg_doc(1000, 120, glowf + rect(0, 0, 1000, 120, fill="#0d0620") + icons, "Cyberpunk skills", "Glowing neon icons.")
    hudf = svg_doc(480, 220, cut_panel(6, 6, 468, 208, p["cyan"], sw=2) +
                   text(24, 34, "+", size=18, fill=p["pink"], family=K.MONO) + text(444, 34, "+", size=18, fill=p["pink"], family=K.MONO, anchor="end"),
                   "HUD frame", "Corner bracket frame overlay.")
    return {"banner.svg": bsvg, "divider.svg": divider, "about-card.svg": card,
            "skills.svg": ssvg, "hud-frame.svg": hudf}


# =====================================================================
# 08 gradient wave
# =====================================================================
def d08(ctx):
    p = ctx["palette"]
    grad = defs(linear_gradient("wg", [("0%", p["g1"]), ("100%", p["g2"])]) +
                linear_gradient("wgb", [("0%", p["g1"], 0.5), ("100%", p["g2"], 0.5)]))
    w1 = path(wave_band_path(1000, 14, 235, 250, 0, fill_to=300), fill="url(#wgb)")
    w2 = path(wave_band_path(1000, 18, 250, 330, 2, fill_to=300), fill="url(#wg)", opacity=0.55)
    w3 = path(wave_band_path(1000, 10, 265, 200, 4, fill_to=300), fill="url(#wg)", opacity=0.85)
    mv = lambda dur: anim_transform_translate(f"0,0;-1000,0", dur)
    band = lambda el, dur: K.animate_on(el, mv(dur))
    body = [rect(0, 0, 1000, 300, fill=p["bg"]),
            band(w1, "18s"), band(w2, "12s"), band(w3, "8s"),
            text(500, 120, ctx["name"], size=44, fill=p["text"], anchor="middle", weight="700", tid="banner-name"),
            text(500, 158, ctx["tagline"], size=17, fill="#A5B4FC" if ctx.get("dark", True) else p["g2"], anchor="middle", tid="banner-tagline"),
            text(500, 190, ctx["role"], size=14, fill=p["g1"], anchor="middle", family=K.MONO, tid="banner-role")]
    bsvg = svg_doc(1000, 300, grad + "".join(body), "Gradient wave banner", "Name above three moving sine waves.")
    wl = path(sine_wave_path(500, 5, 12, 60, twice=True), stroke="url(#wg)", sw=2, fill="none")
    divider = svg_doc(1000, 24, defs(linear_gradient("dg", [("0%", p["g1"]), ("100%", p["g2"])])) +
                      g(K.animate_on(wl, anim_transform_translate("0,0;-500,0", "6s")), transform="translate(250,0)"),
                      "Divider", "Small animated wave.")
    card = svg_doc(480, 220,
        defs(linear_gradient("tg", [("0%", p["g1"]), ("100%", p["g2"])])) +
        rect(0, 0, 480, 220, fill="#111c33", rx=14) + rect(0, 0, 480, 5, fill="url(#tg)", rx=2) +
        circle(70, 84, 32, fill="#0F172A", stroke=p["g1"], sw=2) +
        text(70, 92, ctx["initial"], size=24, fill=p["g2"], anchor="middle", weight="700", tid="card-initial") +
        text(124, 76, ctx["name"], size=20, fill=p["text"], weight="700", tid="card-name") +
        text(124, 100, ctx["role"], size=13, fill="#94A3B8", tid="card-role") +
        _status_dot(40, 150) + text(54, 155, ctx["status"], size=13, fill=p["text"], tid="card-status") +
        text(40, 190, "@" + ctx["username"], size=12, fill=p["g1"], family=K.MONO, tid="card-user"),
        "Wave about card", "Dark card with gradient top border.")
    chips = ""
    x = 30
    for lab in ctx["stack_labels"][:10]:
        wd = max(70, K.tw(lab, 13, mono=False) + 30)
        chips += rect(x, 40, wd, 40, fill="#111c33", rx=20, stroke="url(#wg)", sw=1.5) + \
                 text(x + wd / 2, 65, lab, size=13, fill=p["text"], anchor="middle", tid=f"chip-{lab}")
        x += wd + 14
        if x > 900:
            break
    ssvg = svg_doc(1000, 120, defs(linear_gradient("wg2", [("0%", p["g1"]), ("100%", p["g2"])])) +
                   rect(0, 0, 1000, 120, fill=p["bg"]) + chips.replace("url(#wg)", "url(#wg2)"),
                   "Skills chips", "Gradient-outline pills.")
    fw1 = path(wave_band_path(1000, 12, 20, 260, 1, fill_to=60), fill="url(#wgb)", opacity=0.6)
    fw2 = path(wave_band_path(1000, 14, 30, 340, 3, fill_to=60), fill="url(#wg)", opacity=0.8)
    footer = svg_doc(1000, 60, grad + rect(0, 0, 1000, 60, fill=p["bg"]) +
                     K.animate_on(fw1, anim_transform_translate("0,0;-1000,0", "14s")) +
                     K.animate_on(fw2, anim_transform_translate("0,0;-1000,0", "9s")) +
                     text(500, 46, ctx["footer"], size=13, fill=p["text"], anchor="middle", opacity=0.9, tid="foot-text"),
                     "Wave footer", "Mirrored waves at the page bottom.")
    return {"banner.svg": bsvg, "divider.svg": divider, "about-card.svg": card,
            "skills.svg": ssvg, "wave-footer.svg": footer}


# =====================================================================
# 09 typing intro
# =====================================================================
def d09(ctx):
    p = ctx["palette"]
    phrases = ctx["phrases"]
    cycle = 16.0
    n = len(phrases)
    seg = cycle / n  # each phrase gets type+hold+erase within its slot
    body = [rect(0, 0, 1000, 300, fill=p["bg"]),
            # Issue 15: static/reduced-motion state shows the first phrase in full.
            text(60, 160, phrases[0], size=30, fill=p["text"], family=K.MONO, weight="600", tid="banner-phrase-static")]
    defs_parts = []
    for i, ph in enumerate(phrases):
        w = int(K.tw(ph, 30, mono=False)) + 8
        t0 = i * seg
        keys = f"0;0.45;0.75;1"
        vals = f"0;{w};{w};0"
        clip_id = f"typeClip{i}"
        an = anim("width", vals, f"{seg:.2f}s", begin=f"{t0:.2f}s", repeat="indefinite", calc="linear")
        # base width stays full so static renderers show the whole phrase (issue 15)
        defs_parts.append(f'<clipPath id="{clip_id}"><rect x="60" y="110" width="{w}" height="60">{an}</rect></clipPath>')
        body.append(g(text(60, 160, ph, size=30, fill=p["text"] if i % 2 == 0 else p["accent"],
                           family=K.MONO, weight="600", tid=f"phrase-{i}"), clip=clip_id))
    caret_x = [int(K.tw(ph, 30, mono=False)) + 66 for ph in phrases]
    # single caret that follows active phrase end (stepped)
    cv = ";".join(str(x) for x in caret_x) + ";" + str(caret_x[0])
    kt = ";".join(f"{i / n:.3f}" for i in range(n + 1))
    caret = rect(caret_x[0], 132, 12, 34, fill=p["caret"])
    caret = K.animate_on(caret,
        anim("x", cv, f"{cycle}s", repeat="indefinite", calc="discrete", keytimes=kt),
        anim("opacity", "1;1;0;0", "0.9s", repeat="indefinite", calc="discrete", keytimes="0;0.5;0.5;1"))
    body.append(caret)
    body.append(text(60, 210, "> " + ctx["sub"], size=15, fill=p["muted"], family=K.MONO, tid="banner-sub"))
    bsvg = svg_doc(1000, 300, defs("".join(defs_parts)) + "".join(body),
                   "Typing banner", "Typed phrases cycling every 16 seconds.")
    fillrect = animate_on(rect(100, 10, 800, 3, fill=p["accent"]),
                          anim("width", "0;800", "1.2s", repeat="0", fill="freeze"))
    divider = svg_doc(1000, 24, line(100, 12, 900, 12, stroke=p["muted"], sw=1, dash="2 6") + fillrect,
                      "Divider", "Dotted line filled once left to right.")
    lines = ctx["about_lines"]
    db = [rect(0, 0, 480, 220, fill="#161B22", stroke=p["muted"], sw=1, rx=10)]
    # Issue 6/12: initials avatar in a terminal window frame.
    db.append(rect(392, 152, 64, 52, fill="none", stroke=p["accent"], sw=2, rx=6))
    db.append(text(424, 185, ctx["initials"], size=20, fill=p["accent"], anchor="middle",
                   family=K.MONO, weight="700", tid="card-initials"))
    dparts = []
    for i, ln in enumerate(lines):
        w = int(K.tw(ln, 15)) + 6
        cid = f"ab{i}"
        an = anim("width", f"0;{w};{w}", "6s", begin=f"{i * 1.6:.1f}s", repeat="indefinite", calc="linear")
        # Issue 15: base clip width is full so the card renders its complete text statically.
        dparts.append(f'<clipPath id="{cid}"><rect x="26" y="{40 + i * 44 - 20}" width="{w}" height="30">{an}</rect></clipPath>')
        db.append(g(text(30, 40 + i * 44, ln, size=15, fill=p["text"] if i else p["accent"], family=K.MONO, tid=f"about-{i}"), clip=cid))
    csvg = svg_doc(480, 220, defs("".join(dparts)) + "".join(db), "Typing about card", "Three typed lines.")
    icons = ""
    x = 60
    for ic in ctx["stack_icons"]:
        icons += icon(ic, x, 36, color=p["accent"], size=48, scale=0.8)
        x += 76
    ssvg = svg_doc(1000, 120, rect(0, 0, 1000, 120, fill=p["bg"]) + icons, "Skills", "Static icon row.")
    return {"banner.svg": bsvg, "divider.svg": divider, "about-card.svg": csvg, "skills.svg": ssvg}


# =====================================================================
# 10 snake game
# =====================================================================
def d10(ctx):
    p = ctx["palette"]
    rnd = random.Random(10)
    cells = ""
    for r in range(7):
        for c in range(52):
            lvl = rnd.random()
            col = p["c1"] if lvl < 0.45 else [p["c2"], p["c3"], p["c4"], p["c5"]][int((lvl - 0.45) // 0.14)]
            cells += rect(20 + c * 18.4, 150 + r * 18.4, 16, 16, fill=col, rx=3)
    snake_cells = [(row, col) for row, col in [(3, 10), (3, 11), (3, 12), (3, 13), (2, 13), (1, 13)]]
    snake = ""
    for rr, cc in snake_cells:
        snake += rect(20 + cc * 18.4, 150 + rr * 18.4, 16, 16, fill=p["snake"], rx=4)
    bsvg = svg_doc(1000, 300, rect(0, 0, 1000, 300, fill=p["bg"]) +
                   text(500, 80, ctx["name"], size=40, fill=p["text"], anchor="middle", weight="700", tid="banner-name") +
                   text(500, 112, ctx["tagline"], size=15, fill=p["snake"], anchor="middle", family=K.MONO, tid="banner-tagline") +
                   cells + snake, "Snake banner", "Name over a contribution-grid decoration.")
    row = ""
    for c in range(52):
        row += rect(8 + c * 19.1, 6, 12, 12, fill=[p["c1"], p["c2"], p["c3"], p["c4"], p["c5"]][c % 5], rx=2)
    divider = svg_doc(1000, 24, rect(0, 0, 1000, 24, fill=p["bg"]) + row, "Divider", "Row of contribution cells.")
    card = svg_doc(480, 220,
        rect(0, 0, 480, 220, fill="#161B22", stroke=p["c1"], sw=1, rx=10) +
        circle(70, 80, 30, fill=p["c1"], stroke=p["snake"], sw=2) +
        text(70, 89, ctx["initial"], size=22, fill=p["text"], anchor="middle", weight="700", tid="card-initial") +
        text(122, 72, ctx["name"], size=19, fill=p["text"], weight="700", tid="card-name") +
        text(122, 96, ctx["role"], size=13, fill=p["c5"], family=K.MONO, tid="card-role") +
        _status_dot(40, 142, p["c5"]) + text(54, 147, ctx["status"], size=13, fill=p["text"], tid="card-status") +
        text(40, 186, "@" + ctx["username"] + " · press ▶ to watch the snake", size=12, fill=p["snake"], family=K.MONO, tid="card-note"),
        "Snake about card", "GitHub-dark identity card.")
    icons = ""
    x = 60
    for ic in ctx["stack_icons"]:
        icons += icon(ic, x, 36, color=p["c5"], size=48, scale=0.8)
        x += 76
    ssvg = svg_doc(1000, 120, rect(0, 0, 1000, 120, fill=p["bg"]) + icons, "Skills", "Icon row in contribution greens.")
    return {"banner.svg": bsvg, "divider.svg": divider, "about-card.svg": card, "skills.svg": ssvg}


# =====================================================================
# 11 glow pulse
# =====================================================================
def d11(ctx):
    p = ctx["palette"]
    orb_cx, orb_cy = 500, 150
    glow = defs(fe_gaussian_blur("soft", 12) + fe_drop_shadow("tglow", 0, 0, 6, p["violet"], 0.9) +
                radial_gradient("orb", [("0%", p["pink"], 0.9), ("60%", p["violet"], 0.5), ("100%", p["violet"], 0)]))
    rings = ""
    for i, r in enumerate([34, 52, 72]):
        c = circle(orb_cx, orb_cy, r, fill="none", stroke=p["violet"] if i else p["pink"], sw=2, opacity=0.7)
        c = K.animate_on(c,
            anim("r", f"{r};{r + 10};{r}", "3s", begin=f"{i * 0.5}s", repeat="indefinite", calc="spline",
                 keysplines="0.42 0 0.58 1;0.42 0 0.58 1", keytimes="0;0.5;1"),
            anim("opacity", "0.7;0.25;0.7", "3s", begin=f"{i * 0.5}s", repeat="indefinite", calc="spline",
                 keysplines="0.42 0 0.58 1;0.42 0 0.58 1", keytimes="0;0.5;1"))
        rings += c
    core = circle(orb_cx, orb_cy, 26, fill="url(#orb)", blur="soft")
    name_t = text(500, 250, ctx["name"], size=34, fill=p["text"], anchor="middle", weight="600", tid="banner-name")
    name_t = K.animate_on(name_t.replace("<text", '<text filter="url(#tglow)"'),
                          anim("opacity", "0.85;1;0.85", "4s", repeat="indefinite", calc="spline",
                               keysplines="0.42 0 0.58 1;0.42 0 0.58 1", keytimes="0;0.5;1"))
    body = [rect(0, 0, 1000, 300, fill=p["bg"]), core, rings, name_t,
            text(500, 285, ctx["tagline"], size=15, fill=p["violet"], anchor="middle", tid="banner-tagline")]
    bsvg = svg_doc(1000, 300, glow + "".join(body), "Glow pulse banner", "Pulsing orb behind the name.")
    pdot = circle(0, 12, 6, fill=p["pink"], blur="soft")
    pdot = K.animate_on(pdot, anim_transform_translate("0,12;1000,12", "3s"),
                        anim("opacity", "0;1;1;0", "3s", repeat="indefinite"))
    divider = svg_doc(1000, 24, defs(fe_gaussian_blur("soft2", 6)) +
                      line(0, 12, 1000, 12, stroke=p["violet"], sw=1, opacity=0.4) + pdot,
                      "Divider", "Traveling pulse dot.")
    border = rect(1, 1, 478, 218, fill="#131328", rx=14, stroke=p["violet"], sw=2)
    border = K.animate_on(border, anim("stroke-opacity", "0.35;1;0.35", "5s", repeat="indefinite", calc="spline",
                                        keysplines="0.42 0 0.58 1;0.42 0 0.58 1", keytimes="0;0.5;1"))
    card = svg_doc(480, 220, defs(fe_gaussian_blur("cg", 6)) +
                   rect(0, 0, 480, 220, fill=p["bg"]) +
                   rect(0, 0, 480, 220, fill="none", stroke=p["violet"], sw=6, rx=14, opacity=0.25, blur="cg") + border +
                   circle(70, 80, 30, fill="#1d1b3a", stroke=p["pink"], sw=2) +
                   text(70, 89, ctx["initial"], size=22, fill=p["text"], anchor="middle", weight="700", tid="card-initial") +
                   text(122, 72, ctx["name"], size=19, fill=p["text"], weight="700", tid="card-name") +
                   text(122, 96, ctx["role"], size=13, fill=p["violet"], tid="card-role") +
                   _status_dot(40, 146, p["pink"]) + text(54, 151, ctx["status"], size=13, fill=p["text"], tid="card-status") +
                   text(40, 190, "@" + ctx["username"], size=12, fill=p["pink"], family=K.MONO, tid="card-user"),
                   "Glow about card", "Card with slowly pulsing border glow.")
    icons = ""
    x = 60
    for i, ic in enumerate(ctx["stack_icons"]):
        one = icon(ic, x, 36, color=p["violet"], size=48, scale=0.8)
        # wrap and pulse scale via CSS-like SMIL on group transform
        wrapped = f'<g transform="translate({x + 20},{56})"><g>{icon(ic, -20, -20, color=p["violet"], size=48, scale=0.8)}'
        wrapped = wrapped + K.anim("transform", "scale(1);scale(1.06);scale(1)", "2.4s", begin=f"{i * 0.15:.2f}s",
                                   repeat="indefinite", calc="spline", keysplines="0.42 0 0.58 1;0.42 0 0.58 1", keytimes="0;0.5;1") + "</g></g>"
        icons += wrapped
        x += 76
    ssvg = svg_doc(1000, 120, rect(0, 0, 1000, 120, fill=p["bg"]) + icons, "Skills", "Staggered pulsing icons.")
    return {"banner.svg": bsvg, "divider.svg": divider, "about-card.svg": card, "skills.svg": ssvg}
