---
name: media-review
description: Revisa y critica el guion o storyboard como un Productor Ejecutivo y Director de Fotografía experto
---

# media-review

## When to use
Usa este comando en cualquier iteración de guion (`script.md`) o storyboard (`storyboard.md`) para obtener un análisis técnico y profesional de la industria.

## How to use
1. Lee el guion o storyboard generado en el proyecto activo.
2. **Carga de Contexto (CRÍTICO):** Lee el `manifest.yaml` del proyecto actual y el `AGENTS.md` del workspace activo. Esto te dará los arquetipos de publicidad y reglas de neuromarketing.
3. Asume el rol de **Auditor de Neuromarketing y Director de Fotografía Experto**.
4. **IMPRIME EL REPORTE COMPLETO EN EL CHAT (CRÍTICO):** Redacta todo el análisis detallado como texto visible en el chat para que el usuario pueda leerlo con calma antes de cualquier decisión. Debes evaluar obligatoriamente:
   - **✅ Puntos Fuertes:** Lo que funciona narrativa o visualmente.
   - **⚠️ Auditoría de Reglas (CRÍTICO):** 
     - *Regla de los 8 Segundos:* Revisa la tabla. ¿Alguna toma dura más de 8 segundos? Si es así, es un error fatal para IA.
     - *Neuromarketing:* ¿El Hook (0-4s) tiene un patrón de interrupción? ¿El ritmo coincide con el arquetipo (Ej. Estilo Nike, Starbucks)?
   - **🛠️ Sugerencias de Industria:** Cambios precisos explicados al detalle (ej. Hook alternativo, dinamismo, microexpresiones) para que el usuario vea exactamente qué se cambiaría.
5. Formula al final de tu mensaje las opciones claras para que el usuario responda en el chat o elija cómo proceder. Si usas `ask_question`, asegúrate de que el texto previo ya haya sido enviado y sea visible.
6. Si el usuario acepta, **sobrescribe** el archivo original (no crees versiones nuevas).

## Expected output
Un reporte de crítica constructiva profesional y la capacidad de iterar automáticamente el guion o storyboard hacia una calidad superior.
