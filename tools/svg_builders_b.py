#!/usr/bin/env python3
"""SVG asset builders for designs 12-20."""
import math
import random
from svgkit import *  # noqa
import svgkit as K



def _status_dot(x, y, color="#39D353"):
    return (circle(x, y, 5, fill=color) +
            K.animate_on(circle(x, y, 8, fill="none", stroke=color, sw=1.5, opacity=0.6),
                         anim("r", "7;11;7", "2.4s"), anim("opacity", "0.6;0;0.6", "2.4s")))

# =====================================================================
# pixel font: 5x7 bitmap for A-Z 0-9 space . , ! -
# =====================================================================
GLYPHS = {
    "A": ["01110", "10001", "10001", "11111", "10001", "10001", "10001"],
    "B": ["11110", "10001", "10001", "11110", "10001", "10001", "11110"],
    "C": ["01111", "10000", "10000", "10000", "10000", "10000", "01111"],
    "D": ["11110", "10001", "10001", "10001", "10001", "10001", "11110"],
    "E": ["11111", "10000", "10000", "11110", "10000", "10000", "11111"],
    "F": ["11111", "10000", "10000", "11110", "10000", "10000", "10000"],
    "G": ["01111", "10000", "10000", "10111", "10001", "10001", "01110"],
    "H": ["10001", "10001", "10001", "11111", "10001", "10001", "10001"],
    "I": ["11111", "00100", "00100", "00100", "00100", "00100", "11111"],
    "J": ["00111", "00010", "00010", "00010", "00010", "10010", "01100"],
    "K": ["10001", "10010", "10100", "11000", "10100", "10010", "10001"],
    "L": ["10000", "10000", "10000", "10000", "10000", "10000", "11111"],
    "M": ["10001", "11011", "10101", "10101", "10001", "10001", "10001"],
    "N": ["10001", "11001", "10101", "10011", "10001", "10001", "10001"],
    "O": ["01110", "10001", "10001", "10001", "10001", "10001", "01110"],
    "P": ["11110", "10001", "10001", "11110", "10000", "10000", "10000"],
    "Q": ["01110", "10001", "10001", "10001", "10101", "10010", "01101"],
    "R": ["11110", "10001", "10001", "11110", "10100", "10010", "10001"],
    "S": ["01111", "10000", "10000", "01110", "00001", "00001", "11110"],
    "T": ["11111", "00100", "00100", "00100", "00100", "00100", "00100"],
    "U": ["10001", "10001", "10001", "10001", "10001", "10001", "01110"],
    "V": ["10001", "10001", "10001", "10001", "10001", "01010", "00100"],
    "W": ["10001", "10001", "10001", "10101", "10101", "11011", "10001"],
    "X": ["10001", "10001", "01010", "00100", "01010", "10001", "10001"],
    "Y": ["10001", "10001", "01010", "00100", "00100", "00100", "00100"],
    "Z": ["11111", "00001", "00010", "00100", "01000", "10000", "11111"],
    "0": ["01110", "10001", "10011", "10101", "11001", "10001", "01110"],
    "1": ["00100", "01100", "00100", "00100", "00100", "00100", "01110"],
    "2": ["01110", "10001", "00001", "00010", "00100", "01000", "11111"],
    "3": ["11111", "00010", "00100", "00010", "00001", "10001", "01110"],
    "4": ["00010", "00110", "01010", "10010", "11111", "00010", "00010"],
    "5": ["11110", "10000", "11110", "00001", "00001", "10001", "01110"],
    "6": ["00110", "01000", "10000", "11110", "10001", "10001", "01110"],
    "7": ["11111", "00001", "00010", "00100", "01000", "01000", "01000"],
    "8": ["01110", "10001", "10001", "01110", "10001", "10001", "01110"],
    "9": ["01110", "10001", "10001", "01111", "00001", "00010", "01100"],
    " ": ["00000", "00000", "00000", "00000", "00000", "00000", "00000"],
    ".": ["00000", "00000", "00000", "00000", "00000", "01100", "01100"],
    ",": ["00000", "00000", "00000", "00000", "01100", "00100", "01000"],
    "!": ["00100", "00100", "00100", "00100", "00100", "00000", "00100"],
    "-": ["00000", "00000", "00000", "11111", "00000", "00000", "00000"],
}


def pixel_text(s, x, y, px=4, color="#FFFFFF"):
    """Render a string with the built-in 5x7 bitmap font. Returns SVG rects."""
    out = []
    cx = x
    for ch in s.upper():
        gl = GLYPHS.get(ch, GLYPHS[" "])
        for r_i, row in enumerate(gl):
            run = 0
            for c_i, v in enumerate(row):
                if v == "1":
                    run += 1
                else:
                    if run:
                        out.append(rect(cx + (c_i - run) * px, y + r_i * px, run * px, px, fill=color))
                        run = 0
            if run:
                out.append(rect(cx + (5 - run) * px, y + r_i * px, run * px, px, fill=color))
                run = 0
        cx += 6 * px
    return "".join(out)


def pixel_text_width(s, px=4):
    return len(s) * 6 * px - 2 * px


