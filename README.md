<div align="center">

# github-profile-designs

**20 copy-paste-ready GitHub profile README designs — SVG-first, animated, no JavaScript.**

<img src="docs/images/gallery.png" width="100%" alt="Gallery of all 20 designs"/>

![License](https://img.shields.io/badge/license-MIT-22C55E?style=flat-square)
![Designs](https://img.shields.io/badge/designs-20-2563EB?style=flat-square)
![PRs](https://img.shields.io/badge/PRs-welcome-F59E0B?style=flat-square)

</div>

## How to use in 4 steps

1. Create a repo named **exactly your GitHub username** (e.g. `octocat/octocat`). Its README becomes your profile page.
2. Pick a design below, open its folder, and copy its `README.md` and the whole `assets/` folder into your profile repo. (Each folder also has a `demo/` — the same design already filled with real public data of [`Rishp-3`](https://github.com/Rishp-3) — so you can see it working.)
3. Replace the placeholders (see [`shared/placeholders.md`](shared/placeholders.md)) — or run `python3 tools/replace-placeholders.py --design 05-code-editor --name "..." --username "..."` to do it in one shot.
4. Commit, push, open your profile. Done.

## The 20 designs

| # | Design | Category | Vibe | Animated | Themes | Preview | Folder |
|---|---|---|---|---|---|---|---|
| 01 | [Minimal](designs/01-minimal/) | Minimal / Clean | Clean, lots of white space, text-first | yes | light + dark | <img src="designs/01-minimal/preview.png" width="220" alt="01-minimal preview"/> |
| 02 | [Clean Card](designs/02-clean-card/) | Minimal / Clean | Soft card sections with rounded corners and shadows | yes | light + dark | <img src="designs/02-clean-card/preview.png" width="220" alt="02-clean-card preview"/> |
| 03 | [Monochrome](designs/03-monochrome/) | Minimal / Clean | Black and white only, huge uppercase name, scan line | yes | dark only | <img src="designs/03-monochrome/preview.png" width="220" alt="03-monochrome preview"/> |
| 04 | [Hacker Terminal](designs/04-hacker-terminal/) | Developer / Tech | Green phosphor terminal, typed lines, neofetch card | yes | dark only | <img src="designs/04-hacker-terminal/preview.png" width="220" alt="04-hacker-terminal preview"/> |
| 05 | [Code Editor](designs/05-code-editor/) | Developer / Tech | VS Code look: tabs, line numbers, syntax colors, minimap | yes | dark only | <img src="designs/05-code-editor/preview.png" width="220" alt="05-code-editor preview"/> |
| 06 | [Matrix Rain](designs/06-matrix-rain/) | Developer / Tech | Falling green glyph columns behind a dark readable panel | yes | dark only | <img src="designs/06-matrix-rain/preview.png" width="220" alt="06-matrix-rain preview"/> |
| 07 | [Cyberpunk](designs/07-cyberpunk/) | Developer / Tech | Neon pink/cyan HUD panels, RGB glitch, grid floor | yes | dark only | <img src="designs/07-cyberpunk/preview.png" width="220" alt="07-cyberpunk preview"/> |
| 08 | [Gradient Wave](designs/08-gradient-wave/) | Animated | Moving layered sine waves on a cyan-violet gradient | yes | dark only | <img src="designs/08-gradient-wave/preview.png" width="220" alt="08-gradient-wave preview"/> |
| 09 | [Typing Intro](designs/09-typing-intro/) | Animated | Character-by-character typing that cycles 4 phrases | yes | dark only | <img src="designs/09-typing-intro/preview.png" width="220" alt="09-typing-intro preview"/> |
| 10 | [Snake Game](designs/10-snake-game/) | Animated | Contribution-grid banner + real snake via GitHub Action | yes | dark only | <img src="designs/10-snake-game/preview.png" width="220" alt="10-snake-game preview"/> |
| 11 | [Glow Pulse](designs/11-glow-pulse/) | Animated | Pulsing orb, soft violet glow, calm breathing animations | yes | dark only | <img src="designs/11-glow-pulse/preview.png" width="220" alt="11-glow-pulse preview"/> |
| 12 | [Retro Pixel](designs/12-retro-pixel/) | Colorful / Fun | 8-bit pixel scene, blocky bitmap-font title, RPG dialog card | yes | dark only | <img src="designs/12-retro-pixel/preview.png" width="220" alt="12-retro-pixel preview"/> |
| 13 | [Pastel Soft](designs/13-pastel-soft/) | Colorful / Fun | Drifting pastel blobs, sparkles, rounded everything | yes | light + dark | <img src="designs/13-pastel-soft/preview.png" width="220" alt="13-pastel-soft preview"/> |
| 14 | [Sunset Gradient](designs/14-sunset-gradient/) | Colorful / Fun | Vertical sunset, rising half sun, silhouette hills, birds | yes | light + dark | <img src="designs/14-sunset-gradient/preview.png" width="220" alt="14-sunset-gradient preview"/> |
| 15 | [Neon Dark](designs/15-neon-dark/) | Colorful / Fun | Minimal dark with neon outline box and flickering sign | yes | dark only | <img src="designs/15-neon-dark/preview.png" width="220" alt="15-neon-dark preview"/> |
| 16 | [Space Galaxy](designs/16-space-galaxy/) | Themed | Twinkling stars, spiral galaxy, ringed planet, shooting star | yes | dark only | <img src="designs/16-space-galaxy/preview.png" width="220" alt="16-space-galaxy preview"/> |
| 17 | [Ocean Blue](designs/17-ocean-blue/) | Themed | Layered blue waves, rising bubbles, fish silhouette | yes | dark only | <img src="designs/17-ocean-blue/preview.png" width="220" alt="17-ocean-blue preview"/> |
| 18 | [Forest Green](designs/18-forest-green/) | Themed | Pine silhouettes with parallax sway, fireflies, moon, mist | yes | dark only | <img src="designs/18-forest-green/preview.png" width="220" alt="18-forest-green preview"/> |
| 19 | [Glassmorphism](designs/19-glassmorphism/) | Themed | Frosted glass panels over drifting blurred blobs (SVG imitation) | yes | dark only | <img src="designs/19-glassmorphism/preview.png" width="220" alt="19-glassmorphism preview"/> |
| 20 | [Portfolio Pro](designs/20-portfolio-pro/) | Themed | Professional recruiter-first layout, calm navy, one fade-in | yes | light + dark | <img src="designs/20-portfolio-pro/preview.png" width="220" alt="20-portfolio-pro preview"/> |

## FAQ

**Why SVG?** GitHub strips `<style>` and `<script>` from Markdown, but it *does* render `.svg` files placed in the repo via `<img>`. An SVG carries its own styles and animations, so it survives the sandbox while anything HTML/CSS-based would not.

**Why are animations inside the SVG?** Because CSS/JS in Markdown is removed. Inside the SVG we can use SMIL (`<animate>`, `<animateTransform>`, `<animateMotion>`) and CSS `@keyframes` — and every design ships a `prefers-reduced-motion` off-switch.

**How do I switch dark/light?** For designs 01, 02, 13, 14 and 20 use the `<picture>` pattern shown in their `variants/` files: GitHub renders the correct source based on the visitor's theme. Other designs are intentionally dark-only (see each `colors.md`).

**How do I add the contribution snake?** Only design 10 ships it: copy `designs/10-snake-game/workflow/snake.yml` into your profile repo's `.github/workflows/`, create an empty `output` branch, run the workflow once. Full steps in `designs/10-snake-game/setup.md`.

## Credits & License

Built with a single deterministic generator ([`tools/build.py`](tools/build.py)). Icons are original geometric marks, not trademarked logos. Demo data comes from the public GitHub API snapshot in [`tools/data/rishp-3.json`](tools/data/rishp-3.json).

MIT © 2026 Rishp-3
