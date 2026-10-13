# AI prompt — recreate 01 Minimal

Copy everything below into an AI that outputs SVG code.

---

Create SVG files for a GitHub profile README, design "01-minimal".

**Constraints:** fully self-contained; no `<script>`, no `foreignObject`, no external fonts/images/href URLs (only xmlns); `viewBox` set plus explicit `width`/`height`; one `<title>` and one `<desc>` per file; system font stacks only (`ui-monospace, SFMono-Regular, Menlo, Consolas, monospace` and `-apple-system, "Segoe UI", Helvetica, Arial, sans-serif`); each file under 150 KB; animation via SMIL (`animate`, `animateTransform`, `animateMotion`, `set`) or CSS `@keyframes` inside `<style>` in the SVG only; include `@media (prefers-reduced-motion: reduce){*{animation:none !important;}}`; valid XML.

**Files:**
- banner.svg (1000x300)
- divider.svg (1000x24)
- about-card.svg (480x220)
- skills.svg (1000x120)
- (no extra files)

**Palette:**
- bg: `#FFFFFF`
- bg_dark: `#0B0B0B`
- text: `#111111`
- text_dark: `#F5F5F5`
- muted: `#6B7280`
- line: `#E5E7EB`
- accent: `#111111`

**Typography:** headings in the sans stack, small labels/terminal text in the mono stack; banner name 40–46 px bold, tagline 15–18 px, card name 19–22 px.

**Layout:**
Banner: name at x=60 y=130 (44 px weight 300), tagline x=60 y=172 (18 px muted), role x=60 y=204, hairline rule y=232 from x=60 to 940. Divider: centered 1 px line 60 % width. About card: avatar circle outline left (cx 70 cy 70 r 34), name/role right, status dot + text, thin rule, @username mono. Skills: 12 monochrome 40 px icons, 40 px gaps, no labels.

**Animation:**
Name fades in 0→1 over 0.8 s, tagline delayed 0.2 s, role delayed 0.4 s (CSS keyframes with staggered animation-delay). Reduced-motion off-switch included.

**Text content:** placeholders `YOUR_NAME`, `YOUR_ROLE`, `YOUR_TAGLINE`, `YOUR_STATUS`. Banner shows only name/tagline/role (no design name). No email addresses in SVG.

**Output:** only the SVG code per file, each in its own fenced block labelled with the file name.
