---
name: media-render
description: Divide guion final en micro-videos y genera prompts listos para IA
---

# media-render

## When to use
Usa este comando cuando el storyboard final esté aprobado para preparar todo para la generación de video por IA.

## How to use
1. Lee el storyboard aprobado.
2. Divide el contenido en micro-escenas de 8-10 segundos en la carpeta `scenes/` (ej: `scene_001.md`).
3. Genera prompts ESTRUCTURADOS EN INGLÉS basándose en `config/providers.yaml`.
4. Guarda en `prompts/video/`, `prompts/image/`, `prompts/audio/`.
5. Asegura que cada archivo de prompt tenga metadata YAML (platform, model, seed, negative_prompt, etc.).

## Examples
*Usuario:* "/media-render"
*Agente:* Genera archivos individuales por escena y prepara los prompts en inglés para Google Flow VEO y otros proveedores.

## Expected output
Escenas divididas y todos los prompts generados y organizados, listos para ser introducidos en plataformas IA.
