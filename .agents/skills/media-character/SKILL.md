---
name: media-character
description: Registra un nuevo personaje en el Lore del cliente activo
---

# media-character

## When to use
Usa este comando cuando el usuario quiera registrar un nuevo personaje recurrente (actor, avatar, o elemento consistente como "La Salteña") para que sea utilizado en múltiples proyectos de video del mismo cliente.

## How to use
1. **Verifica el cliente activo:** Asegúrate de saber qué cliente está activo (ej. usando la configuración de `/media-in`).
2. **Identifica el Tipo de Entidad:** Pregúntale al usuario si está registrando un **"Actor/Personaje"** (con voz y personalidad) o un **"Prop/Objeto"** (como un vehículo, un producto o "La Salteña").
3. **Solicita la información:**
   - Nombre de la entidad.
   - Lore (Si es personaje: Personalidad. Si es Objeto: Contexto y cómo se usa en los videos).
   - Visual Prompt (Cómo se ve físicamente, texturas, colores).
   - Voice & Audio Config (Solo si es personaje, omite esto si es un objeto).
4. **Nomenclatura y Sanitización (CRÍTICO):** Convierte el nombre a minúsculas, reemplaza espacios por guiones medios (kebab-case), elimina tildes y cambia la "ñ" por "n" (ej. "La Salteña" -> `la-saltena`, "mesa casa codi" -> `mesa-casa-codi`). Esto será su **ID_Tag**.
5. **Crea la estructura:** Crea una carpeta en `clients/[CLIENTE_ACTIVO]/characters/[ID_Tag]/`.
6. **Genera la Ficha Técnica:** Escribe un archivo `[ID_Tag].md` usando este formato:

```markdown
# LORE ENTITY: [Nombre Original]
**Tipo:** [Actor/Personaje u Objeto/Prop]
**ID_Tag:** [[ID_Tag]]

## 🧠 Lore / Contexto (Para Guionistas)
**Descripción:** [Personalidad si es actor, o contexto/importancia si es objeto]
**Comportamiento/Uso:** [Cómo actúa o cómo interactúan los personajes con este objeto]

## 👁️ Visual Prompt / Appearance (Para Video/Imagen AI)
**[ENGLISH]** [Traducción al inglés del aspecto físico, texturas, iluminación ideal, etc.]

## 🗣️ Voice & Audio Config (Para IA de Voz)
[Solo incluye esta sección si es un Personaje/Actor. Detalla el modelo y tono. Si es un objeto, escribe: "N/A - Entidad inanimada"]
```

6. **Instrucciones Finales:** Pídele al usuario que guarde manualmente sus imágenes de referencia dentro de la carpeta creada. (Sugiere nombres como `[nombre]_frontal.jpg` o `[nombre]_reference.jpg` en lugar de "fullbody" si es un objeto).

## Expected output
La carpeta del personaje creada con su archivo `.md` estructurado y un mensaje confirmando el éxito.
