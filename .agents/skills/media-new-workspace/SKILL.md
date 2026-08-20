---
name: media-new-workspace
description: Crea un nuevo workspace (empresa/marca/productora)
---

# media-new-workspace

## When to use
Usa este skill para empezar a trabajar con un nuevo workspace, marca o productora.

## How to use
1. Solicita al usuario el nombre del workspace y detalles básicos.
2. Crea una carpeta para el workspace en `workspaces/` usando formato `kebab-case`, y dentro de ella crea las subcarpetas `projects/`, `characters/` y `assets/`.
3. Copia `templates/workspace/AGENTS.md`, `templates/workspace/README.md` y `templates/workspace/workspace.yaml` a la nueva carpeta.
4. Actualiza la información en los archivos copiados con los datos del workspace, especialmente en el `workspace.yaml`.

## Examples
*Usuario:* "/media-new-workspace para una empresa de zapatillas llamada RunFast"
*Agente:* Crea `workspaces/run-fast/` y configura sus archivos.

## Expected output
Carpeta del workspace configurada correctamente en `workspaces/` lista para añadir proyectos de video.
