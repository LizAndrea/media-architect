import re

in_path = "/opt/publicidad/media-architect/workspaces/neuro-viral-studio/projects/0004-promo-ciclismo-mtb/script/script.md"
out_path = "/opt/publicidad/media-architect/workspaces/neuro-viral-studio/projects/0004-promo-ciclismo-mtb/storyboard/storyboard.md"

with open(in_path, 'r') as f:
    lines = f.readlines()

scenes = []
for line in lines:
    if line.startswith('| ') and not line.startswith('| Toma |') and not line.startswith('| :--- |'):
        parts = [p.strip() for p in line.split('|')[1:-1]]
        if len(parts) >= 4:
            dur = parts[1].split('(')[0].strip()
            num = re.search(r'\d+', parts[0])
            if num:
                scene_num = num.group(0)
                vis = parts[2]
                aud = parts[3]
                scenes.append({
                    'num': scene_num,
                    'dur': dur,
                    'vis': vis,
                    'aud': aud
                })

def translate_vis(vis):
    v = vis.lower()
    is_garage = "garaje" in v
    bg = "dark garage background, chiaroscuro lighting" if is_garage else "outdoor mountain trail, forest, bright daylight"
    
    action = v.replace("int. garaje - día. ", "").replace("int. garaje. ", "").replace("ext. montaña. ", "").replace("ext. sendero. ", "").replace("ext. bosque. ", "").replace("ext. charco. ", "").replace("ext. rocas. ", "").replace("ext. curva. ", "").replace("ext. cresta. ", "")
    action_en = "generic mountain biker in action"
    if "casco" in v: action_en = "biker putting on a green full-face helmet"
    elif "llanta" in v or "rueda" in v: action_en = "close up of a mountain bike wheel"
    elif "cadena" in v or "cassette" in v: action_en = "close up of bike chain and gears"
    elif "dron" in v: action_en = "wide aerial shot of biker on a trail"
    elif "salto" in v or "desnivel" in v: action_en = "biker jumping over the camera"
    elif "derrapa" in v or "skid" in v: action_en = "biker skidding and kicking up dirt"
    elif "logo" in v or "negra" in v: action_en = "abstract close up or solid color, no text"
    elif "silueta" in v: action_en = "silhouette of a mountain biker"
    elif "ajustando" in v: action_en = "biker adjusting their gear and jersey"
    elif "suspen" in v: action_en = "close up of the rear suspension of the bike"
    
    return f"Background: {bg}. {action_en}."

out = "# STORYBOARD - Promo Ciclismo Enduro y MTB (Replica)\n\n"
out += "**Reparto (Lore):** none\n\n"

for i in range(0, len(scenes), 6):
    chunk = scenes[i:i+6]
    start = int(chunk[0]['num'])
    end = int(chunk[-1]['num'])
    out += f"## Bloque Escenas {start}-{end}\n\n"
    
    # Prompt in English
    num_panels = len(chunk)
    rows = 2 if num_panels > 3 else 1
    cols = min(num_panels, 3)
    if num_panels == 4:
        rows, cols = 2, 2
    if num_panels == 5:
        rows, cols = 2, 3
    
    out += f"*PROMPT:*\n"
    out += f"*High-End Commercial, action sports MTB, dynamic fast cuts style. A {num_panels}-panel comic-style storyboard layout ({rows} rows of {cols} panels). The images should depict generic mountain biker, faceless subjects, and B-Roll elements.\n"
    for idx, s in enumerate(chunk):
        out += f"Panel {idx+1}: {translate_vis(s['vis'])}\n"
    out += "CRITICAL: Do not include any text, letters, subtitles, words, or speech bubbles anywhere in the image. The image must be completely free of typography.*\n\n"
    
    out += f"![Storyboard](assets/board_{start:02d}_{end:02d}.jpg)\n\n"
    
    for s in chunk:
        vis = s['vis'].replace("**", "")
        plano = "General / Lente Gran Angular" if "general" in vis.lower() or "dron" in vis.lower() else ("Detalle (ECU) / Lente Macro" if "detalle" in vis.lower() else "Plano Medio (MS) / Lente 35mm")
        ilum = "Chiaroscuro / Dramatic Key" if "GARAJE" in vis.upper() else "Luz natural / Bright Daylight"
        mov = "Shaky / Handheld" if "mano" in vis.lower() else ("Whip Pan" if "látigo" in vis.lower() else "Dinámico")
        
        out += f"### Toma {s['num']} (Escena {s['num']})\n"
        out += f"- **Toma:** {s['num']}\n"
        out += f"- **Thumbnail (Visual):** {vis}\n"
        out += f"- **Acción/Narrativa:** {vis}\n"
        out += f"- **Cámara y Fotografía:**\n"
        out += f"  - **Plano:** {plano}\n"
        out += f"  - **Movimiento de cámara:** {mov}\n"
        out += f"  - **Iluminación:** {ilum}\n"
        out += f"  - **Color Grading:** Alto contraste, Teal & Orange\n"
        out += f"- **Duración:** {s['dur']}\n"
        out += f"- **Audio/Voz en Off:** \"{s['aud']}\"\n"
        out += f"- **Transición:** Hard Cut\n\n"

with open(out_path, 'w') as f:
    f.write(out)
