---
name: media-new
description: Crea nuevo proyecto de video dentro del cliente activo
---

# media-new

## When to use
Usa este comando para crear un nuevo proyecto de video para el cliente activo actual.

## How to use
1. Solicita nombre y tipo del video (short, youtube, documentary, commercial).
2. **Creación y Seguridad:** Crea una carpeta dentro del cliente activo usando el estándar de la industria `YYYYMMDD-kebab-case` (Ej: `20260725-un-robot-en-cochabamba`). **CRÍTICO:** Antes de crearla, verifica que el nombre no exista ya. Si existe, detente inmediatamente y avisa al usuario, **NUNCA sobrescribas** un proyecto existente.
3. Copia `templates/video-project/AGENTS.md`, `README.md`, `manifest.yaml` y la configuración `config/providers.yaml`.
4. Crea la estructura interna: `script/`, `storyboard/`, `scenes/`, `prompts/video/`, `prompts/image/`, `prompts/audio/`, `assets/`, `render/`.
5. **ACTUALIZACIÓN CRÍTICA DEL README:** Abre el archivo `README.md` del cliente activo (Ej: `clients/cody/README.md`) y **añade obligatoriamente** una nueva fila a la tabla "Proyectos de Video" documentando el nuevo proyecto con 6 columnas: (Nombre con link relativo `[nombre](./nombre/)`, Formato, Estado, Archivado (escribe "No"), Fecha, Descripción). Si omites este paso, se romperá la base de datos.
6. Recomienda al usuario utilizar `/media-commit` si desea guardar estos cambios en el control de versiones.

## Examples
*Usuario:* "/media-new documental sobre historia de bolivia"
*Agente:* Inicializa la estructura bajo `clients/cliente-activo/historia-bolivia` y recomienda hacer commit.

## Expected output
Estructura de directorios del proyecto creada y configurada correctamente con plantillas adaptadas.
