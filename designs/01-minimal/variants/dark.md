# Dark variant

Use `<picture>` so GitHub picks the SVG by visitor theme:

```html
<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/banner-dark.svg"/>
  <img alt="Minimal banner" src="assets/banner.svg"/>
</picture>
```

`assets/banner-dark.svg` is generated for this design (demo copy in `demo/assets/banner-dark.svg`).