# =====================================================================
# 12 retro pixel
# =====================================================================
def d12(ctx):
    p = ctx["palette"]
    rnd = random.Random(12)
    stars = ""
    for i in range(26):
        sx, sy = rnd.randrange(0, 125) * 8, rnd.randrange(1, 20) * 8
        st = rect(sx, sy, 4, 4, fill=p["white"])
        st = K.animate_on(st, anim("opacity", "1;0.2;1", f"{rnd.choice([2, 3, 4])}s",
                                   begin=f"{rnd.uniform(0, 3):.1f}s", repeat="indefinite", calc="discrete"))
        stars += st
    mtn = ""
    heights = [4, 7, 5, 9, 6, 10, 8, 5, 7, 4, 6, 3]
    bx = 0
    for hi, hgt in enumerate(heights):
        for step in range(hgt):
            w = (hgt - step) * 16
            mtn += rect(bx + hi * 84 - step * 8, 300 - (step + 1) * 8, w, 8, fill=["#3D405B", "#4A4E69"][hi % 2])
    desk = rect(120, 236, 120, 8, fill=p["white"]) + rect(140, 244, 8, 40, fill=p["white"]) + rect(212, 244, 8, 40, fill=p["white"])
    mon = rect(150, 204, 56, 32, fill="#1A1C2C", stroke=p["green"], sw=4) + rect(158, 212, 40, 16, fill=p["cyan"] if "cyan" in p else "#4CC9F0")
    char_ = (rect(176, 164, 16, 16, fill="#FFDAB9") + rect(172, 160, 24, 6, fill=p["red"]) +
             rect(170, 180, 28, 24, fill=p["yellow"]) + rect(166, 184, 6, 14, fill=p["yellow"]) +
             rect(198, 184, 6, 14, fill=p["yellow"]))
    title = ctx["name"].upper()[:12]
    tx = 500 - pixel_text_width(title, 6) / 2
    name_px = pixel_text(title, tx, 60, px=6, color=p["yellow"])
    sub = pixel_text(ctx["role"].upper()[:18], 500 - pixel_text_width(ctx["role"].upper()[:18], 3) / 2, 120, px=3, color=p["white"])
    bsvg = svg_doc(1000, 300,
        rect(0, 0, 1000, 300, fill=p["bg"]) + stars + mtn + char_ + mon + desk + name_px + sub,
        "Retro pixel banner", "Pixel-art night scene with mountains and a developer at a desk.")
    hearts = ""
    for i in range(12):
        hx = 200 + i * 50
        col = [p["red"], p["yellow"], p["green"]][i % 3]
        hearts += (rect(hx + 4, 6, 6, 6, fill=col) + rect(hx + 14, 6, 6, 6, fill=col) +
                   rect(hx, 10, 24, 6, fill=col) + rect(hx + 4, 16, 16, 4, fill=col) +
                   rect(hx + 8, 20, 8, 3, fill=col))
    divider = svg_doc(1000, 24, rect(0, 0, 1000, 24, fill=p["bg"]) + hearts, "Divider", "Repeating pixel hearts.")
    dialog = (rect(0, 0, 480, 220, fill="#1A1C2C", stroke=p["white"], sw=4) +
              rect(8, 8, 464, 204, fill="none", stroke=p["white"], sw=2) +
              pixel_text("PLAYER 1", 30, 28, px=4, color=p["yellow"]) +
              pixel_text(ctx["name"].upper()[:10], 30, 62, px=4, color=p["white"]) +
              text(30, 118, "HP", size=13, fill=p["red"], family=K.MONO, weight="700", tid="hp-lbl") +
              rect(60, 106, 380, 16, fill="#111", stroke=p["white"], sw=2) +
              rect(64, 110, 372, 8, fill=p["red"]) +
              text(30, 152, "XP", size=13, fill=p["green"], family=K.MONO, weight="700", tid="xp-lbl") +
              rect(60, 140, 380, 16, fill="#111", stroke=p["white"], sw=2))
    xpfill = animate_on(rect(64, 144, 0, 8, fill=p["green"]),
                        anim("width", "0;372", "2.5s", begin="0.4s", repeat="0", fill="freeze"))
    card = svg_doc(480, 220, dialog + xpfill +
                   pixel_text("LV 2023+", 30, 176, px=3, color=p["white"]),
                   "Pixel dialog card", "RPG dialog box with HP/XP bars.")
    tiles = ""
    labels = ctx["stack_labels"]
    for i, ic in enumerate(ctx["stack_icons"][:12]):
        tx2 = 20 + i * 82
        col = [p["yellow"], p["red"], p["green"], p["white"]][i % 4]
        tiles += rect(tx2, 24, 64, 64, fill="#1A1C2C", stroke=col, sw=4) + \
                 icon(ic, tx2 + 8, 32, color=col, size=48, scale=1.0) + \
                 pixel_text(labels[i][:4].upper(), tx2 + 6, 96, px=2, color=p["white"])
    ssvg = svg_doc(1000, 120, rect(0, 0, 1000, 120, fill=p["bg"]) + tiles, "Pixel skills", "32px-style icon tiles.")
    return {"banner.svg": bsvg, "divider.svg": divider, "about-card.svg": card, "skills.svg": ssvg}


# =====================================================================
# 13 pastel soft
# =====================================================================
def blob(cx, cy, r, color, dur, drift, opacity=0.7, blurid="bblur"):
    b = circle(cx, cy, r, fill=color, opacity=opacity, blur=blurid)
    return K.animate_on(b, anim_transform_translate(f"0,0;{drift[0]},{drift[1]};0,0", dur))


