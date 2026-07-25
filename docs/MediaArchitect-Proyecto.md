# PROPUESTA EJECUTIVA: MEDIA-ARCHITECT
## Framework de Producción Audiovisual con IA para Agencias y Productoras

**Proyecto:** media-architect  
**Repositorio:** https://github.com/LizAndrea/media-architect  
**Versión del documento:** 1.0  
**Fecha:** 25 de julio de 2026  
**Autores:** Liz Andrea & Equipo  
**Estado:** En fase de diseño (pre-implementación)

---

## 📋 ÍNDICE EJECUTIVO

1. Resumen Ejecutivo
2. Problema que Resuelve
3. Solución Propuesta
4. Visión y Misión
5. Arquitectura del Sistema
6. Flujo de Trabajo
7. Casos de Uso
8. Roadmap y Fases
9. Beneficios Esperados
10. Inversión y Recursos
11. Análisis de Riesgos
12. Decisiones Estratégicas a Tomar
13. Próximos Pasos

---

## 1. 🎯 RESUMEN EJECUTIVO

**media-architect** es un framework CLI (Command Line Interface) basado en agentes de Inteligencia Artificial que automatiza y profesionaliza el proceso de producción audiovisual. Permite a agencias, productoras y creadores de contenido transformar una idea textual en un video completo producido mediante IA, generando de forma estructurada todos los artefactos necesarios: guiones profesionales, storyboards cinematográficos, prompts optimizados para plataformas de generación de video (Google Flow VEO, Runway, Sora), assets organizados y metadata profesional.

**Propuesta de valor única:** Es el primer sistema que combina el rigor de la producción cinematográfica tradicional con la velocidad de la IA generativa, mediante un flujo de trabajo guiado por comandos (`/media-new`, `/media-script`, `/media-render`) que un agente de IA ejecuta de forma autónoma siguiendo estándares de la industria.

---

## 2. ⚠️ PROBLEMA QUE RESUELVE

### 2.1 El problema actual en la producción de videos con IA

Los creadores de contenido enfrentan **tres grandes desafíos** al producir videos con herramientas de IA generativa:

**A) Fragmentación del flujo de trabajo**
- Uso de 4-6 herramientas diferentes (ChatGPT para guiones, Midjourney para imágenes, Google Flow/Runway para video, ElevenLabs para audio, editores para compilar)
- Pérdida de contexto entre herramientas
- Copiar/pegar información manualmente en cada paso

**B) Falta de estándares profesionales**
- Los guiones generados carecen de estructura cinematográfica (planos, movimientos de cámara, iluminación)
- Los prompts son inconsistentes y producen resultados variables
- No hay un sistema de versionado ni archivo del proceso creativo

**C) Escalabilidad limitada**
- Imposible gestionar múltiples proyectos simultáneos
- No se capitaliza el conocimiento adquirido en proyectos anteriores
- Dificultad para escalar a nivel de agencia/productora con múltiples clientes

### 2.2 Métricas del problema

| Indicador | Valor actual | Con media-architect |
|-----------|-------------|---------------------|
| Tiempo producción video 10 min | 8-12 horas | 2-4 horas |
| Herramientas utilizadas | 4-6 | 1 (CLI + IA) |
| Pérdida de contexto | Alta | Nula (jerárquica) |
| Reproducibilidad de resultados | Baja | Alta (prompts versionados) |
| Proyectos simultáneos gestionables | 1-2 | 10+ |

---

## 3. 💡 SOLUCIÓN PROPUESTA

### 3.1 ¿Qué es media-architect?

Un **framework CLI asistido por IA** que proporciona:

1. **Estructura jerárquica profesional**
   - Agencias → Clientes → Proyectos de Video → Escenas
   - Cada nivel con su propio contexto y metadata

2. **Biblioteca de skills especializados**
   - 11 comandos (`/media-init`, `/media-new`, `/media-script`, etc.)
   - Cada skill ejecuta una etapa del proceso de producción

