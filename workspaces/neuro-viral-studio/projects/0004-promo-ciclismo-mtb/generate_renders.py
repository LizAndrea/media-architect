import re
import os

script_path = "/opt/publicidad/media-architect/workspaces/neuro-viral-studio/projects/0004-promo-ciclismo-mtb/script/script.md"
render_dir = "/opt/publicidad/media-architect/workspaces/neuro-viral-studio/projects/0004-promo-ciclismo-mtb/render"
os.makedirs(render_dir, exist_ok=True)

with open(script_path, 'r') as f:
    lines = f.readlines()

scenes = []
for line in lines:
    if line.startswith('| ') and not line.startswith('| Escena |') and not line.startswith('| --- |'):
        parts = [p.strip() for p in line.split('|')[1:-1]]
        if len(parts) >= 4:
            scenes.append({
                'num': parts[0],
                'dur': parts[1],
                'vis': parts[2],
                'aud': parts[3]
            })

for s in scenes:
    idx = int(s['num'])
    filename = f"{render_dir}/scene_{idx:03d}_video.md"
    
    # Simple logic for backgrounds and negative prompts
    is_garage = "GARAJE" in s['vis'].upper()
    location_en = "dark garage, cinematic chiaroscuro lighting, high contrast" if is_garage else "mountain dirt trail, forest, bright daylight, cinematic action sports style"
    
    vis_en = s['vis'].replace("INT. GARAJE - DÍA. ", "").replace("INT. GARAJE. ", "").replace("EXT. MONTAÑA. ", "").replace("EXT. SENDERO. ", "").replace("EXT. BOSQUE. ", "")
    
    content = f"""---
platform: "youtube_longform"
model: "Google Flow VEO"
seed: 0
negative_prompt: "text, logos, words, deformed, unnatural movements"
---

*PROMPT:*
SCENE: {location_en}. A generic mountain biker (no specific face). High-End Commercial, action sports MTB, dynamic fast cuts.
ACTION: 0-2s: The scene depicts: {vis_en}
CAMERA: Dynamic camera movement as described in the action.

CRITICAL: The character must NOT speak. Mouth is closed.

NEGATIVE PROMPT:
No text, no logos, no letters, no watermarks, no mutations, no deformed bike parts, no other people.
"""
    with open(filename, 'w') as f:
        f.write(content)

music_content = """---
platform: "youtube_longform"
model: "Suno AI"
---
*PROMPT:*
Aggressive heavy rock alternative metal, intense driving bassline, fast drum beats, electric guitar riffs, cinematic build-up to climax, instrumental only, high adrenaline, mountain biking action sport soundtrack.
"""
with open(f"{render_dir}/music.md", 'w') as f:
    f.write(music_content)

