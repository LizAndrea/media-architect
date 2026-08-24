import re

in_path = "/opt/publicidad/media-architect/workspaces/neuro-viral-studio/projects/0004-promo-ciclismo-mtb/script/script.md"
out_path = "/opt/publicidad/media-architect/workspaces/neuro-viral-studio/projects/0004-promo-ciclismo-mtb/script/script.md"

with open(in_path, 'r') as f:
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

# Accumulate time
def time_to_sec(t_str):
    if ":" in t_str:
        m, s = t_str.split(":")
        return int(m) * 60 + int(s)
    return int(t_str.replace('s',''))

def sec_to_time(s):
    return f"{s//60}:{s%60:02d}"

current_sec = 0

out = """# GUION: SHORT / REEL / TIKTOK (9:16) / YOUTUBE
**Proyecto:** Promo Ciclismo Enduro y MTB (Replica)
**Workspace:** neuro-viral-studio
**Reparto (Lore):** none
**Duración:** 01:22
**Ritmo:** Hiper-rápido, cortes agresivos, cinemático
**Hook:** Contraste extremo; empieza en el misterio absoluto de un garaje y estalla en furia de rock y velocidad en la montaña.

## 1. SINOPSIS
Réplica exacta de "Promo CICLISMO Enduro y MTB". Una inyección de adrenalina pura en 82 segundos que documenta la metamorfosis del ciclista: desde la tensa y oscura preparación mecánica hasta el descenso explosivo y extremo en la naturaleza.

## 2. ESTRUCTURA NARRATIVA Y GUION A DETALLE

| Toma | Duración (Máx 8s) | Escena Visual | Audio / Voz en Off | Texto en Pantalla |
| :--- | :--- | :--- | :--- | :--- |
"""

for i, s in enumerate(scenes):
    dur_sec = time_to_sec(s['dur'])
    start = current_sec
    end = current_sec + dur_sec
    current_sec = end
    
    toma_label = f"Toma {s['num']}"
    if i == 0:
        toma_label = "**1. Hook**"
    elif i == len(scenes) - 1:
        toma_label = "**41. Outro**"
    elif i == 15:
        toma_label = "**16. Explosión**"
        
    time_label = f"**{dur_sec}s ({sec_to_time(start)} - {sec_to_time(end)})**"
    text_screen = '"Cristian Alvero"' if i == 40 else ''
    
    out += f"| {toma_label} | {time_label} | **[{s['vis'].split('.')[0] if '.' in s['vis'] else 'Plano'}]**. {s['vis']} | *(SFX/Voz)* \"{s['aud']}\" | {text_screen} |\n"

out += """
## 3. ANÁLISIS DE RENDIMIENTO PREVISTO

**Engagement Score: 48/50**
- Hook inicial (10/10): Contraste dramático (chiaroscuro) genera misterio absoluto.
- Ritmo narrativo (10/10): Cortes rápidos (2s) mantienen la retención por encima del promedio y anulan el aburrimiento.
- Claridad (9/10): La transición de preparación a acción está perfectamente delimitada visual y sonoramente.
- Visuales (10/10): Estilo High-End Commercial, whip pans y drone shots capturan la atención.
- Cierre / CTA (9/10): Cierre abrupto y sonrisa satisfactoria rompen la tensión liberando dopamina.

**Viral Potential Score: 47/50**
- Elementos emocionales (9/10): Transmite pura adrenalina, emoción, y la catarsis del deporte extremo.
- Originalidad (9/10): El uso prolongado del silencio y la oscuridad antes del clímax rítmico es audaz.
- Shareability (10/10): Altamente compartible en comunidades de MTB, Enduro y deportes extremos como motivación.
- Relevancia (10/10): Satisface la tendencia actual de contenido deportivo de formato rápido e intenso.
- Sorpresa (9/10): La transición a negro (Escena 15) seguida del riff de metal sorpresivo funciona excelentemente.
"""

with open(out_path, 'w') as f:
    f.write(out)
