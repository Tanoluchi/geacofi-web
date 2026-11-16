# Sitio Geacofi en Astro

Build the four-page Geacofi website in Astro from the approved direction C mockups and design system.
Sources of truth: PRODUCT.md, DESIGN.md, docs/geacofi-proyecto/ (README, 05_sistema_de_diseno/, 06_html_fuente/, 04_pantallas/).
The approved desktop/mobile mockups (S1–S5, M1–M3 HTML + PNG) are the comps for comp-first; the build must match them.

## Specs

- **S1** User request: "Continua armando el sitio". Build the site from the existing project docs.
- **S2** User request: "Este es el ejemplo de las cartas /Users/lucianovalenzuela/Downloads/TwitterSaver.Net_ZiW-Gd4b_QAx3T7t_1080p.mp4". The sobre de cafés (coffee card pack) must behave like that example (observed sequence in L2), using the existing prototype `docs/geacofi-proyecto/04_pantallas/sobre-de-cafes-prototipo/index.html` and the data rules in `05_sistema_de_diseno/2-datos.md`.
- **S3** From docs/geacofi-proyecto/README.md (approved decisions): "Sitio de cuatro páginas: Home, Carta, Eventos y Visitanos. Sin pedidos ni reservas online; el contacto es por WhatsApp." and "Tostadores fijos: Komún, MOMO, La Motofeca y Lo de Pepe. Los cafés rotan y salen de un archivo de datos que el café edita."
- **S4** From 2-datos.md: "Todo lo que cambia seguido vive en archivos de datos, no en el diseño." Four files: `carta.json`, `cafes.json`, `eventos.json`, `local.json`, with the schemas and rules in that document (sobre: "5 figuritas, como máximo 2 del mismo tostador, solo cafés con `en_barra: true`"; events split future/past automatically; "La pastilla "abierto / cerrado" del hero se calcula con estos horarios en la zona horaria de Argentina (UTC−3).").
- **S5** From the brand book: "No inventar: precios, horarios y cafés salen de los datos del café. Lo que falta se escribe como `[a confirmar]` hasta tenerlo."
- **S6** From the brand book: "Liviano y siempre opcional. Con `prefers-reduced-motion: reduce`, todo queda quieto."
- **S7** From 3-implementacion.md: "Objetivo: menos de 1 MB por página y LCP por debajo de 2,5 s en 4G." Fonts self-hosted, rana as SVG, map loaded on demand, `CafeOrCoffeeShop` structured data, per-page titles.
- **S8** Stack (user answer during init): "Astro (Recomendado)" — static output.

## Tasks

- [x] T0 · S1 · inline · git init + this document · commit: see git log
- [ ] T1 · S3 S4 S5 S7 S8 · worker · Astro scaffold, tokens.css, base.css, self-hosted fonts, data JSON, assets (logos, rana SVGs), Layout (Nav, Pie, WhatsApp flotante, SEO), shared components (Boton, EstadoVacio, Ticket, PastillaHorario) · commit: —
- [ ] T2 · S1 S4 S5 S6 · worker · Home page (S1_Home / M1_Home) · commit: —
- [ ] T3 · S1 S4 S5 · worker · Carta page (S2_Carta / M2_Carta) · commit: —
- [ ] T4 · S2 S4 S6 · worker · SobreCafes component (video + prototype) · commit: —
- [ ] T5 · S1 S3 S4 S5 · worker · Eventos + Visitanos pages (S3, S4, M3) · commit: —
- [ ] T6 · S1–S8 · verify · build, screenshots desktop/mobile vs mockups, reduced motion, keyboard, contrast, page weight · commit: —

## Log

- **L1** (user, 2026-11-15): "Este es el ejemplo de las cartas /Users/lucianovalenzuela/Downloads/TwitterSaver.Net_ZiW-Gd4b_QAx3T7t_1080p.mp4. Continua armando el sitio"
- **L2** (evidence, frames of the video, 17.4 s, 1920×1080): a foil pack centered on a light background with a soft floor shadow → on click the top tears off, a rainbow wavy ribbon and confetti burst out of the pack → five cards fly out, stack, then fan into one horizontal row; each card has a colored background, a character illustration, a name and small meta text, and a holographic sheen; hovering tilts the card in 3D → a small pill button "Open another pack" appears below → the next pack has a different color; opening it reshuffles the cards in a different order.
- **L3** (decision): no git repo existed; initialized one locally (no remote) for ODD work-unit commits.
