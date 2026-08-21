---
name: media-script
description: Genera y permite iterar guion profesional
---

# media-script

## When to use
Usa este comando después de crear un proyecto de video para escribir y refinar el guion.

## How to use
1. **ASUME EL ROL DE:** **Guionista Profesional (Hollywood Screenwriter) y Estratega de Contenido Viral**.
2. **Carga de Contexto Automática:** No le pidas la visión al usuario de entrada. Lee primero el `AGENTS.md` y `manifest.yaml` del proyecto activo para extraer la temática, duración, plataformas y tono. Solo pregunta si la visión está vacía o es muy ambigua.
3. **Declaración de Reparto (CRÍTICO):** Revisa el bloque `casting.characters` en el `manifest.yaml` del proyecto.
   - Si contiene personajes (Ej: `[cody]`), el guion debe estar protagonizado por este personaje.
   - Si está vacío (`[]`), es contenido **Genérico / Institucional / B-Roll**. Está estrictamente prohibido incluir al personaje en pantalla o hacerlo hablar en primera persona. Mantén el "sabor" de la marca pero con tomas genéricas o voz en off genérica.
   - Si `voiceover_only` es `true`, el personaje narra pero no aparece físicamente.
4. **Ingeniería Viral (CRÍTICO):** Aplica estrictamente la estructura psicológica (Hook de 0-3s, Alta Utilidad, Cliffhanger, CTA) definida en el `AGENTS.md` del workspace.
5. **Redacción del Guion:** Genera un master script profesional utilizando la plantilla correspondiente en `templates/scripts/` (Ej: `master-script-short.md`). 
   - **Locación (CRÍTICO):** Lee el campo `visuals.location` del `manifest.yaml`. Debes ambientar las escenas explícitamente en ese lugar geográfico o concepto (Ej: "Cochabamba, Bolivia") para darle identidad cultural o visual al guion (Ej: "EXT. CERRO TUNARI, COCHABAMBA - DÍA"). Si está vacío, propón tú una locación coherente.
   - **Separación Visual/Audio:** Separa claramente lo que se ve en cámara (Visual) de lo que se escucha (Audio) para facilitar el storyboard.
   - **Lucha contra el Sesgo de Belleza de la IA (AI Beauty Bias):** Si el guion requiere que un objeto o escena se vea feo, de mala calidad, arruinado o amateur (Ej. un "antes" de un producto o un cuarto sucio), la columna Visual DEBE usar **adjetivos extremos y agresivos** (Ej: colores lavados, blanquecino, calidad pésima, sobreexpuesto). De lo contrario, los siguientes agentes y la IA generarán algo demasiado estético.
   - **REGLA DE ORO DE LOS 8 SEGUNDOS (CRÍTICO):** Como el video final se generará con IA (Ej. Google Flow VEO), **NINGUNA TOMA/ESCENA** en la tabla del guion puede durar más de 8 segundos continuos. Si una acción narrativa toma 15 segundos, divídela obligatoriamente en 2 tomas (Ej. Toma 2A - 8s y Toma 2B - 7s).
6. **Guardado y Métricas:** Guarda el resultado en `script/script.md`. Analiza el "engagement score" y "viral potential" basándote en las rúbricas de `resources/metrics/` y presenta estas métricas al usuario para recibir su feedback.
7. **Actualización de Base de Datos:** Cuando el usuario apruebe el guion final, actualiza los valores `engagement_score` y `viral_potential` dentro del `manifest.yaml` del proyecto.
8. **Casting & Siguientes Pasos:** Al finalizar y aprobar, recomiéndale al usuario usar `/media-casting` para generar los prompts visuales del reparto, y `/media-commit` para versionar el guion.

## Examples
*Usuario:* "/media-script hagamos el guion, quiero un tono épico y rápido para TikTok"
*Agente:* Genera `script.md`, muestra métricas de retención y pide feedback.

## Expected output
Guiones generados, calificados con métricas de engagement, y guardados en el archivo maestro `script.md`.
