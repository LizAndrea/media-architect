# GUÍA: GOOGLE FLOW VEO 3.1 Y OMNI FLASH

Esta guía describe cómo optimizar prompts para los modelos de video de Google AI Studio.

## Modelos
1. **Veo 3.1 Quality:**
   - Mejor para tomas complejas, texturas realistas y anatomía humana.
   - Tiempo de generación: más lento.
   - Aspect Ratios soportados: 16:9, 9:16, 1:1.
   - Duración máxima ideal: 8-10 segundos.

2. **Veo 3.1 Fast:**
   - Para borradores rápidos o tomas de paisajes sin humanos detallados.
   - Tiempo de generación: muy rápido.

3. **Omni Flash:**
   - Extremadamente rápido, ideal para iteraciones tempranas de storyboards animados.

## Mejores Prácticas de Prompting (En Inglés)
- Empieza con el tipo de plano y movimiento de cámara: `A medium shot panning slowly right...`
- Describe la acción principal de forma clara y directa.
- Usa adjetivos precisos para la iluminación: `cinematic dramatic lighting, neon rim light...`
- Evita prompts excesivamente largos. Mantén el foco en lo visual.
