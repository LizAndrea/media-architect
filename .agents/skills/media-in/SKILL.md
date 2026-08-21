---
name: media-in
description: Selecciona workspace y proyecto activo para acotar el contexto
---

# media-in

## When to use
Usa este skill para establecer el enfoque de trabajo en un workspace y proyecto específico antes de ejecutar otros comandos, limitando así el contexto.

## How to use

Existen tres modos de usar este skill: **Modo Rápido**, **Modo Global** y **Modo Interactivo**.

### MODO RÁPIDO (Recomendado): `/media-in [workspace]/[id]`
Si el usuario provee el workspace y el ID (Ej: `/media-in cody/1` o `/media-in cody/0001`):
1. **Identificación:** Rellena el ID con ceros a la izquierda hasta tener 4 dígitos (ej. `1` -> `0001`). 
2. **Búsqueda:** Usa `list_dir` o `run_command` para listar `workspaces/[WORKSPACE]/projects/` y encontrar la carpeta exacta que empiece con ese prefijo (Ej: `0001-quien-es-cody`).
3. **Carga de Contexto (Workspace):** Usa `view_file` para leer `workspaces/[WORKSPACE]/AGENTS.md`, `workspaces/[WORKSPACE]/workspace.yaml` y `workspaces/[WORKSPACE]/README.md`.
4. **Carga de Contexto (Proyecto):** Usa `view_file` para leer el `AGENTS.md`, `README.md` y `manifest.yaml` que se encuentran dentro de la carpeta del proyecto encontrada.

### MODO GLOBAL (Ideación): `/media-in [workspace]`
Si el usuario solo provee el nombre del workspace sin ID de proyecto (Ej: `/media-in cody`):
1. **Carga de Contexto (Workspace):** Usa `view_file` para leer `workspaces/[WORKSPACE]/AGENTS.md`, `workspaces/[WORKSPACE]/workspace.yaml` y `workspaces/[WORKSPACE]/README.md`.
2. Informa al usuario que el contexto global fue cargado exitosamente y que está listo para usar comandos como `/media-ideas` o `/media-new`. No busques ni cargues proyectos.

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
*Usuario:* "/media-in cody"
*Agente:* Carga solo Workspace. Responde: "Contexto global activo: cody. Listo para ideación."
