---
name: media-status
description: Genera un reporte completo del estado del proyecto activo
---

# media-status

## When to use
Usa este comando en cualquier punto para dar al usuario un panorama visual del progreso, tareas pendientes y calidad actual del proyecto activo.

## How to use
1. Verifica el contexto activo. Si no hay, avisa que deben usar `/media-in`.
2. Analiza el directorio y crea un reporte de:
   - 📊 PROGRESO GENERAL
   - 📝 GUIÓN (métricas, iteraciones)
   - 🎬 ESCENAS (total, duración)
   - 🤖 PROMPTS (cantidad por medio, modelo y estado)
   - 🖼️ ASSETS (cantidad registrada)
   - 📈 MÉTRICAS (engagement actual)
   - 🕒 HISTORIAL (últimos commits)
   - ⚠️ PENDIENTES
   - 💡 RECOMENDACIONES
3. Imprime este reporte usando Emojis y Markdown.

## Examples
*Usuario:* "/media-status"
*Agente:* Imprime tabla de reporte y dice "Falta renderizar los prompts de la escena 5".

## Expected output
Un reporte completo en español impreso en la terminal/chat con recomendaciones priorizadas de próximos pasos.
