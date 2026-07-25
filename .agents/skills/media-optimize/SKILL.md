---
name: media-optimize
description: Comprime imágenes generadas (PNG) a formatos ligeros (JPG)
---

# media-optimize

## When to use
Usa este comando después de haber generado imágenes o storyboards visuales pesados (como archivos PNG), para comprimirlos antes de subirlos al repositorio de Git y mantener el proyecto ligero.

## How to use
1. Identifica el directorio que contiene las imágenes pesadas (usualmente `storyboard/assets/` o `assets/` dentro del proyecto del cliente).
2. Asegúrate de que el entorno virtual de Python exista en la raíz (`venv/`) y las dependencias de `scripts/requirements.txt` estén instaladas.
3. Ejecuta el script de optimización mediante bash, activando el entorno virtual:
   `source venv/bin/activate && python scripts/media_optimizer.py <ruta_del_directorio>`
4. Muestra un resumen al usuario de cuántas imágenes fueron convertidas exitosamente.

## Examples
*Usuario:* "/media-optimize storyboard/assets"
*Agente:* Activa el entorno, corre `media_optimizer.py` apuntando a la carpeta, y reporta cuántas imágenes `.png` se convirtieron a `.jpg`.

## Expected output
Las imágenes pesadas en la carpeta objetivo se comprimen y reemplazan (ej. PNG a JPG), según la configuración de calidad del `.env`.
