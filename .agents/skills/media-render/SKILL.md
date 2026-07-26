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
   - **CRÍTICO (LORE GLOSSARY):** Si hay personajes en el array de Reparto, **DEBES inyectar el bloque de variables (LORE GLOSSARY)** al inicio del archivo del prompt (Ej: `*LORE GLOSSARY:* \n *[ID_Tag] = [Visual Prompt en Inglés]*`).
   - **LOCACIÓN Y CONTINUIDAD (CRÍTICO):** Cada micro-video se renderiza por separado. Por lo tanto, **DEBES describir la locación o el fondo exacto en CADA UNO de los prompts** (ej: "in a cyberpunk room with neon signs" o "on a dirt path in Parque Nacional Tunari"). Jamás asumas que la IA sabe dónde está el personaje.
   - **LIP-SYNC & DIÁLOGO:** 
     - Si la escena **SÍ** incluye voz en off o diálogo, incluye al final: `*LIP-SYNC DIALOGUE:* "[Texto exacto]" (Language: Spanish)`.
     - Si la escena **NO** incluye diálogo (solo acción o música), debes incluir dentro del `*PROMPT*`: `CRITICAL: The character must NOT speak. Mouth is closed.` y NO crear bloque de Lip-Sync. Esto evita que la IA alucine diálogos en inglés.
5. Guarda TODOS los resultados unificados dentro de la carpeta `render/` utilizando las convenciones oficiales de nombrado (Ej: `render/scene_001_video.md`, `render/scene_001_image.md`, `render/voiceover.md`).
6. Asegura que cada archivo de prompt tenga metadata YAML (platform, model, seed, negative_prompt, etc.) siguiendo las directrices de `AGENTS.md`.

## Examples
*Usuario:* "/media-render"
*Agente:* Genera archivos individuales por escena y prepara los prompts en inglés para Google Flow VEO y otros proveedores.

## Expected output
Escenas divididas y todos los prompts generados y organizados, listos para ser introducidos en plataformas IA.
