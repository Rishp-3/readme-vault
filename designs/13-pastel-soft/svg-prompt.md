# AI prompt — recreate 13 Pastel Soft

Copy everything below into an AI that outputs SVG code.

---

Create SVG files for a GitHub profile README, design "13-pastel-soft".

**Constraints:** fully self-contained; no `<script>`, no `foreignObject`, no external fonts/images/href URLs (only xmlns); `viewBox` set plus explicit `width`/`height`; one `<title>` and one `<desc>` per file; system font stacks only (`ui-monospace, SFMono-Regular, Menlo, Consolas, monospace` and `-apple-system, "Segoe UI", Helvetica, Arial, sans-serif`); each file under 150 KB; animation via SMIL (`animate`, `animateTransform`, `animateMotion`, `set`) or CSS `@keyframes` inside `<style>` in the SVG only; include `@media (prefers-reduced-motion: reduce){*{animation:none !important;}}`; valid XML.

**Files:**
- banner.svg (1000x300)
- divider.svg (1000x24)
- about-card.svg (480x220)
- skills.svg (1000x120)
- (no extra files)

**Palette:**
- bg: `#FFF1F5`
- pink: `#FFC8DD`
- blue: `#BDE0FE`
- lilac: `#CDB4DB`
- mint: `#B7E4C7`
- text: `#6B5B73`
- bg_dark: `#2A2433`

**Typography:** headings in the sans stack, small labels/terminal text in the mono stack; banner name 40–46 px bold, tagline 15–18 px, card name 19–22 px.

**Layout:**
Banner: light pink bg; four blurred pastel blobs (stdDev 22) drifting; eight 4-point sparkles twinkling; name 40 px centered y=150 with soft lilac drop shadow; tagline y=192; role lilac y=224. Divider: three 5 px dots pink/blue/lilac centered. About card: 24 px rounded card with pastel gradient wash, dashed avatar ring. Skills: 60 px round pastel tiles alternating colors.

**Animation:**
Four blurred pastel blobs translate along a slow there-and-back path (10–14 s). Eight sparkles fade 0.2→1→0.2 randomly. All ease.

**Text content:** placeholders `YOUR_NAME`, `YOUR_ROLE`, `YOUR_TAGLINE`, `YOUR_STATUS`. Banner shows only name/tagline/role (no design name). No email addresses in SVG.

**Output:** only the SVG code per file, each in its own fenced block labelled with the file name.
