# CASTING ROLE: Mateo (Joven Fraterno Urbano de Cochabamba)
**Actor Base:** `mateo` (Personaje Oficial del Lore de Wistus Cochabamba)  
**Proyecto:** `0001-el-primer-paso`  

---

## 🖼️ Activos Base e Imágenes de Referencia

Para vestir a Mateo con el auténtico traje de Tinku de los Wistus en **Google Flow / Nano Banana Pro** (manteniendo su rostro original y clonando el traje real), se utilizan como entrada estas 3 referencias:

| Slot en Nano Banana | Archivo Recomendado | Función para la IA |
| :--- | :--- | :--- |
| **Imagen 1 (Identidad / Rostro):** | [`characters/mateo/mateo_frontal.jpg`](../../characters/mateo/mateo_frontal.jpg) | Conservar intacto al 100% el rostro de Mateo (22 años, taper fade, ojos oscuros, tez morena clara de valle, complexión atlética). |
| **Imagen 2 (Traje Real de Gala):** | [`casting/references/ref_joven_urbano_fraterno_2.jpg`](./references/ref_joven_urbano_fraterno_2.jpg) | Clonar exactamente la chaquetilla negra con bordados geométricos multicolores, mangas con puños fucsia, faja con tiras de telar andino en cascada (flecos arcoíris), pantalón lila/lavanda, polainas de rombos, calcetas blancas y abarcas. |
| **Imagen 3 (Montera Oficial):** | [`casting/references/ref_montera_detalle.jpg`](./references/ref_montera_detalle.jpg) o [`assets/montera01/montera-01.jpg`](../../assets/montera01/montera-01.jpg) | Colocar en su mano la montera de cuero tradicional con vaqueta, espejos circulares, borlas colgantes y penacho de plumas de suri naranja. |

---

## 🛠️ PASO 1: Generar a Mateo Vestido de Gala (Cuerpo Entero Frontal)

### ¿Por qué falló el intento anterior?
En el intento previo, el prompt en texto describía un chaleco rojo/verde con morado y letras frontales. Los modelos multimodales (Nano Banana Pro / Gemini) priorizan el texto si entra en conflicto con la imagen. Por eso colocó la montera (que sí coincidía con el texto) pero sustituyó el traje negro de la **Imagen 2** por el chaleco rojo/verde descrito en el prompt.

### Solución: Prompt Multimodal Alineado al 100% con la Imagen 2
Copia y pega este prompt exacto en el cuadro de texto de Nano Banana Pro con las 3 imágenes subidas:

```text
A hyper-realistic full-body front-facing studio portrait of the young Bolivian urban male from Image 1, maintaining 100% of his exact facial features, bone structure, clean taper fade haircut, dark brown eyes, youthful light-tan valley complexion, and athletic build. Do not modify his face or hair.

Completely replace his clothing with the exact authentic Bolivian Tinku festival gala costume worn by the dancer in Image 2: a tailored black traditional jacket (chaquetilla) densely adorned with vibrant multicolor geometric starburst and floral embroidery across the chest and front panels, black sleeves with vertical embroidery ending in vibrant magenta-fuchsia embroidered cuffs. Around his waist is a wide traditional Andean woven waistband from which multiple long, vibrant horizontal rainbow-striped textile ribbons (aguayo strips/chumpis) cascade down covering the upper legs, ending in long white cotton fringe tassels. He wears light lavender-violet woven trousers underneath, hand-knitted woolen leg warmers (polainas) with bright multicolor diamond-rhombus geometric patterns, thick white woolen knitted socks, and authentic black leather tire-tread sandals (abarcas).

In his right hand, held comfortably at thigh level, he holds the authentic traditional leather combat helmet (montera) shown in Image 3, with cowhide texture, small circular reflective mirrors, multicolored hanging pompons, and a tall vibrant plume of dyed rhea feathers in bright orange.

He stands in an athletic, proud, confident front-facing pose, looking directly into the camera. Solid, clean, neutral light-gray seamless background. Professional cinematic studio lighting with soft highlights, sharp textiles, natural skin pores, 8k resolution, photorealistic shot on ARRI Alexa 65.
```

