---
name: media-storyboard
description: Crea storyboard visual con anotaciones cinematográficas
---

# media-storyboard

## When to use
Usa este comando una vez que el usuario ha aprobado el `final_script.md`.

## How to use
1. Lee y parsea el "shot list" (lista de tomas) del guion final.
2. **Hereda el Reparto:** Copia textualmente la línea `**Reparto (Lore):** [...]` del script y ponla al principio del storyboard.
3. Genera el desglose del storyboard (toma por toma) **ESTRICTAMENTE usando el siguiente formato de lista anidada** para garantizar el estándar de la industria:
   ```markdown
   ### Toma [X] ([Nombre de la Escena/Toma])
   - **Toma:** [X]
   - **Thumbnail (Visual):** [Breve descripción visual]
   - **Acción/Narrativa:** [Explicación de la acción]
   - **Cámara y Fotografía:**
     - **Plano:** [Ej: CU, MS, ECU] / Lente [Ej: 35mm, f/1.4]
     - **Movimiento de cámara:** [Ej: Fijo, Handheld]
     - **Iluminación:** [Ej: Golden Hour, Soft Key]
     - **Color Grading:** [Ej: Tonos cálidos, Desaturado]
   - **Duración:** [Ej: 0:00 - 0:04]
   - **Audio/Voz en Off:** "[Audio o diálogo]"
   - **Transición:** [Ej: Hard Cut, Match Cut]
   ```
4. Guarda o sobrescribe el resultado siempre en `storyboard/storyboard.md`.
4. **Paginación y Prompts:** Agrupa las escenas en "bloques" de máximo 6 cuadros (Ej: Escenas 1-6, 7-12). Por cada bloque, **escribe explícitamente en el archivo markdown** un "Prompt Visual Global" genérico en inglés (en formato itálica). 
   - **VARIABLES (LORE GLOSSARY):** Si hay personajes en el array de Reparto, el prompt DEBE iniciar con un bloque de glosario definiendo cada tag. (Ej: `*LORE GLOSSARY:* \n *[ID_Tag] = [Visual Prompt en Inglés]*`).
   - **FORMATO DEL PROMPT:** Inmediatamente después, escribe `*PROMPT:*`. El prompt DEBE iniciar exigiendo explícitamente un grid tipo cómic. Por ejemplo: *"A 6-panel comic-style storyboard layout (2 rows of 3 panels)."* Luego debes describir brevemente qué pasa en cada panel (*"Panel 1: [ID_Tag] does something..."*). Esto es crítico para que la IA grafique todo el storyboard y no solo una sola imagen resumen.
   - **CONTINUIDAD Y LOCACIONES:** Si todas las escenas ocurren en el mismo lugar, define el "Background" de forma global. Si el guion salta de una locación a otra (ej. de un carrito a la calle), DEBES especificar el background individualmente para cada panel dentro del prompt.
   - **CRÍTICO:** Dentro del texto del prompt, DEBES incluir obligatoriamente y de forma literal al final: *"CRITICAL: Do not include any text, letters, subtitles, words, or speech bubbles anywhere in the image. The image must be completely free of typography."*
5. **Generación de Prueba (Test de Prompt):** Si tienes acceso a herramientas de generación de imágenes (como `generate_image`), **utiliza EXACTAMENTE EL PROMPT EN INGLÉS QUE ACABAS DE REDACTAR** para generar la imagen del bloque. 
   - **USO DE FOTOS DE REFERENCIA (CRÍTICO):** Si el proyecto tiene personajes registrados en su array de Reparto, **DEBES pasar la ruta absoluta de sus imágenes de referencia** (ej. `_reference_sheet.jpg`) a la herramienta generadora de imágenes para asegurar consistencia visual con el Lore.
   - **REGLA DE LIMPIEZA CRÍTICA:** Al copiar/mover la imagen a la carpeta `storyboard/assets/`, **DEBES renombrarla a un formato estricto** (ej. `board_01_06.jpg` o `.png`). Elimina obligatoriamente cualquier sufijo que la herramienta generadora haya añadido. Si ya existía un archivo con ese nombre, sobrescríbelo. 
   - Incrusta la imagen limpia en el markdown (ej. `![Storyboard](assets/board_01_06.jpg)`) justo debajo del prompt en inglés.
## Examples
*Usuario:* "/media-storyboard"
*Agente:* Parsea `script/script.md` y genera el storyboard estructurado.

## Expected output
Storyboard completo y detallado guardado en la carpeta `storyboard/`.