def d13(ctx):
    p = ctx["palette"]
    dark = ctx.get("dark", False)
    bg = p["bg_dark"] if dark else p["bg"]
    txt = "#F3EAF5" if dark else p["text"]
    D = defs(fe_gaussian_blur("bblur", 22))
    blobs = (blob(140, 80, 90, p["pink"], "12s", (40, 25)) +
             blob(860, 90, 100, p["blue"], "14s", (-35, 30)) +
             blob(500, 260, 80, p["lilac"], "10s", (30, -22)) +
             blob(240, 250, 60, p["mint"], "13s", (-28, -18)))
    sparkles = ""
    rnd = random.Random(13)
    for i in range(8):
        sx, sy = rnd.randrange(80, 920), rnd.randrange(40, 260)
        sp = path(f"M{sx} {sy - 8} L{sx + 3} {sy - 3} L{sx + 8} {sy} L{sx + 3} {sy + 3} L{sx} {sy + 8} L{sx - 3} {sy + 3} L{sx - 8} {sy} L{sx - 3} {sy - 3} Z",
                  fill="#FFFFFF" if not dark else p["lilac"])
        sp = K.animate_on(sp, anim("opacity", "0.2;1;0.2", f"{rnd.choice([2.5, 3, 4])}s",
                                   begin=f"{rnd.uniform(0, 3):.1f}s", repeat="indefinite"))
        sparkles += sp
    name_sh = text(500, 150, ctx["name"], size=40, fill=txt, anchor="middle", weight="700", blur="nsh", tid="banner-name")
    D2 = defs(fe_drop_shadow("nsh", 0, 3, 6, p["lilac"], 0.5))
    body = [rect(0, 0, 1000, 300, fill=bg), blobs, sparkles, name_sh,
            text(500, 192, ctx["tagline"], size=16, fill=txt, opacity=0.8, anchor="middle", tid="banner-tagline"),
            text(500, 224, ctx["role"], size=14, fill=p["lilac"] if not dark else p["pink"], anchor="middle", weight="600", tid="banner-role")]
    bsvg = svg_doc(1000, 300, D + D2 + "".join(body), "Pastel banner", "Drifting pastel blobs with sparkles.")
    divider = svg_doc(1000, 24, circle(470, 12, 5, fill=p["pink"]) + circle(500, 12, 5, fill=p["blue"]) +
                      circle(530, 12, 5, fill=p["lilac"]), "Divider", "Three pastel dots.")
    card = svg_doc(480, 220,
        defs(linear_gradient("pg", [("0%", p["pink"]), ("50%", p["blue"]), ("100%", p["lilac"])]) +
             fe_gaussian_blur("bblur2", 18)) +
        rect(0, 0, 480, 220, fill=bg, rx=24) + rect(0, 0, 480, 220, fill="url(#pg)", rx=24, opacity=0.5) +
        circle(76, 88, 34, fill=bg if not dark else "#241F2C", stroke="#FFFFFF", sw=3, dash="6 6") +
        text(76, 97, ctx["initial"], size=26, fill=txt, anchor="middle", weight="700", tid="card-initial") +
        text(134, 80, ctx["name"], size=21, fill=txt, weight="700", tid="card-name") +
        text(134, 104, ctx["role"], size=13, fill=txt, opacity=0.85, tid="card-role") +
        _status_dot(46, 156, "#7BC96F") + text(60, 161, ctx["status"], size=13, fill=txt, tid="card-status") +
        text(46, 194, "@" + ctx["username"], size=12, fill=txt, opacity=0.8, family=K.MONO, tid="card-user"),
        "Pastel about card", "Gradient card with dashed avatar ring.")
    tiles = ""
    pastels = [p["pink"], p["blue"], p["lilac"], p["mint"]]
    x = 40
    for i, ic in enumerate(ctx["stack_icons"]):
        c = pastels[i % 4]
        tiles += circle(x + 24, 60, 30, fill=c, opacity=0.55) + icon(ic, x, 36, color="#5B4A63" if not dark else "#2A2433", size=48, scale=0.85)
        x += 80
    ssvg = svg_doc(1000, 120, rect(0, 0, 1000, 120, fill=bg) + tiles, "Pastel skills", "Round tiles in alternating pastels.")
    return {"banner.svg": bsvg, "divider.svg": divider, "about-card.svg": card, "skills.svg": ssvg}


# =====================================================================
# 14 sunset gradient
# =====================================================================
def d14(ctx):
    p = ctx["palette"]
    D = defs(linear_gradient("sky", [("0%", p["o"]), ("35%", p["p1"]), ("70%", p["p2"]), ("100%", p["deep"])],
                             x1="0%", y1="0%", x2="0%", y2="100%") +
             radial_gradient("sunr", [("0%", "#FFF3C4"), ("100%", p["sun"])]) +
             fe_gaussian_blur("sunglow", 10))
    sun = g(circle(500, 210, 70, fill="url(#sunr)") + circle(500, 210, 84, fill=p["sun"], opacity=0.35, blur="sunglow"),
            tid="banner-sun")
    sun = K.animate_on(sun, anim_transform_translate("0,14;0,-14;0,14", "12s"))
    hills = (path("M0 300 L0 250 Q 150 200 320 248 T 640 240 T 1000 252 L1000 300 Z", fill=p["p2"], opacity=0.85) +
             path("M0 300 L0 272 Q 220 232 430 270 T 780 262 T 1000 276 L1000 300 Z", fill="#5A2A6E", opacity=0.9) +
             path("M0 300 L0 288 Q 300 262 560 288 T 1000 286 L1000 300 Z", fill=p["deep"]))
    birds = ""
    for bi, (yy, dd, off) in enumerate([(90, 20, "0s"), (120, 26, "3s"), (78, 18, "7s")]):
        bird = path(f"M0 0 q {dd // 2} {-dd // 2} {dd} 0 q {dd // 2} {-dd // 2} {dd} 0", stroke="#3A1C4A", sw=2.5, fill="none", scap="round")
        mv = f'<animateMotion path="M-60 {yy} L1060 {yy - 12}" dur="{20 + bi * 4}s" begin="-{off}" repeatCount="indefinite"/>'
        birds += K.animate_on(bird, mv)
    body = [rect(0, 0, 1000, 300, fill="url(#sky)"), sun,
            text(500, 120, ctx["name"], size=44, fill=p["text"], anchor="middle", weight="700", tid="banner-name"),
            text(500, 156, ctx["tagline"], size=16, fill=p["text"], opacity=0.92, anchor="middle", tid="banner-tagline"),
            birds, hills]
    bsvg = svg_doc(1000, 300, D + "".join(body), "Sunset banner", "Half sun rising over layered silhouette hills.")
    divider = svg_doc(1000, 24,
        defs(linear_gradient("hg", [("0%", p["o"]), ("50%", p["p1"]), ("100%", p["p2"])], x1="0%", y1="0%", x2="100%", y2="0%")) +
        line(0, 12, 1000, 12, stroke="url(#hg)", sw=3) + circle(500, 12, 5, fill=p["sun"]),
        "Divider", "Horizon line with sun dot.")
    card = svg_doc(480, 220,
        defs(linear_gradient("cg", [("0%", p["p1"]), ("100%", p["p2"])], x1="0%", y1="0%", x2="0%", y2="100%")) +
        rect(0, 0, 480, 220, fill="url(#cg)", rx=16) +
        rect(20, 20, 440, 180, fill="#FFFFFF", opacity=0.18, rx=12, stroke="#FFFFFF", sw=1) +
        circle(76, 88, 32, fill="#FFFFFF", opacity=0.25, stroke="#FFFFFF", sw=2) +
        text(76, 97, ctx["initial"], size=24, fill=p["text"], anchor="middle", weight="700", tid="card-initial") +
        text(132, 80, ctx["name"], size=20, fill=p["text"], weight="700", tid="card-name") +
        text(132, 104, ctx["role"], size=13, fill=p["text"], opacity=0.9, tid="card-role") +
        _status_dot(48, 152, "#FFE29A") + text(62, 157, ctx["status"], size=13, fill=p["text"], tid="card-status") +
        text(48, 188, "@" + ctx["username"], size=12, fill=p["text"], opacity=0.9, family=K.MONO, tid="card-user"),
        "Sunset about card", "Translucent white card over gradient.")
    pills = ""
    x = 40
    for ic in ctx["stack_icons"]:
        pills += rect(x - 6, 26, 68, 68, fill="#FFFFFF", opacity=0.16, rx=34, stroke="#FFFFFF", sw=1) + \
                 icon(ic, x + 4, 40, color="#FFFFFF", size=48, scale=0.75)
        x += 80
    ssvg = svg_doc(1000, 120, rect(0, 0, 1000, 120, fill=p["deep"]) + pills, "Sunset skills", "White icons on translucent pills.")
    return {"banner.svg": bsvg, "divider.svg": divider, "about-card.svg": card, "skills.svg": ssvg}