*Guarda la imagen resultante como:*  
👉 `workspaces/wistus-cocha/projects/0001-el-primer-paso/casting/mateo_tinku_front.jpg`

---

## 🛠️ PASO 2: Generar la Hoja de Referencia 360° (Model Turnaround - Front & Back)

Una vez que tengas la foto frontal aprobada del Paso 1 (`mateo_tinku_front.jpg`), generamos la hoja de referencia completa para que los modelos de video (VEO / Kling) conozcan la espalda y perfil del traje.

### ¿Cómo configurarlo en Google Flow / Nano Banana Pro?
1. Sube como imágenes de referencia:
   * **Imagen 1:** `mateo_tinku_front.jpg` *(tu foto frontal generada en el Paso 1)*.
   * **Imagen 2:** [`casting/references/ref_espalda_wistus_zapateo.jpg`](./references/ref_espalda_wistus_zapateo.jpg) *(foto dorsal donde se ve la espalda de la chaqueta con 'WIST'US', la faja blanca 'WIST'US BICENTENARIO' y las tiras arcoíris)*.
2. Copia y pega el siguiente prompt:

```text
Create a professional technical character reference sheet turnaround based strictly on the young Bolivian male dressed in the Tinku gala attire from Image 1, combined with the exact authentic dorsal back view details from Image 2. Use a clean, neutral, and smooth light-gray studio background. Present the sheet as a technical model turnaround, maintaining 100% identity consistency, photorealism, textures, and textile patterns.

Subject Description: The exact 22-year-old Bolivian urban male from Image 1 wearing the complete authentic Tinku gala costume: black embroidered chaquetilla jacket with vibrant multicolor geometric embroidery, fuchsia cuffs, cascading rainbow-striped aguayo fringe strips, lavender-violet trousers, multicolored diamond-patterned polainas, white socks, and black leather abarcas. On the back view, clearly showcase the exact back of the black jacket as shown in Image 2: yellow embroidered Wistus emblem on the upper back with bold rainbow embroidered lettering 'WIST'US' below it, a white padded sash with rainbow embroidered 'WIST'US BICENTENARIO', and long multicolored hanging woven strips. Holding the leather montera helmet with orange feather plume in his hand.

Composition: Organized in two horizontal rows.
- Top row: Four full-body standing views side-by-side in this order: front view, left profile view, right profile view, and a detailed back view (clearly showcasing the back embroidery and rear aguayo fringes).
- Bottom row: Three high-detail close-up portraits aligned under the full-body row in this order: front portrait, left profile portrait, right profile portrait.

Technical constraints: Maintain perfect identity consistency across all panels. Relaxed athletic A-pose, consistent scale, precise anatomy, clean silhouette. Uniform spacing, consistent head height across the top row, and consistent facial scale on the bottom row. Soft neutral studio lighting with natural controlled shadows preserving embroidery threads and textile weave. Sharp, print-ready, photorealistic 8k quality.
```

*Guarda la imagen resultante como:*  
👉 `workspaces/wistus-cocha/projects/0001-el-primer-paso/casting/mateo_tinku_reference.jpg`

---

## 🤖 Configuración para Google Flow (Character Info)
*Si vas a registrar a Mateo vestido de Tinku en Google Flow u otra plataforma similar, usa estos datos:*

*   **Name:** `Mateo_Wistus_Gala`
*   **Character Info:** `22-year-old modern urban Bolivian Latino male college student from Cochabamba, athletic build, taper fade haircut, clean-shaven, intense and proud gaze. Wearing authentic Bolivian Tinku gala attire: tailored black jacket with dense vibrant multicolor geometric embroidery, fuchsia cuffs, cascading rainbow-striped aguayo fringe strips over lavender trousers, hand-knitted multicolor diamond-patterned polainas, white socks, and black leather tire-tread abarcas. Holding leather montera helmet with orange and fuchsia feather plume.`

---

## 🗣️ Configuración de Voz (Google Flow)
*   **Voice Name:** `Enceladus`
*   **Customize Performance:** `Speak in warm, youthful, urban Latin American Spanish (Bolivian Cochabamba cadence). A fresh, energetic 22-year-old male baritone voice. Natural, conversational, confident, and inspiring without forced theatrical accents.`
