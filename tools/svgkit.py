#!/usr/bin/env python3
"""svgkit - tiny self-contained SVG builder helpers for GitHub profile designs.

Rules enforced by build.py on top of this:
 * no <script>, no foreignObject, no external hrefs (only the xmlns)
 * every file has viewBox + width/height + <title> + <desc>
 * SMIL or in-SVG CSS keyframes only, always with prefers-reduced-motion off-switch
 * system font stacks only
"""
import math
import random
import re

SANS = "-apple-system, 'Segoe UI', Helvetica, Arial, sans-serif"
MONO = "ui-monospace, SFMono-Regular, Menlo, Consolas, monospace"

# Approximate advance widths (fraction of font-size) so demo text never overflows.
_MONO_W = 0.60


def tw(s, size, mono=True):
    """Estimated rendered width of a string."""
    return len(s) * size * (_MONO_W if mono else 0.52)


def esc(s):
    return (str(s).replace("&", "&amp;").replace("<", "&lt;")
            .replace(">", "&gt;").replace('"', "&quot;"))


def style_block(css):
    return "<style><![CDATA[\n" + css + "\n]]></style>"


REDUCED = "@media (prefers-reduced-motion: reduce){*{animation:none !important;}}\n"


REDUCED_CSS = "@media (prefers-reduced-motion: reduce){*{animation:none !important;}}"


def ensure_reduced_motion(doc):
    """Issue 7: every SVG that contains animation must carry the reduced-motion off-switch.

    Applied centrally in svg_doc so no builder can forget it. SMIL animations are
    frozen at their base attribute value by the media query, so builders must keep
    base attributes showing the final content (issue 15).
    """
    animated = ("<animate" in doc) or ("@keyframes" in doc) or ("<set " in doc)
    if not animated or "prefers-reduced-motion" in doc:
        return doc
    block = "<style><![CDATA[\n" + REDUCED_CSS + "\n]]></style>"
    m = re.search(r'(<svg[^>]*>)', doc)
    if m:
        i = m.end()
        return doc[:i] + block + doc[i:]
    return block + doc


def svg_doc(w, h, body, title, desc, extra_defs=""):
    """Wrap body into a valid standalone SVG document."""
    return ensure_reduced_motion(f"""<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}" role="img" aria-labelledby="ttl dsc">
<title id="ttl">{esc(title)}</title>
<desc id="dsc">{esc(desc)}</desc>
{extra_defs}
{body}
</svg>
""")


def text(x, y, s, size=16, fill="#FFFFFF", family=SANS, weight="normal",
         anchor="start", spacing=None, opacity=None, tid=None, cls=None, blur=None):
    a = f' x="{x}" y="{y}"'
    st = f"font-family:{family};font-size:{size}px;font-weight:{weight};"
    if spacing:
        st += f"letter-spacing:{spacing}px;"
    at = (f' transform="translate({x},{y})" x="0" y="0"' if False else a)
    attrs = f'{at} font-family="{family}" font-size="{size}" font-weight="{weight}" fill="{fill}" text-anchor="{anchor}"'
    if spacing:
        attrs += f' letter-spacing="{spacing}"'
    if opacity is not None:
        attrs += f' opacity="{opacity}"'
    if tid:
        attrs += f' id="{tid}"'
    if cls:
        attrs += f' class="{cls}"'
    if blur:
        attrs += f' filter="url(#{blur})"'
    return f"<text{attrs}>{esc(s)}</text>"


def rect(x, y, w, h, fill="none", rx=0, stroke=None, sw=1, opacity=None,
         dash=None, rid=None, blur=None, clip=None):
    attrs = f'x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" fill="{fill}"'
    if stroke:
        attrs += f' stroke="{stroke}" stroke-width="{sw}"'
    if opacity is not None:
        attrs += f' opacity="{opacity}"'
    if dash:
        attrs += f' stroke-dasharray="{dash}"'
    if rid:
        attrs += f' id="{rid}"'
    if blur:
        attrs += f' filter="url(#{blur})"'
    if clip:
        attrs += f' clip-path="url(#{clip})"'
    return f"<rect {attrs}/>"


def circle(cx, cy, r, fill="none", stroke=None, sw=1, opacity=None, dash=None, cid=None, blur=None):
    attrs = f'cx="{cx}" cy="{cy}" r="{r}" fill="{fill}"'
    if stroke:
        attrs += f' stroke="{stroke}" stroke-width="{sw}"'
    if opacity is not None:
        attrs += f' opacity="{opacity}"'
    if dash:
        attrs += f' stroke-dasharray="{dash}"'
    if cid:
        attrs += f' id="{cid}"'
    if blur:
        attrs += f' filter="url(#{blur})"'
    return f"<circle {attrs}/>"


