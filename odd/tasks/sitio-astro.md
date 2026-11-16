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

- [x] T0 · S1 · inline · git init + this document · commit: dcd2ce4
- [x] T1 · S3 S4 S5 S7 S8 · worker · Astro scaffold, tokens.css, base.css, self-hosted fonts, data JSON, assets (logos, rana SVGs), Layout (Nav, Pie, WhatsApp flotante, SEO), shared components (Boton, EstadoVacio, Ticket, PastillaHorario) · commit: 6f856f8 (build + 5/5 tests observed)
- [x] T2 · S1 S4 S5 S6 · worker · Home page (S1_Home / M1_Home) · commit: see git log "feat: add Home page" (astro check 0 errors, build OK, screenshots 1440/390 by worker; open: 390px scrollWidth 411 from rotated cinta, tostador dots outside figuritas per mockup vs DESIGN.md Tostador Rule → T6)
- [x] T3 · S1 S4 S5 · worker · Carta page (S2_Carta / M2_Carta) · commit: see git log "feat: add Carta page" (astro check 0, build OK, screenshots 1440/390 match comps, no overflow)
- [x] T4 · S2 S4 S6 · worker · SobreCafes component (video + prototype) · commit: see git log "feat: add coffee card pack" (astro check 0, build OK, playwright desktop flow: open → 5 cards, dialog, Escape, another pack; JS 8.7 KB min. Open for T6: mobile layout, mid-animation frames, MOMO holo, reduced-motion in browser, 600px stage gap. Wave uses brand/tostador colors instead of the video's rainbow.)
- [x] T5 · S1 S3 S4 S5 · worker · Eventos + Visitanos pages (S3, S4, M3) · commit: 192895a (astro check 0 errors, build OK; not visually verified → T6)
- [x] T6 · S1–S8 · worker · build, screenshots desktop/mobile vs mockups, reduced motion, keyboard, contrast, page weight + consistency fixes · commit: see git log "fix: verification pass" (verdicts: S1 partial, S2–S8 pass; tests 5/5, astro check 0, build 4 pages; weights 191–418 KB)

## Log

- **L1** (user, 2026-11-15): "Este es el ejemplo de las cartas /Users/lucianovalenzuela/Downloads/TwitterSaver.Net_ZiW-Gd4b_QAx3T7t_1080p.mp4. Continua armando el sitio"
- **L2** (evidence, frames of the video, 17.4 s, 1920×1080): a foil pack centered on a light background with a soft floor shadow → on click the top tears off, a rainbow wavy ribbon and confetti burst out of the pack → five cards fly out, stack, then fan into one horizontal row; each card has a colored background, a character illustration, a name and small meta text, and a holographic sheen; hovering tilts the card in 3D → a small pill button "Open another pack" appears below → the next pack has a different color; opening it reshuffles the cards in a different order.
- **L3** (decision): no git repo existed; initialized one locally (no remote) for ODD work-unit commits.
- **L4** (T1 evidence): coffees in cafes.json are the prototype's sample coffees marked en_barra so the pack has content; real bar coffees remain [a confirmar]. Event years inferred from weekday (2026-02-13, 2025-11-23); both are past today, so Eventos shows the empty state. Opening hours apply to every day until days are confirmed (shortcut in horario.ts).
- **L6** (decision for T6): pages are inconsistent on eyebrow labels: Carta kept them (DESIGN.md prescribes DM Mono uppercase eyebrows), Home/Eventos/Visitanos dropped them citing the craft-floor kicker ban. Impeccable rule "the brief wins": DESIGN.md is the brief, so T6 restores the mockups' eyebrows everywhere. Tostador color dots on the Home roaster chips follow the mockup; T6 updates the DESIGN.md Tostador Rule to allow them as small identification dots (told the user this default).
- **L7** (T6 evidence): S1 partial — Home bonus-track photos not built (no confirmed photo↔item mapping); Carta "Edición especial" card uses a title instead of the compact eyebrow. Fixed: Escape closes mobile menu, flyers now use real images (cafeyeso.jpg, sensorial.jpg), hardcoded address/nomination moved to local.json, cinta overflow, sobre stage height. Not checked: real 4G LCP, Safari/Firefox.
- **L5** (slice boundary): T1 commit 6f856f8 is ~1,277 authored lines (scaffold + data + layout as one foundation unit). Delivery strategy: one commit per remaining task (T2–T5 each its own slice, T6 fixes separate); push/PR remain the user's decision.
