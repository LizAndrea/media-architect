---
name: media-new
description: Crea nuevo proyecto de video dentro del workspace activo
---

# media-new

## When to use
Usa este comando para crear un nuevo proyecto de video para el workspace activo actual.

## How to use
1. Solicita nombre y tipo del video (short, youtube, documentary, commercial).
2. **Creación y Seguridad:** Crea una carpeta dentro del workspace activo bajo la ruta `workspaces/[WORKSPACE_ACTIVO]/projects/`. **Nomenclatura (CRÍTICO):** Usa el estándar de ID auto-incremental `000X-kebab-case` (Ej: si el último proyecto en `projects/` o en `projects/_archive/` es `0003-xxx`, el tuyo debe ser `0004-nuevo-proyecto`). Antes de crearla, verifica que el nombre no exista ya. **NUNCA sobrescribas** un proyecto existente.
3. Copia `templates/video-project/AGENTS.md`, `README.md`, `manifest.yaml` y la configuración `config/providers.yaml` al nuevo directorio.
4. **POBLAR PLANTILLAS (CRÍTICO):** Abre los archivos `AGENTS.md` y `README.md` que acabas de copiar al nuevo proyecto y **reemplaza todos los placeholders** (ej. `[Nombre del proyecto]`, `[Duración]`, visión creativa, etc.) con la información real del video que te proporcionó el usuario. Asegúrate también de establecer la fecha de creación correcta en el `manifest.yaml`. No los dejes vacíos.
5. Crea la estructura interna: `script/`, `storyboard/`, `scenes/`, `prompts/video/`, `prompts/image/`, `prompts/audio/`, `assets/`, `render/`.
6. Recomienda al usuario utilizar `/media-commit` si desea guardar estos cambios en el control de versiones.

## Examples
*Usuario:* "/media-new documental sobre historia de bolivia"
*Agente:* Calcula que el último proyecto es 0014, entonces inicializa la estructura bajo `workspaces/workspace-activo/projects/0015-historia-bolivia` y recomienda hacer commit.

## Expected output
Estructura de directorios del proyecto creada en la carpeta `projects/` con ID auto-incremental y configurada correctamente con plantillas adaptadas.
