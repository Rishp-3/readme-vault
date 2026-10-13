# AI prompt — recreate 05 Code Editor

Copy everything below into an AI that outputs SVG code.

---

Create SVG files for a GitHub profile README, design "05-code-editor".

**Constraints:** fully self-contained; no `<script>`, no `foreignObject`, no external fonts/images/href URLs (only xmlns); `viewBox` set plus explicit `width`/`height`; one `<title>` and one `<desc>` per file; system font stacks only (`ui-monospace, SFMono-Regular, Menlo, Consolas, monospace` and `-apple-system, "Segoe UI", Helvetica, Arial, sans-serif`); each file under 150 KB; animation via SMIL (`animate`, `animateTransform`, `animateMotion`, `set`) or CSS `@keyframes` inside `<style>` in the SVG only; include `@media (prefers-reduced-motion: reduce){*{animation:none !important;}}`; valid XML.

**Files:**
- banner.svg (1000x300)
- divider.svg (1000x24)
- about-card.svg (480x220)
- skills.svg (1000x120)
- status-bar.svg (1000x32): blue VS Code style status bar; tabs.svg (1000x40): three file tabs

**Palette:**
- bg: `#1E1E1E`
- sidebar: `#252526`
- tab: `#2D2D2D`
- text: `#D4D4D4`
- keyword: `#569CD6`
- string: `#CE9178`
- fn: `#DCDCAA`
- comment: `#6A9955`
- number: `#B5CEA8`

**Typography:** headings in the sans stack, small labels/terminal text in the mono stack; banner name 40–46 px bold, tagline 15–18 px, card name 19–22 px.

**Layout:**
Banner: sidebar strip top 34 px (#252526) with active tab `about.js`; line numbers gutter x≈60; 7 code lines at y=54+30·i, 15 px mono, tokens colored keyword/string/comment/number; minimap column x=930 w=70 with gray bars; status bar 32 px #569CD6 bottom. About card: package.json tab + JSON lines. Skills: explorer tree `▾ stack/` with 8 file rows. Extras: status bar, tabs.

**Animation:**
Each code line group fades 0→1 in 0.3 s, delayed 0.4 s per line. Caret rect blinks 0.9 s discrete.

**Text content:** placeholders `YOUR_NAME`, `YOUR_ROLE`, `YOUR_TAGLINE`, `YOUR_STATUS`. Banner shows only name/tagline/role (no design name). No email addresses in SVG.

**Output:** only the SVG code per file, each in its own fenced block labelled with the file name.
