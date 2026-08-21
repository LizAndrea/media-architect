---
name: media-review
description: Revisa y critica el guion o storyboard como un Productor Ejecutivo y Director de Fotografía experto
---

# media-review

## When to use
Usa este comando en cualquier iteración de guion (`script.md`) o storyboard (`storyboard.md`) para obtener un análisis técnico y profesional de la industria.

## How to use
1. Lee el guion o storyboard generado en el proyecto activo.
2. **Carga de Contexto (CRÍTICO):** Lee el `manifest.yaml` del proyecto. Fíjate específicamente en los bloques `casting`, `visuals.style_override` y `visuals.location`.
3. Asume el rol de **Director Creativo y Director de Fotografía Experto (Nivel Industria/Hollywood)**.
4. **IMPRIME EL REPORTE EN EL CHAT:** Redacta este análisis como un mensaje normal de texto en el chat para que el usuario pueda leerlo. El reporte debe evaluar si el documento cumple con la promesa del manifest, e incluir:
   - **✅ Puntos Fuertes:** Lo que funciona narrativa o visualmente.
   - **⚠️ Crítica Constructiva:** Fallos de ritmo, falta de detalles técnicos (lentes, iluminación), o **desviaciones del manifest** (Ej: el manifest pide B-Roll pero el guion metió a Cody, o pide Cochabamba y no hay referencias andinas).
   - **🛠️ Sugerencias de Industria:** Cambios precisos que harían el proyecto más "premium".
5. Una vez impreso el reporte, utiliza la herramienta `ask_question` para preguntarle al usuario: *"¿Qué te parecen estas sugerencias? ¿Quieres que las aplique en el documento?"*
6. Si el usuario acepta, **sobrescribe** el archivo original (no crees versiones nuevas) y recuérdale usar `/media-commit` para guardar el historial.

## Expected output
Un reporte de crítica constructiva profesional y la capacidad de iterar automáticamente el guion o storyboard hacia una calidad superior.
