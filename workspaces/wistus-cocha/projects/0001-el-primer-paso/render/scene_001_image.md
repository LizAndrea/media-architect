---
platform: google_flow
model: google_flow_nano_banana_pro
scene: 1
type: image
aspect_ratio: "9:16"
seed: 42
---

# ESCENA 001 - IMAGEN BASE MULTIMODAL (KEYFRAME INICIAL)
**Toma:** 1 - Hook de Shock (El Retumbar)  
**Formato:** Vertical (9:16)  
**Técnica:** Image-to-Image Multimodal (2 Referencias obligatorias en Nano Banana Pro)  

---

## 🖼️ Configuración de Slots en Nano Banana Pro

Para que la IA no invente un pie genérico ni altere los colores de la ropa, **DEBES subir 2 imágenes de referencia** en la interfaz:

| Slot en Nano Banana | Archivo en el Workspace | Función para la IA |
| :--- | :--- | :--- |
| **Imagen 1 (Vestuario y Piernas):** | [`casting/mateo_tinku_legs_crop.jpg`](../casting/mateo_tinku_legs_crop.jpg) *(o `mateo_tinku_front.jpg`)* | Clonar al 100% las polainas altas de rombos/zigzag multicolores, las tiras de aguayo con flecos blancos colgantes, el pantalón lila y las abarcas de llanta sobre calceta blanca. |
| **Imagen 2 (Set / Asfalto):** | [`sets/set_01_asfalto_cochabamba_macro.jpg`](../sets/set_01_asfalto_cochabamba_macro.jpg) | Proveer la textura real del pavimento, los granos de asfalto y la iluminación rasante dorada de amanecer. |

---

## 🎬 PROMPT MULTIMODAL EN INGLÉS (COPIAR Y PEGAR)

```text
A cinematic ground-level macro action shot capturing the exact legs, textiles, and footwear of the Bolivian Tinku dancer from Image 1, positioned seamlessly onto the rough asphalt pavement shown in Image 2.

Strictly replicate 100% of the clothing and textile details from Image 1:
- The exact hand-knitted tall woolen polainas on his shins, featuring bold, vibrant multicolor geometric patterns (one leg with multi-colored chevrons/zigzags in cyan, lime green, red, and yellow with braided hanging pompoms; the other leg with large concentric diamonds in black, cyan, yellow, and magenta).
- The long white cotton fringe tassels of the horizontal rainbow-striped aguayo sash strips cascading down from the waist, dangling dynamically over the knees and shins.
- The light lavender-violet woven trousers tucked into the top of the polainas.
- The authentic black tire-tread abarca sandal with hand-cut rubber straps and tied cords, worn strictly OVER a thick white hand-knitted woolen sock (calceta de lana blanca) with zero bare skin.

Action: One foot stomps aggressively down onto the rough asphalt pavement in dramatic 120fps slow-motion, detonating an explosive conical shockwave of fine mineral dust and gravel catching golden amber dawn side-lighting. Deep depth of field, razor-sharp focus on the textile weave and flying dust particles, shot on ARRI Alexa 65 macro lens, 8k resolution, photorealistic.

NEGATIVE PROMPT: bare skin, bare feet, bare toes, bare legs, purple solid socks, plain short socks, missing white fringes, missing aguayo strips, metal buckles, modern sneakers, cartoon, 3d render, blurry focus, text, watermark.
```

---

## 💡 ¿Por qué este prompt soluciona el problema?
1. **Anclaje Visual Directo (`Image 1`):** La IA ahora tiene la orden explícita de clonar la indumentaria de la **Imagen 1**, impidiendo que invente esas medias moradas cortas o sandalias genéricas.
2. **Presencia de Flecos y Aguayos:** Detalla los flecos blancos colgantes (*white fringe tassels*) que caen sobre las polainas, tal como se ve en la foto oficial de Mateo.
3. **Set Fiel (`Image 2`):** Fusiona el zapateo con la placa macro de asfalto que ya aprobaste previamente.