3. **Agente de IA con múltiples roles expertos**
   - Ingeniero de prompts, guionista, director de fotografía, diseñador gráfico
   - Actúa según el contexto del proyecto activo

4. **Sistema de versionado y archivo automático**
   - Git commits incrementales en cada etapa
   - Registro completo de assets (locales + URLs)

5. **Métricas de calidad integradas**
   - Engagement score (0-50)
   - Potencial viral (0-50)
   - Análisis automático de guiones

### 3.2 Diferenciadores clave

✅ **Estándares cinematográficos aplicados a IA**  
✅ **Prompts estructurados en inglés (mejor rendimiento)** + contenido en español  
✅ **Escenas optimizadas para Google Flow VEO (8-10 segundos)**  
✅ **Motor Backend en Python** (Ejecución ultrarrápida de comandos sin consumo excesivo de tokens IA)  
✅ **Soporte multiplataforma** (VEO, Runway, Sora, Midjourney, ElevenLabs)  
✅ **Jerarquía de contexto** para agencias con múltiples clientes  
✅ **Métricas de engagement** integradas en el análisis  
✅ **Pipeline automatizado** con `/media-pipeline`  

---

## 4. 🔭 VISIÓN Y MISIÓN

### Visión
"Democratizar la producción audiovisual profesional mediante IA, permitiendo que cualquier creador o agencia produzca contenido de calidad cinematográfica a escala."

### Misión
"Proporcionar un framework estructurado que combine el arte del storytelling con la potencia de la IA generativa, manteniendo los estándares profesionales de la industria cinematográfica."

### Valores fundamentales

| Valor | Descripción |
|-------|-------------|
| **Profesionalismo** | Estándares cinematográficos aplicados a cada producción |
| **Reproducibilidad** | Todo proceso y prompt queda registrado y versionado |
| **Escalabilidad** | Arquitectura preparada para múltiples clientes y proyectos |
| **Transparencia** | Historia completa del proceso creativo disponible |
| **Calidad** | Métricas objetivas de engagement y potencial viral |

---

## 5. 🏗️ ARQUITECTURA DEL SISTEMA

### 5.1 Estructura jerárquica

```
media-architect/
|
|-- clients/
|   |-- agencia-xyz/                    (Nivel 1: Cliente)
|   |   |-- AGENTS.md                   (Contexto del cliente)
|   |   |-- README.md
|   |   |
|   |   |-- como-llegar-a-tarata-bici/  (Nivel 2: Proyecto)
|   |   |   |-- AGENTS.md               (Contexto del proyecto)
|   |   |   |-- script/                 (Guiones y versiones)
|   |   |   |-- storyboard/             (Storyboards)
|   |   |   |-- scenes/                 (Micro-guiones)
|   |   |   |-- prompts/                (Prompts por plataforma)
|   |   |   |-- assets/                 (Imágenes, audio, video)
|   |   |   +-- render/                 (Salida final)
|   |   |
|   |   +-- otro-proyecto/
|   |
|   +-- cliente-2/
|
|-- resources/                          (Bibliotecas de conocimiento)
|-- templates/                          (Plantillas profesionales)
|-- scripts/                            (Backend Python para ejecución rápida)
|-- venv/                               (Entorno virtual aislado)
+-- .agents/skills/                     (Comandos ejecutables)
```

### 5.2 Biblioteca de Skills (Comandos)

| Comando | Función | Duración estimada |
|---------|---------|-------------------|
| `/media-init` | Inicializa el framework | 1 min |
| `/media-new-client` | Crea un cliente/empresa | 2 min |
| `/media-in` | Selecciona proyecto activo | 1 min |
| `/media-new` | Crea proyecto de video | 3 min |
| `/media-script` | Genera guion profesional | 15-30 min |
| `/media-storyboard` | Crea storyboard cinematográfico | 10-20 min |
| `/media-render` | Divide en escenas + genera prompts | 10-15 min |
| `/media-pipeline` | Ejecuta todo el flujo de una vez | 30-60 min |
| `/media-commit` | Commit git incremental | 1 min |
| `/media-archive` | Archiva proyectos sin mover carpetas | < 1 min |
| `/media-assets` | Gestiona assets locales/URLs | Variable |
| `/media-status` | Reporte del estado del proyecto | 1 min |