# =====================================================================
# 15 neon dark
# =====================================================================
def d15(ctx):
    p = ctx["palette"]
    D = defs(fe_gaussian_blur("nglow15", 5))
    name = ctx["name"]
    nw = K.tw(name, 46, mono=False)
    boxw = int(nw + 120)
    bx = 500 - boxw // 2
    glow_box = rect(bx, 84, boxw, 110, fill="none", stroke=p["cyan"], sw=3, rx=18, opacity=0.55, blur="nglow15")
    solid_box = rect(bx, 84, boxw, 110, fill="none", stroke=p["cyan"], sw=2, rx=18)
    # one letter flickers: split name into tspans
    mid = len(name) // 2
    tsp = (f'<text x="500" y="152" text-anchor="middle" font-family="{K.SANS}" font-size="46" font-weight="700" fill="{p["text"]}">'
           f'{esc(name[:mid])}'
           f'<tspan id="flicker-letter">{esc(name[mid])}'
           f'<animate attributeName="opacity" values="1;1;0.15;1;0.3;1;1;0.1;1" keyTimes="0;0.6;0.63;0.66;0.7;0.73;0.9;0.93;1" dur="7s" repeatCount="indefinite" calcMode="discrete"/>'
           f'</tspan>{esc(name[mid + 1:])}</text>')
    body = [rect(0, 0, 1000, 300, fill=p["bg"]), glow_box, solid_box, tsp,
            text(500, 226, ctx["role"].upper(), size=15, fill=p["green"], anchor="middle", spacing=6, family=K.MONO, tid="banner-role"),
            text(500, 254, ctx["tagline"], size=13, fill=p["magenta"], anchor="middle", tid="banner-tagline")]
    bsvg = svg_doc(1000, 300, D + "".join(body), "Neon dark banner", "Name in a glowing neon box, one letter flickers.")
    capL = rect(96, 6, 4, 12, fill=p["cyan"])
    capR = rect(900, 6, 4, 12, fill=p["cyan"])
    divider = svg_doc(1000, 24, line(100, 12, 900, 12, stroke=p["cyan"], sw=2, opacity=0.8) + capL + capR,
                      "Divider", "Neon line with end caps.")
    cyc = ";".join([p["cyan"], p["green"], p["magenta"], p["cyan"]])
    border = rect(10, 10, 460, 200, fill="#101010", rx=14, stroke=p["cyan"], sw=2)
    border = K.animate_on(border, anim("stroke", cyc, "12s", repeat="indefinite", calc="discrete",
                                       keytimes="0;0.33;0.66;1"))
    glow_b = rect(10, 10, 460, 200, fill="none", rx=14, stroke=p["cyan"], sw=4, opacity=0.4, blur="nglow15")
    glow_b = K.animate_on(glow_b, anim("stroke", cyc, "12s", repeat="indefinite", calc="discrete", keytimes="0;0.33;0.66;1"))
    card = svg_doc(480, 220, D + rect(0, 0, 480, 220, fill=p["bg"]) + glow_b + border +
                   text(40, 60, ctx["name"], size=24, fill=p["text"], weight="700", tid="card-name") +
                   text(40, 92, ctx["role"], size=14, fill=p["green"], family=K.MONO, tid="card-role") +
                   _status_dot(46, 128, p["green"]) + text(60, 133, ctx["status"], size=13, fill=p["text"], tid="card-status") +
                   text(40, 172, "@" + ctx["username"], size=13, fill=p["magenta"], family=K.MONO, tid="card-user"),
                   "Neon about card", "Dark card with cycling neon border.")
    icons = ""
    x = 60
    cols = [p["cyan"], p["green"], p["magenta"]]
    for i, ic in enumerate(ctx["stack_icons"]):
        c = cols[i % 3]
        icons += icon(ic, x, 28, color=c, size=48, scale=0.8) + line(x + 4, 82, x + 42, 82, stroke=c, sw=2, opacity=0.7)
        x += 76
    ssvg = svg_doc(1000, 120, rect(0, 0, 1000, 120, fill=p["bg"]) + icons, "Neon skills", "Icons with neon underlines.")
    return {"banner.svg": bsvg, "divider.svg": divider, "about-card.svg": card, "skills.svg": ssvg}


