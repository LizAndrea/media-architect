---
name: media-new
description: Crea nuevo proyecto de video dentro del workspace activo
---

# media-new

## When to use
Usa este comando para crear un nuevo proyecto de video para el workspace activo actual.

## How to use
1. **Recopilación:** Si el usuario no proporcionó un nombre o tipo de video, pídele que los especifique. Adicionalmente, verifica si este video incluirá a los personajes de la marca (casting) o si será genérico/B-Roll.
2. **Creación y Seguridad:** Dentro del workspace activo, crea el nuevo proyecto en la ruta `workspaces/[WORKSPACE_ACTIVO]/projects/`. **Nomenclatura (CRÍTICO):** Usa el estándar de ID auto-incremental `000X-kebab-case` (Ej: si el último proyecto en `projects/` o en `projects/_archive/` es `0003-xxx`, el tuyo debe ser `0004-[nombre]`). Verifica que el nombre no exista. **NUNCA sobrescribas** nada.
3. **Copia de Plantillas:** Copia el contenido de `templates/video-project/` al nuevo directorio.
4. **POBLAR PLANTILLAS (CRÍTICO):** Reemplaza TODOS los placeholders. En `manifest.yaml` actualiza `project_id`, `name`, `type`, la fecha actual y rellena el bloque `casting.characters` (deja vacío `[]` si es genérico o pon `[nombre_personaje]` si aplica). En `AGENTS.md` y `README.md` desarrolla la visión creativa.
5. **Estructura Interna:** Crea las carpetas `script/`, `storyboard/`, `scenes/`, `prompts/video/`, `prompts/image/`, `prompts/audio/`, `assets/`, `render/` dentro del proyecto.
6. **Carga Automática:** Una vez creado, lee los archivos recién modificados para tenerlos en contexto y recomiéndale al usuario utilizar `/media-commit` si desea guardar estos cambios.

## Examples
*Usuario:* "/media-new documental sobre historia de bolivia"
*Agente:* Calcula que el último proyecto es 0014, entonces inicializa la estructura bajo `workspaces/workspace-activo/projects/0015-historia-bolivia` y recomienda hacer commit.

## Expected output
Estructura de directorios del proyecto creada en la carpeta `projects/` con ID auto-incremental y configurada correctamente con plantillas adaptadas.