### 5.3 Roles del Agente de IA

El agente actúa como **equipo creativo completo** con 12 especialidades:

1. 🎬 **Director Creativo** – Visión general y storytelling
2. ✍️ **Guionista Profesional** – Cine, publicidad, documentales
3. 🎥 **Director de Fotografía** – Composición, lentes, iluminación
4. 🎨 **Diseñador Gráfico** – Artes digitales y fotografía
5. 👤 **Diseñador de Personajes** – Psicología y arcos de personaje
6. 🔧 **Ingeniero de Prompts** – Prompts optimizados en inglés
7. 📊 **Productor Multiplataforma** – YouTube, TikTok, Reels, Podcast
8. 🎭 **Especialista en Lenguaje Cinematográfico** – Planos y transiciones
9. 🎞️ **Editor y Post-productor** – Montaje y ritmo
10. 📈 **Estratega de Contenido Viral** – Engagement y viralidad
11. 📚 **Archivista Digital** – Gestión de assets y versionado
12. 🎯 **Analista de Métricas** – Engagement y viral potential scores

---

## 6. 🔄 FLUJO DE TRABAJO

### 6.1 Diagrama del proceso

```
IDEA TEXTUAL
     |
     v
/media-new-client -----------> Creación de Cliente
     |
     v
/media-in ------------------> Selección de contexto
     |
     v
/media-new -----------------> Creación de Proyecto de Video
     |
     v
/media-script --------------> Generación de Guion
     |                         |- Iteraciones (v1, v2, v3...)
     |                         |- Análisis de Engagement
     |                         +-- Análisis Viral Potential
     v
/media-storyboard -----------> Storyboard Cinematográfico
     |
     v
/media-render --------------> División en Escenas (8-10s)
     |                         |- Prompts Google Flow VEO
     |                         |- Prompts Midjourney (imágenes)
     |                         +-- Prompts ElevenLabs (audio)
     v
/media-assets --------------> Registro de Assets Generados
     |
     v
/media-status --------------> Reporte de Estado
     |
     v
PRODUCCIÓN FINAL EN PLATAFORMAS DE IA
```

### 6.2 Flujo rápido (recomendado)

```bash
/media-new-client          # 1. Crear cliente
/media-in                  # 2. Seleccionar cliente
/media-new                 # 3. Crear proyecto
/media-pipeline            # 4. TODO EN UN SOLO COMANDO
                           #    Script → Storyboard → Render
/media-status              # 5. Ver estado
/media-commit              # 6. Guardar progreso
```

---

## 7. 🎯 CASOS DE USO

### Caso 1: Short de TikTok (60s)
- **Input:** "Cómo llegar a Tarata en bici"
- **Output:**
  - Guion de 60 segundos con 6-7 escenas
  - 6-7 prompts para Google Flow VEO (8-10s c/u)
  - Storyboard vertical (9:16)
  - Prompts de música trending
  - Engagement score: 42/50

### Caso 2: Video de YouTube (10 min)
- **Input:** "Documental sobre la ruta del Che"
- **Output:**
  - Guion completo con personajes y arcos
  - 60-70 escenas de 8-10s
  - 60-70 prompts VEO
  - Prompts de voz en off (ElevenLabs)
  - Storyboard horizontal (16:9)

### Caso 3: Reel comercial (45s)
- **Input:** "Anuncio de restaurante"
- **Output:**
  - Guion publicitario con call-to-action
  - 5 escenas optimizadas para conversión
  - Prompts de video + imágenes (Midjourney)
  - Análisis de viral potential

