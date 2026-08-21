---
name: media-ideas
description: Genera 10 ideas de contenido viral basadas en el contexto del workspace
---

# media-ideas

## When to use
Usa este comando en la fase de **Ideación** (Top of the Funnel), cuando el usuario necesita inspiración o propuestas concretas para generar contenido viral antes de crear un proyecto formal. Ideal para campañas, promoción de cursos o crecimiento orgánico.

## How to use
1. **Verificación de Contexto:** Asegúrate de tener cargado el contexto global del workspace (archivos `AGENTS.md` y `workspace.yaml`). Si no lo tienes, pide al usuario que ejecute `/media-in [workspace]`.
2. **Adopción de Rol:** Asume inmediatamente el rol de **Estratega de Contenido Viral y Director Creativo**.
3. **Generación de Ideas (Reglas Estrictas):**
   - Genera 10 ideas basadas en el tema o solicitud del usuario.
   - **CRÍTICO:** Cada idea DEBE respetar estrictamente las reglas definidas en la sección "Ingeniería Viral y Embudos (Hooks & CTAs)" del `AGENTS.md` del workspace.
   - **CRÍTICO:** No propongas ideas genéricas ni violes las "Líneas Rojas" del workspace.
4. **Formato de Salida:** Presenta las 10 ideas en un formato muy fácil de digerir. Para cada idea, incluye:
   - **Título Provisional**
   - **Hook (Gancho):** (Ej: "¿Tu código React es lento? Es por esto.")
   - **Núcleo de Valor:** (Breve resumen de la utilidad)
   - **CTA:** (Hacia dónde empuja el embudo, ej: "Comenta X para el curso")
5. **Call to Action del Sistema:** Al final de la lista, pregúntale al usuario cuál idea le gusta más y recomiéndale ejecutar **`/media-new [nombre-del-proyecto]`** para materializarla.

## Examples
*Usuario:* "/media-ideas para promocionar un curso de React para juniors"
*Agente:* Genera 10 ideas estructuradas (Hook -> Valor -> CTA) respetando el tono de la marca y pregunta con cuál avanzar hacia `/media-new`.

## Expected output
Una lista estructurada e inspiradora de 10 ideas de alto potencial viral, diseñadas a medida de la psicología del workspace.