# =====================================================================
# 16 space galaxy
# =====================================================================
def d16(ctx):
    p = ctx["palette"]
    rnd = random.Random(16)
    stars = ""
    for i in range(80):
        sx, sy = rnd.randrange(6, 994), rnd.randrange(6, 294)
        r = rnd.choice([1, 1.5, 2.5])
        st = circle(sx, sy, r, fill=p["star"])
        st = K.animate_on(st, anim("opacity", "0.3;1;0.3", f"{rnd.uniform(2, 5):.1f}s",
                                   begin=f"{rnd.uniform(0, 4):.1f}s", repeat="indefinite"))
        stars += st
    D = defs(radial_gradient("gal", [("0%", "#FFFFFF", 0.9), ("25%", p["violet"], 0.7), ("70%", p["indigo"], 0.35), ("100%", p["indigo"], 0)]))
    arms = ""
    for k in range(4):
        e = ellipse(210, 150, 120 - k * 22, 46 - k * 9, fill="none", stroke=p["violet"], sw=2 + k, opacity=0.28 - k * 0.04, rot=30 + k * 40)
        arms += e
    gal = g(circle(210, 150, 34, fill="url(#gal)") + arms, tid="galaxy")
    gal = K.animate_on(gal, '<animateTransform attributeName="transform" type="rotate" values="0 210 150;360 210 150" dur="120s" repeatCount="indefinite"/>')
    planet = (circle(830, 90, 34, fill=p["indigo"]) + circle(830, 90, 34, fill=p["violet"], opacity=0.35) +
              ellipse(830, 90, 58, 14, fill="none", stroke=p["pink"], sw=3, opacity=0.8, rot=-18))
    shoot = ('<g id="shooting-star">'
             '<animateMotion path="M-80 40 L1080 190" dur="9s" repeatCount="indefinite"/>'
             '<animate attributeName="opacity" values="0;1;1;0" keyTimes="0;0.05;0.3;0.45" dur="9s" repeatCount="indefinite"/>' +
             path("M0 0 L70 0", stroke="#FFFFFF", sw=2, opacity=0.7) + circle(70, 0, 3, fill="#FFFFFF") + "</g>")
    body = [rect(0, 0, 1000, 300, fill=p["bg"]), stars, gal, planet, shoot,
            text(500, 150, ctx["name"], size=40, fill="#F8FAFC", anchor="middle", weight="300", spacing=4, tid="banner-name"),
            text(500, 190, ctx["tagline"], size=15, fill=p["violet"], anchor="middle", tid="banner-tagline"),
            text(500, 220, ctx["role"], size=13, fill=p["pink"], anchor="middle", spacing=3, family=K.MONO, tid="banner-role")]
    bsvg = svg_doc(1000, 300, D + "".join(body), "Galaxy banner", "Stars, spiral galaxy, ringed planet, shooting star.")
    dstars = ""
    for i in range(20):
        dstars += circle(100 + i * 42, 12, 1.6, fill=p["star"], opacity=0.8)
    divider = svg_doc(1000, 24, line(100, 12, 900, 12, stroke=p["indigo"], sw=1, opacity=0.5) + dstars,
                      "Divider", "Line of tiny stars.")
    card = svg_doc(480, 220,
        rect(0, 0, 480, 220, fill="#0A0A24", stroke=p["indigo"], sw=1, rx=14) +
        "".join(circle(rnd.randrange(10, 470), rnd.choice([12, 208]), 1.4, fill=p["star"], opacity=0.7) for _ in range(14)) +
        circle(76, 84, 32, fill="#12122e", stroke=p["violet"], sw=2) +
        text(76, 93, ctx["initial"], size=24, fill=p["pink"], anchor="middle", weight="700", tid="card-initial") +
        text(130, 76, ctx["name"], size=20, fill="#F8FAFC", weight="600", tid="card-name") +
        text(130, 100, ctx["role"], size=13, fill=p["violet"], tid="card-role") +
        _status_dot(46, 150, p["pink"]) + text(60, 155, ctx["status"], size=13, fill="#E2E8F0", tid="card-status") +
        text(46, 190, "@" + ctx["username"], size=12, fill=p["indigo"], family=K.MONO, tid="card-user"),
        "Galaxy about card", "Dark card with star-dust corners.")
    orbit = ""
    cx, cy = 500, 60
    ring_defs = []
    for ri, (rr, cnt, durdir) in enumerate([(46, 6, "60s"), (78, 6, "-80s")]):
        orbit += circle(cx, cy, rr, fill="none", stroke=p["indigo"], sw=1, opacity=0.35)
        inner = ""
        for ii in range(cnt):
            ang = ii * (360 / cnt)
            ix = cx + rr * math.cos(math.radians(ang))
            iy = cy + rr * math.sin(math.radians(ang))
            col = [p["violet"], p["pink"], "#FFFFFF"][ii % 3]
            inner += icon(ctx["stack_icons"][ri * cnt + ii], ix - 12, iy - 12, color=col, size=48, scale=0.5)
        deg = -360 if durdir.startswith("-") else 360
        grp = f'<g id="orbit{ri}">{inner}<animateTransform attributeName="transform" type="rotate" values="0 {cx} {cy};{deg} {cx} {cy}" dur="{durdir.lstrip("-")}" repeatCount="indefinite"/></g>'
        orbit += grp
    ssvg = svg_doc(1000, 120, rect(0, 0, 1000, 120, fill=p["bg"]) + orbit, "Orbit skills", "Icons on two slowly rotating orbit rings.")
    return {"banner.svg": bsvg, "divider.svg": divider, "about-card.svg": card, "skills.svg": ssvg}


