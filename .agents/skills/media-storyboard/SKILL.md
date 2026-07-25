---
name: media-storyboard
description: Crea storyboard visual con anotaciones cinematográficas
---

# media-storyboard

## When to use
Usa este comando una vez que el usuario ha aprobado el `final_script.md`.

## How to use
1. Lee y parsea el "shot list" (lista de tomas) del guion final.
2. Genera un storyboard por escena que contenga:
   - Número de escena y toma
   - Thumbnail descriptivo visual (texto que podría generar una imagen)
   - Descripción narrativa y de acción
   - Tipo de plano y movimiento de cámara
   - Duración, audio/música, y transiciones.
3. Guarda el resultado en `storyboard/storyboard_v1.md` o iteraciones finales.

## Examples
*Usuario:* "/media-storyboard"
*Agente:* Parsea `script/final_script.md` y genera el storyboard estructurado.

## Expected output
Storyboard completo y detallado guardado en la carpeta `storyboard/`.
