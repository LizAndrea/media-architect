---
name: media-script
description: Genera y permite iterar guion profesional
---

# media-script

## When to use
Usa este comando después de crear un proyecto de video para escribir y refinar el guion.

## How to use
1. Solicita visión, temática, duración objetivo, estilo, audiencia, y tono.
2. Genera un master script profesional utilizando la plantilla correspondiente en `templates/scripts/`. 
   - **CRÍTICO:** Como experto, el agente DEBE proponer una locación exacta y coherente para el video (Ej: "INT. SALTEÑERIA TRADICIONAL COCHABAMBINA - DÍA" o "EXT. PLAZA 14 DE SEPTIEMBRE - TARDE"). Esta locación debe especificarse claramente al inicio del guion y en cada escena para mantener la continuidad visual.
3. Analiza el "engagement score" y "viral potential" (usando rúbricas de `resources/metrics/`).
4. Guarda como `script/v1_script.md`.
5. Permite iteraciones del usuario guardándolas como `v2`, `v3`, etc.
6. Cuando se apruebe, marca como `script/final_script.md`.

## Examples
*Usuario:* "/media-script hagamos el guion, quiero un tono épico y rápido para TikTok"
*Agente:* Genera `v1_script.md`, muestra métricas y pide feedback.

## Expected output
Guiones generados, calificados con métricas de engagement, y versión final aprobada en `final_script.md`.
