---
name: media-commit
description: Hace commit git incremental con mensaje descriptivo
---

# media-commit

## When to use
Usa este comando frecuentemente después de completar hitos importantes (nuevo proyecto, nuevo guion, renderizado, etc.) para guardar el estado del progreso de manera estructurada.

## How to use
1. Detecta los cambios recientes usando herramientas o scripts de git.
2. Formula un mensaje descriptivo y profesional (ej. "feat: guion v2 para proyecto X").
3. Ejecuta git add . y git commit.
4. Muestra al usuario el hash y el mensaje del commit resultante.

## Examples
*Usuario:* "/media-commit"
*Agente:* "Commit guardado correctamente: feat: generación de prompts para escenas de VEO."

## Expected output
El repositorio local se actualiza mediante un commit de Git con un mensaje descriptivo de la etapa actual.
