# Implementación

Recomendaciones para programar el sitio de forma simple, rápida y fácil de mantener.

## Stack sugerido

- **Astro** como generador de sitio estático: páginas en HTML puro, JavaScript solo donde hace falta (el sobre de cafés, el menú en celular). Alternativa: Next.js con exportación estática, si ya lo usás.
- **Datos** en `/src/data/*.json` (ver Datos del sitio) o una planilla de Google publicada como CSV que se lee al construir el sitio. Con la planilla, un webhook o una tarea programada vuelve a construirlo cuando el café cambia algo.
- **Hosting** gratuito: Netlify, Vercel o Cloudflare Pages, con dominio propio.

## Estructura

```
src/
  data/        carta.json · cafes.json · eventos.json · local.json
  styles/      tokens.css (de este sistema) · base.css
  components/  Boton · TarjetaCarta · Figurita · SobreCafes · Ticket · EstadoVacio · Nav · Pie
  assets/rana/ los SVG de la biblia (carbón y crema)
  pages/       index · carta · eventos · visitanos
```

## Tokens

Copiá `tokens.css` de este sistema y usá siempre las variables (`var(--terracota)`, `var(--radius-md)`), nunca los valores sueltos. El tema *Noche* se activa con `data-theme="noche"` en cada sección oscura.

## Rendimiento

- Fuentes: cargar solo los pesos usados (Gaegu 700; Barlow Condensed 700 y 800 itálica; Nunito 400, 800 y 900; DM Mono 400 y 500) con `display=swap`. Mejor aún: alojarlas en el sitio.
- La rana como SVG: liviana y nítida. En línea solo si se anima (parpadeo, manija); si no, como `<img>`.
- Fotos en WebP o AVIF, con `loading="lazy"` y tamaños declarados.
- Mapa de Google cargado recién al llegar a la sección (o con un botón "ver mapa").
- Objetivo: menos de 1 MB por página y LCP por debajo de 2,5 s en 4G.

## SEO local

- Datos estructurados `CafeOrCoffeeShop` (schema.org) con dirección, horarios, teléfono y redes.
- Títulos por página: "Geacofi · café de especialidad en Corrientes", "La carta · Geacofi".
- Imagen para compartir (Open Graph) con la rana y el logo sobre durazno.
- Perfil de Google Business del café con el link al sitio.

## Sobre de cafés

- Usar Web Animations API y `<canvas>` para la ola de vapor y los papelitos (como en el prototipo).
- El sobre es un `<button>`; cada figurita, un `<button>` que abre el detalle.
- Con `prefers-reduced-motion`, las figuritas aparecen directo en su lugar.
- Lista completa de cafés en HTML debajo del sobre.

## Antes de publicar

- [ ] Días de apertura confirmados
- [ ] Cafés actuales en `cafes.json`
- [ ] Carta con precios al día
- [ ] Logo y rana como SVG (ya están)
- [ ] Fotos en alta resolución
- [ ] Favicon con la rana oficial
- [ ] Prueba en celular real (iPhone y Android)
- [ ] Contraste y navegación con teclado revisados
