---
name: media-init
description: Inicializa media-architect creando estructura base
---

# media-init

## When to use
Usa este skill cuando necesites inicializar el repositorio por primera vez, configurando toda la estructura base del framework `media-architect`.

## How to use
El agente debe asegurarse de que todas las carpetas, plantillas (`templates/`), recursos (`resources/`) y archivos de configuración raíz como `AGENTS.md`, `README.md` y `.gitignore` existan en el directorio del proyecto. 
**REGLA DE SEGURIDAD CRÍTICA:** Si alguno de estos archivos o carpetas ya existe, el agente **NO DEBE** sobrescribirlos ni modificarlos. Este comando es estrictamente incremental y seguro.

## Examples
*Usuario:* "Inicializa media-architect"
*Agente:* Crea toda la estructura y avisa que el entorno está listo para crear el primer workspace.

## Expected output
Estructura completa de directorios y archivos base creados correctamente.
