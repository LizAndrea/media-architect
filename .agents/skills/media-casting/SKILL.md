---
name: media-casting
description: Analiza un guion aprobado y genera las Hojas de Referencia (Reference Sheets) de los personajes para el proyecto.
---

# media-casting

## When to use
Usa este comando **inmediatamente después** de que el usuario apruebe el guion final en un proyecto (`script.md`). Este comando es el puente entre el guion y la generación de imágenes/video por IA.

## How to use
1. **ASUME EL ROL DE:** **Director de Casting y Diseñador de Vestuario**.
2. **Lectura de Guion:** Lee el archivo `script.md` del proyecto activo actual.
3. **Identificación de Roles:** Identifica todos los personajes que interactúan visualmente en el guion.
4. **Cruce con Actores Base:** Pregunta al usuario si desea utilizar alguno de los actores base del workspace (ubicados en `workspaces/[WORKSPACE_ACTIVO]/characters/`) para estos roles, o si desea inventar "Extras" nuevos exclusivamente para este proyecto.
5. **Generación de Prompts (Reference Sheets):** Por cada rol, genera un archivo Markdown dentro de `workspaces/[WORKSPACE_ACTIVO]/projects/[ID_PROYECTO]/casting/[rol].md`. (Si la carpeta `casting/` no existe, créala).
6. **Estructura del Archivo de Casting:** Cada archivo generado debe seguir este formato EXACTO:

```markdown
# CASTING ROLE: [Nombre del Rol en la Historia]
**Actor Base:** [Nombre del actor base o "Nuevo Extra"]
**Proyecto:** [ID del Proyecto]

## 🎭 Contexto en el Guion
**Actitud / Emoción:** [Ej: Asustada, Estresada, Eufórico]
**Vestuario (Wardrobe):** [Descripción detallada de la ropa, colores y accesorios según la locación del guion]

## 📸 Prompt 1: Imagen Frontal de Cuerpo Entero (Google Flow Face / Base Cref)
*Genera PRIMERO esta imagen. Será tu "Plato Principal" para generar el turnaround después.*
> **PROMPT EN INGLÉS:** A hyper-realistic full-body front-facing portrait of the subject in the loaded reference image. [Subject Description: Edad, género, etnia, vestuario completo INCLUYENDO pantalones/zapatos, peinado]. She/He has a [expresión facial], looking directly at the camera, standing in a relaxed pose. Clean, neutral gray background. Soft cinematic studio lighting, highly detailed face, natural skin texture and pores. Shot on ARRI Alexa 65, 8k resolution.

## 📸 Prompt 2: Hoja de Referencia (Character Reference Sheet)
*Una vez generada y aprobada la imagen de cuerpo entero, usa ESA imagen como referencia (Cref) junto con este prompt en tu IA generadora:*
> **PROMPT EN INGLÉS:** Create a professional character reference sheet based strictly on the loaded reference image. Use a clean, neutral, and smooth background. Present the sheet as a technical model turnaround, maintaining exactly the same visual style, level of realism, rendering focus, textures, color treatment, and general aesthetics as the reference.
> 
> **Subject Description:** [Copiar la misma descripción del vestuario completo que el prompt anterior].
> 
> **Composition:** Organize in two horizontal rows.
> - **Top row:** Four full-body standing views side-by-side in this order: front view, left profile view, right profile view, back view.
> - **Bottom row:** Three high-detail close-up portraits aligned under the full-body row in this order: front portrait, left profile portrait, right profile portrait.
> 
> **Technical constraints:** Maintain perfect identity consistency across all panels. Place the character in a relaxed A-pose, with consistent scale, precise anatomy, and clear silhouette. Ensure uniform spacing, clean separation between panels, consistent head height across the top row, and consistent facial scale on the bottom row.
> **Lighting:** Coherent across all panels (same direction, intensity, and softness), with natural controlled shadows that preserve detail without dramatic changes in atmosphere. Sharp, print-ready, well-defined details.

## 🤖 Configuración para Google Flow (Character Info)
*Si vas a guardar este personaje en Google Flow u otra plataforma similar, usa estos datos:*

**Name:** `[ID_Unico_del_Rol_en_Inglés]` *(Nota: Usa un nombre de rol como `MTB_Cyclist_1`, NO el nombre del actor base, para no confundir a la IA si hay múltiples roles o clones)*
**Character Info:** `[Misma descripción que Subject Description en el prompt visual, resumiendo los rasgos base y la ropa inmutable]`

## 🗣️ Configuración de Voz (Google Flow)
**Voice Name:** `[Sugerir una voz. Si es hombre, elige UNA de esta lista: Zubenelgenubi, Achird, Algenib, Algieba, Alnilam, Charon, Enceladus, Fenrir, Iapetus, Orus, Puck, Rasalgethi, Sadachbia, Sadaltager, Schedar, Umbriel. Si es mujer, sugiere una femenina estándar de Flow]`
**Customize Performance:** `Speak in neutral Latin American Spanish. [Define SOLO el tono base del personaje, ej: Confident and energetic male tone. NO incluyas emociones específicas de escenas aquí]`
```

7. **Instrucciones al Usuario:** Una vez creados los archivos, indícale al usuario que debe ir a su IA de imágenes con esos prompts, generar a los personajes vestidos, y guardar las imágenes resultantes en la carpeta `assets/` del proyecto. Solo después de eso, estarán listos para `/media-render`.

## Examples
*Usuario:* "/media-casting"
*Agente:* Lee el guion. "Veo que necesitamos una doctora y un paciente. ¿Usamos a Isabella como la doctora? (Genera `isabella_doctora.md` en el proyecto con su vestuario de hospital)".

## Expected output
Archivos `.md` generados en la carpeta `casting/` del proyecto, conteniendo prompts exactos para generar Hojas de Referencia de Personajes (Reference Sheets) con el vestuario y actitud de la historia.