# =====================================================================
# 17 ocean blue
# =====================================================================
def d17(ctx):
    p = ctx["palette"]
    D = defs(linear_gradient("sea", [("0%", p["light"]), ("55%", p["mid"]), ("100%", p["deep"])], x1="0%", y1="0%", x2="0%", y2="100%"))
    waves = ""
    for li, (amp, wl, yb, op, dur) in enumerate([(10, 240, 150, 0.25, "9s"), (14, 320, 175, 0.35, "13s"),
                                                  (18, 420, 205, 0.5, "17s"), (22, 520, 240, 0.7, "21s")]):
        w = path(wave_band_path(1000, amp, yb, wl, li, fill_to=300), fill=p["foam"], opacity=op)
        waves += K.animate_on(w, anim_transform_translate("0,0;-1000,0", dur))
    bubbles = ""
    rnd = random.Random(17)
    for bi in range(10):
        bx = rnd.randrange(40, 960)
        r = rnd.choice([3, 4, 6])
        b = circle(bx, 300, r, fill="none", stroke=p["foam"], sw=1.5, opacity=0.6)
        b = K.animate_on(b,
            anim_transform_translate(f"0,0;{rnd.randint(-30, 30)},-320", f"{rnd.uniform(6, 12):.1f}s", begin=f"-{rnd.uniform(0, 8):.1f}s"),
            anim("opacity", "0.6;0.6;0", f"{rnd.uniform(6, 12):.1f}s", begin=f"-{rnd.uniform(0, 8):.1f}s", repeat="indefinite"))
        bubbles += b
    fish = ('<g id="fish"><animateMotion path="M1060 120 C 700 90, 400 160, -60 120" dur="24s" repeatCount="indefinite"/>' +
            path("M0 0 q 14 -10 30 0 q -16 10 -30 0 Z M30 0 l 12 -8 v 16 z", fill=p["foam"], opacity=0.85) + "</g>")
    body = [rect(0, 0, 1000, 300, fill="url(#sea)"), bubbles, fish, waves,
            text(500, 100, ctx["name"], size=44, fill=p["foam"], anchor="middle", weight="700", tid="banner-name"),
            text(500, 134, ctx["tagline"], size=16, fill=p["foam"], opacity=0.9, anchor="middle", tid="banner-tagline")]
    bsvg = svg_doc(1000, 300, D + "".join(body), "Ocean banner", "Four wave layers, bubbles and a passing fish.")
    wl = path(sine_wave_path(1000, 4, 12, 120), stroke=p["light"], sw=2, fill="none")
    divider = svg_doc(1000, 24, wl, "Divider", "Foam-line wave.")
    caustics = ""
    for ci in range(4):
        cp = path(f"M{20 + ci * 120} 40 q 40 20 80 0 q 40 -20 80 0", stroke="#BFE9FF", sw=1.5, fill="none", opacity=0.25)
        caustics += K.animate_on(cp, anim("opacity", "0.1;0.35;0.1", f"{4 + ci}s", repeat="indefinite"))
    card = svg_doc(480, 220,
        rect(0, 0, 480, 220, fill=p["mid"], rx=16, opacity=0.9) +
        rect(0, 0, 480, 220, fill="none", stroke=p["foam"], sw=1, rx=16, opacity=0.5) + caustics +
        circle(76, 88, 32, fill=p["deep"], stroke=p["foam"], sw=2) +
        text(76, 97, ctx["initial"], size=24, fill=p["foam"], anchor="middle", weight="700", tid="card-initial") +
        text(132, 80, ctx["name"], size=20, fill=p["foam"], weight="700", tid="card-name") +
        text(132, 104, ctx["role"], size=13, fill="#BFE9FF", tid="card-role") +
        _status_dot(48, 152, p["foam"]) + text(62, 157, ctx["status"], size=13, fill=p["foam"], tid="card-status") +
        text(48, 192, "@" + ctx["username"], size=12, fill="#BFE9FF", family=K.MONO, tid="card-user"),
        "Ocean about card", "Glassy water-blue card with caustic lines.")
    icons = ""
    x = 50
    for i, ic in enumerate(ctx["stack_icons"]):
        bub = g(circle(x + 24, 60, 30, fill=p["light"], opacity=0.4, stroke=p["foam"], sw=1) +
                icon(ic, x, 36, color=p["foam"], size=48, scale=0.8))
        bub = K.animate_on(bub, anim_transform_translate("0,0;0,-3;0,0", "3s", begin=f"{i * 0.2:.1f}s"))
        icons += bub
        x += 80
    ssvg = svg_doc(1000, 120, rect(0, 0, 1000, 120, fill=p["deep"]) + icons, "Ocean skills", "Icons on bobbing bubbles.")
    return {"banner.svg": bsvg, "divider.svg": divider, "about-card.svg": card, "skills.svg": ssvg}


# =====================================================================
# 18 forest green
# =====================================================================
def pine_tree(x, base, hgt, wdt, color, sway=None):
    t1 = path(f"M{x} {base - hgt} L{x - wdt / 2} {base - hgt * 0.45} L{x + wdt / 2} {base - hgt * 0.45} Z", fill=color)
    t2 = path(f"M{x} {base - hgt * 0.72} L{x - wdt * 0.62 / 2} {base - hgt * 0.18} L{x + wdt * 0.62 / 2} {base - hgt * 0.18} Z", fill=color)
    trunk = rect(x - 4, base - hgt * 0.2, 8, hgt * 0.2, fill=color)
    grp = "<g>" + trunk + t2 + t1
    if sway:
        grp += f'<animateTransform attributeName="transform" type="rotate" values="-1 {x} {base};1 {x} {base};-1 {x} {base}" dur="{sway}" repeatCount="indefinite"/>'
    grp += "</g>"
    return grp


