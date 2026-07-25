# media-architect

> **Descripción Corta (GitHub About):**
> *Framework de automatización end-to-end diseñado por un Arquitecto de Software y un Product Owner para digitalizar, estructurar y orquestar todo el flujo de producción de video con IA (del guion al render final).*

---

## 📄 Acerca del Proyecto

Este repositorio implementa un **motor de automatización y orquestación de contenido audiovisual de punta a punta**. Abordado desde una perspectiva de ingeniería de software y gestión de producto, el sistema centraliza, digitaliza y estandariza toda la información y los metadatos necesarios para transformar una idea en un video automatizado utilizando múltiples herramientas de Inteligencia Artificial.

El proyecto está diseñado bajo la dualidad de dos roles clave:
*   **Product Owner:** Define la visión estratégica, el valor del contenido, la estructura de los guiones, el storytelling y los requerimientos funcionales del producto multimedia.
*   **Arquitecto de Software:** Diseña la estructura técnica, la modularidad de los datos, la consistencia de personajes (avatares) y los flujos de integración (*pipelines*) entre diversas plataformas de IA (como generadores de texto, storyboards, avatares, música y video).

---

## ⚙️ Pipeline de Producción Digitalizado

El sistema gestiona y automatiza de forma modular cada una de las fases del ciclo de vida del video:

1. **Ideación y Guionización (`Scripting & Backlog`):** 
   * Estructuración del contenido narrativo por bloques temporales (ej. fragmentación en clips de corta duración).
   * Gestión de textos en pantalla, ganchos (*hooks*) y llamadas a la acción (*CTA*).
2. **Diseño de Personajes y Coherencia Visual (`Character Consistency`):** 
   * Definición estricta de metadatos y atributos fijos de avatares para evitar alucinaciones visuales y asegurar continuidad en múltiples escenas.
3. **Generación de Storyboards (`Grid & Layout Processing`):** 
   * Orquestación de prompts en inglés optimizados para grillas visuales con especificaciones de cinematografía técnica (*close-ups*, iluminación, planos).
4. **Producción y Corrección de Video (`AI Video Generation & Fixes`):** 
   * Integración de comandos maestros para plataformas de generación de video con control de continuidad.
5. **Sincronización de Audio y Postproducción (`Voice & Transition Flow`):** 
   * Automatización de la sincronización de voz en off, transiciones dinámicas y gestión de la música de fondo.

---

## 🚀 Framework CLI Asistido por IA

Proporciona una estructura jerárquica profesional y automatiza el proceso de producción audiovisual para agencias y productoras.

### Requisitos
- Antigravity CLI instalado.
- Entorno de Python configurado (ver [Guía de Instalación](docs/INSTALLATION.md)).

### Guía de Inicio Rápido
Sigue estos pasos para comenzar:
1. `/media-init`: Inicializa el repositorio con la estructura base.
2. `/media-new-client`: Crea un cliente/empresa.
3. `/media-in`: Selecciona el cliente y proyecto activo.
4. `/media-new`: Crea un nuevo proyecto de video.
5. `/media-pipeline`: Ejecuta todo el flujo (script → storyboard → render) automáticamente.

### Comandos (Skills)
- `/media-init`: Inicializa media-architect.
- `/media-new-client`: Crea un nuevo cliente.
- `/media-in`: Selecciona cliente y proyecto activo.
- `/media-new`: Crea nuevo proyecto de video.
- `/media-script`: Genera y permite iterar guion profesional.
- `/media-storyboard`: Crea storyboard visual con anotaciones cinematográficas.
- `/media-review`: Análisis experto y crítica para mejorar guiones y storyboards.
- `/media-render`: Divide guion en escenas y genera prompts.
- `/media-pipeline`: Ejecuta todo el flujo inicial.
- `/media-commit`: Hace commit git incremental.
- `/media-archive`: Archiva un proyecto sin mover carpetas.
- `/media-assets`: Gestiona assets locales y URLs.
- `/media-status`: Reporte completo del estado del proyecto activo.

### Convenciones de Archivos
- Todo el contenido en ESPAÑOL, prompts de IA en INGLÉS.
- Nombres de clientes en `kebab-case`.
- Nombres de proyectos en `YYYYMMDD-kebab-case`.
- Escenas como `scene_XXX.md`.
- Iteraciones de guiones como `v1_script.md`, `v2_script.md`, `final_script.md`.

### Estructura de Proyecto
```text
media-architect/
├── .agents/skills/      (Comandos del CLI)
├── clients/             (Espacios de trabajo por cliente)
├── templates/           (Plantillas para inicialización)
├── resources/           (Bibliotecas, guías y métricas)
└── docs/                (Documentación del sistema)
```

### Sistema de Proveedores
La configuración de plataformas IA (como Google AI Studio, Runway, Midjourney, etc.) se define en `config/providers.yaml` dentro de cada proyecto de video. 

### Roadmap
- **Fase 1:** Framework base (CLI + Arquitectura jerárquica).
- **Fase 2:** Integración Python/APIs vía MCP (Model Context Protocol).
