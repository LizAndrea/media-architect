---
name: media-in
description: Selecciona workspace y proyecto activo para acotar el contexto
---

# media-in

## When to use
Usa este skill para establecer el enfoque de trabajo en un workspace y proyecto específico antes de ejecutar otros comandos, limitando así el contexto.

## How to use

Existen tres modos de usar este skill: **Modo Rápido**, **Modo Global** y **Modo Interactivo**.

### MODO RÁPIDO (Recomendado): `/media-in [workspace]/[id]` o `/media-in [workspace]/post/[id]`
1. **Para Proyectos de Video (`/media-in [workspace]/[id]`):**
   - Rellena el ID con ceros a la izquierda hasta tener 4 dígitos (ej. `1` -> `0001`). 
   - Busca en `workspaces/[WORKSPACE]/projects/` la carpeta que empiece con ese prefijo (Ej: `0001-lanzamiento-...`).
   - Carga el contexto: `workspace.yaml`, `AGENTS.md`, `manifest.yaml` y `README.md`.
2. **Para Publicaciones / Infografías (`/media-in [workspace]/post/[id]` o `/media-in [workspace]/posts/[id]`):**
   - Rellena el ID con ceros a la izquierda hasta tener 4 dígitos (ej. `1` -> `0001`).
   - Busca en `workspaces/[WORKSPACE]/posts/` la carpeta que empiece con ese prefijo (Ej: `0001-mas-alla-del-prompt`).
   - Carga el contexto: `workspace.yaml`, `workspaces/[WORKSPACE]/AGENTS.md`, y dentro de la carpeta del post: `post.yaml`, `copy.md`, `prompt_image.md` y `README.md`.
   - Si el `post.yaml` tiene un `linked_project`, carga también la información básica de ese video para heredar personajes y sets.

### MODO GLOBAL (Ideación): `/media-in [workspace]`
Si el usuario solo provee el nombre del workspace sin ID de proyecto ni post (Ej: `/media-in novalabs`):
1. **Carga de Contexto (Workspace):** Usa `view_file` para leer `workspaces/[WORKSPACE]/AGENTS.md`, `workspaces/[WORKSPACE]/workspace.yaml` y `workspaces/[WORKSPACE]/README.md`.
2. Informa al usuario que el contexto global fue cargado exitosamente y que está listo para usar comandos como `/media-ideas`, `/media-new` o `/media-post`. No busques ni cargues proyectos ni posts.

### MODO INTERACTIVO (Fallback): `/media-in` sin argumentos
1. Ejecuta `[ -f ./venv/bin/python ] && ./venv/bin/python scripts/list_active.py || python3 scripts/list_active.py`.
2. Usa `ask_question` para que el usuario seleccione el Workspace.
3. Ejecuta el mismo script pasándole el workspace elegido para listar los proyectos.
4. Usa `ask_question` para que el usuario seleccione el Proyecto.
5. Carga los archivos de contexto descritos en el paso 3 y 4 del Modo Rápido.

## Reporte Final
Al responderle al usuario, **especifica las rutas relativas completas** de todos los archivos que leíste y haz un resumen brevísimo indicando el nivel de contexto (Solo Workspace, o Workspace + Proyecto).

## Examples
*Usuario:* "/media-in cody/1"
*Agente:* Carga Workspace y Proyecto. Responde: "Contexto activo: cody / 0001-quien-es-cody".
*Usuario:* "/media-in novalabs/post/1"
*Agente:* Carga Workspace y Post. Responde: "Contexto activo: novalabs / Post 0001 (Más Allá del Prompt)".
*Usuario:* "/media-in cody"
*Agente:* Carga solo Workspace. Responde: "Contexto global activo: cody. Listo para ideación."
