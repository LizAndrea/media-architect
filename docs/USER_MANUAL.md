# 🎬 Media-Architect: Manual de Usuario Definitivo

Bienvenido a **Media-Architect**, el framework CLI impulsado por IA para la producción audiovisual automatizada, gestión de agencias (Workspaces) y generación de video con inteligencia artificial (Google Flow VEO, Kling, Sora, Midjourney).

Este manual está diseñado para enseñar a productores, directores creativos y editores cómo utilizar el ecosistema de forma profesional, evitando los errores comunes de las inteligencias artificiales.

---

## 🏛️ 1. Arquitectura del Sistema: Core vs Workspaces

Entender esta filosofía de "Separación de Poderes" es clave para dominar el framework:

*   **EL CORE (Los Skills):** Aquí viven las "habilidades mecánicas" del sistema (`/media-render`, `/media-script`, etc.). Definen **CÓMO** se hacen las cosas (la sintaxis exacta, las líneas de tiempo por segundos, el formato de los negative prompts). Son reglas universales protegidas que aplican a todos tus proyectos.
*   **LOS WORKSPACES (Las Productoras):** Son carpetas aisladas (ej. `neuro-viral-studio`). Definen el **QUÉ**. Contienen la identidad visual (Ej. colores Teal & Orange, ritmo de cortes), el arquetipo publicitario, los personajes (actores virtuales) y los proyectos.

---

## 🚀 2. El Flujo de Trabajo (Workflow Paso a Paso)

Crear un video viral de alta gama requiere seguir este orden estricto. Cada paso es ejecutado por un comando inteligente (Skill).

### Paso 1: Configurar la Productora
Si estás empezando una marca nueva, usa el comando:
> **`/media-new-workspace`**
Esto creará una carpeta aislada con su propio `workspace.yaml` (donde defines tu estilo visual, luces y tipo de cámara) y su `AGENTS.md` (donde le das un contexto creativo a la agencia).

### Paso 2: El Casting (Crear Personajes)
Si tu video necesita protagonistas humanos recurrentes, usa:
> **`/media-character`**
Esto generará un perfil exhaustivo del personaje en la carpeta `characters/` (ej. `ciclista.md`) con descripciones físicas milimétricas para evitar que la IA cambie de actor entre toma y toma.

### Paso 3: Crear un Nuevo Proyecto
Entra a tu Workspace y ejecuta:
> **`/media-new`**
Te pedirá el título del video (Ej. `0002-curso-ia`). El sistema orquestará y creará las carpetas para el guion, el storyboard, el render y las redes sociales.

### Paso 4: Escribir el Guion Maestro
> **`/media-script`**
La IA tomará tu idea y la transformará en un guion profesional de doble columna (Visual/Audio). 
*⚠️ Regla de Oro:* Ninguna toma visual dura más de 8 segundos (límite actual para mantener alta coherencia en IAs como Google Flow).

### Paso 5: Generar Prompts de Video (El Render)
> **`/media-render`**
El paso más mágico. La IA traducirá tu guion en español a una serie de archivos individuales `.md` (ej. `scene_001_video.md`) escritos en un inglés hiper-técnico, estructurados matemáticamente (0-2s, 2-4s) para ser copiados y pegados directamente en Google Flow.

### Paso 6: Redes Sociales
> **`/media-publish`**
Analizará tu proyecto finalizado y generará un archivo `publish.md` con los títulos SEO, los hashtags y el "copy" persuasivo adaptado a los algoritmos de TikTok, YouTube Shorts, Instagram y Facebook Reels.

---

## 🛑 3. Prevención de Alucinaciones (Best Practices)

Las IAs de video son increíblemente literales y si cometes un error en el prompt, "alucinarán" (inventarán cosas extrañas). Media-Architect maneja esto por ti, pero debes entender por qué lo hace:

*   **El `NEGATIVE PROMPT`:** Las IAs ignoran instrucciones como "(No pongas rodilleras)". En su lugar, el framework usa un bloque aislado al final del archivo llamado `NEGATIVE PROMPT:` donde se prohíben conceptos (Ej: `No logos, no text, no floating faces`).
*   **Caras Flotantes (Error de Audio):** Si pides sincronización de labios (`LIP-SYNC`) en un plano donde no se ve el rostro (ej. un plano subjetivo POV o un celular), la IA entrará en pánico y dibujará una cara flotando en el cielo solo para tener una boca que animar. Por eso, el sistema automáticamente prohíbe mencionar el audio en tomas sin rostro.
*   **Sesgo de Belleza (AI Beauty Bias):** La IA está entrenada para hacer que todo se vea estéticamente hermoso. Si necesitas que algo se vea feo (ej. una foto arruinada para un "Antes y Después"), debes usar adjetivos destructivos extremos en tu guion: *"Foto asquerosa, amateur, quemada por el sol, calidad pésima"*.

---

## 🎙️ 4. La Estrategia del "Voiceoff Verde" (Audio Avanzado)

¿Cómo mantienes la misma voz de tu actor IA en las escenas POV donde la cara no aparece en el video?
El framework soluciona esto con la táctica de extracción de audio:
1. Al ejecutar `/media-render`, si detecta que hay diálogo pero no hay rostro, generará un archivo secundario llamado `voiceoff_XXX.md`.
2. Este prompt engaña a la IA ordenándole: *"Dibuja al personaje estático sobre un fondo verde leyendo este diálogo"*.
3. **Tu trabajo:** Generas ese video auxiliar en Flow, lo llevas a CapCut, haces clic derecho en "Extraer Audio" y borras el clip verde. ¡Obtienes la pista de voz perfecta, fluida y consistente sin arruinar tu plano original!

---
*Desarrollado con arquitectura modular por Media-Architect AI.*
