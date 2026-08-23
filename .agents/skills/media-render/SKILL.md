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
4. Genera prompts ESTRUCTURADOS EN INGLÉS **bajo el estándar "Image-to-Video"**. Para CADA escena del storyboard generarás DOS archivos: `scene_XXX_image.md` y `scene_XXX_video.md`.
   - **PASO A: PROMPT DE IMAGEN BASE (`scene_XXX_image.md`)**
     - Prompt estático para generar el "Keyframe" inicial (Midjourney / Imagen3).
     - Si hay personajes, usa sus Hojas de Referencia y descríbelos detalladamente con ropa y colores específicos (Ej: "A young man wearing a dusty black and red jersey...").
     - **Estilo Visual:** Inyecta el `visuals.style_override` del `manifest.yaml` y asegúrate de describir el fondo (combina locación de escena con locación macro de `manifest.yaml`).
   - **PASO B: PROMPT DE VIDEO (`scene_XXX_video.md`)**
     - **ESTRUCTURA GOOGLE FLOW VEO (CRÍTICA):** El texto principal debe ser un párrafo descriptivo ESTRUCTURADO con las siguientes reglas:
       - **Inicio:** Define el estilo, formato y duración (Ej: "Hyper-realistic cinematic... vertical 9:16, approximately 6 seconds.") y ubica a los personajes en el mismo entorno que la imagen ("Henry sits in a dark room...").
       - **Refuerzo de Personaje:** Repite EXACTAMENTE la misma ropa del prompt de imagen (Ej: "Henry wears exactly the same dusty black and red jersey").
       - **Acción y Cámara:** Describe la acción fluida y el movimiento de cámara (Ej: "The camera performs a smooth crash zoom...").
       - **SPEAKER CONTROL (Si hay diálogo/cara visible):** Especifica quién habla (Ej: "SPEAKER CONTROL: Henry speaks first in a frustrated tone...").
       - **SPEAKER FOCUS RULE (Si hay diálogo/cara visible):** (Ej: "SPEAKER FOCUS RULE: Maintain medium-close framing on Henry's face...").
       - **FLOW SAFETY:** Añade SIEMPRE este boilerplate al final del párrafo principal: `FLOW SAFETY: fictional adults only, safe nonviolent context, respectful natural behavior, no recognizable people, minors, brands, logos, protected characters or readable text.`
       - **LIPSYNC / DIÁLOGO:** Si el personaje NO se ve (POV/lejos), **no pongas SPEAKER CONTROL ni audio** y usa la *Estrategia de Voz en Off* creando un archivo `voiceoff_XXX.md` falso (pantalla verde). Si el personaje SE VE, añade debajo del párrafo principal:
         `LIPSYNC A — ESCENA X — (PERSONAJE):`
         `"[Diálogo exacto]"`
         *(Si hay más personajes hablando, usa LIPSYNC B, C, etc.)*
       - **SOUND (SFX):** IGNORA los efectos de sonido en los prompts. El usuario lo añadirá en post-producción.
   - **PREVENCIÓN DE ALUCINACIONES Y NEGATIVE PROMPT (CRÍTICO):** 
     - **Negative Prompt:** Al final de AMBOS documentos, incluye una sección `NEGATIVE PROMPT:` con todas las prohibiciones visuales (Ej: `No logos, no text, no FOX brand, no mutations`).
     - **Sesgo de Belleza:** Si algo debe verse mal o amateur, usa adjetivos extremos (`terrible, washed-out, ugly`).
     - **POV:** Si es primera persona añade "CRITICAL: No other people in front of camera".
     - **Mouth Closed:** Si hay cara pero NO habla, añade `CRITICAL: The character must NOT speak. Mouth is closed.`
5. **MÚSICA Y SFX:** Lee los campos `Audio / SFX` del storyboard. Si el proyecto tiene un mood musical claro, genera un archivo `render/music.md` con un prompt en inglés optimizado para plataformas como Suno AI o Udio (especificando género, ritmo, instrumentos y mood, siempre pidiendo "instrumental only").
6. Guarda TODOS los resultados unificados dentro de la carpeta `render/` utilizando las convenciones oficiales de nombrado (Ej: `render/scene_001_video.md`, `render/scene_001_image.md`, `render/voiceover.md`, `render/music.md`).
7. Asegura que cada archivo de prompt tenga metadata YAML (platform, model, seed, negative_prompt, etc.) siguiendo las directrices de `AGENTS.md`.

## Examples
*Usuario:* "/media-render"
*Agente:* Genera archivos individuales por escena y prepara los prompts en inglés para Google Flow VEO y otros proveedores.

## Expected output
Escenas divididas y todos los prompts generados y organizados, listos para ser introducidos en plataformas IA.
