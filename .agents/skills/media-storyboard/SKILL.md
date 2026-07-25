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
4. **Paginación y Prompts:** Agrupa las escenas en "bloques" de máximo 6 cuadros (Ej: Escenas 1-6, 7-12). Por cada bloque, redacta un "Prompt Visual" genérico en inglés. 
   - **CONTINUIDAD Y LOCACIONES:** Si todas las escenas ocurren en el mismo lugar, define el "Background" de forma global. Si el guion salta de una locación a otra (ej. de un carrito a la calle), DEBES especificar el background individualmente para cada panel dentro del prompt (ej. *"Panel 1: Background is a street cart. Panel 2: Background is a colonial street"*).
   - **CRÍTICO:** Dentro del texto del prompt, DEBES incluir obligatoriamente y de forma literal al final: *"CRITICAL: Do not include any text, letters, subtitles, words, or speech bubbles anywhere in the image. The image must be completely free of typography."*
5. **Generación Automática:** Si tienes acceso a herramientas de generación de imágenes (como `generate_image`), ejecuta la generación de cada bloque. 
   - **REGLA DE LIMPIEZA CRÍTICA:** Al copiar/mover la imagen a la carpeta `storyboard/assets/`, **DEBES renombrarla a un formato estricto** (ej. `board_01_05.jpg` o `.png`). Elimina obligatoriamente cualquier sufijo numérico o de marca de tiempo (timestamp) que la herramienta generadora haya añadido. Si ya existía un archivo con ese nombre, sobrescríbelo. 
   - Solo debe haber UN archivo gráfico por bloque para evitar confundir al usuario. Finalmente, incrusta la imagen limpia en el markdown (ej. `![Storyboard](assets/board_01_05.jpg)`).
## Examples
*Usuario:* "/media-storyboard"
*Agente:* Parsea `script/final_script.md` y genera el storyboard estructurado.

## Expected output
Storyboard completo y detallado guardado en la carpeta `storyboard/`.