### Caso 4: Mini documental (15 min)
- **Input:** "Historia de los textiles andinos"
- **Output:**
  - Guion con entrevistas y B-roll
  - 90+ escenas + transiciones
  - Prompts para VEO, Midjourney y ElevenLabs
  - Assets de referencia (URLs) organizados

---

## 8. 🗺️ ROADMAP Y FASES

### FASE 1: Framework Base (Actual) – 4-6 semanas
- [x] Diseño conceptual
- [ ] Implementación de skills base (v1.0)
- [ ] Documentación completa
- [ ] Templates profesionales
- [ ] Testing con 3 proyectos piloto

### FASE 2: Integración API – 6-8 semanas
- [ ] Scripts Python para Google Flow VEO API
- [ ] Integración MCP (Model Context Protocol)
- [ ] Automatización completa del renderizado
- [ ] Dashboard de métricas en tiempo real
- [ ] Sistema de cache de prompts

### FASE 3: Colaboración y Escala – 8-10 semanas
- [ ] Multi-usuario (equipos de trabajo)
- [ ] Biblioteca compartida de assets
- [ ] Marketplace de templates
- [ ] Analytics avanzados (A/B testing de prompts)
- [ ] Plugin para After Effects / Premiere

### FASE 4: Producto Comercial – 12 semanas
- [ ] SaaS con interfaz web
- [ ] Marketplace de proyectos
- [ ] Monetización de templates
- [ ] Certificación de creadores

### Hitos clave

| Hito | Fecha objetivo | Métrica de éxito |
|------|----------------|------------------|
| MVP funcional | Q3 2026 | 3 proyectos completos |
| Integración API | Q4 2026 | 80% de automatización |
| Primer cliente pagado | Q1 2027 | Ingresos recurrentes |
| 100 usuarios activos | Q2 2027 | Crecimiento mensual 20% |

---

## 9. 💎 BENEFICIOS ESPERADOS

### 9.1 Beneficios operativos

| Métrica | Antes | Después | Mejora |
|---------|-------|---------|--------|
| Tiempo de producción | 8-12 horas | 2-4 horas | **70% reducción** |
| Consistencia de resultados | Variable | Alta | **+40%** |
| Proyectos gestionables/mes | 2-4 | 15-20 | **5x más** |
| Pérdida de conocimiento | Alta | Nula | **100% preservado** |

### 9.2 Beneficios estratégicos

✅ **Ventaja competitiva:** Primero en ofrecer framework profesional de video con IA  
✅ **Propiedad intelectual:** Sistema de templates y prompts patentable  
✅ **Escalabilidad:** Base para SaaS futuro  
✅ **Capitalización del conocimiento:** Cada proyecto mejora los siguientes  
✅ **Monetización múltiple:** Framework + templates + SaaS + consultoría  

### 9.3 Beneficios creativos

✅ **Calidad cinematográfica:** Estándares profesionales garantizados  
✅ **Iteración acelerada:** Múltiples versiones en minutos  
✅ **Reproducibilidad:** Mismos resultados con mismas condiciones  
✅ **Historial completo:** Aprendizaje continuo del equipo  

---

## 10. 💰 INVERSIÓN Y RECURSOS

### 10.1 Recursos necesarios (Fase 1)

| Recurso | Cantidad | Costo estimado |
|---------|----------|----------------|
| Desarrollo (tiempo) | 4-6 semanas | Tiempo de equipo |
| Herramientas IA (créditos) | Google Flow, ChatGPT Pro | ~$50-100/mes |
| Infraestructura | GitHub (gratuito) | $0 |
| Testing | 3 proyectos piloto | Tiempo de equipo |

### 10.2 ROI estimado (Fase 2-3)

**Escenario conservador:**
- 10 clientes pagando $200/mes = $2,000/mes
- 50 templates vendidos a $29 = $1,450 ingreso único
- **ROI: 300% en 6 meses**

