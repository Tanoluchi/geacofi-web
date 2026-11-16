# Bebidas ilustradas en la Carta

Hand-drawn SVG illustrations for every hot and cold drink, shown in the Carta as an illustrated grid inspired by fasan-menu.vercel.app.
Builds on odd/tasks/sitio-astro.md. Sources of truth: PRODUCT.md, DESIGN.md, src/data/carta.json.

## Specs

- **S1** User request: "Genera para las bebidas imagenes dibujadas como esta pagina https://fasan-menu.vercel.app/, para las bebidas frias y calientes". Every item in the `calientes` (11) and `frios` (6) categories of src/data/carta.json gets its own original illustration.
- **S2** User: "No tengo codex, utiliza Claude". No raster generator: the illustrations are SVG hand-authored by Claude.
- **S3** User style choice: "Mezcla: línea + aguada" — the brand's marker line (single carbón ink, thick wobbly stroke, round caps, as in src/assets/dibujos/) with soft watercolor washes behind it, like a drawing colored by hand.
- **S4** Shown in the Carta like the reference (L2): a grid of drink cards with the illustration on top, name, description, price, and a hot/cold tag. Names, descriptions, options and prices only from carta.json; never redraw the rana; reduced motion respected; page weight under 1 MB.

## Tasks

- [ ] T1 · S1 S2 S3 · worker · 17 drink SVGs in src/assets/bebidas/<slug>.svg · commit: —
- [ ] T2 · S4 · worker · Carta grid for calientes and fríos using the illustrations (missing file → graceful fallback) · commit: —
- [ ] T3 · S1–S4 · parent · build, browser check desktop/mobile, weight · commit: —

## Log

- **L1** (user, 2026-11-16): "Genera para las bebidas imagenes dibujadas como esta pagina https://fasan-menu.vercel.app/, para las bebidas frias y calientes"
- **L2** (evidence, fasan-menu): watercolor drink paintings on transparent background over a paper texture; iced drinks in clear plastic cups with ice and marbled layers, hot drinks in paper cups; cards in a 4-column grid: small outlined pill tag ("ICED"), image, name in bold mono, short description, price in red; some cards have an "⇄ hot" toggle.
- **L3** (user, 2026-11-16): "No tengo codex, utiliza Claude" — Codex was unavailable (expired token). Claude drew two SVG watercolor samples (/tmp/geacofi-bebidas/preview.png); espresso read well, ice latte pale.
- **L4** (user choice, 2026-11-16): "Mezcla: línea + aguada".
- **L5** (decision): vessels are illustrative assumptions (no photo evidence of Geacofi's cups yet); slug = item name lowercased, accents removed, spaces → hyphens (e.g. "café con leche" → cafe-con-leche, "ice latte" → ice-latte).
