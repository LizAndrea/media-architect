---
name: media-assets
description: Registra y gestiona assets locales y URLs
---

# media-assets

## When to use
Usa este comando al importar o generar nuevos recursos multimedia (imágenes, video, audios) para el proyecto, o cuando se requiera registrar URLs externas de inspiración/plataformas.

## How to use
1. Pregunta si se registrará un archivo local o una URL.
2. Si es local, copia el archivo a la carpeta correspondiente en `assets/` (images, audio, video).
3. Si es URL, crea un registro en `assets/references/`.
4. Actualiza `manifest.yaml` con la metadata del asset (fecha, descripción, proveedor si fue generado externamente, y costo estimado).

## Examples
*Usuario:* "/media-assets registra esta URL como inspiración para escena 1"
*Agente:* Registra la URL en `assets/references/url_registry.yaml` y actualiza el manifiesto.

## Expected output
Archivos y links organizados y catalogados con correcta metadata en el sistema del proyecto.
