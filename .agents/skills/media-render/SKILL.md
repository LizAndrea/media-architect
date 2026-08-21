---
name: media-render
description: Divide guion final en micro-videos y genera prompts listos para IA
---

# media-render

## When to use
Usa este comando cuando el storyboard final esté aprobado para preparar todo para la generación de video por IA.

## How to use
1. Lee el storyboard aprobado en el proyecto activo.
2. **Revisa el Lore (Casting/Props):** Antes de escribir los prompts, verifica si el storyboard menciona entidades (ej: "Cody" o "La Salteña"). Si es así, lee la carpeta `workspaces/[WORKSPACE_ACTIVO]/characters/` para buscar sus fichas técnicas.
3. Extrae cada escena o toma individualmente. **La duración de cada micro-video debe ser exactamente la que marca el Storyboard (Ej: 3s, 5s, 7s).** ¡Nunca unas escenas! Cada toma del storyboard debe ser un archivo de video independiente.
4. Genera prompts ESTRUCTURADOS EN INGLÉS.
   - **ESTILO VISUAL (CRÍTICO):** Lee el bloque `visuals.style_override` del `manifest.yaml` del proyecto. Si tiene contenido, inyéctalo al inicio de cada prompt.
   - **CRÍTICO (ESTRUCTURA GOOGLE FLOW):** Al redactar el PROMPT de video, debes usar ESTRICTAMENTE la siguiente estructura basada en cronología (en inglés para máxima compatibilidad, aunque la estructura puede tener los títulos en inglés: SCENE, ACTION, CAMERA, AUDIO).
     - **SCENE:** Describe el entorno, la iluminación (usando `manifest.yaml`), y al personaje usando el tag `@ID_Rol` (Ej: `@MTB_Cyclist is riding...`).
     - **ACTION:** Divide la acción en bloques de 2 segundos (Ej: `0-2s: @MTB_Cyclist rides fast... 2-4s: He brakes and dust kicks up... 4-6s: The dust settles down...`). Esto es vital para la progresión temporal.
     - **AUDIO (Lip-Sync):** Define el diálogo exacto (Ej: `LIP-SYNC DIALOGUE: "Texto"` y la actitud). Si no hay diálogo, pon explícitamente `CRITICAL: Mouth is closed. No speaking.`
     - **SOUND (SFX):** Describe los efectos de sonido. **Añade siempre "NO MUSIC. Ambient SFX only."** ya que la música se añadirá en post-producción.
   - **USO DE TAGS (@):** Como los videos durarán menos de 8s, la interfaz de Flow permite usar el tag `@Nombre`. Vuelve a inyectar el bloque `*LORE GLOSSARY:* \n *@ID_Rol = [Descripción]*` al inicio del archivo como referencia, y usa SIEMPRE el `@ID_Rol` dentro del prompt.
   - **LOCACIÓN Y CONTINUIDAD (CRÍTICO):** Extrae la locación específica de esa escena desde el guion/storyboard (Ej: "INT. SALTEÑERIA") y combínala con la macro-locación global del `manifest.yaml` (Ej: "Cochabamba, Bolivia"). Como cada micro-video se renderiza por separado, **DEBES describir el fondo exacto en CADA UNO de los prompts** combinando ambas (Ej: "inside a traditional Salteñeria in Cochabamba, Bolivia"). Jamás asumas que la IA sabe dónde están.
   - **FILTRO ANTI-LITERALIDAD (Cámaras y Marcas):** Al redactar el prompt, **JAMÁS** uses marcas de cámaras (Ej: Kodak, Arri). Sustituye por términos genéricos (Ej: "cinematic film look"). Además, debes incluir siempre instrucciones anti-logos para la ropa (Ej: `plain clothing, NO logos, NO text, NO brands`) para evitar que la IA alucine marcas deportivas genéricas (como Nike o Fox).
   - **LIP-SYNC & DIÁLOGO:** 
     - Si la escena **SÍ** incluye voz en off o diálogo, incluye al final: `*LIP-SYNC DIALOGUE:* "[Texto exacto]" (Language: Spanish) (Acting Direction: [Extrae la emoción de la escena, ej: Out of breath, frustrated, calm])`.
     - Si la escena **NO** incluye diálogo (solo acción o música), debes incluir dentro del `*PROMPT*`: `CRITICAL: The character must NOT speak. Mouth is closed.` y NO crear bloque de Lip-Sync. Esto evita que la IA alucine diálogos en inglés.
5. **MÚSICA Y SFX:** Lee los campos `Audio / SFX` del storyboard. Si el proyecto tiene un mood musical claro, genera un archivo `render/music.md` con un prompt en inglés optimizado para plataformas como Suno AI o Udio (especificando género, ritmo, instrumentos y mood, siempre pidiendo "instrumental only").
6. Guarda TODOS los resultados unificados dentro de la carpeta `render/` utilizando las convenciones oficiales de nombrado (Ej: `render/scene_001_video.md`, `render/scene_001_image.md`, `render/voiceover.md`, `render/music.md`).
7. Asegura que cada archivo de prompt tenga metadata YAML (platform, model, seed, negative_prompt, etc.) siguiendo las directrices de `AGENTS.md`.

## Examples
*Usuario:* "/media-render"
*Agente:* Genera archivos individuales por escena y prepara los prompts en inglés para Google Flow VEO y otros proveedores.

## Expected output
Escenas divididas y todos los prompts generados y organizados, listos para ser introducidos en plataformas IA.
