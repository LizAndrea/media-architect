---
name: media-new
description: Crea nuevo proyecto de video dentro del workspace activo
---

# media-new

## When to use
Usa este comando para crear un nuevo proyecto de video para el workspace activo actual.

## How to use
1. **Recopilación:** Si el usuario no proporcionó un nombre o tipo de video, pídele que los especifique.
2. **Creación y Seguridad:** Dentro del workspace activo, crea el nuevo proyecto en la ruta `workspaces/[WORKSPACE_ACTIVO]/projects/`. **Nomenclatura (CRÍTICO):** Usa el estándar de ID auto-incremental `000X-kebab-case` (Ej: si el último proyecto en `projects/` o en `projects/_archive/` es `0003-xxx`, el tuyo debe ser `0004-[nombre]`). Verifica que el nombre no exista. **NUNCA sobrescribas** nada.
3. **Copia de Plantillas:** Copia el contenido de `templates/video-project/` al nuevo directorio.
4. **POBLAR PLANTILLAS (CRÍTICO):** Reemplaza TODOS los placeholders. En `manifest.yaml` actualiza `project_id`, `name`, `type`, la fecha actual. En `AGENTS.md` y `README.md` desarrolla la visión creativa.
5. **Estructura Interna:** Crea las carpetas `script/`, `casting/`, `sets/`, `storyboard/`, `scenes/`, `prompts/video/`, `prompts/image/`, `prompts/audio/`, `assets/`, `render/` dentro del proyecto.
6. **Carga Automática:** Una vez creado, lee los archivos recién modificados para tenerlos en contexto y recomiéndale al usuario iniciar el guion con `/media-script`.

## Examples
*Usuario:* "/media-new documental sobre historia de bolivia"
*Agente:* Calcula que el último proyecto es 0014, entonces inicializa la estructura bajo `workspaces/workspace-activo/projects/0015-historia-bolivia` y recomienda escribir el guion.

## Expected output
Estructura de directorios del proyecto creada en la carpeta `projects/` (incluyendo `casting/`) con ID auto-incremental y configurada correctamente.
