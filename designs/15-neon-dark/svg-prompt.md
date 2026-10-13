# AI prompt — recreate 15 Neon Dark

Copy everything below into an AI that outputs SVG code.

---

Create SVG files for a GitHub profile README, design "15-neon-dark".

**Constraints:** fully self-contained; no `<script>`, no `foreignObject`, no external fonts/images/href URLs (only xmlns); `viewBox` set plus explicit `width`/`height`; one `<title>` and one `<desc>` per file; system font stacks only (`ui-monospace, SFMono-Regular, Menlo, Consolas, monospace` and `-apple-system, "Segoe UI", Helvetica, Arial, sans-serif`); each file under 150 KB; animation via SMIL (`animate`, `animateTransform`, `animateMotion`, `set`) or CSS `@keyframes` inside `<style>` in the SVG only; include `@media (prefers-reduced-motion: reduce){*{animation:none !important;}}`; valid XML.

**Files:**
- banner.svg (1000x300)
- divider.svg (1000x24)
- about-card.svg (480x220)
- skills.svg (1000x120)
- (no extra files)

**Palette:**
- bg: `#0A0A0A`
- cyan: `#00F0FF`
- green: `#39FF14`
- magenta: `#FF2EC4`
- text: `#F5F5F5`

**Typography:** headings in the sans stack, small labels/terminal text in the mono stack; banner name 40–46 px bold, tagline 15–18 px, card name 19–22 px.

**Layout:**
Banner: pure dark #0A0A0A; rounded rect 18 px around name: solid cyan stroke 2 px + blurred duplicate 3 px 55 %; name 46 px white centered with middle letter in a flickering tspan; role green mono letterspaced y=226; tagline magenta y=254. Divider: cyan line with 4x12 end caps. About card: cycling-border card (stroke values cyan;green;magenta discrete 12 s) + blurred halo copy. Skills: icons with matching neon underline bars.

**Animation:**
One letter of the name flickers like a faulty sign: tspan opacity discrete values 1;0.15;1;0.3;1;0.1;1 with irregular keyTimes on a 7 s loop. Card border stroke cycles cyan→green→magenta over 12 s (discrete).

**Text content:** placeholders `YOUR_NAME`, `YOUR_ROLE`, `YOUR_TAGLINE`, `YOUR_STATUS`. Banner shows only name/tagline/role (no design name). No email addresses in SVG.

**Output:** only the SVG code per file, each in its own fenced block labelled with the file name.
