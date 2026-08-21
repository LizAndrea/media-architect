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
     - **AUDIO (Lip-Sync):** **REGLA DE ORO:** Solo puedes usar el comando de `LIP-SYNC DIALOGUE` si la cara del personaje es claramente visible en la toma (Ej: Close up). Si la toma es un POV, una captura de pantalla, o el personaje está muy lejos, DEBES poner `CRITICAL: No speaking. No lip-sync.` para evitar que la IA alucine una cara flotante. Todo diálogo "en off" se añadirá en post-producción.
     - **SOUND (SFX):** La generación de audio en IA de video es deficiente. **DEBES poner siempre:** `MUTE. DO NOT GENERATE SOUND OR MUSIC. No audio track. Ambient and SFX will be added in post-production.`
   - **USO DE TAGS (@):** Como los videos durarán menos de 8s, la interfaz de Flow permite usar el tag `@Nombre`. Vuelve a inyectar el bloque `*LORE GLOSSARY:* \n *@ID_Rol = [Descripción]*` al inicio del archivo como referencia, y usa SIEMPRE el `@ID_Rol` dentro del prompt.
   - **LOCACIÓN Y CONTINUIDAD (CRÍTICO):** Extrae la locación específica de esa escena desde el guion/storyboard (Ej: "INT. SALTEÑERIA") y combínala con la macro-locación global del `manifest.yaml` (Ej: "Cochabamba, Bolivia"). Como cada micro-video se renderiza por separado, **DEBES describir el fondo exacto en CADA UNO de los prompts** combinando ambas (Ej: "inside a traditional Salteñeria in Cochabamba, Bolivia"). Jamás asumas que la IA sabe dónde están.
   - **FILTRO ANTI-LITERALIDAD (Cámaras y Marcas):** Al redactar el prompt, **JAMÁS** uses marcas de cámaras tradicionales (Ej: Kodak, Arri). Sustituye por términos genéricos (Ej: "cinematic film look"). **EXCEPCIÓN:** Puedes usar la palabra "GoPro" exclusivamente cuando necesites lograr el efecto visual ultra-gran angular (POV) de deportes extremos. Además, debes incluir siempre instrucciones anti-logos para la ropa (Ej: `plain clothing, NO logos, NO text, NO brands`) para evitar que la IA alucine marcas deportivas genéricas (como Nike o Fox).
   - **PREVENCIÓN DE ALUCINACIONES (CRÍTICO):** Las IAs de video cometen errores de contexto lógicos. Al redactar cada toma, DEBES anticipar y bloquear estos errores usando "(CRÍTICO: No [X])":
     - Si es un POV (Primera persona): Añade `CRITICAL: No other people in front of the camera, empty path.`
     - Si son manos sosteniendo un objeto (celular, taza): Añade `CRITICAL: No faces or people visible in the background.`
     - Si es un deporte amateur/casual: Añade prohibiciones de equipo extremo (Ej: `NO knee pads, NO heavy armor, NO race bibs`).
     - Si es una calle vacía: Añade `CRITICAL: No cars, no pedestrians.`
     - **SESGO DE BELLEZA DE LA IA (AI Beauty Bias):** Los modelos de IA siempre intentan hacer que todo se vea bonito y profesional. Si el guion requiere que algo se vea feo, amateur, de mala calidad o arruinado (Ej: una foto de "Antes", un cuarto desordenado, comida quemada), **DEBES usar adjetivos extremos y agresivos** (Ej: `terrible, washed-out, low-contrast, overexposed, amateur, ugly`) o la IA ignorará la instrucción y lo dibujará bonito.
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
