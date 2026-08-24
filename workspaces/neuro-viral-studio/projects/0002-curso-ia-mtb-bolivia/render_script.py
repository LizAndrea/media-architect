import os
import glob

render_dir = '/opt/publicidad/media-architect/workspaces/neuro-viral-studio/projects/0002-curso-ia-mtb-bolivia/render'
os.makedirs(render_dir, exist_ok=True)

# Clean up old voiceoff files to avoid confusion
for f in glob.glob(os.path.join(render_dir, 'voiceoff_*.md')):
    os.remove(f)

def write_file(filename, content):
    with open(os.path.join(render_dir, filename), 'w') as f:
        f.write(content)

style = "Hyper-realistic cinematic video, vertical 9:16"
camera_style = "Cinematic, GoPro style POV mixed with high-end ARRI Alexa shots. High contrast, dynamic outdoor lighting transitioning to moody indoor lighting."

# Character templates
char_ext = "Preserve Henry's established face, adult male in his late 30s. Preserve his high-end MTB cycling gear, technical long-sleeve jersey with dirt and dust, half-shell MTB trail helmet with visor and sports sunglasses on his head."
char_int = "Preserve Henry's established face, adult male in his late 30s. Preserve his high-end MTB cycling gear, technical long-sleeve jersey with dirt and dust. He is NOT wearing a helmet."

safety = "FLOW SAFETY: fictional adults only, safe nonviolent context, respectful natural behavior, no recognizable people, minors, brands, logos, protected characters or readable text."
language = "LANGUAGE: All spoken dialogue must be ONLY in neutral Latin American Spanish. Voice Style: Confident and natural male tone, deep voice that inspires confidence (Voz grave de persona mayor que da confianza). Do not translate, paraphrase or rewrite the provided dialogue."
negative = "NEGATIVE PROMPT: No logos, no text, no FOX brand, no Nike, no letters, no mutations, no deformed bikes, no floating faces."

# Scene 1
write_file('scene_001_image.md', f"""---
platform: tiktok_shorts
model: midjourney
---
**SCENE 001 - IMAGE PROMPT**
Cinematic, GoPro style POV mixed with high-end ARRI Alexa shots. High contrast, dynamic outdoor lighting. First-person POV from mountain bike handlebars riding fast on a scenic mountain dirt trail in the Andes. Very dusty, intense midday sunlight. 
CRITICAL: No text, no letters, no words. No other people in front of camera.
{negative}
""")

write_file('scene_001_video.md', f"""---
platform: tiktok_shorts
model: google_flow_veo
---
**SCENE 001 - VIDEO PROMPT**
{style}, exact duration 4 seconds. {camera_style}. First-person POV from mountain bike handlebars riding fast on a scenic mountain dirt trail in the Andes. The camera shakes aggressively with handheld action as the bike speeds down the dusty path under intense midday sunlight.
CAMERA / TIMING: Maintain aggressive POV motion throughout. 
CRITICAL: No other people in front of the camera, empty path. No text anywhere.
{safety}
{language}
VOZ EN OFF (HENRY habla):
"Te sientes como un piloto profesional en la montaña..."
{negative}
""")

# Scene 2
write_file('scene_002_image.md', f"""---
platform: tiktok_shorts
model: midjourney
---
**SCENE 002 - IMAGE PROMPT**
Cinematic high-end ARRI Alexa shot. High contrast, dynamic outdoor lighting.
Low angle shot of an adult male in his late 30s wearing high-end MTB cycling gear, technical long-sleeve jersey with dirt and dust, half-shell MTB trail helmet with visor and sports sunglasses on his head. He is riding his mountain bike and braking aggressively on a dirt trail. Backlit lighting from the sun illuminating the dust.
{negative}
""")

write_file('scene_002_video.md', f"""---
platform: tiktok_shorts
model: google_flow_veo
---
**SCENE 002 - VIDEO PROMPT**
{style}, exact duration 4 seconds. {camera_style}. Same outdoor dirt trail, midday. {char_ext}. Henry rides his mountain bike fast and brakes, kicking up a subtle trail of dust that is backlit by the sun. 
CAMERA / TIMING: The camera is fixed on the ground at a low angle. Fast and dynamic action at normal speed, no slow-motion. 
CRITICAL: The character must NOT speak. Mouth is closed.
{safety}
{language}
VOZ EN OFF (HENRY habla):
"...volando por los senderos y sintiendo la adrenalina."
{negative}
""")

# Scene 3
write_file('scene_003_image.md', f"""---
platform: tiktok_shorts
model: midjourney
---
**SCENE 003 - IMAGE PROMPT**
Cinematic high-end ARRI Alexa shot. Moody indoor lighting, chiaroscuro.
Close up 50mm shot of an adult male in his late 30s in a dark modern studio room. He is wearing a technical long-sleeve jersey with dirt and dust, but no helmet. His face is illuminated only by the cold blue light of a computer monitor. He looks deeply disappointed and frustrated. Hard shadows on the wall behind him.
{negative}
""")

write_file('scene_003_video.md', f"""---
platform: tiktok_shorts
model: google_flow_veo
---
**SCENE 003 - VIDEO PROMPT**
{style}, exact duration 6 seconds. {camera_style}. Same dark modern studio room. {char_int}. His face is illuminated by the cold blue light of a computer monitor with hard chiaroscuro shadows in the background. Henry looks deeply disappointed and frustrated as he looks at the screen. 
CAMERA / TIMING: The camera performs a smooth, fast crash zoom toward his face. 
CRITICAL: The character must NOT speak. Mouth is closed.
{safety}
{language}
VOZ EN OFF (HENRY habla):
"Pero llegas a casa, revisas la galería..."
{negative}
""")

