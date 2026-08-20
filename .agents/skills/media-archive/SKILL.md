---
name: media-archive
description: Archiva un proyecto para ocultarlo de las listas activas
---

# media-archive

## When to use
Usa este skill cuando el usuario desee archivar un proyecto de video que ha sido finalizado, cancelado o pausado indefinidamente, para evitar generar ruido visual en las listas de trabajo activo.

## How to use
1. Identifica el workspace y el proyecto que el usuario quiere archivar.
2. Crea el directorio `workspaces/[WORKSPACE_ACTIVO]/projects/_archive` si no existe.
3. Mueve la carpeta física del proyecto de `projects/` a `workspaces/[WORKSPACE_ACTIVO]/projects/_archive/[NOMBRE_DEL_PROYECTO]`. **No modifiques el README.md.**
4. Confirma al usuario que el proyecto ha sido movido al archivo.

## Examples
*Usuario:* "/media-archive un-robot-en-cochabamba"
*Agente:* Mueve la carpeta a `workspaces/cody/projects/_archive/0003-un-robot-en-cochabamba` y reporta el éxito.

## Expected output
El directorio del proyecto es movido físicamente a `projects/_archive`.
