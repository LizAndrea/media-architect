---
name: media-post
description: Genera publicaciones, infografías y piezas gráficas virales con prompts de IA y copywriting persuasivo para redes sociales
version: "1.0.0"
author: "media-architect"
---

# media-post

## 1. PROPÓSITO
Esta habilidad permite crear publicaciones estáticas, infografías tecnológicas y piezas de liderazgo de pensamiento (Thought Leadership / Direct Response) de alto impacto para redes sociales (LinkedIn, Instagram, Facebook, WhatsApp). Permite tanto el **Repropósito de Contenido** derivado de un proyecto de video existente como la creación de **Publicaciones Independientes** del workspace.

---

## 2. REQUISITOS PREVIOS Y CONTEXTO
1. Verifica el workspace activo (ej. `workspaces/[WORKSPACE_ACTIVO]/`).
2. Verifica si existe un proyecto de video activo en `.agents/active_context` o si el usuario invocó la skill dentro del contexto de un video.
   - **Si está vinculado a un video:** Lee `manifest.yaml`, `script/script.md` y `storyboard/storyboard.md`. Hereda la paleta de colores, el reparto (`[ID_Tag]`) y los sets (`sets/*.jpg`) para garantizar 100% de coherencia visual.
   - **Si es independiente:** Lee `workspace.yaml` y `assets/brand/` para mantener la identidad corporativa.

---

## 3. CONVENIO DE NOMBRADO Y ESTRUCTURA DE ARCHIVOS
Cada publicación se almacena en su propio directorio con numeración incremental dentro de `posts/`:
`workspaces/[WORKSPACE_ACTIVO]/posts/[ID_INCREMENTAL]-[slug]/`
*(Ejemplo: `workspaces/novalabs/posts/0001-mas-alla-del-prompt/`)*

Dentro de la carpeta del post, se generan obligatoriamente estos archivos:

1. **`post.yaml`**: Metadata del post.
   ```yaml
   id: "0001"
   slug: "mas-alla-del-prompt"
   title: "Más allá del prompt: Uso, Contexto y Sistemas"
   category: "b2b_thought_leadership" # Opciones: b2b_thought_leadership | tech_infographic | direct_response_flyer
   linked_project: "0001-lanzamiento-engineering-innovation" # O 'none'
   aspect_ratio: "4:5" # 4:5 (vertical feed), 1:1 (cuadrado), 16:9 (horizontal)
   created_at: "YYYY-MM-DD"
   status: "ready"
   ```

2. **`prompt_image.md`**: Prompt maestro de ingeniería visual para IA (Ideogram v2, Flux 1.1 Pro o Google Imagen 3 / Nano Banana Pro).
   - **Estructura del Prompt:**
     - **Formato y Relación de Aspecto:** 4:5 vertical o 1:1.
     - **Escena Base Fotorrealista:** Descripción cinematográfica de la oficina o set, iluminación chiaroscuro/estudio, paleta de marca (`#0A0A0A`, `#00BCD4`, `#FFFFFF`).
     - **Sujetos / Personajes:** Si está vinculado a un video, reinsertar el personaje de Lore (ej. `@lead-engineer` con su vestuario y corte de cabello).
     - **Gráficos HUD / Infografía Integrada:** Elementos de UI translúcidos, flechas de flujo, pantallas holográficas y cajas con iconos.
     - **Textos Legibles Integrados:** Titular grande (máximo 4-6 palabras en tipografía moderna limpia) y 3 etiquetas numéricas concisas (ej: `1. USO`, `2. CONTEXTO`, `3. SISTEMAS`).
     - **Negative Prompt:** Prohibición estricta de párrafos largos ilegibles, marcas de agua, texto borroso o deformaciones anatómicas.

