---
name: media-in
description: Selecciona workspace y proyecto activo para acotar el contexto
---

# media-in

## When to use
Usa este skill para establecer el enfoque de trabajo en un workspace y proyecto específico antes de ejecutar otros comandos, limitando así el contexto.

## How to use
1. **Selección de Workspace:** Ejecuta directamente el comando `[ -f ./venv/bin/python ] && ./venv/bin/python scripts/list_active.py || python3 scripts/list_active.py`. **INSTRUCCIÓN CRÍTICA:** Inmediatamente después, usa `ask_question`. HAZLO SIEMPRE, incluso si hay un solo workspace. NO tomes decisiones lógicas, solo muestra el menú.
2. **Selección de Proyecto:** Ejecuta `[ -f ./venv/bin/python ] && ./venv/bin/python scripts/list_active.py NOMBRE_DEL_WORKSPACE_SELECCIONADO || python3 scripts/list_active.py NOMBRE_DEL_WORKSPACE_SELECCIONADO`. **INSTRUCCIÓN CRÍTICA:** Usa inmediatamente `ask_question`. NO RAZONES.
3. **Carga de Contexto:** Usa tu herramienta `view_file` para leer directamente los archivos `workspaces/NOMBRE_WORKSPACE/AGENTS.md` y `workspaces/NOMBRE_WORKSPACE/projects/NOMBRE_PROYECTO/AGENTS.md`. **CRÍTICO:** NO ejecutes comandos `list_dir` para buscar carpetas ni adivines rutas, ve directo a los archivos.
4. **Reporte:** Al responderle al usuario, **especifica las rutas relativas completas** de los archivos que leíste (Ej: `workspaces/cody/AGENTS.md`) en lugar de decir genéricamente "Leí AGENTS.md".

## Examples
*Usuario:* "/media-in workspace acme proyecto comercial-verano"
*Agente:* Lee el contexto y confirma: "Contexto activo: acme / comercial-verano".

## Expected output
El agente ajusta su atención al workspace y proyecto especificado y lo reporta al usuario.
