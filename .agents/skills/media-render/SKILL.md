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
3. Divide el contenido en micro-escenas de 8-10 segundos en la carpeta `scenes/` (ej: `scene_001.md`).
4. Genera prompts ESTRUCTURADOS EN INGLÉS basándose en `config/providers.yaml`.
   - **CRÍTICO:** Cuando un personaje/prop registrado aparezca en la escena, **DEBES HACER COPY-PASTE de su "Visual Prompt" en inglés** (extraído de su ficha técnica) dentro del prompt de video para garantizar consistencia visual absoluta. ¡No inventes ropa ni características nuevas!
5. Guarda los resultados en `prompts/video/`, `prompts/image/`, y `prompts/audio/`.
6. Asegura que cada archivo de prompt tenga metadata YAML (platform, model, seed, negative_prompt, etc.).

## Examples
*Usuario:* "/media-render"
*Agente:* Genera archivos individuales por escena y prepara los prompts en inglés para Google Flow VEO y otros proveedores.

## Expected output
Escenas divididas y todos los prompts generados y organizados, listos para ser introducidos en plataformas IA.