def d18(ctx):
    p = ctx["palette"]
    D = defs(fe_gaussian_blur("mist", 8) + fe_gaussian_blur("moong", 12))
    moon = circle(880, 70, 30, fill="#FDF6DC") + circle(880, 70, 40, fill="#FDF6DC", opacity=0.25, blur="moong")
    far = "".join(pine_tree(60 + i * 130, 300, 120, 70, "#0B2E1A", sway="9s") for i in range(8))
    mid = "".join(pine_tree(30 + i * 150, 300, 160, 90, p["pine"], sway="7s") for i in range(7))
    near = "".join(pine_tree(90 + i * 210, 300, 210, 120, "#0A331F", sway="5s") for i in range(5))
    fireflies = ""
    rnd = random.Random(18)
    for fi in range(9):
        fx, fy = rnd.randrange(120, 880), rnd.randrange(120, 260)
        ff = circle(fx, fy, 2.5, fill="#FDE68A")
        ff = K.animate_on(ff,
            anim("opacity", "0;1;0.2;1;0", f"{rnd.uniform(2.5, 5):.1f}s", begin=f"{rnd.uniform(0, 4):.1f}s", repeat="indefinite"),
            anim_transform_translate(f"0,0;{rnd.randint(-18, 18)},{rnd.randint(-14, 14)};0,0", f"{rnd.uniform(6, 11):.1f}s", begin=f"{rnd.uniform(0, 3):.1f}s"))
        fireflies += ff
    mistband = K.animate_on(rect(0, 200, 1000, 26, fill="#FFFFFF", opacity=0.10, blur="mist"),
                            anim_transform_translate("0,0;60,0;0,0", "16s"))
    body = [rect(0, 0, 1000, 300, fill=p["bg"]), moon, far, mid, mistband, near, fireflies,
            text(500, 100, ctx["name"], size=42, fill=p["text"], anchor="middle", weight="700", tid="banner-name"),
            text(500, 136, ctx["tagline"], size=16, fill=p["light"], anchor="middle", tid="banner-tagline")]
    bsvg = svg_doc(1000, 300, D + "".join(body), "Forest banner", "Layered pines with parallax sway, fireflies, moon and mist.")
    trees = ""
    for ti in range(10):
        tx = 200 + ti * 60
        trees += path(f"M{tx} 4 L{tx - 8} 18 L{tx + 8} 18 Z", fill=p["green"], opacity=0.8)
    divider = svg_doc(1000, 24, line(100, 20, 900, 20, stroke=p["pine"], sw=1) + trees, "Divider", "Tiny tree row.")
    grain = "".join(path(f"M20 {yy} q 220 {4 if yy % 3 else -4} 440 0", stroke="#5E4327", sw=1, fill="none", opacity=0.35) for yy in range(40, 220, 26))
    card = svg_doc(480, 220,
        rect(0, 0, 480, 220, fill="#6B4E2E", rx=14) +
        rect(10, 10, 460, 200, fill="#7C5A3A", rx=10) + grain +
        rect(24, 24, 432, 172, fill="#0F3D22", rx=8, stroke="#D8B98C", sw=2) +
        text(48, 68, ctx["name"], size=22, fill=p["text"], weight="700", tid="card-name") +
        text(48, 96, ctx["role"], size=13, fill=p["light"], family=K.MONO, tid="card-role") +
        _status_dot(52, 128, p["green"]) + text(66, 133, ctx["status"], size=13, fill=p["text"], tid="card-status") +
        text(48, 168, "@" + ctx["username"], size=12, fill=p["light"], family=K.MONO, tid="card-user"),
        "Wooden sign card", "About card styled as a wooden trail sign.")
    tiles = ""
    x = 40
    for i, ic in enumerate(ctx["stack_icons"]):
        c = [p["green"], p["light"], p["pine"]][i % 3]
        tiles += path(f"M{x} 24 q 48 0 48 48 q 0 48 -48 48 q -24 0 -24 -24 q 0 -48 24 -72 Z", fill=c, opacity=0.28, stroke=c, sw=1) + \
                 icon(ic, x + 4, 36, color=p["text"], size=48, scale=0.75)
        x += 80
    ssvg = svg_doc(1000, 120, rect(0, 0, 1000, 120, fill=p["bg"]) + tiles, "Leaf skills", "Leaf-shaped tiles with icons.")
    return {"banner.svg": bsvg, "divider.svg": divider, "about-card.svg": card, "skills.svg": ssvg}


# =====================================================================
# 19 glassmorphism
# =====================================================================
def glass_panel(x, y, w, h, rx=18):
    hl = defs(linear_gradient("ghl", [("0%", "#FFFFFF", 0.35), ("100%", "#FFFFFF", 0)]))
    return (hl + rect(x, y, w, h, fill="#FFFFFF", opacity=0.18, rx=rx, stroke="#FFFFFF", sw=1) +
            rect(x + 1, y + 1, w - 2, h * 0.35, fill="url(#ghl)", rx=rx - 2, opacity=0.5))