**Escenario optimista:**
- 50 clientes SaaS a $99/mes = $4,950/mes
- 200 templates vendidos = $5,800 ingreso único
- Consultoría especializada = $2,000/mes
- **ROI: 800% en 12 meses**

---

## 11. ⚠️ ANÁLISIS DE RIESGOS

### 11.1 Riesgos técnicos

| Riesgo | Probabilidad | Impacto | Mitigación |
|--------|--------------|---------|------------|
| Cambios en APIs de IA | Media | Alto | Abstracción modular de integraciones |
| Calidad inconsistente de IA | Alta | Media | Rúbricas de calidad + iteraciones |
| Dependencia de Antigravity CLI | Media | Alta | Plan B: wrapper propio |

### 11.2 Riesgos de mercado

| Riesgo | Probabilidad | Impacto | Mitigación |
|--------|--------------|---------|------------|
| Competencia rápida | Alta | Media | Primer mover advantage + comunidad |
| Saturación de herramientas IA | Media | Media | Nicho especializado (agencias) |
| Cambios en plataformas IA | Alta | Media | Multi-plataforma desde el inicio |

### 11.3 Riesgos operativos

| Riesgo | Probabilidad | Impacto | Mitigación |
|--------|--------------|---------|------------|
| Curva de aprendizaje CLI | Media | Media | Documentación + video tutoriales |
| Adopción lenta | Media | Alta | Casos de uso demostrativos |

---

## 12. 🎯 DECISIONES ESTRATÉGICAS A TOMAR

### Decisión 1: Enfoque inicial de mercado
- **Opción A:** Agencias/productoras pequeñas (B2B) – Mayor ticket, menos volumen
- **Opción B:** Creadores independientes (B2C) – Menor ticket, más volumen
- **Opción C:** Hybrid – Agencias como ancla, creadores como escala
- **Recomendación:** Opción C (B2B2C)

### Decisión 2: Modelo de negocio futuro
- **Opción A:** SaaS por suscripción
- **Opción B:** Marketplace de templates
- **Opción C:** Framework open-source + servicios premium
- **Recomendación:** Opción C (Open core + SaaS)

### Decisión 3: Plataformas prioritarias (Fase 2)
- **Opción A:** Solo Google Flow VEO (enfoque profundo)
- **Opción B:** Multi-plataforma (VEO + Runway + Sora)
- **Opción C:** Modular según cliente
- **Recomendación:** Opción A inicial → Opción B en Fase 2

### Decisión 4: Velocidad de lanzamiento
- **Opción A:** MVP en 4 semanas (features mínimas)
- **Opción B:** Beta en 8 semanas (más pulido)
- **Opción C:** V1.0 en 12 semanas (completo)
- **Recomendación:** Opción A (iteración rápida con feedback real)

### Decisión 5: Equipo de desarrollo
- **Opción A:** Desarrollo interno (Liz Andrea + socia)
- **Opción B:** Contratar dev especializado en IA
- **Opción C:** Outsourcing parcial
- **Recomendación:** Opción A + freelancers específicos

### Decisión 6: Estrategia de contenido
- **Opción A:** Proyectos propios como showcase
- **Opción B:** Documentar el proceso (meta-content)
- **Opción C:** Casos de estudio con clientes reales
- **Recomendación:** Las tres (pirámide de contenido)

---

## 13. 🚀 PRÓXIMOS PASOS INMEDIATOS

### Semana 1-2: Validación
- [ ] Aprobación de propuesta por parte de socias
- [ ] Definición de 3 proyectos piloto concretos
- [ ] Setup del repositorio GitHub
- [ ] Ejecución de Fase 1 del prompt (generación de estructura)

### Semana 3-4: Implementación
- [ ] Testing de skills base con proyecto piloto #1
- [ ] Refinamiento de templates según feedback
- [ ] Documentación de uso para equipo

### Semana 5-6: Validación comercial
- [ ] Proyecto piloto #2 (cliente externo si es posible)
- [ ] Recolección de feedback estructurado
- [ ] Planificación de Fase 2 (integración API)

