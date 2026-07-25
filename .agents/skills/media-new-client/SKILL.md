---
name: media-new-client
description: Crea un nuevo cliente (empresa/marca/productora)
---

# media-new-client

## When to use
Usa este skill para empezar a trabajar con un nuevo cliente, marca o productora.

## How to use
1. Solicita al usuario el nombre del cliente y detalles básicos.
2. Crea una carpeta para el cliente en `clients/` usando formato `kebab-case`.
3. Copia `templates/client/AGENTS.md` y `templates/client/README.md` a la nueva carpeta.
4. Actualiza la información en los archivos copiados con los datos del cliente.

## Examples
*Usuario:* "/media-new-client para una empresa de zapatillas llamada RunFast"
*Agente:* Crea `clients/run-fast/` y configura sus archivos.

## Expected output
Carpeta del cliente configurada correctamente en `clients/` lista para añadir proyectos de video.
