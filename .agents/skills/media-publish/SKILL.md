---
name: "media-publish"
description: "Genera descripciones, títulos SEO y hashtags optimizados para múltiples redes sociales basados en el guion del proyecto activo."
version: "1.0.0"
author: "media-architect"
---

# INSTRUCCIONES PARA EL AGENTE: `media-publish`

## 1. PROPÓSITO
Esta habilidad se encarga de la etapa final del embudo de distribución: El Copywriting para Redes Sociales. El agente debe analizar el proyecto finalizado y generar un kit de publicación adaptado a los algoritmos y restricciones de cada plataforma importante.

## 2. REQUISITOS PREVIOS
Antes de ejecutar la habilidad, debes asegurarte de que:
- Existe un Workspace activo y un Proyecto seleccionado (ver `.agents/active_context`).
- Existe el archivo `script/script.md` o `manifest.yaml` para entender el tono y el Call to Action (Llamado a la acción) del video.

## 3. FLUJO DE TRABAJO DE PUBLICACIÓN
Genera un archivo llamado `publish/publish.md` dentro de la carpeta del proyecto. Este archivo debe contener 4 secciones principales, respetando las siguientes reglas algorítmicas:

### A. TikTok
- **Regla:** Tono súper casual, directo, como si le hablaras a un amigo.
- **Estructura:** Gancho inicial en forma de pregunta + Desarrollo corto + Call to Action claro ("Comenta X").
- **Hashtags:** Máximo 6-8 hashtags. Mezcla de hashtags muy amplios (Ej: #InteligenciaArtificial) y muy de nicho (Ej: #MTBBolivia).

### B. YouTube Shorts
- **Regla:** Enfoque fuerte en SEO (Search Engine Optimization).
- **Título:** Máximo 60 caracteres. Debe incluir las palabras clave principales por las que la gente buscaría este contenido.
- **Descripción:** Puede ser más larga. Debe incluir contexto, locación y el Call to Action.
- **Etiquetas (Tags):** Lista de 10-15 palabras clave separadas por comas.

### C. Instagram Reels
- **Regla:** Estética visual y alto engagement para el algoritmo de Instagram.
- **Estructura:** Uso estratégico de emojis. Espaciado limpio. Formato de historia corta. Call to Action enfocado en la interacción por Mensaje Directo (Ej: "Comenta X y te envío por DM").
- **Hashtags:** 10-12 hashtags altamente relevantes al nicho.

### D. Facebook Reels
- **Regla:** Audiencia ligeramente mayor, buscar la identificación personal ("¿A quién más le pasa?").
- **Estructura:** Tono empático, directo, menos "techy" y más enfocado en resolver el problema del usuario común.

## 4. CREACIÓN DEL ARCHIVO
Usa la herramienta de escritura de archivos para crear `publish/publish.md` con el formato Markdown estructurado (`## TikTok`, `## YouTube Shorts`, etc.). Presenta un resumen al usuario tras la creación.
