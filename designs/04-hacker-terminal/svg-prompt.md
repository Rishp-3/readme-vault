# AI prompt — recreate 04 Hacker Terminal

Copy everything below into an AI that outputs SVG code.

---

Create SVG files for a GitHub profile README, design "04-hacker-terminal".

**Constraints:** fully self-contained; no `<script>`, no `foreignObject`, no external fonts/images/href URLs (only xmlns); `viewBox` set plus explicit `width`/`height`; one `<title>` and one `<desc>` per file; system font stacks only (`ui-monospace, SFMono-Regular, Menlo, Consolas, monospace` and `-apple-system, "Segoe UI", Helvetica, Arial, sans-serif`); each file under 150 KB; animation via SMIL (`animate`, `animateTransform`, `animateMotion`, `set`) or CSS `@keyframes` inside `<style>` in the SVG only; include `@media (prefers-reduced-motion: reduce){*{animation:none !important;}}`; valid XML.

**Files:**
- banner.svg (1000x300)
- divider.svg (1000x24)
- about-card.svg (480x220)
- skills.svg (1000x120)
- prompt-footer.svg (1000x40): `$ echo "thanks for visiting"` prompt line

**Palette:**
- bg: `#050A05`
- text: `#33FF66`
- dim: `#1A8F3C`
- bar: `#0F2A14`
- warn: `#FFBD2E`

**Typography:** headings in the sans stack, small labels/terminal text in the mono stack; banner name 40–46 px bold, tagline 15–18 px, card name 19–22 px.

**Layout:**
Banner: terminal title bar 940x40 rx 8 at (30,24) with 3 traffic dots, mono title centered; 4 typed lines start x=56, y=100/140/180/220, 20 px mono; blinking block cursor after last line; CRT scanline pattern overlay 6 % opacity. About card: neofetch block — 3-line ASCII logo left column, key/value pairs right (OS/Shell/Role/Stack/Status). Skills: `$ ls ./stack` header + 8 file rows with tiny icons. Footer: prompt echo line.

**Animation:**
Four terminal lines revealed sequentially with clipPath rect width 0→full, 0.9 s each, starting at 0.6 s, spaced 1.1 s apart, calcMode linear, fill freeze. Block cursor blinks 1 s (discrete 0.5 duty).

**Text content:** placeholders `YOUR_NAME`, `YOUR_ROLE`, `YOUR_TAGLINE`, `YOUR_STATUS`. Banner shows only name/tagline/role (no design name). No email addresses in SVG.

**Output:** only the SVG code per file, each in its own fenced block labelled with the file name.
