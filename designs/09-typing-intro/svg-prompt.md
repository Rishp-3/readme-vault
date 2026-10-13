# AI prompt — recreate 09 Typing Intro

Copy everything below into an AI that outputs SVG code.

---

Create SVG files for a GitHub profile README, design "09-typing-intro".

**Constraints:** fully self-contained; no `<script>`, no `foreignObject`, no external fonts/images/href URLs (only xmlns); `viewBox` set plus explicit `width`/`height`; one `<title>` and one `<desc>` per file; system font stacks only (`ui-monospace, SFMono-Regular, Menlo, Consolas, monospace` and `-apple-system, "Segoe UI", Helvetica, Arial, sans-serif`); each file under 150 KB; animation via SMIL (`animate`, `animateTransform`, `animateMotion`, `set`) or CSS `@keyframes` inside `<style>` in the SVG only; include `@media (prefers-reduced-motion: reduce){*{animation:none !important;}}`; valid XML.

**Files:**
- banner.svg (1000x300)
- divider.svg (1000x24)
- about-card.svg (480x220)
- skills.svg (1000x120)
- (no extra files)

**Palette:**
- bg: `#0D1117`
- text: `#C9D1D9`
- accent: `#58A6FF`
- caret: `#58A6FF`
- muted: `#8B949E`

**Typography:** headings in the sans stack, small labels/terminal text in the mono stack; banner name 40–46 px bold, tagline 15–18 px, card name 19–22 px.

**Layout:**
Banner: bg #0D1117; phrases 30 px mono at x=60 baseline y=160, each clipped by a rect animated in a 16 s type/hold/erase cycle; caret 12x34 follows phrase end; sub line 15 px muted y=210. Divider: dotted line + accent rect filling 0→800 once. About card: three typed lines 15 px mono in a #161B22 rounded card. Skills: static accent-colored icon row.

**Animation:**
One `<text>` per phrase clipped by an animated rect width (0→w→w→0) within a 16 s cycle split across 4 phrases; caret rect steps x between phrase ends (discrete) and blinks 0.9 s.

**Text content:** placeholders `YOUR_NAME`, `YOUR_ROLE`, `YOUR_TAGLINE`, `YOUR_STATUS`. Banner shows only name/tagline/role (no design name). No email addresses in SVG.

**Output:** only the SVG code per file, each in its own fenced block labelled with the file name.
