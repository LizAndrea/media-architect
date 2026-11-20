---
platform: google_flow
model: google_flow_nano_banana_pro
scene: 2
type: image
aspect_ratio: "9:16"
seed: 42
---

# ESCENA 002 - IMAGEN BASE MULTIMODAL (KEYFRAME INICIAL)
**Toma:** 2 - Preparación Rápida (Acomodar la Abarca)  
**Formato:** Vertical (9:16)  
**Técnica:** Image-to-Image Multimodal (2 Referencias en Nano Banana Pro)  

---

## 🖼️ Configuración de Slots en Nano Banana Pro

| Slot en Nano Banana | Archivo en el Workspace | Función para la IA |
| :--- | :--- | :--- |
| **Imagen 1 (Personaje / Ropa Real):** | [`casting/mateo_tinku_legs_crop.jpg`](../casting/mateo_tinku_legs_crop.jpg) *(o `mateo_tinku_front.jpg`)* | Clonar al 100% las chalinas de aguayo con flecos blancos colgantes, las polainas geométricas altas, el pantalón lila y las abarcas de llanta. |
| **Imagen 2 (Set / Asfalto):** | [`sets/set_01_asfalto_cochabamba_macro.jpg`](../sets/set_01_asfalto_cochabamba_macro.jpg) | Proveer la calle y el asfalto al amanecer. |

---

## 🎬 PROMPT OPTIMIZADO (LIMPIO, SIN SOBREDESCRIPCIÓN)

```text
A cinematic ground-level close-up shot of the lower body, legs, and feet of the Bolivian Tinku dancer from Image 1, on the dawn asphalt street from Image 2.

The dancer's hands are adjusting and checking the snug fit of the black rubber tire abarca around his ankle, ensuring the strap is firm and secure for dancing. NO tying shoelaces, NO strings.

Strictly preserve all clothing and accessories exactly as shown in Image 1:
- The long rainbow-striped chalinas (aguayo sash ribbons) with long white cotton fringe tassels hanging down over the knees and shins.
- The tall hand-knitted woolen polainas with bold multicolor geometric patterns covering the shins.
- The light lavender-violet trousers and thick white wool socks inside the black tire abarcas.

Single continuous frame, early dawn golden rim lighting, sharp focus on textiles and asphalt, shot on ARRI Alexa 65, 8k resolution, photorealistic.

NEGATIVE PROMPT: tying shoelaces, shoe laces, strings, knots, modern sneakers, metal buckles, bare skin, bare legs, missing chalinas, missing white fringes, purple plain socks, split screen, collage, multiple panels.
```

---

## 💡 Claves de esta corrección:
1. **Gesto Auténtico:** Se eliminó la palabra "cordón" y "amarrar" que hacía que la IA dibujara cordones de zapatillas. Ahora el prompt indica `adjusting and checking the snug fit of the rubber tire strap` (acomodar la abarca y verificar que esté bien firme).
2. **Inclusión de las Chalinas:** Se exige explícitamente `long rainbow-striped chalinas with long white cotton fringe tassels hanging over knees and shins`.
3. **Prompt Limpio (Anti-Saturación):** Al no saturar de adjetivos innecesarios, Nano Banana le da máxima prioridad visual a la **Imagen 1**.