# Scene 4
write_file('scene_004_image.md', f"""---
platform: tiktok_shorts
model: midjourney
---
**SCENE 004 - IMAGE PROMPT**
Cinematic, moody indoor lighting. Extreme close up.
Extreme close up of a smartphone screen being held in a dark room. The screen shows a terrible, overexposed, washed-out cycling photo with a white blown-out sky. 
CRITICAL: No text, no letters. No faces or people visible in the background.
{negative}
""")

write_file('scene_004_video.md', f"""---
platform: tiktok_shorts
model: google_flow_veo
---
**SCENE 004 - VIDEO PROMPT**
{style}, exact duration 5 seconds. {camera_style}. Extreme close up of a smartphone screen held in a dark room. The screen displays a terrible, washed-out, overexposed, amateur cycling photo with a blown-out white sky.
CAMERA / TIMING: The camera experiences a slight handheld tremor.
CRITICAL: No faces or people visible in the background. No text on the screen.
{safety}
{language}
VOZ EN OFF (HENRY habla):
"...y parece que tomaste la foto con una calculadora."
{negative}
""")

# Scene 5
write_file('scene_005_image.md', f"""---
platform: tiktok_shorts
model: midjourney
---
**SCENE 005 - IMAGE PROMPT**
Cinematic high-end ARRI Alexa shot. Moody indoor lighting.
Medium close up 35mm shot of an adult male in his late 30s in a dark modern studio room. He is wearing high-end MTB cycling gear, technical long-sleeve jersey with dirt and dust, but no helmet. His face is illuminated by a warm and bright computer monitor light. He is smiling confidently as he types on a keyboard.
{negative}
""")

write_file('scene_005_video.md', f"""---
platform: tiktok_shorts
model: google_flow_veo
---
**SCENE 005 - VIDEO PROMPT**
{style}, exact duration 6 seconds. {camera_style}. Same dark modern studio room. {char_int}. The screen light illuminating his face transitions from cold blue to warm and bright. Henry smiles confidently and begins typing quickly on his keyboard. Both characters naturally look at each other while speaking (he looks at the camera).
SPEAKER CONTROL: Henry speaks confidently directly to the camera.
REGLA DE ENFOQUE DEL HABLANTE: Si solo un personaje habla, cambia de inmediato a un plano medio corto de ese personaje al comenzar el diálogo. Mantén continuidad de posición, vestuario, iluminación y fondo.
CAMERA / TIMING: Start with a medium close up. The camera performs a fast whip pan to his face as he smiles confidently. 
{language}
{safety}
LIPSYNC A — ESCENA 5 — (HENRY habla):
"Tranquilo. Con un poco de inteligencia artificial..."
{negative}
""")

# Scene 6
write_file('scene_006_image.md', f"""---
platform: tiktok_shorts
model: midjourney
---
**SCENE 006 - IMAGE PROMPT**
A terrible, washed-out, desaturated, overexposed amateur photo of a professional MTB cyclist on a dirt trail. The photo looks ugly, flat, and lacks contrast.
CRITICAL: No text, no letters, no UI elements. No split screens.
{negative}
""")

write_file('scene_006_video.md', f"""---
platform: tiktok_shorts
model: google_flow_veo
---
**SCENE 006 - VIDEO PROMPT**
{style}, exact duration 8 seconds. A clean screencast animation of a vertical comparison slider moving smoothly from left to right across the screen. The video starts entirely as the terrible washed-out photo. As the slider moves right, it magically transforms and reveals a stunning, perfectly color-graded professional version of the same MTB photo with vibrant colors and a blue sky. 
CAMERA / TIMING: The camera remains completely static. The only movement is the slider wiping across from left to right.
CRITICAL: No text, no letters, no UI elements.
{safety}
{language}
VOZ EN OFF (HENRY habla):
"...puedes rescatar esa foto y dejarla a nivel revista profesional."
{negative}
""")

# Scene 7
write_file('scene_007_image.md', f"""---
platform: tiktok_shorts
model: midjourney
---
**SCENE 007 - IMAGE PROMPT**
Cinematic high-end ARRI Alexa shot. Moody indoor lighting.
Medium shot 50mm of an adult male in his late 30s in a dark modern studio room. He is wearing high-end MTB cycling gear, technical long-sleeve jersey with dirt and dust, no helmet. He is pointing downwards at the camera with a confident smile. Soft key light on his face and a nice blueish rim light on his shoulders. Bokeh background.
{negative}
""")

write_file('scene_007_video.md', f"""---
platform: tiktok_shorts
model: google_flow_veo
---
**SCENE 007 - VIDEO PROMPT**
{style}, exact duration 7 seconds. {camera_style}. Same dark modern studio room. {char_int}. He smiles with confidence and points his finger directly downwards at the camera. Soft key light illuminates his face while a blueish rim light highlights his shoulders against a bokeh background. 
SPEAKER CONTROL: Henry speaks confidently directly to the camera.
REGLA DE ENFOQUE DEL HABLANTE: Si solo un personaje habla, cambia de inmediato a un plano medio corto de ese personaje al comenzar el diálogo. Mantén continuidad de posición, vestuario, iluminación y fondo.
CAMERA / TIMING: The camera performs a very slow and smooth push-in (dolly in).
{language}
{safety}
LIPSYNC A — ESCENA 7 — (HENRY habla):
"¿Tus fotos dan pena? Comenta 'RUTA' y te paso el curso de IA."
{negative}
""")

print("All scenes regenerated successfully in render/ (voiceoff merged)")
