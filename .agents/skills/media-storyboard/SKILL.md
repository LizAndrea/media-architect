---
name: media-storyboard
description: Crea storyboard visual con anotaciones cinematográficas
---

# media-storyboard

## When to use
Usa este comando una vez que el usuario ha aprobado el `final_script.md`.

## How to use
1. Lee y parsea la lista de tomas del archivo `script/script.md`.
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
5. **Paginación y Prompts:** Agrupa las escenas en "bloques" de máximo 6 cuadros (Ej: Escenas 1-6, 7-12). Por cada bloque, **escribe explícitamente en el archivo markdown** un "Prompt Visual Global" genérico en inglés (en formato itálica). 
   - **ESTILO VISUAL (CRÍTICO):** Lee el bloque `visuals.style_override` del `manifest.yaml`. Si tiene contenido, inyéctalo al inicio del prompt. Si no, usa el estilo del `workspace.yaml`.
   - **LOCACIÓN Y CONTINUIDAD (CRÍTICO):** Extrae la locación específica de cada toma (Ej: "INT. ESTUDIO") desde el guion. Combina esto con el contexto global de `visuals.location` del manifest (Ej: "Cochabamba"). **DEBES especificar el background (fondo) individualmente para cada panel** dentro del prompt, respetando si los personajes cambiaron de lugar.
   - **VARIABLES (LORE GLOSSARY):** Si hay personajes, el prompt DEBE iniciar definiendo cada tag (Ej: `*LORE GLOSSARY:* \n *[cody] = [Visual Prompt]*`). **CRÍTICO:** Si el reparto es `none`, NO incluyas glosario; pide explícitamente que la imagen contenga sujetos genéricos, personas sin rostro, o elementos estáticos (B-Roll).
   - **FORMATO DEL PROMPT:** Inmediatamente después, escribe `*PROMPT:*`. Exige un grid tipo cómic: *"A 6-panel comic-style storyboard layout (2 rows of 3 panels)."* Luego describe qué pasa en cada panel. Esto es crítico para graficar todo el bloque.
   - **REGLA DE TEXTO:** Dentro del prompt, incluye obligatoriamente: *"CRITICAL: Do not include any text, letters, subtitles, words, or speech bubbles anywhere in the image. The image must be completely free of typography."*
6. **Generación de Prueba (Test de Prompt):** Si tienes acceso a herramientas de generación de imágenes (como `generate_image`), **utiliza EXACTAMENTE EL PROMPT EN INGLÉS QUE ACABAS DE REDACTAR** para generar la imagen del bloque. 
   - **USO DE FOTOS DE REFERENCIA (CRÍTICO):** Si el proyecto tiene personajes (`[ID_Tag]`), **BUSCA la foto de referencia** en la ruta `workspaces/[WORKSPACE_ACTIVO]/characters/[ID_Tag]/` (busca archivos como `*_reference_sheet.jpg` o `*.jpg`) y pásala como ruta absoluta a la herramienta generadora de imágenes. Si el reparto es `none`, no pases ninguna imagen.
   - **REGLA DE LIMPIEZA CRÍTICA:** Al guardar la imagen en `storyboard/assets/`, **renómbrala a un formato estricto** (ej. `board_01_06.jpg`). Elimina cualquier sufijo de la herramienta. 
   - Incrusta la imagen limpia en el markdown (ej. `![Storyboard](assets/board_01_06.jpg)`) debajo del prompt.
## Examples
*Usuario:* "/media-storyboard"
*Agente:* Parsea `script/script.md` y genera el storyboard estructurado.

## Expected output
Storyboard completo y detallado guardado en la carpeta `storyboard/`.
