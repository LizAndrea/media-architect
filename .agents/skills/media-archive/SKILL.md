---
name: media-archive
description: Archiva un proyecto para ocultarlo de las listas activas
---

# media-archive

## When to use
Usa este skill cuando el usuario desee archivar un proyecto de video que ha sido finalizado, cancelado o pausado indefinidamente, para evitar generar ruido visual en las listas de trabajo activo.

## How to use
1. Identifica el cliente y el proyecto que el usuario quiere archivar.
2. Abre el archivo `README.md` del cliente activo (Ej: `clients/cody/README.md`).
3. Encuentra la fila correspondiente al proyecto en la tabla "Proyectos de Video" y cambia el valor de la columna "Archivado" de 'No' a **'Sí'**. **CRÍTICO:** No modifiques la columna "Estado" (para conservar en qué etapa se quedó) ni muevas carpetas físicas en el disco.
4. Confirma al usuario que el estado del proyecto ha sido actualizado exitosamente en la base de datos (README).

## Examples
*Usuario:* "/media-archive un-robot-en-cochabamba"
*Agente:* Mueve la carpeta a `clients/cody/_archive/20260725-un-robot-en-cochabamba`, actualiza el README y reporta el éxito.

## Expected output
El directorio del proyecto es movido a `_archive` y el README del cliente es actualizado.