### Mes 2: Lanzamiento beta
- [ ] 3-5 proyectos completos documentados
- [ ] Publicación de blog post / video explicativo
- [ ] Búsqueda de primeros usuarios beta

---

## 📞 CONTACTO Y SEGUIMIENTO

**Contacto del proyecto:** Liz Andrea  
**Repositorio:** https://github.com/LizAndrea/media-architect  
**Próxima revisión:** [Fecha a definir]

---

## 📝 RESUMEN PARA TOMA DE DECISIONES

### ✅ Razones para APROBAR el proyecto

1. **Mercado en crecimiento:** La producción de video con IA crecerá 300% en los próximos 3 años
2. **Diferenciador claro:** No existe un framework profesional similar en el mercado
3. **Bajo costo de entrada:** Se puede construir con herramientas existentes
4. **Múltiples vías de monetización:** Framework, SaaS, templates, consultoría
5. **Alineación con tendencias:** IA generativa + contenido vertical + agilidad

### ⚠️ Consideraciones importantes

1. **Riesgo tecnológico:** Dependencia de herramientas de IA que evolucionan rápidamente
2. **Inversión de tiempo:** Requiere dedicación sostenida de 4-6 semanas iniciales
3. **Competencia emergente:** Otros equipos pueden desarrollar soluciones similares
4. **Necesidad de marketing:** Sin estrategia de distribución, el producto no despega

### 🎯 Recomendación final

**APROBAR el proyecto media-architect con las siguientes condiciones:**

1. ✅ Iniciar con Fase 1 (4-6 semanas) y evaluar antes de Fase 2
2. ✅ Definir 3 proyectos piloto concretos antes de implementar
3. ✅ Establecer métricas de éxito claras (tiempos, calidad, usuarios)
4. ✅ Reservar presupuesto mínimo para créditos de IA ($50-100/mes)
5. ✅ Planificar estrategia de contenido desde el inicio

---

## 📌 PREGUNTAS CLAVE PARA LA REUNIÓN

1. **¿En qué fase quieren enfocarse primero?** (¿Agencias B2B o creadores B2C?)
2. **¿Tienen 4-6 semanas dedicadas para el MVP?**
3. **¿Cuáles son los 3 proyectos piloto ideales?** (ej: 1 short, 1 youtube, 1 comercial)
4. **¿Cuál es el presupuesto inicial para créditos de IA?**
5. **¿Quién manejará la estrategia de marketing/contenido?**

---

*"La mejor manera de predecir el futuro de la producción audiovisual es construirlo."*

**media-architect – Framework de Producción Audiovisual con IA**

---

*Documento generado el 25 de julio de 2026*

---

## 📥 Cómo guardar este documento

**Opción 1: Guardar como Markdown (recomendado)**
1. Copia todo el contenido de arriba
2. Pégalo en un archivo llamado `PROPUESTA-MEDIA-ARCHITECT.md`
3. Ábrelo en VS Code, GitHub, o cualquier editor de markdown

**Opción 2: Convertir a PDF profesional**
1. Pega el contenido en: https://dillinger.io/ (editor online de markdown)
2. Haz clic en "Export" → "PDF"
3. Obtendrás un PDF profesional listo para presentar

**Opción 3: Subir a GitHub directamente**
1. Crea un archivo `PROPUESTA.md` en tu repo media-architect
2. Pega el contenido
3. GitHub lo renderizará automáticamente con formato profesional

## 🎯 Puntos clave para la reunión

1. **Enfoque de mercado:** ¿Agencias (B2B) o creadores (B2C)? Recomiendo híbrido
2. **Velocidad:** MVP en 4-6 semanas para validar rápido
3. **Proyectos piloto:** Definir 3 tipos de videos concretos para probar
4. **Presupuesto:** $50-100/mes en créditos de IA durante Fase 1
5. **Roles:** Tú como productor creativo, tu socia como estratega comercial