def ellipse(cx, cy, rx, ry, fill="none", stroke=None, sw=1, opacity=None, rot=None):
    attrs = f'cx="{cx}" cy="{cy}" rx="{rx}" ry="{ry}" fill="{fill}"'
    if stroke:
        attrs += f' stroke="{stroke}" stroke-width="{sw}"'
    if opacity is not None:
        attrs += f' opacity="{opacity}"'
    if rot:
        attrs += f' transform="rotate({rot} {cx} {cy})"'
    return f"<ellipse {attrs}/>"


def line(x1, y1, x2, y2, stroke="#888", sw=1, opacity=None, dash=None):
    attrs = f'x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{stroke}" stroke-width="{sw}"'
    if opacity is not None:
        attrs += f' opacity="{opacity}"'
    if dash:
        attrs += f' stroke-dasharray="{dash}"'
    return f"<line {attrs}/>"


def path(d, fill="none", stroke=None, sw=1, opacity=None, scap=None, sjoin=None, pid=None):
    attrs = f'd="{d}" fill="{fill}"'
    if stroke:
        attrs += f' stroke="{stroke}" stroke-width="{sw}"'
    if opacity is not None:
        attrs += f' opacity="{opacity}"'
    if scap:
        attrs += f' stroke-linecap="{scap}"'
    if sjoin:
        attrs += f' stroke-linejoin="{sjoin}"'
    if pid:
        attrs += f' id="{pid}"'
    return f"<path {attrs}/>"


def polygon(points, fill="none", stroke=None, sw=1, opacity=None):
    attrs = f'points="{points}" fill="{fill}"'
    if stroke:
        attrs += f' stroke="{stroke}" stroke-width="{sw}"'
    if opacity is not None:
        attrs += f' opacity="{opacity}"'
    return f"<polygon {attrs}/>"


def g(inner, tid=None, transform=None, opacity=None, clip=None, cls=None):
    attrs = ""
    if tid:
        attrs += f' id="{tid}"'
    if transform:
        attrs += f' transform="{transform}"'
    if opacity is not None:
        attrs += f' opacity="{opacity}"'
    if clip:
        attrs += f' clip-path="url(#{clip})"'
    if cls:
        attrs += f' class="{cls}"'
    return f"<g{attrs}>{inner}</g>"


def defs(inner):
    return f"<defs>{inner}</defs>"


def linear_gradient(gid, stops, x1="0%", y1="0%", x2="100%", y2="0%"):
    parts = []
    for st in stops:
        o, c = st[0], st[1]
        op = st[2] if len(st) > 2 else None
        parts.append(f'<stop offset="{o}" stop-color="{c}"' +
                     (f' stop-opacity="{op}"' if op is not None else "") + "/>")
    return f'<linearGradient id="{gid}" x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}">{"".join(parts)}</linearGradient>'


def radial_gradient(gid, stops, cx="50%", cy="50%", r="50%"):
    parts = []
    for st in stops:
        o, c = st[0], st[1]
        op = st[2] if len(st) > 2 else None
        parts.append(f'<stop offset="{o}" stop-color="{c}"' +
                     (f' stop-opacity="{op}"' if op is not None else "") + "/>")
    return f'<radialGradient id="{gid}" cx="{cx}" cy="{cy}" r="{r}">{"".join(parts)}</radialGradient>'


def fe_gaussian_blur(gid, std):
    return f'<filter id="{gid}" x="-50%" y="-50%" width="200%" height="200%"><feGaussianBlur stdDeviation="{std}"/></filter>'


def fe_drop_shadow(gid, dx=0, dy=4, std=8, color="#000000", opacity=0.35):
    return (f'<filter id="{gid}" x="-50%" y="-50%" width="200%" height="200%">'
            f'<feDropShadow dx="{dx}" dy="{dy}" stdDeviation="{std}" flood-color="{color}" flood-opacity="{opacity}"/></filter>')


# ---------------- SMIL helpers ----------------

def anim(attr, values, dur, begin="0s", repeat="indefinite", calc=None,
         keytimes=None, keysplines=None, fill=None, target_id=None):
    """Return an <animate .../> element (place inside the animated element or use xlink-free href via id parent)."""
    a = f' attributeName="{attr}" values="{values}" dur="{dur}" begin="{begin}" repeatCount="{repeat}"'
    if calc:
        a += f' calcMode="{calc}"'
    if keytimes:
        a += f' keyTimes="{keytimes}"'
    if keysplines:
        a += f' keySplines="{keysplines}"'
    if fill:
        a += f' fill="{fill}"'
    return f"<animate {a}/>"


