# Setup — 04 Hacker Terminal

1. Create a repository named exactly `YOUR_USERNAME` (same as your GitHub account name). GitHub renders its README on your profile page.
2. Copy this folder's `README.md` and the entire `assets/` directory into that repo (keep the relative paths).
3. Replace every placeholder listed in `../../shared/placeholders.md` (`YOUR_NAME`, `YOUR_USERNAME`, `YOUR_ROLE`, `YOUR_TAGLINE`, socials, stack items).
4. Edit the SVG text directly: open the file in any editor and change the `<text>` elements —
   - `assets/banner.svg`: ids `banner-name`, `banner-role`, `banner-tagline`
   - `assets/about-card.svg`: ids `card-name`, `card-role`, `card-status`, `card-user`
   - `assets/skills.svg`: icon groups (swap `icon(...)` blocks; see `../../shared/icons/`)
5. Change colors by find-and-replacing the hex values from `colors.md` inside the SVGs.
6. Commit and push, then open `https://github.com/YOUR_USERNAME` to check the profile.

## Troubleshooting

- **Image not loading** — path typos are the usual cause; GitHub serves images from camo, which needs the exact relative path and committed files.
- **Animation not playing** — some browsers only animate SVG when opened directly; in the README it animates in Chrome/Firefox/Safari. If nothing moves, your OS "reduce motion" setting disables it (by design — every SVG respects `prefers-reduced-motion`).
- **Stale image after editing** — camo caches aggressively; append `?v=2` to the `src` or wait a few minutes.
- **Text overflow** — keep replaced names under ~14 characters at the current font size, or lower `font-size` in the `<text>` element.
