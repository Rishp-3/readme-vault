# AI prompt — recreate 17 Ocean Blue

Copy everything below into an AI that outputs SVG code.

---

Create SVG files for a GitHub profile README, design "17-ocean-blue".

**Constraints:** fully self-contained; no `<script>`, no `foreignObject`, no external fonts/images/href URLs (only xmlns); `viewBox` set plus explicit `width`/`height`; one `<title>` and one `<desc>` per file; system font stacks only (`ui-monospace, SFMono-Regular, Menlo, Consolas, monospace` and `-apple-system, "Segoe UI", Helvetica, Arial, sans-serif`); each file under 150 KB; animation via SMIL (`animate`, `animateTransform`, `animateMotion`, `set`) or CSS `@keyframes` inside `<style>` in the SVG only; include `@media (prefers-reduced-motion: reduce){*{animation:none !important;}}`; valid XML.

**Files:**
- banner.svg (1000x300)
- divider.svg (1000x24)
- about-card.svg (480x220)
- skills.svg (1000x120)
- (no extra files)

**Palette:**
- deep: `#062A5C`
- mid: `#0077B6`
- light: `#00B4D8`
- foam: `#E0F2FE`

**Typography:** headings in the sans stack, small labels/terminal text in the mono stack; banner name 40–46 px bold, tagline 15–18 px, card name 19–22 px.

**Layout:**
Banner: vertical gradient light blue→deep navy; four foam wave bands (amp 10→22, speed 9→21 s) anchored to bottom; ten outlined bubbles rising with animateMotion + fade; small fish silhouette crossing leftwards 24 s; name foam-white 44 px y=100, tagline y=134. Divider: single 4 px-amplitude foam wave stroke. About card: mid-blue rounded card with animated low-opacity caustic curves. Skills: icons inside 30 px bubble circles bobbing 3 px staggered.

**Animation:**
Four foam wave bands translate 0→−1000 seamlessly at 9/13/17/21 s. Ten bubbles animateMotion upward with opacity fade. Fish silhouette crosses on animateMotion 24 s. Skill bubbles bob 3 px over 3 s staggered.

**Text content:** placeholders `YOUR_NAME`, `YOUR_ROLE`, `YOUR_TAGLINE`, `YOUR_STATUS`. Banner shows only name/tagline/role (no design name). No email addresses in SVG.

**Output:** only the SVG code per file, each in its own fenced block labelled with the file name.