3. **`copy.md`**: Copywriting persuasivo estructurado por plataforma:
## 4. REGLAS VISUALES Y DE COMPOSICIÓN (DISEÑO GRÁFICO CON IA)
Para evitar errores comunes de renderizado en infografías y piezas estáticas:
1. **Tipografía Unificada:** Toda la tipografía en la imagen DEBE ser de una sola familia moderna geométrica **Sans-Serif** (tipo Montserrat, Helvetica, Inter). NUNCA mezclar fuentes Serif (romanas) con Sans-Serif en la misma pieza.
2. **Ambiente Ejecutivo Luminoso (Por Defecto):** A menos que la temática sea explícitamente nocturna o cyberpunk, el escenario debe ser una **oficina corporativa diurna y luminosa** (salas de juntas con ventanales de piso a techo, luz natural, madera cálida y plantas). Evitar estéticas de "cueva o sótano de hacker" que restan credibilidad B2B.
3. **Despeje Espacial (Spatial Clearance):** Los paneles u hologramas de infografía flotantes NUNCA deben atravesar el cuerpo, cuello o rostro de las personas. El expositor (@lead-engineer) debe estar posicionado **a un lado de la mesa gesticulando hacia la infografía**, con suficiente aire y separación espacial.
4. **Branding Ambiental:** El logotipo de la empresa se integra como un **elemento arquitectónico del entorno** (grabado sutil en relieve en el vidrio esmerilado de fondo, madera o pared de la sala). NUNCA como un sticker o marca de agua flotante pegada encima de la gente.
5. **Dimensiones Oficiales para Feed Móvil:** Usar proporción **3:4 o 4:5 vertical** (equivalente a 1080x1440 o 1080x1350). Son las dimensiones estándar directas para publicar en los muros de Facebook, Instagram y LinkedIn en dispositivos móviles.

---

## 5. REGLAS DE COPYWRITING Y LENGUAJE (SIN PRESUNCIÓN)
1. **PROHIBICIÓN ESTRICTA DE ASTERISCOS EN FACEBOOK Y LINKEDIN:**
   - En Facebook y LinkedIn, los asteriscos de Markdown `**texto**` **NO se convierten en negritas**; se publican como caracteres rotos (`**Nivel 1**`).
   - Para resaltar en Facebook y LinkedIn, usa **MAYÚSCULAS LIMPIAS** en los títulos y viñetas con emojis ordenados (ej. `1️⃣ NIVEL 1: USO (Prompts Aislados)`).
2. **Tono Humilde, Empático y de Alta Autoridad (Cero Arrogancia):**
   - NUNCA usar palabras despectivas o condescendientes que suenen a presunción (prohibido usar *"mediocres"*, *"piezas baratas"*, *"vender humo"*, o frases clichés como *"jugar en las grandes ligas"*).
   - Usar un tono constructivo y educativo: *"resultados genéricos o poco profesionales"*, *"piezas estándar que pasan desapercibidas"*, *"destacar con autoridad en tu sector"*.
3. **Llamadas a la Acción Amables:** La invitación al cierre debe invitar a *"conversar"* o *"agendar una sesión"*, sin sonar a venta desesperada ni insistente.

---

## 6. GUÍA DE USO DE PROMPTS PARA EL EQUIPO (QUÉ COPIAR Y QUÉ NO)
Al entregar el archivo `prompt_image.md`, el agente debe instruir al equipo:
- **QUÉ COPIAR:** Únicamente el bloque descriptivo en inglés y el negative prompt.
- **QUÉ NO COPIAR:** NUNCA copiar ni pegar en las herramientas de IA (Google Flow / Nano Banana / Ideogram) la cabecera técnica YAML (`--- post_id... ---`) ni los títulos Markdown (`# PROMPT IMAGEN...`).
- **CONFIGURACIÓN DE HERRAMIENTA:** Recordar siempre verificar que la herramienta esté en **Modo Imagen** (NO en Modo Video) y en proporción **3:4 o vertical**.

---

## 8. EJEMPLOS DE USO
*Usuario:* "**/media-post**" (dentro de un proyecto de video)
*Agente:* Extrae el guion, el lore del personaje y el set del video activo, y genera una infografía de repropósito con copy y previsualización.

*Usuario:* "**/media-post 'Gobernanza de IA en Empresas'**" (tema independiente)
*Agente:* Genera un post estático nuevo dentro de `posts/` basado en la identidad y Brand Book del workspace.

## 9. SALIDA ESPERADA
Directorio `workspaces/[WORKSPACE]/posts/[ID]-[slug]/` con:
- `post.yaml`
- `prompt_image.md`
- `copy.md` (LinkedIn, Facebook, Instagram, WhatsApp)
- `README.md`
- `assets/post_preview.jpg` (optimizada)
