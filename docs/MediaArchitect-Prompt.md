Eres un arquitecto experto en desarrollo de proyectos de IA y producción audiovisual. Tu tarea es inicializar y generar el proyecto completo llamado "media-architect" (https://github.com/LizAndrea/media-architect) siguiendo los estándares de Antigravity CLI y las mejores prácticas de la industria cinematográfica.

# CONTEXTO DEL PROYECTO

media-architect es un framework CLI para agencias/productoras de video que usan IA. Permite gestionar múltiples WORKSPACES, cada uno con sus PROYECTOS DE VIDEO, cubriendo el ciclo completo: desde la visión creativa hasta prompts listos para plataformas de generación de video (Google AI Studio con Veo 3.1/Omni Flash, y futuras integraciones con Runway, Sora, etc.).

## Objetivo del agente
Convertir una idea en texto (como "cómo llegar a Tarata en bici") en un video producido profesionalmente mediante IA, generando todos los artefactos necesarios (guiones, storyboards, prompts de video/audio/imagen, assets, metadata) de forma estructurada y versionada.

## Plataformas prioritarias
- **Principal:** Google AI Studio (Veo 3.1 Quality, Veo 3.1 Fast, Omni Flash) - escenas de 8-10 segundos
- **Secundarias (futuras):** Runway, Sora, Pika, Midjourney, ElevenLabs

## Idiomas
- Todo el CONTENIDO (guiones, narración, diálogos, documentación) en ESPAÑOL
- Todos los PROMPTS generados para IA (video, imagen, audio) en INGLÉS (mejores resultados en modelos)

# ESTRUCTURA DE ARCHIVOS

```
media-architect/
├── AGENTS.md
├── README.md
├── .gitignore
├── .agents/
│   └── skills/
│       ├── media-init/SKILL.md
│       ├── media-new-workspace/SKILL.md
│       ├── media-in/SKILL.md
│       ├── media-new/SKILL.md
│       ├── media-script/SKILL.md
│       ├── media-storyboard/SKILL.md
│       ├── media-review/SKILL.md
│       ├── media-render/SKILL.md
│       ├── media-pipeline/SKILL.md
│       ├── media-commit/SKILL.md
│       ├── media-archive/SKILL.md
│       ├── media-assets/SKILL.md
│       └── media-status/SKILL.md
├── templates/
│   ├── workspace/
│   │   ├── AGENTS.md
│   │   └── README.md
│   ├── video-project/
│   │   ├── AGENTS.md
│   │   └── README.md
│   ├── scripts/
│   │   ├── master-script-short.md
│   │   ├── master-script-youtube.md
│   │   ├── master-documentary.md
│   │   ├── master-commercial.md
│   │   ├── shot-list-template.md
│   │   └── scene-template.md
│   └── prompts/
│       ├── video-prompt-template.md
│       ├── image-prompt-template.md
│       └── audio-prompt-template.md
├── scripts/
│   ├── list_active.py
│   ├── media_optimizer.py
│   └── requirements.txt
├── venv/
├── workspaces/
│   └── .gitkeep
├── resources/
│   ├── character-templates/character-template.md
│   ├── cinematography/
│   │   ├── shot-types.md
│   │   ├── camera-movements.md
│   │   ├── lighting-styles.md
│   │   └── color-grading.md
│   ├── prompt-libraries/
│   │   ├── video-prompts-en.md
│   │   ├── image-prompts-en.md
│   │   ├── audio-prompts-en.md
│   │   └── negative-prompts-en.md
│   ├── video-types/
│   │   ├── shorts-specs.md
│   │   ├── youtube-specs.md
│   │   ├── documentary-specs.md
│   │   └── commercial-specs.md
│   └── metrics/
│       ├── engagement-rubric.md
│       └── viral-potential-rubric.md
└── docs/
    ├── workflow.md
    └── google-flow-guide.md
```

# ESTRUCTURA DE UN PROYECTO DE VIDEO (dentro de workspaces/[workspace]/[proyecto]/)

```
[proyecto]/
├── AGENTS.md
├── README.md
├── manifest.yaml
├── config/
│   ├── providers.yaml (configuración de plataformas IA)
│   └── prompt-templates.yaml (templates por tipo de medio)
├── script/
│   ├── script.md
│   ├── shot_list.md
│   ├── characters.md
│   └── iterations/
├── storyboard/
│   └── storyboard.md
├── scenes/
│   └── scene_001.md, scene_002.md, ... (micro-guiones 8-10s)
├── prompts/
│   ├── video/ (scene_XXX_video.md, scene_XXX_video_fast.md, scene_XXX_video_flash.md)
│   ├── image/ (scene_XXX_image.md, scene_XXX_image_reference.md)
│   └── audio/ (voiceover.md, dialogues.md, music.md, sfx.md)
├── assets/
│   ├── images/
│   ├── audio/
│   ├── video/
│   └── references/
│       └── url_registry.yaml
└── render/
    └── final_cuts/
```

# SISTEMA DE PROVEEDORES DE IA (config/providers.yaml)

Estructura del archivo de configuración de proveedores:

```yaml
# config/providers.yaml
providers:
  video:
    primary:
      platform: Google AI Studio
      model: Veo 3.1 Quality
      max_duration: 10s
      aspect_ratios: [9:16, 16:9, 1:1]
      api_endpoint: google_flow_veo
    alternates:
      - platform: Google AI Studio
        model: Veo 3.1 Fast
        use_case: "borradores rápidos"
      - platform: Google AI Studio
        model: Omni Flash
        use_case: "generación ultra-rápida"
      - platform: Runway
        model: Gen-4
        use_case: "futuro - cuando tengamos créditos"
  
  image:
    primary:
      platform: Google AI Studio
      model: Imagen 4
      api_endpoint: google_imagen
    alternates:
      - platform: Midjourney
        model: v6.1
        use_case: "futuro"
  
  audio:
    voiceover:
      platform: ElevenLabs
      model: Multilingual v2
    music:
      platform: Suno AI
      model: v4

preferences:
  default_duration: 8-10s
  default_aspect_ratio: 16:9
  language_prompts: english
  language_content: spanish
```

# CONTENIDO DE AGENTS.md (Nivel raíz)

Debe incluir:

## 1. DESCRIPCIÓN
media-architect como framework CLI para producción audiovisual con IA en agencias/productoras.

## 2. ROL DEL AGENTE
Actúa como equipo creativo completo con estas especialidades:
- 🎬 Director Creativo – Visión y storytelling
- ✍️ Guionista Profesional – Cine, publicidad, documentales, shorts virales
- 🎥 Director de Fotografía – Composición, lentes, iluminación, cámara
- 🎨 Diseñador Gráfico y Artista Digital
- 👤 Diseñador de Personajes y Avatares – Psicología, arcos, visuales
- 🔧 Ingeniero de Prompts Multimedia (EN para prompts, ES para contenido)
- 📊 Productor Multiplataforma – YouTube, TikTok, Instagram, Podcast, Documentales, Cortos
- 🎭 Especialista en Lenguaje Cinematográfico – Planos, transiciones, ritmo
- 🎞️ Editor y Post-productor
- 📈 Estratega de Contenido Viral y de Impacto
- 🎯 Analista de Engagement y Potencial Viral
- 📚 Archivista Digital – Gestión de assets locales y URLs

## 3. CONVENIOS DE NOMBRADO
- Workspaces: kebab-case ("mi-workspace-corp")
- Proyectos de video: Fecha + kebab-case ("20260725-como-llegar-a-tarata")
- Escenas: `scene_001.md`, `scene_002.md`
- Prompts de video: `scene_001_video.md`, `scene_001_video_fast.md`, `scene_001_video_flash.md`
- Prompts de imagen: `scene_001_image.md`, `scene_001_image_reference.md`
- Prompts de audio: `voiceover.md`, `music.md`, `sfx.md`
- Archivos únicos: `script.md`, `storyboard.md` (El versionamiento se maneja exclusivamente con Git a través de `/media-commit`)

## 4. FLUJO DE TRABAJO
Crear workspace → Crear proyecto → Visión/temática → Guion → Iterar → Storyboard → Dividir en escenas (8-10s para Google Flow) → Generar prompts → Registrar assets → Sugerir commit al usuario

## 5. CONTEXTO JERÁRQUICO
Cada workspace y proyecto tiene su propio AGENTS.md para mantener contexto acotado (evita token overhead)

## 6. ESTÁNDARES DE ESCENA
- Duración: 8-10 segundos (Google Flow VEO)
- Aspect ratio según tipo: 9:16 shorts, 16:9 youtube, 1:1 reels
- Metadata obligatoria por escena: plataforma, modelo, seed, negative prompt
- Cada prompt incluye YAML frontmatter con metadata del modelo usado

# BIBLIOTECA DE SKILLS (11 comandos)

## SKILL: media-init
- **Descripción:** Inicializa media-architect creando estructura base
- **Cuando usar:** Primera vez en el repositorio
- **Acciones:** Crear carpetas, copiar templates, generar .gitignore, README inicial
- **Output:** Estructura completa del framework lista para usar

## SKILL: media-new-workspace
- **Descripción:** Crea un nuevo workspace (empresa/marca/productora) dentro de workspaces/
- **Cuando usar:** Empezar a trabajar con un nuevo workspace
- **Acciones:** Solicitar nombre y datos del workspace, crear carpeta, copiar templates, crear AGENTS.md específico del workspace, crear README del workspace con lista de proyectos
- **Output:** Carpeta de workspace inicializada en workspaces/

## SKILL: media-in
- **Descripción:** Selecciona workspace y proyecto activo para acotar el contexto
- **Cuando usar:** Antes de trabajar en un proyecto
- **Acciones:** **ESTRATEGIA HÍBRIDA DE VELOCIDAD:** NO uses comandos ListDir lentos. Ejecuta directamente `[ -f ./venv/bin/python ] && ./venv/bin/python scripts/list_active.py` para obtener bases de datos. Usa Prompt Engineering estricto: *"INSTRUCCIÓN CRÍTICA: Lanza el ask_question inmediatamente, NO RAZONES, HAZLO SIEMPRE"*. Carga contexto del AGENTS.md del workspace y del proyecto. Reporta explícitamente las rutas leídas.
- **Output:** Contexto del proyecto cargado instantáneamente y listo para trabajar

## SKILL: media-new
- **Descripción:** Crea nuevo proyecto de video dentro del workspace activo
- **Cuando usar:** Empezar un nuevo video
- **Acciones:** Solicitar nombre y tipo (short/youtube/documentary/commercial), crear carpeta con estructura completa, copiar templates específicos del tipo de video, crear AGENTS.md del proyecto con metadata inicial, crear config/providers.yaml con configuración por defecto, sugerir al usuario hacer commit.
- **Output:** Proyecto de video inicializado con estructura completa

## SKILL: media-script
- **Descripción:** Genera y permite iterar guion profesional
- **Cuando usar:** Después de crear el proyecto
- **Acciones:** Solicitar visión, temática, duración. Generar master script, personajes, shot list. Analizar engagement score. Permitir iteraciones y sobrescribir `script.md`.
- **Output:** Guion profesional `script.md` en script/ con análisis de calidad

## SKILL: media-storyboard
- **Descripción:** Crea storyboard visual con anotaciones cinematográficas
- **Cuando usar:** Con guion final aprobado
- **Acciones:** Parsear shot list, generar storyboard por escena con: thumbnail descriptivo, descripción visual, tipo de plano, movimiento de cámara, iluminación, composición, tiempo, notas. Guardar en storyboard/
- **Output:** Storyboard completo con todas las escenas anotadas

## SKILL: media-review
- **Descripción:** Actúa como Director de Fotografía/Productor Ejecutivo para criticar y mejorar el guion o storyboard.
- **Cuando usar:** Para iterar y mejorar el guion (`script.md`) o el storyboard (`storyboard.md`) en cualquier etapa del proceso.
- **Acciones:** Analiza la versión actual, destaca puntos fuertes, encuentra debilidades técnicas (falta de ópticas, iluminación pobre, ritmo lento), propone mejoras de estándar Hollywood, y pregunta al usuario si desea aplicar los cambios para generar la siguiente iteración.
- **Output:** Reporte experto y generación de versión mejorada.

## SKILL: media-render
- **Descripción:** Divide guion final en micro-videos y genera prompts listos para IA
- **Cuando usar:** Con storyboard aprobado
- **Acciones:** Dividir guion en escenas de 8-10s (configurable), crear scene_XXX.md por cada una en scenes/, generar prompts ESTRUCTURADOS EN INGLÉS para cada escena en prompts/ organizados por tipo de medio (video/, image/, audio/). Cada prompt incluye metadata YAML con: platform, model, model_alternates (para A/B testing), aspect_ratio, duration, seed, negative_prompt. Leer configuración de proveedores activos desde config/providers.yaml. Generar versión primaria + versiones alternates si se configuran (ej: scene_001_video.md con Veo 3.1 Quality, scene_001_video_fast.md con Veo 3.1 Fast). Crear manifest.yaml con metadata completa del proyecto.
- **Output:** Escenas y prompts listos para usar en plataformas de IA

## SKILL: media-pipeline
- **Descripción:** Ejecuta todo el flujo inicial de forma automática
- **Cuando usar:** Quieres ejecutar script → storyboard → render de una sola vez
- **Acciones:** Verificar contexto activo, ejecutar media-script con los parámetros dados, esperar aprobación del usuario, ejecutar media-storyboard, esperar aprobación, ejecutar media-render. Sugerir al usuario que ejecute `/media-commit` al final.
- **Output:** Proyecto completo desde guion hasta prompts en un solo comando

## SKILL: media-commit
- **Descripción:** Hace commit git incremental con mensaje descriptivo
- **Cuando usar:** Después de cada etapa importante (nuevo proyecto, guion v1, guion final, storyboard, render)
- **Acciones:** SOLO SE EJECUTA A PETICIÓN DEL USUARIO. Detectar cambios, generar mensaje descriptivo del commit (ej: "feat: actualización de guion para proyecto X"), ejecutar git add + commit, mostrar hash del commit
- **Output:** Commit git con mensaje profesional

## SKILL: media-archive
- **Descripción:** Archiva o desarchiva un proyecto modificando su bandera en el README
- **Cuando usar:** Cuando un proyecto finaliza o se cancela para limpiar los menús interactivos
- **Acciones:** Recibe el workspace y proyecto. Edita el README.md del workspace buscando la fila del proyecto y cambia la columna "Archivado" a "Sí" o "No". No mueve carpetas para no romper repositorios Git.
- **Output:** Tabla README actualizada y proyecto oculto de /media-in

## SKILL: media-assets
- **Descripción:** Registra y gestiona assets locales y URLs
- **Cuando usar:** Importar imágenes, videos, referencias, o guardar resultados generados externamente
- **Acciones:** Copiar archivo local a assets/ apropiado (images/audio/video/references), registrar metadata en manifest.yaml con path + descripción + origen. Para URLs: guardar referencia en assets/references/ con metadata completa (URL, descripción, fecha captura, uso en escena). Soporta registro de resultados generados externamente (imágenes de Google Imagen, videos de Google Flow, audios de ElevenLabs). Cuando se registra un asset generado externamente, incluir en la metadata: provider, model, prompt_file_reference (path al archivo de prompt usado), generation_time, cost_estimate.
- **Output:** Asset registrado en el proyecto con metadata completa

## SKILL: media-status
- **Descripción:** Genera un reporte completo del estado del proyecto activo con estadísticas, métricas y progreso
- **Cuando usar:** Quieres ver el estado actual del proyecto, revisar progreso antes de tomar decisiones, o presentar avances a stakeholders
- **Acciones:**
  1. VERIFICAR CONTEXTO: Si no hay proyecto activo (no se ejecutó /media-in), mostrar mensaje claro: "⚠️ No hay proyecto activo. Por favor ejecuta primero /media-in para seleccionar un proyecto de video."
  2. Si hay proyecto activo, analizar y mostrar reporte con las siguientes secciones:
     - 📊 PROGRESO GENERAL: % completado de cada etapa (script/storyboard/render)
     - 📝 GUIÓN: versiones existentes (v1, v2... final), engagement score, viral potential score, recomendaciones de mejora
     - 🎬 ESCENAS: total de escenas generadas, duración total del video, escenas pendientes de renderizar
     - 🤖 PROMPTS: cantidad por tipo de medio (video/image/audio), cantidad por proveedor/modelo (Google Flow Veo 3.1 Quality, Fast, Omni Flash, etc.), prompts listos vs pendientes
     - 🖼️ ASSETS: cantidad de imágenes/audio/video locales registrados, URLs de referencia, assets generados externamente
     - 📈 MÉTRICAS: engagement score actual, viral potential, duración estimada vs objetivo
     - 🕒 HISTORIAL: últimos 5 commits con mensaje, fecha y hash
     - ⚠️ PENDIENTES: lista de acciones recomendadas (ej: "Falta storyboard final", "3 escenas sin prompts generados")
     - 💡 RECOMENDACIONES: próximos pasos sugeridos basados en el estado actual
- **Output:** Tabla resumen visual + detalles de cada sección + recomendaciones priorizadas
- **Formato:** Reporte en español con emojis para mejor legibilidad, estados con símbolos (✅ completado, 🔄 en progreso, ⏳ pendiente)

# FORMATO DE PROMPTS ESTRUCTURADOS (AGNÓSTICO DE PROVEEDOR)

Cada archivo de prompt debe incluir YAML frontmatter con metadata del modelo:

```yaml
---
# Metadata del proveedor y modelo
platform: Google AI Studio
model: Veo 3.1 Quality
model_alternates: 
  - Veo 3.1 Fast
  - Omni Flash
aspect_ratio: 16:9
duration: 8s
resolution: 1080p
fps: 24
seed: 12345
negative_prompt: "blurry, low quality, distorted faces"
created: 2026-07-25
version: 1.0
---
```

Luego el contenido del prompt:

```
[SCENE CONTEXT]
Scene X of Y - [brief narrative context]

[VISUAL DESCRIPTION]
Detailed description of what happens visually, action, composition.

[CINEMATOGRAPHY]
- Shot type: [wide/medium/close-up/extreme close-up]
- Camera movement: [static/pan/tilt/tracking/dolly/crane/handheld]
- Lens: [24mm/35mm/50mm/85mm/telephoto]
- Lighting: [natural/golden hour/neon/dramatic/soft]

[STYLE]
- Visual style: [cinematic/documentary/anime/realistic/etc]
- Color palette: [specific colors or mood]

[CHARACTERS]
Description of characters, their appearance, clothing, expressions.

[ATMOSPHERE]
Mood, weather, time of day, ambient elements.

[TECHNICAL NOTES]
Any specific technical requirements or platform-specific optimizations.
```

# ESTÁNDARES DE STORYBOARD

Cada escena en el storyboard debe incluir:
- Número de escena y toma
- Thumbnail descriptivo (texto detallado que podría ser generado como imagen)
- Descripción narrativa
- Tipo de plano (WS, MS, CU, ECU, POV, Overhead)
- Óptica / Lente (ej. 35mm para entorno, 85mm para detalle)
- Movimiento de cámara
- Iluminación (ej. High key, Moody, Golden Hour) y Colorimetría
- Duración exacta
- Audio/música/narración
- Transición a siguiente escena
- Notas de producción

# MÉTRICAS DE CALIDAD (resources/metrics/)

## engagement-rubric.md
- Hook inicial (0-10)
- Ritmo narrativo (0-10)
- Claridad del mensaje (0-10)
- Elementos visuales memorables (0-10)
- Call-to-action o resolución (0-10)
- **SCORE TOTAL /50**

## viral-potential-rubric.md
- Elementos emocionales (0-10)
- Originalidad del concepto (0-10)
- Shareability (0-10)
- Relevancia cultural (0-10)
- Factor sorpresa (0-10)
- **SCORE TOTAL /50**

# CONTENIDO DE README.md PRINCIPAL

Debe incluir:
1. Descripción del proyecto
2. Requisitos (Antigravity CLI instalado)
3. Guía de inicio rápido:
   - `/media-init` → `/media-new-workspace` → `/media-in` → `/media-new` → `/media-pipeline`
4. Descripción detallada de cada skill
5. Convenciones de archivos
6. Estructura de proyecto
7. Ejemplos de uso con proyecto de ejemplo
8. Sistema de proveedores (cómo funciona config/providers.yaml)
9. Roadmap (Fase 1: framework base / Fase 2: integración Python/APIs vía MCP)

# INSTRUCCIONES FINALES DE GENERACIÓN

1. Genera TODA la estructura de archivos y carpetas listada
2. Crea el contenido COMPLETO de AGENTS.md raíz con todos los roles
3. Crea cada SKILL.md siguiendo el formato YAML frontmatter de Antigravity (name, description) + secciones: When to use, How to use, Examples, Expected output
4. Crea todos los templates profesionales (scripts por tipo de video, prompts, storyboard)
5. Crea README.md principal completo, enlazando a la guía de instalación y listando todos los comandos (incluyendo `/media-archive`)
6. Crea `docs/INSTALLATION.md` explicando cómo configurar el entorno virtual `venv` y ejecutar el backend de Python.
7. Crea `templates/workspace/README.md` asegurándote de incluir una tabla Markdown de "Proyectos de Video" con las siguientes columnas obligatorias: `Proyecto | Formato | Estado | Archivado | Fecha Creación | Descripción / Notas`. (La columna "Archivado" es crítica para `/media-in`).
8. Crea .gitignore apropiado (ignorar assets grandes, venv, .DS_Store, etc.)
9. Crea manifest.yaml template con schema definido
8. Crea config/providers.yaml template con la estructura de proveedores
9. Crea rúbricas de engagement y viral potential
10. Documenta especificaciones de Google Flow VEO en docs/google-flow-guide.md
11. Usa ESPAÑOL para toda la documentación, INGLÉS solo dentro de los templates de prompts
12. Los skills deben seguir el patrón "progressive disclosure" de Antigravity
13. Incluye ejemplos concretos en cada template y skill
14. Al terminar, ejecuta `/media-init` para dejar el proyecto listo para usar
15. Haz el primer commit con `/media-commit` con mensaje "feat: inicialización de media-architect"

# INICIO DE EJECUCIÓN

Comienza generando la estructura completa del proyecto y luego el contenido de cada archivo, uno por uno, verificando que todo sea coherente entre sí. Prioriza:
1. Estructura de carpetas
2. AGENTS.md raíz
3. Skills en orden lógico de flujo (init → new-workspace → in → new → script → storyboard → render → pipeline → commit → assets → status)
4. Templates profesionales
5. Sistema de proveedores (config/providers.yaml)
6. Recursos y documentación
7. README.md final