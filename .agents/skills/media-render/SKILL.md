---
name: media-render
description: Divide guion final en micro-videos y genera prompts listos para IA
---

# media-render

## When to use
Usa este comando cuando el storyboard final esté aprobado para preparar todo para la generación de video por IA.

## How to use
1. Lee el storyboard aprobado en el proyecto activo.
2. **Revisa el Lore (Casting/Props):** Antes de escribir los prompts, verifica si el storyboard menciona entidades (ej: "Cody" o "La Salteña"). Si es así, lee la carpeta `clients/[CLIENTE_ACTIVO]/characters/` para buscar sus fichas técnicas.
3. Extrae cada escena o toma individualmente. **La duración de cada micro-video debe ser exactamente la que marca el Storyboard (Ej: 3s, 5s, 7s).** ¡Nunca unas escenas! Cada toma del storyboard debe ser un archivo de video independiente.
4. Genera prompts ESTRUCTURADOS EN INGLÉS.
   - **CRÍTICO (LORE GLOSSARY):** Si hay personajes en el array de Reparto, **DEBES inyectar el bloque de variables (LORE GLOSSARY)** al inicio del archivo del prompt (Ej: `*LORE GLOSSARY:* \n *[ID_Tag] = [Visual Prompt en Inglés]*`). Extrae este visual prompt de su ficha técnica (`characters/`). Luego, en el texto del prompt en sí, utiliza los tags (Ej: `[ID_Tag] walks...`).
   - **LIP-SYNC & DIÁLOGO:** Si la escena incluye voz en off o un personaje hablando a la cámara, **DEBES incluir un bloque al final del archivo llamado `*LIP-SYNC DIALOGUE:*`** con el texto exacto que el personaje dirá. Esto es vital para herramientas de próxima generación como Google Flow VEO o HeyGen que sincronizan los labios con el texto.
5. Guarda TODOS los resultados unificados dentro de la carpeta `render/` utilizando las convenciones oficiales de nombrado (Ej: `render/scene_001_video.md`, `render/scene_001_image.md`, `render/voiceover.md`).
6. Asegura que cada archivo de prompt tenga metadata YAML (platform, model, seed, negative_prompt, etc.) siguiendo las directrices de `AGENTS.md`.

## Examples
*Usuario:* "/media-render"
*Agente:* Genera archivos individuales por escena y prepara los prompts en inglés para Google Flow VEO y otros proveedores.

## Expected output
Escenas divididas y todos los prompts generados y organizados, listos para ser introducidos en plataformas IA.