def d19(ctx):
    p = ctx["palette"]
    D = defs(fe_gaussian_blur("bbg", 30) +
             linear_gradient("gbg", [("0%", p["bg1"]), ("100%", p["bg2"])], x1="0%", y1="0%", x2="100%", y2="100%"))
    blobs = (blob(220, 90, 110, p["blob1"], "14s", (60, 40), opacity=0.8, blurid="bbg") +
             blob(780, 210, 120, p["blob2"], "12s", (-50, -30), opacity=0.8, blurid="bbg") +
             blob(520, 60, 70, p["blob1"], "10s", (30, 50), opacity=0.6, blurid="bbg"))
    panel = glass_panel(150, 70, 700, 160, rx=20)
    body = [rect(0, 0, 1000, 300, fill="url(#gbg)"), blobs, panel,
            text(500, 140, ctx["name"], size=40, fill=p["text"], anchor="middle", weight="700", tid="banner-name"),
            text(500, 176, ctx["tagline"], size=16, fill=p["text"], opacity=0.9, anchor="middle", tid="banner-tagline"),
            text(500, 206, ctx["role"], size=13, fill=p["text"], opacity=0.75, anchor="middle", family=K.MONO, tid="banner-role")]
    bsvg = svg_doc(1000, 300, D + "".join(body), "Glass banner", "Frosted panel over drifting blurred blobs (imitation).")
    pill = glass_panel(300, 2, 400, 20, rx=10)
    divider = svg_doc(1000, 24, defs(linear_gradient("gbg2", [("0%", p["bg1"]), ("100%", p["bg2"])])) +
                      rect(0, 0, 1000, 24, fill="url(#gbg2)") + pill, "Divider", "Glass pill.")
    card = svg_doc(480, 220,
        defs(fe_gaussian_blur("bc", 24) + linear_gradient("gc", [("0%", p["bg1"]), ("100%", p["bg2"])])) +
        rect(0, 0, 480, 220, fill="url(#gc)", rx=16) +
        blob(390, 170, 90, p["blob1"], "12s", (-20, -14), opacity=0.9, blurid="bc") +
        blob(90, 60, 70, p["blob2"], "10s", (16, 12), opacity=0.8, blurid="bc") +
        glass_panel(24, 24, 432, 172, rx=16) +
        circle(76, 88, 30, fill="#FFFFFF", opacity=0.25, stroke="#FFFFFF", sw=1.5) +
        text(76, 97, ctx["initial"], size=22, fill=p["text"], anchor="middle", weight="700", tid="card-initial") +
        text(128, 80, ctx["name"], size=19, fill=p["text"], weight="700", tid="card-name") +
        text(128, 104, ctx["role"], size=13, fill=p["text"], opacity=0.85, tid="card-role") +
        _status_dot(48, 150, "#6EE7B7") + text(62, 155, ctx["status"], size=13, fill=p["text"], tid="card-status") +
        text(48, 184, "@" + ctx["username"], size=12, fill=p["text"], opacity=0.8, family=K.MONO, tid="card-user"),
        "Glass about card", "Smaller glass card overlapping a blob.")
    tiles = ""
    x = 30
    for ic in ctx["stack_icons"]:
        tiles += rect(x, 20, 72, 80, fill="#FFFFFF", opacity=0.16, rx=14, stroke="#FFFFFF", sw=1) + \
                 rect(x + 1, 21, 70, 26, fill="#FFFFFF", opacity=0.12, rx=12) + \
                 icon(ic, x + 12, 32, color=p["text"], size=48, scale=0.85)
        x += 82
    ssvg = svg_doc(1000, 120, defs(linear_gradient("gs", [("0%", p["bg1"]), ("100%", p["bg2"])]) + fe_gaussian_blur("bs", 20)) +
                   rect(0, 0, 1000, 120, fill="url(#gs)") +
                   circle(200, 30, 60, fill=p["blob1"], opacity=0.7, blur="bs") +
                   circle(700, 100, 70, fill=p["blob2"], opacity=0.7, blur="bs") + tiles,
                   "Glass skills", "Row of glass tiles.")
    return {"banner.svg": bsvg, "divider.svg": divider, "about-card.svg": card, "skills.svg": ssvg}


# =====================================================================
# 20 portfolio pro
# =====================================================================
def d20(ctx):
    p = ctx["palette"]
    dark = ctx.get("dark", False)
    bg = p["bg_dark"] if dark else p["bg"]
    text_c = p["text_dark"] if dark else p["text"]
    slate = "#94A3B8" if dark else p["slate"]
    css = REDUCED + ".fadein{animation:fi 1s ease both}\n@keyframes fi{from{opacity:0}to{opacity:1}}\n"
    chips = ""
    cx = 60
    for lab in ctx["facts"]:
        wd = K.tw(lab, 14, mono=False) + 28
        chips += rect(cx, 210, wd, 34, fill=p["navy"] if not dark else "#16233B", rx=17) + \
                 text(cx + wd / 2, 232, lab, size=14, fill="#FFFFFF", anchor="middle", tid=f"fact-{lab}")
        cx += wd + 14
    body = [rect(0, 0, 1000, 300, fill=bg),
            rect(0, 0, 8, 300, fill=p["blue"]),
            g(text(60, 120, ctx["name"], size=40, fill=text_c, weight="600", tid="banner-name"), cls="fadein"),
            g(text(60, 158, ctx["role"], size=19, fill=p["blue"] if not dark else "#60A5FA", weight="600", tid="banner-role"), cls="fadein"),
            g(text(60, 190, ctx["value"], size=15, fill=slate, tid="banner-value"), cls="fadein"),
            g(chips, cls="fadein")]
    bsvg = svg_doc(1000, 300, style_block(css) + "".join(body), "Portfolio pro banner", "Calm navy professional banner.")
    divider = svg_doc(1000, 24, line(60, 12, 940, 12, stroke=p["border"] if not dark else "#243146", sw=1),
                      "Divider", "Thin slate line.")
    card = svg_doc(480, 220,
        rect(0, 0, 480, 220, fill=bg) +
        rect(16, 16, 448, 188, fill="#F8FAFC" if not dark else "#111C31", rx=12, stroke=p["border"] if not dark else "#243146", sw=1) +
        circle(72, 84, 30, fill=p["navy"] if not dark else "#16233B") +
        text(72, 93, ctx["initial2"], size=20, fill="#FFFFFF", anchor="middle", weight="700", tid="card-initials") +
        text(122, 76, ctx["name"], size=20, fill=text_c, weight="700", tid="card-name") +
        text(122, 100, ctx["role"], size=13, fill=p["blue"] if not dark else "#60A5FA", tid="card-role") +
        text(40, 146, ctx["value_short"], size=12.5, fill=slate, tid="card-value") +
        text(40, 176, "@" + ctx["username"] + " · " + ctx["contact_line"], size=12, fill=slate, family=K.MONO, tid="card-contact"),
        "Pro about card", "Clean card with initials avatar.")
    groups = ""
    gx = 40
    for gname, items in ctx["skill_groups"]:
        groups += text(gx, 30, gname, size=12, fill=p["blue"] if not dark else "#60A5FA", weight="700", spacing=1, tid=f"grp-{gname}")
        gy = 52
        for it in items:
            groups += rect(gx, gy - 12, 6, 6, fill=p["navy"] if not dark else "#60A5FA") + \
                      text(gx + 12, gy - 6, it, size=12, fill=text_c, tid=f"g-{gname}-{it}")
            gy += 20
        gx += 240
    ssvg = svg_doc(1000, 120, rect(0, 0, 1000, 120, fill=bg) + groups, "Grouped skills", "Frontend / Backend / Tools columns.")
    return {"banner.svg": bsvg, "divider.svg": divider, "about-card.svg": card, "skills.svg": ssvg}
