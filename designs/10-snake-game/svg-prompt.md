# AI prompt — recreate 10 Snake Game

Copy everything below into an AI that outputs SVG code.

---

Create SVG files for a GitHub profile README, design "10-snake-game".

**Constraints:** fully self-contained; no `<script>`, no `foreignObject`, no external fonts/images/href URLs (only xmlns); `viewBox` set plus explicit `width`/`height`; one `<title>` and one `<desc>` per file; system font stacks only (`ui-monospace, SFMono-Regular, Menlo, Consolas, monospace` and `-apple-system, "Segoe UI", Helvetica, Arial, sans-serif`); each file under 150 KB; animation via SMIL (`animate`, `animateTransform`, `animateMotion`, `set`) or CSS `@keyframes` inside `<style>` in the SVG only; include `@media (prefers-reduced-motion: reduce){*{animation:none !important;}}`; valid XML.

**Files:**
- banner.svg (1000x300)
- divider.svg (1000x24)
- about-card.svg (480x220)
- skills.svg (1000x120)
- (no extra files)

**Palette:**
- bg: `#0D1117`
- c1: `#161B22`
- c2: `#0E4429`
- c3: `#006D32`
- c4: `#26A641`
- c5: `#39D353`
- snake: `#58A6FF`
- text: `#C9D1D9`

**Typography:** headings in the sans stack, small labels/terminal text in the mono stack; banner name 40–46 px bold, tagline 15–18 px, card name 19–22 px.

**Layout:**
Banner: GitHub dark bg; name 40 px centered y=80, tagline mono y=112; static 52x7 contribution grid starting (20,150), 16 px cells rx 3 in five greens, six-cell blue snake sitting on the grid. Divider: one row of 52 cells. About card: #161B22 rounded card like 09. Skills: green icon row.

**Animation:**
No SVG animation required (the snake itself is a generated GIF/SVG from the Action). Grid cells static.

**Text content:** placeholders `YOUR_NAME`, `YOUR_ROLE`, `YOUR_TAGLINE`, `YOUR_STATUS`. Banner shows only name/tagline/role (no design name). No email addresses in SVG.

**Output:** only the SVG code per file, each in its own fenced block labelled with the file name.