def animate_on(elem_str, *anims):
    """Insert animation children into a self-closing element string like <rect .../>."""
    inner = "".join(anims)
    if elem_str.endswith("/>"):
        tag = re.match(r"<([A-Za-z]+)", elem_str).group(1)
        return elem_str[:-2] + ">" + inner + "</" + tag + ">"
    # already open/close: insert before final closing tag
    idx = elem_str.rindex("</")
    return elem_str[:idx] + inner + elem_str[idx:]


def anim_transform_translate(values, dur, begin="0s", repeat="indefinite"):
    return (f'<animateTransform attributeName="transform" type="translate" '
            f'values="{values}" dur="{dur}" begin="{begin}" repeatCount="{repeat}"/>')


def anim_transform_rotate(values, dur, cx, cy, begin="0s", repeat="indefinite"):
    return (f'<animateTransform attributeName="transform" type="rotate" '
            f'values="{values}" dur="{dur}" begin="{begin}" repeatCount="{repeat}"/>')


def fade_in(delay=0.0, dur=0.8):
    return anim("opacity", "0;1", f"{dur}s", begin=f"{delay}s", repeat="0", fill="freeze")


def sine_wave_path(width, amp, ybase, wl, phase=0.0, twice=False):
    """Build a smooth sine polyline path across `width` (optionally doubled for seamless loops)."""
    total = width * 2 if twice else width
    pts = []
    step = wl / 24.0
    x = 0.0
    while x <= total + 0.01:
        y = ybase + amp * math.sin(2 * math.pi * (x / wl) + phase)
        pts.append((round(x, 1), round(y, 1)))
        x += step
    d = "M" + " L".join(f"{px} {py}" for px, py in pts)
    return d


def wave_band_path(width, amp, ybase, wl, phase=0.0, fill_to=None):
    """Sine wave that closes down to fill_to (for filled wave bands). Doubled width for seamless translate loops."""
    d = sine_wave_path(width, amp, ybase, wl, phase, twice=True)
    if fill_to is not None:
        d += f" L{width * 2} {fill_to} L0 {fill_to} Z"
    return d


# ---------------- original mini icon set (48x48 grids, simple geometric marks) ----------------

