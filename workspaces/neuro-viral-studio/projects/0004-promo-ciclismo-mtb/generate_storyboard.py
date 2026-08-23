import re

script_content = """# MASTER SCRIPT - Promo Ciclismo Enduro y MTB (Replica)

**Reparto (Lore):** none
**Locación:** Garaje oscuro (Intro) / Senderos de Montaña y Bosque (Acción)

| Escena | T | Visual (Acción + Cámara + Estilo) | Audio (Diálogo + SFX + Música) |
| --- | --- | --- | --- |
| 1 | 0:02 | INT. GARAJE - DÍA. Plano general. Iluminación Chiaroscuro. Silueta de la bicicleta de montaña en la oscuridad. | [Música] Inicia intro de rock alternativo con bajo marcando el pulso. |
| 2 | 0:02 | INT. GARAJE. Plano medio. El ciclista aparece de pie junto a su bicicleta. Iluminación dramática desde arriba. | [Música] Pulso constante. |
| 3 | 0:03 | INT. GARAJE. Plano detalle extremo (ECU) al logo "OLYMPIA" en el marco de la bicicleta. Alto contraste. | [Música] La batería comienza a subir. |
| 4 | 0:02 | INT. GARAJE. Plano detalle del ciclista ajustándose el cierre del jersey de ciclismo. | [SFX] Sonido nítido de cremallera. |
| 5 | 0:03 | INT. GARAJE. Plano cerrado. El ciclista se pone un casco integral verde Fox. | [SFX] Ajuste plástico del casco. |
| 6 | 0:02 | INT. GARAJE. Plano detalle de la rodilla del ciclista; la tela del short se ajusta. | [Música] Sube la tensión. |
| 7 | 0:02 | INT. GARAJE. Plano cerrado a las manos ajustando la tela del short y guantes. | [SFX] Roce de tela sintética. |
| 8 | 0:02 | INT. GARAJE. Silueta lateral de la cabeza del ciclista mirando hacia abajo. Misterio. | [Música] Platillos en crescendo. |
| 9 | 0:02 | INT. GARAJE. Plano detalle del desviador trasero y los piñones (cassette). | [SFX] Clic metálico de engranajes. |
| 10 | 0:02 | INT. GARAJE. Plano detalle extremo a los eslabones de la cadena en cámara lenta. | [SFX] Cadena girando suavemente. |
| 11 | 0:02 | INT. GARAJE. Plano detalle de la suspensión trasera del cuadro. | [Música] Tensión máxima. |
| 12 | 0:02 | INT. GARAJE. Plano cerrado del ciclista abrochando la correa de su casco bajo la barbilla. | [SFX] "Clic" fuerte de la hebilla. |
| 13 | 0:02 | INT. GARAJE. Plano general. El ciclista levanta la bicicleta y la inclina hacia adelante. | [Música] Batería rompe. |
| 14 | 0:02 | INT. GARAJE. Plano detalle de la horquilla delantera moviéndose hacia la salida. | [Música] Pausa dramática en el track. |
| 15 | 0:02 | TRANSICIÓN. Corte abrupto a negro absoluto. | [Silencio] Medio segundo de vacío sonoro. |
| 16 | 0:03 | EXT. MONTAÑA. Toma de dron alta. El ciclista pedaleando rápido en un sendero de tierra curvo. | [Música] Explota el riff principal de rock pesado. |
| 17 | 0:02 | EXT. SENDERO. Toma lateral de seguimiento (Tracking shot) del ciclista acelerando por un sendero estrecho. | [SFX] Neumáticos triturando grava. |
| 18 | 0:02 | EXT. BOSQUE. Toma frontal baja, el ciclista corriendo directamente hacia la cámara entre árboles. | [SFX] Viento y cadena botando. |
| 19 | 0:02 | EXT. CHARCO. Plano detalle en cámara lenta (60fps) de la llanta trasera salpicando agua fangosa. | [SFX] Agua salpicando ("Splash"). |
| 20 | 0:02 | EXT. ROCAS. Toma desde abajo. El ciclista hace un pequeño salto bajando un escalón de piedra. | [SFX] Impacto seco de llanta contra roca. |
| 21 | 0:02 | EXT. BOSQUE DENSO. Toma de seguimiento trasero. Ciclista maniobrando curvas cerradas entre pinos. | [Música] Guitarra eléctrica intensa. |
| 22 | 0:02 | EXT. MONTAÑA. Toma frontal baja (Low Angle). El ciclista pedalea con furia de pie sobre los pedales. | [SFX] Respiración agitada mezclada en el track. |
| 23 | 0:02 | EXT. SENDERO. Plano detalle de la bota y el pedal girando rápidamente. | [Música] Rápida. |
| 24 | 0:02 | EXT. SENDERO. Toma trasera. El ciclista hace un derrape (skid) levantando una nube de polvo. | [SFX] Derrape fuerte sobre tierra seca. |
| 25 | 0:02 | EXT. CURVA. Toma lateral, látigo rápido (Whip Pan) siguiendo al ciclista mientras toma una curva con peralte. | [SFX] Zumbido "Whoosh" en el paneo. |
| 26 | 0:02 | EXT. MONTAÑA ABIERTA. Toma de dron desde atrás siguiendo al ciclista en un tramo recto rápido. | [Música] Sube de intensidad. |
| 27 | 0:02 | EXT. DESNIVEL. Toma baja contrapicada. El ciclista salta pasando literalmente por encima del lente. | [SFX] Viento cortado. |
| 28 | 0:02 | EXT. BOSQUE. Toma frontal, el ciclista esquiva ramas y se inclina fuertemente hacia la izquierda. | [Música] Guitarra. |
| 29 | 0:03 | EXT. CRESTA. Toma de dron lejana. Ciclista surcando una cresta de montaña con cielo nublado al fondo. | [Música] Épico, expansivo. |
| 30 | 0:02 | EXT. SENDEROS DE ROCA. Toma lateral cámara en mano (shaky). La suspensión trabaja furiosamente. | [SFX] Golpes de amortiguador y chasis. |
| 31 | 0:02 | EXT. SENDERO. Plano cerrado a las manos firmes sujetando el manillar sobre terreno irregular. | [Música] Continúa rápida. |
| 32 | 0:02 | EXT. CURVA CERRADA. Plano frontal. El ciclista derrapa y la tierra vuela directamente a cámara. | [SFX] Impacto de tierra. |
| 33 | 0:02 | EXT. MONTAÑA. Toma de seguimiento lateral, la bicicleta gana gran velocidad en bajada pura. | [Música] Acercándose al final del riff. |
| 34 | 0:02 | EXT. BOSQUE. Plano medio. El ciclista asoma por detrás de un gran pino a toda velocidad. | [Música] Rápida. |
| 35 | 0:02 | EXT. SENDERO ESTRECHO. Cámara subjetiva (POV) pecho/casco mostrando el rápido paso de los árboles. | [SFX] Viento fuerte contra el micrófono. |
| 36 | 0:02 | EXT. COLINA. Toma trasera baja. La rueda trasera levanta una piedra pequeña. | [SFX] Rocas saltando. |
| 37 | 0:02 | EXT. PLANICIE. Toma lateral en cámara lenta. El ciclista hace un pequeño manual (caballito). | [Música] Se ralentiza para el clímax. |
| 38 | 0:02 | EXT. ZONA BOSCOSA. Toma de dron retrocediendo rápido mientras el ciclista avanza hacia ella. | [Música] Clímax inminente. |
| 39 | 0:02 | EXT. META (ZONA ABIERTA). El ciclista reduce la velocidad drásticamente derrapando. | [SFX] Frenada larga de disco. |
| 40 | 0:03 | EXT. META. Plano medio cerrado. El ciclista se detiene, respirando agitado. Retira el casco mostrando una gran sonrisa. Sudado. | [Música] Desvanece el rock pesado. |
| 41 | 0:03 | PANTALLA NEGRA. Aparece el logotipo en blanco "Cristian Alvero" en el centro. | [SFX] Reverberación final de guitarra desvaneciéndose. |
"""

