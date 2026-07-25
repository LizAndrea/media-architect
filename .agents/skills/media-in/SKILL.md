---
name: media-in
description: Selecciona cliente y proyecto activo para acotar el contexto
---

# media-in

## When to use
Usa este skill para establecer el enfoque de trabajo en un cliente y proyecto específico antes de ejecutar otros comandos, limitando así el contexto.

## How to use
1. Lista los clientes disponibles en la carpeta `clients/`.
2. Lista los proyectos asociados a ese cliente.
3. Solicita confirmación si no se especifica.
4. Lee el `AGENTS.md` del cliente y el del proyecto.
5. Usa esa información como base de contexto para todo lo demás.

## Examples
*Usuario:* "/media-in cliente acme proyecto comercial-verano"
*Agente:* Lee el contexto y confirma: "Contexto activo: acme / comercial-verano".

## Expected output
El agente ajusta su atención al cliente y proyecto especificado y lo reporta al usuario.
