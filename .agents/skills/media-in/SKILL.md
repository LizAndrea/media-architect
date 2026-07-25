---
name: media-in
description: Selecciona cliente y proyecto activo para acotar el contexto
---

# media-in

## When to use
Usa este skill para establecer el enfoque de trabajo en un cliente y proyecto específico antes de ejecutar otros comandos, limitando así el contexto.

## How to use
1. **Selección de Cliente:** Ejecuta directamente el comando `[ -f ./venv/bin/python ] && ./venv/bin/python scripts/list_active.py || python3 scripts/list_active.py`. **INSTRUCCIÓN CRÍTICA:** Inmediatamente después, usa `ask_question`. HAZLO SIEMPRE, incluso si hay un solo cliente. NO tomes decisiones lógicas, solo muestra el menú.
2. **Selección de Proyecto:** Ejecuta `[ -f ./venv/bin/python ] && ./venv/bin/python scripts/list_active.py NOMBRE_DEL_CLIENTE_SELECCIONADO || python3 scripts/list_active.py NOMBRE_DEL_CLIENTE_SELECCIONADO`. **INSTRUCCIÓN CRÍTICA:** Usa inmediatamente `ask_question`. NO RAZONES.
3. **Carga de Contexto:** Usa tu herramienta `view_file` para leer directamente los archivos `clients/NOMBRE_CLIENTE/AGENTS.md` y `clients/NOMBRE_CLIENTE/NOMBRE_PROYECTO/AGENTS.md`. **CRÍTICO:** NO ejecutes comandos `list_dir` para buscar carpetas ni adivines rutas, ve directo a los archivos.
4. **Reporte:** Al responderle al usuario, **especifica las rutas relativas completas** de los archivos que leíste (Ej: `clients/cody/AGENTS.md`) en lugar de decir genéricamente "Leí AGENTS.md".

## Examples
*Usuario:* "/media-in cliente acme proyecto comercial-verano"
*Agente:* Lee el contexto y confirma: "Contexto activo: acme / comercial-verano".

## Expected output
El agente ajusta su atención al cliente y proyecto especificado y lo reporta al usuario.