lines = script_content.strip().split('\n')
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

out = "# STORYBOARD - Promo Ciclismo Enduro y MTB (Replica)\n\n"
out += "**Reparto (Lore):** none\n\n"

for i in range(0, len(scenes), 6):
    chunk = scenes[i:i+6]
    start = i + 1
    end = min(i + 6, len(scenes))
    out += f"## Bloque Escenas {start}-{end}\n\n"
    
    # Prompt
    out += f"*PROMPT:*\n"
    out += f"*High-End Commercial, action sports MTB, dynamic fast cuts, cinematic chiaroscuro for intro, bright daylight for trail. A {len(chunk)}-panel comic-style storyboard layout. The images should depict generic mountain biker, no specific face.\n"
    for idx, s in enumerate(chunk):
        out += f"Panel {idx+1}: {s['vis']}\n"
    out += "CRITICAL: Do not include any text, letters, subtitles, words, or speech bubbles anywhere in the image. The image must be completely free of typography.*\n\n"
    
    out += f"![Storyboard](assets/board_{start:02d}_{end:02d}.jpg)\n\n"
    
    for s in chunk:
        plano = "General" if "general" in s['vis'].lower() else ("Detalle" if "detalle" in s['vis'].lower() else "Medio")
        ilum = "Chiaroscuro" if "INT. GARAJE" in s['vis'] else "Luz de día"
        
        out += f"### Toma {s['num']} (Escena {s['num']})\n"
        out += f"- **Toma:** {s['num']}\n"
        out += f"- **Thumbnail (Visual):** {s['vis']}\n"
        out += f"- **Acción/Narrativa:** {s['vis']}\n"
        out += f"- **Cámara y Fotografía:**\n"
        out += f"  - **Plano:** {plano}\n"
        out += f"  - **Movimiento de cámara:** Dinámico\n"
        out += f"  - **Iluminación:** {ilum}\n"
        out += f"  - **Color Grading:** Alto contraste\n"
        out += f"- **Duración:** {s['dur']}\n"
        out += f"- **Audio/Voz en Off:** \"{s['aud']}\"\n"
        out += f"- **Transición:** Hard Cut\n\n"

with open('/opt/publicidad/media-architect/workspaces/neuro-viral-studio/projects/0004-promo-ciclismo-mtb/storyboard/storyboard.md', 'w') as f:
    f.write(out)
