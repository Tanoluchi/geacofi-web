# Botón sticker

El botón de Geacofi: un sticker inclinado con contorno bordó y sombra dura que se endereza al pasar el mouse.

- **Principal** (`.btn`): fondo `terracota`, texto `on-accent`, Barlow Condensed itálica 24 px. Una acción principal por bloque.
- **Secundario** (`.btn.ghost`): fondo `durazno`, texto `bordo`, inclinado al otro lado.
- **Estados**: hover → `rotate(0)` y `sticker-hover`; presionado → se pega (`translate(5px,5px)`, sin sombra); foco → anillo `focus` de 3 px.
- Altura mínima 48 px. Texto en minúscula, verbo + objeto: "ver la carta", "escribinos".
- WhatsApp lleva el ícono de línea a la izquierda.
- Es un `<a>` si navega y un `<button>` si hace algo en la página.
