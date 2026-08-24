---
name: media-render
description: Divide guion final en micro-videos y genera prompts listos para IA
---

# media-render

## When to use
Usa este comando cuando el storyboard final esté aprobado para preparar todo para la generación de video por IA.

## How to use
1. Lee el storyboard aprobado en el proyecto activo.
2. **Revisa el Lore (Casting/Props):** Antes de escribir los prompts, verifica si el storyboard menciona entidades (ej: "Cody" o "La Salteña"). Si es así, lee la carpeta `workspaces/[WORKSPACE_ACTIVO]/characters/` y `casting/` para buscar sus fichas técnicas, incluyendo su estilo de ropa estricto y configuración de voz (`Voice Style`).
3. Extrae cada escena o toma individualmente. **La duración de cada micro-video debe ser exactamente la que marca el Storyboard (Ej: 3s, 5s, 7s).** ¡Nunca unas escenas! Cada toma del storyboard debe ser un archivo de video independiente.
4. Genera prompts ESTRUCTURADOS **bajo el estándar "Image-to-Video"**. Para CADA escena del storyboard generarás DOS archivos: `scene_XXX_image.md` y `scene_XXX_video.md`.
   - **PASO A: PROMPT DE IMAGEN BASE (`scene_XXX_image.md`)**
     - Prompt estático en INGLÉS para generar el "Keyframe" inicial (Midjourney / Imagen3).
     - Describir al personaje usando su ropa y colores estandarizados de su hoja de casting (no inventar colores si el casting dice "neutral" o genérico).
     - **Estilo Visual:** Inyecta el `visuals.style_override` del `manifest.yaml` y asegúrate de describir el fondo sin usar nombres específicos de ciudades o marcas que causen alucinaciones textuales (Ej: usa "the Andes" en lugar de "Cochabamba").
   - **PASO B: PROMPT DE VIDEO (`scene_XXX_video.md`)**
     - **ESTRUCTURA GOOGLE FLOW VEO (CRÍTICA):** El prompt debe ser en INGLÉS (excepto bloques de diálogo/comandos fijos) ESTRUCTURADO con las siguientes reglas:
       - **Inicio:** Define el estilo, formato y duración EXACTA (Ej: "Hyper-realistic cinematic video, vertical 9:16, exact duration 6 seconds.") y ubica a los personajes en el mismo entorno que la imagen.
       - **Refuerzo de Personaje:** Repite EXACTAMENTE la misma ropa y aspecto de la hoja de casting (Ej: "Preserve Henry's established face, adult male... Preserve his high-end MTB cycling gear...").
       - **SPEAKER CONTROL (Si hay diálogo/cara visible):** (Ej: "SPEAKER CONTROL: Henry speaks confidently directly to the camera.").
       - **REGLA DE ENFOQUE (Si hay diálogo/cara visible):** (Ej: "REGLA DE ENFOQUE DEL HABLANTE: Si solo un personaje habla, cambia de inmediato a un plano medio corto de ese personaje al comenzar el diálogo. Mantén continuidad de posición, vestuario, iluminación y fondo.").
       - **CAMERA / TIMING:** Describe la acción y cámara (Ej: "CAMERA / TIMING: The camera performs a smooth crash zoom...").
       - **LANGUAGE Y VOICE STYLE (CRÍTICO SI HAY VOZ):** Extrae el estilo de voz del casting (Ej: "LANGUAGE: All spoken dialogue must be ONLY in neutral Latin American Spanish. Voice Style: Confident and natural male tone, deep voice that inspires confidence. Do not translate, paraphrase or rewrite the provided dialogue.").
       - **FLOW SAFETY:** `FLOW SAFETY: fictional adults only, safe nonviolent context, respectful natural behavior, no recognizable people, minors, brands, logos, protected characters or readable text.`
       - **VOZ / DIÁLOGO:** ¡Todo va en este archivo de video!
         - Si el personaje NO se ve hablando a cámara (POV/voz en off/acción), usa: `VOZ EN OFF (PERSONAJE habla):` seguido del `"Diálogo"`.
         - Si el personaje SÍ se ve hablando a cámara, usa: `LIPSYNC A — ESCENA X — (PERSONAJE habla):` seguido del `"Diálogo"`.
       - **SOUND (SFX):** IGNORA los efectos de sonido.
   - **PREVENCIÓN DE ALUCINACIONES Y NEGATIVE PROMPT:** 
     - **Negative Prompt:** Al final de AMBOS documentos, incluye `NEGATIVE PROMPT:` con todas las prohibiciones visuales (Ej: `No logos, no text, no FOX brand, no mutations`).
     - **Mouth Closed:** Si hay cara pero NO habla, añade `CRITICAL: The character must NOT speak. Mouth is closed.`
5. **MÚSICA Y SFX:** Lee los campos `Audio / SFX` del storyboard. Si el proyecto tiene un mood musical claro, genera un archivo `render/music.md` con un prompt en inglés optimizado para plataformas como Suno AI o Udio.
6. Guarda TODOS los resultados dentro de la carpeta `render/` (Ej: `render/scene_001_video.md`, `render/scene_001_image.md`, `render/music.md`).
7. Asegura que cada archivo de prompt tenga metadata YAML (platform, model, seed, negative_prompt, etc.) siguiendo las directrices de `AGENTS.md`.

## Examples
*Usuario:* "/media-render"
*Agente:* Genera archivos individuales por escena y prepara los prompts hiper-detallados (con control de cámara, voz y estructura VEO) listos para IA.

## Expected output
Escenas divididas y todos los prompts generados y organizados, con inyección directa de Voiceoff, Lipsync y metadata, listos para plataformas IA.
