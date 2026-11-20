# LORE ENTITY: Mateo
**Tipo:** Actor Base / Personaje Principal Recurrente  
**ID_Tag:** `mateo`  
**Rol:** Joven fraterno universitario de Cochabamba (Portavoz y bailarín principal de Wistus Filial Cocha)

## 🖼️ Archivos Oficiales del Modelo Base
- **Retrato Frontal Base:** [`mateo_frontal.jpg`](./mateo_frontal.jpg) (1792 × 2400 px, RGB)
- **Hoja de Referencia (Turnaround):** [`mateo_reference.jpg`](./mateo_reference.jpg) (1376 × 768 px, RGB)

---

## 🧠 Lore / Contexto (Para Guionistas)
*   **Descripción del Actor Base:** Mateo es un joven boliviano de 22 años nacido y criado en la ciudad de Cochabamba. Es estudiante universitario, sociable, de complexión atlética, carismático y con la energía fresca de la juventud urbana de la Llajta. No es un personaje de estética rural ni originaria; representa al chico de ciudad que descubre la pasión por el Tinku en las calles de Cochabamba y se une con devoción y disciplina a la Fraternidad Tinkus Wistus.
*   **Comportamiento en Pantalla:** Seguro, expresivo, con mirada franca y sonrisa contagiosa en momentos relajados, pero con una concentración marcial, mandíbula tensa y fiera determinación al entrar en modo zapateo.
*   **Estrategia de Uso (Actor Base Multirrol):** Mateo es el rostro oficial recurrente del workspace. Se genera una sola vez con ropa neutra para congelar su identidad física (rostro, ojos, peinado y anatomía). Luego, en cada proyecto de video, se mantiene su rostro intacto mediante referencia de imagen (Cref) y solo se le cambia el vestuario según la narrativa:
    *   *Traje de Gala Oficial de Tinku Wistus* (para entradas, Corso de Corsos y tráilers épicos).
    *   *Ropa Deportiva de Ensayo* (camiseta negra/morada Wistus, joggers y zapatillas para videos de preparación).
    *   *Ropa Casual Urbana* (hoodie o polera universitaria para storytelling cotidiano).

---

## 📸 PROMPTS PARA GENERAR LA IDENTIDAD BASE DE MATEO

> **Instrucción:** Usa estos prompts en tu IA generadora de imágenes (Midjourney, FLUX o Google Imagen 3) con ropa neutra para crear el modelo maestro de Mateo. Guarda las imágenes resultantes en esta misma carpeta: `workspaces/wistus-cocha/characters/mateo/mateo_frontal.jpg` y `mateo_reference.jpg`.

### 📸 Prompt 1: Imagen Frontal Base de Cuerpo Entero (Identity Anchor)
*Genera PRIMERO esta imagen. Establece su rostro, proporciones corporales y cabello urbano.*

> **PROMPT EN INGLÉS:**  
> A hyper-realistic full-body front-facing studio portrait of an authentic 22-year-old modern urban Bolivian Latino male college student from Cochabamba. He has handsome and expressive youthful features, charismatic and determined dark brown eyes, clean-shaven face, warm light-tan valley skin tone with natural skin pores and texture. He has contemporary styled short dark textured hair with a clean, sharp taper fade on the sides. Athletic and lean build. He is dressed in neutral minimalist modern casual clothing: a fitted plain charcoal grey crewneck t-shirt, slim-fit dark raw denim jeans, and clean minimalist dark grey urban sneakers. He stands in a relaxed, confident pose, looking directly into the camera with an intense, engaging, and friendly expression. Solid, clean, neutral light-gray seamless background. Soft cinematic studio lighting with subtle rim light, highly detailed face, perfectly photorealistic. Shot on ARRI Alexa 65, 85mm lens, f/2.8, 8k resolution.

---

### 📸 Prompt 2: Hoja de Referencia Base (Master Model Turnaround Sheet)
*Una vez generada y aprobada la imagen frontal de Mateo, usa ESA imagen como referencia (Cref) junto con este prompt para crear su hoja técnica de 360 grados:*

> **PROMPT EN INGLÉS:**  
> Create a professional character reference sheet based strictly on the loaded reference image of the young Bolivian urban male. Use a clean, neutral, and smooth light-gray background. Present the sheet as a technical model turnaround, maintaining exactly the same facial features, haircut, skin texture, body proportions, and realism as the reference.
> 
> **Subject Description:** A 22-year-old modern urban Bolivian Latino male college student from Cochabamba, short dark textured hair with taper fade, charismatic dark brown eyes, clean-shaven, light-tan complexion. Wearing a fitted plain charcoal grey crewneck t-shirt, slim-fit dark denim jeans, and dark urban sneakers.
> 
> **Composition:** Organized in two horizontal rows.
> - **Top row:** Four full-body standing views side-by-side in this order: front view, left profile view, right profile view, back view.
> - **Bottom row:** Three high-detail close-up portraits aligned under the full-body row in this order: front portrait, left profile portrait, right profile portrait.
> 
> **Technical constraints:** Maintain 100% facial and anatomical identity consistency across all panels. The character is placed in a relaxed A-pose, with consistent scale, precise anatomy, and clear silhouette. Ensure uniform spacing, clean separation between panels, consistent head height across the top row, and consistent facial scale on the bottom row.
> **Lighting:** Coherent across all panels, soft neutral studio lighting with natural controlled shadows that preserve fine facial details. Sharp, print-ready, photorealistic 8k quality.

---

## 🔄 ¿Cómo Cambiarle la Ropa en Cada Proyecto?

Una vez que tengas `mateo_frontal.jpg`:
1.  **En Midjourney / FLUX:** Cargas la imagen de Mateo en el canal de generación y usas el parámetro `--cref [URL_MATEO]` (Character Reference) junto con el prompt de vestuario específico del proyecto (ejemplo: el traje de gala de Tinku de `projects/0001-el-primer-paso/casting/mateo.md`).
2.  **En Google Flow / Kling:** Asignas a `mateo_frontal.jpg` como el sujeto base (*Actor*) y describes la acción y la ropa específica de la escena en el prompt de video.

---

## 🗣️ Configuración de Voz (Google Flow / ElevenLabs)
*   **Voice Name:** `Enceladus` *(Google Flow)* o `mateo_cocha_voice` *(ElevenLabs)*
*   **Customize Performance:** `Speak in warm, youthful, urban Latin American Spanish with a natural Bolivian Cochabamba cadence. A fresh, energetic 22-year-old male baritone voice. Natural, conversational, confident, and inspiring without forced theatrical accents or overly dramatic tones.`