def icon(name, x, y, color="#9CA3AF", size=48, scale=None):
    """Draw an original generic tech/social glyph at (x,y) top-left within a `size` box.

    These are simple abstract marks (not trademarked logos) so they stay safe and monochrome-tintable.
    """
    k = size / 48.0
    if scale:
        k *= scale
    def P(pts):
        return " ".join(f"{x + a * k},{y + b * k}" for a, b in pts)
    c = color
    m = size / 2.0
    ox, oy = x, y
    if name == "react":
        return (f'<g transform="translate({ox},{oy}) scale({k})">'
                f'<circle cx="24" cy="24" r="4" fill="{c}"/>'
                f'<ellipse cx="24" cy="24" rx="20" ry="8" fill="none" stroke="{c}" stroke-width="2"/>'
                f'<ellipse cx="24" cy="24" rx="20" ry="8" fill="none" stroke="{c}" stroke-width="2" transform="rotate(60 24 24)"/>'
                f'<ellipse cx="24" cy="24" rx="20" ry="8" fill="none" stroke="{c}" stroke-width="2" transform="rotate(120 24 24)"/></g>')
    if name == "js":
        return (f'<g transform="translate({ox},{oy}) scale({k})">'
                f'<rect x="4" y="4" width="40" height="40" rx="4" fill="none" stroke="{c}" stroke-width="2.5"/>'
                f'<path d="M18 16v10a4 4 0 0 1-7 2" fill="none" stroke="{c}" stroke-width="2.5" stroke-linecap="round"/>'
                f'<path d="M30 16v12" stroke="{c}" stroke-width="2.5" stroke-linecap="round"/>'
                f'<path d="M34 30a4 4 0 0 1-7 1" fill="none" stroke="{c}" stroke-width="2.5" stroke-linecap="round"/></g>')
    if name == "html":
        return (f'<g transform="translate({ox},{oy}) scale({k})">'
                f'<path d="M8 6l-4 8 4 8" fill="none" stroke="{c}" stroke-width="2.5" stroke-linecap="round" transform="translate(6,10)"/>'
                f'<path d="M40 6l4 8-4 8" fill="none" stroke="{c}" stroke-width="2.5" stroke-linecap="round" transform="translate(-6,10)"/>'
                f'<path d="M27 12l-6 24" stroke="{c}" stroke-width="2.5" stroke-linecap="round"/></g>')
    if name == "css":
        return (f'<g transform="translate({ox},{oy}) scale({k})">'
                f'<rect x="6" y="6" width="36" height="36" rx="6" fill="none" stroke="{c}" stroke-width="2.5"/>'
                f'<path d="M16 18h8M16 24h12M16 30h6" stroke="{c}" stroke-width="2.5" stroke-linecap="round"/></g>')
    if name == "tailwind":
        return (f'<g transform="translate({ox},{oy}) scale({k})">'
                f'<path d="M6 26c6-10 18-10 22-4 3 5 8 6 14 2-4 8-14 10-19 6-4-4-10-3-17-4z" fill="{c}"/></g>')
    if name == "node":
        return (f'<g transform="translate({ox},{oy}) scale({k})">'
                f'<polygon points="24,4 42,14 42,34 24,44 6,34 6,14" fill="none" stroke="{c}" stroke-width="2.5"/>'
                f'<path d="M17 30V18l14 12V18" fill="none" stroke="{c}" stroke-width="2.5" stroke-linecap="round"/></g>')
    if name == "git":
        return (f'<g transform="translate({ox},{oy}) scale({k})">'
                f'<circle cx="14" cy="14" r="5" fill="none" stroke="{c}" stroke-width="2.5"/>'
                f'<circle cx="14" cy="34" r="5" fill="none" stroke="{c}" stroke-width="2.5"/>'
                f'<circle cx="34" cy="24" r="5" fill="none" stroke="{c}" stroke-width="2.5"/>'
                f'<path d="M14 19v10M18 31l12-6" stroke="{c}" stroke-width="2.5"/></g>')
    if name == "github":
        return (f'<g transform="translate({ox},{oy}) scale({k})">'
                f'<path d="M24 6a18 18 0 0 0-6 35c1 2 2 1 2 1v-5c-8 1-9-4-9-4-1-2-2-3-2-3-3-2 0-2 0-2 3 0 5 3 5 3 3 4 7 3 8 2 1-2 2-3 2-3-8-1-9-8-9-8-2-2-2-5-2-5 1-3 4-3 4-3 4 0 6 4 6 4 3 4 7 3 8 3 1-3 3-4 4-4-7-1-14-5-14-14a11 11 0 0 1 3-8c-1-2-1-5 0-7 0 0 3 0 7 3a18 18 0 0 1 10 0c4-3 7-3 7-3 1 2 1 5 0 7a11 11 0 0 1 3 8c0 9-7 13-14 14 2 1 3 3 3 6v8s1 1 2-1a18 18 0 0 0-6-35z" fill="{c}"/></g>')
    if name == "java":
        return (f'<g transform="translate({ox},{oy}) scale({k})">'
                f'<path d="M20 8c6 4-1 8-1 12 0 3 2 5 2 5s-8-1-8-7c0-5 5-7 7-10z" fill="{c}"/>'
                f'<path d="M14 30c8 4 20 2 26-4-4 8-14 12-22 9-3-1-5-3-4-5z" fill="{c}"/></g>')
    if name == "c":
        return (f'<g transform="translate({ox},{oy}) scale({k})">'
                f'<circle cx="24" cy="24" r="18" fill="none" stroke="{c}" stroke-width="2.5"/>'
                f'<path d="M30 17a9 9 0 1 0 0 14" fill="none" stroke="{c}" stroke-width="3" stroke-linecap="round"/></g>')
    if name == "netlify":
        return (f'<g transform="translate({ox},{oy}) scale({k})">'
                f'<polygon points="24,6 40,22 24,38 8,22" fill="none" stroke="{c}" stroke-width="2.5"/>'
                f'<path d="M16 28l8-12 8 12" fill="none" stroke="{c}" stroke-width="2.5"/></g>')
    if name == "bootstrap":
        return (f'<g transform="translate({ox},{oy}) scale({k})">'
                f'<rect x="6" y="6" width="36" height="36" rx="8" fill="none" stroke="{c}" stroke-width="2.5"/>'
                f'<path d="M18 16h8a5 5 0 0 1 0 8h-8m0 0h9a5 5 0 0 1 0 8h-9V16z" fill="none" stroke="{c}" stroke-width="2.5"/></g>')
    if name in ("linkedin", "x", "instagram", "youtube", "mail", "codepen", "medium", "leetcode", "gfg", "stackoverflow"):
        return social_icon(name, x, y, c, k)
    # fallback: rounded square with initial
    return (f'<g transform="translate({ox},{oy}) scale({k})">'
            f'<rect x="6" y="6" width="36" height="36" rx="8" fill="none" stroke="{c}" stroke-width="2.5"/>'
            f'<text x="24" y="31" text-anchor="middle" font-family="{MONO}" font-size="20" fill="{c}">{esc(name[0].upper())}</text></g>')


