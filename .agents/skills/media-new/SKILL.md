---
name: media-new
description: Crea nuevo proyecto de video dentro del cliente activo
---

# media-new

## When to use
Usa este comando para crear un nuevo proyecto de video para el cliente activo actual.

## How to use
1. Solicita nombre y tipo del video (short, youtube, documentary, commercial).
2. Crea una carpeta dentro del cliente activo en formato `kebab-case`.
3. Copia `templates/video-project/AGENTS.md`, `README.md`, `manifest.yaml` y la configuración `config/providers.yaml`.
4. Crea la estructura interna: `script/`, `storyboard/`, `scenes/`, `prompts/video/`, `prompts/image/`, `prompts/audio/`, `assets/`, `render/`.
5. Ejecuta el primer commit de git informando la creación del proyecto.

## Examples
*Usuario:* "/media-new documental sobre historia de bolivia"
*Agente:* Inicializa la estructura bajo `clients/cliente-activo/historia-bolivia` y hace el commit.

## Expected output
Estructura de directorios del proyecto creada y configurada correctamente con plantillas adaptadas.
