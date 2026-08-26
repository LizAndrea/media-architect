---
name: media-set
description: Genera el prompt maestro para crear un Set base (Background Plate) en el proyecto activo
---

# media-set

## When to use
Usa este comando cuando el usuario necesite crear o definir la locación base (Set vacío o Background Plate) para las escenas de su proyecto. Esto asegura consistencia visual en todas las tomas antes de añadir personajes o desenfoques de profundidad de campo.

## How to use
1. **Comando:** `/media-set [nombre_del_set_o_descripcion]`
2. **Contexto:** Asegúrate de tener el contexto del workspace y proyecto activo (si no, pide al usuario usar `/media-in`). Revisa el `manifest.yaml` y el `AGENTS.md` del proyecto y del workspace para capturar la estética (colores, estilo cinematográfico, etc.).
3. **Generación del Archivo:** Crea un nuevo archivo markdown en la carpeta `sets/` del proyecto activo, numerándolo secuencialmente (ej. `sets/set_01_podcast.md`, `sets/set_02_oficina.md`).
4. **Estructura del Archivo Generado:**
   El archivo DEBE seguir esta estructura estricta:

   ```markdown
   # LOCATION / SET PROMPT: [Nombre del Set]

   **Nombre del Set:** [Nombre]
   **Ubicación:** `workspaces/[workspace]/projects/[proyecto]/sets/set_XX_[nombre].md`

   ## 🎬 Prompt de Generación (Image-to-Image / Style Reference)

   Para generar el escenario vacío perfecto que servirá de fondo (Background Plate) en todas las tomas de este proyecto, utiliza el siguiente prompt hiper-realista.

   **(Opcional) ⚠️ INSTRUCCIÓN CRÍTICA (LOGO REF):**
   *Si el set requiere un logo de la marca, incluye una instrucción indicando que se debe pasar el logo como referencia (Image Prompt / Cref) a la IA para integrar su forma.*

   **[ENGLISH PROMPT]**
   [REDACTA AQUÍ EL PROMPT EN INGLÉS SIGUIENDO LAS REGLAS CRÍTICAS]

   ## ⚙️ Parámetros Técnicos
   - **Aspect Ratio:** [Extraído del manifest.yaml, ej. 9:16 o 16:9]
   - **Negative Prompt:** People, humans, text, letters, typography, cartoon, 3d render, messy cables, blur, bokeh, out of focus.
   ```

5. **REGLAS CRÍTICAS PARA EL PROMPT EN INGLÉS:**
   - **Ángulo:** Debe ser `Perfect front-facing, symmetrical wide camera angle` para capturar la mayor cantidad de información del set como placa base.
   - **Enfoque (CRÍTICO):** Debe especificar `Every element from foreground to background is in perfectly sharp focus (deep depth of field, f/11 aperture, no blur, no bokeh)`. No debe haber nada desenfocado.
   - **Vacío:** `NO PEOPLE. EMPTY CHAIR.` El set debe ser solo el fondo/escenario.
   - **Estética:** Inyecta las directrices visuales del workspace/proyecto (ej. `Ultra-realistic, cinematic High-End, shot on ARRI Alexa 65, 8k resolution, photorealistic architecture`).
   - **Logo:** Si corresponde, añade `perfectly defined, undistorted, elegant glowing neon sign that perfectly mimics the shape of the provided reference logo`.

## Expected output
Creación de un archivo en la carpeta `sets/` con el prompt estructurado, seguido de un mensaje al usuario confirmando la ruta del archivo y recomendándole probar el prompt en su motor de generación (Midjourney/Nanobanana).
