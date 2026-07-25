---
name: media-pipeline
description: Ejecuta todo el flujo inicial de forma automática
---

# media-pipeline

## When to use
Usa este comando para automatizar el ciclo completo: desde la generación del guion hasta la creación de prompts, de manera rápida.

## How to use
1. Verifica que haya un cliente y proyecto activo (si no, pide usar `/media-in`).
2. Ejecuta `/media-script` con los parámetros proporcionados y espera validación.
3. Al validar, ejecuta `/media-storyboard` y espera validación.
4. Al validar, ejecuta `/media-render`.
5. Se encarga de usar `/media-commit` automáticamente en cada hito importante.

## Examples
*Usuario:* "/media-pipeline para el proyecto activo, temática viajes espaciales"
*Agente:* Guía al usuario de manera orquestada paso a paso reduciendo fricción.

## Expected output
El proyecto se lleva de inicio a fin (hasta la fase de pre-producción/prompts) de un solo golpe con checkpoints.