def social_icon(name, x, y, c, k):
    ox, oy = x, y
    if name == "linkedin":
        return (f'<g transform="translate({ox},{oy}) scale({k})">'
                f'<rect x="6" y="6" width="36" height="36" rx="6" fill="none" stroke="{c}" stroke-width="2.5"/>'
                f'<path d="M16 20v12M16 15v.5M24 32V24a4 4 0 0 1 8 0v8" stroke="{c}" stroke-width="2.5" fill="none" stroke-linecap="round"/></g>')
    if name == "x":
        return (f'<g transform="translate({ox},{oy}) scale({k})">'
                f'<path d="M10 10l28 28M38 10L10 38" stroke="{c}" stroke-width="3" stroke-linecap="round"/></g>')
    if name == "instagram":
        return (f'<g transform="translate({ox},{oy}) scale({k})">'
                f'<rect x="8" y="8" width="32" height="32" rx="9" fill="none" stroke="{c}" stroke-width="2.5"/>'
                f'<circle cx="24" cy="24" r="7" fill="none" stroke="{c}" stroke-width="2.5"/>'
                f'<circle cx="34" cy="14" r="2" fill="{c}"/></g>')
    if name == "youtube":
        return (f'<g transform="translate({ox},{oy}) scale({k})">'
                f'<rect x="6" y="12" width="36" height="24" rx="8" fill="none" stroke="{c}" stroke-width="2.5"/>'
                f'<polygon points="21,19 21,29 30,24" fill="{c}"/></g>')
    if name == "mail":
        return (f'<g transform="translate({ox},{oy}) scale({k})">'
                f'<rect x="6" y="12" width="36" height="24" rx="4" fill="none" stroke="{c}" stroke-width="2.5"/>'
                f'<path d="M8 14l16 12 16-12" fill="none" stroke="{c}" stroke-width="2.5"/></g>')
    if name == "codepen":
        return (f'<g transform="translate({ox},{oy}) scale({k})">'
                f'<polygon points="24,6 42,17 42,31 24,42 6,31 6,17" fill="none" stroke="{c}" stroke-width="2.5"/>'
                f'<path d="M24 6v11m0 24V30M6 17l18 11 18-11M6 31l18-11 18 11" stroke="{c}" stroke-width="2" fill="none"/></g>')
    if name == "medium":
        return (f'<g transform="translate({ox},{oy}) scale({k})">'
                f'<ellipse cx="14" cy="24" rx="8" ry="14" fill="none" stroke="{c}" stroke-width="2.5"/>'
                f'<ellipse cx="30" cy="24" rx="5" ry="14" fill="none" stroke="{c}" stroke-width="2.5"/>'
                f'<line x1="40" y1="12" x2="40" y2="36" stroke="{c}" stroke-width="2.5"/></g>')
    if name == "leetcode":
        return (f'<g transform="translate({ox},{oy}) scale({k})">'
                f'<path d="M12 14c-6 6-6 14 0 20" fill="none" stroke="{c}" stroke-width="3" stroke-linecap="round"/>'
                f'<path d="M36 14c6 6 6 14 0 20" fill="none" stroke="{c}" stroke-width="3" stroke-linecap="round"/>'
                f'<path d="M20 34l8-20" stroke="{c}" stroke-width="3" stroke-linecap="round"/></g>')
    if name == "gfg":
        return (f'<g transform="translate({ox},{oy}) scale({k})">'
                f'<rect x="8" y="8" width="32" height="32" rx="4" fill="none" stroke="{c}" stroke-width="2.5"/>'
                f'<path d="M30 18a8 8 0 1 0 0 12h-6" fill="none" stroke="{c}" stroke-width="2.5"/></g>')
    if name == "stackoverflow":
        return (f'<g transform="translate({ox},{oy}) scale({k})">'
                f'<path d="M12 34v-8l18 2v6H12zM14 24l18 1M16 17l18 2M20 10l16 4M26 6l12 7" fill="none" stroke="{c}" stroke-width="2.5" stroke-linecap="round"/></g>')
    return ""


STACK_ICONS = ["html", "css", "js", "react", "tailwind", "bootstrap", "node", "git", "github", "netlify", "c", "java"]
SOCIAL_ICONS = ["github", "linkedin", "x", "instagram", "youtube", "codepen", "medium", "leetcode", "gfg", "stackoverflow"]
