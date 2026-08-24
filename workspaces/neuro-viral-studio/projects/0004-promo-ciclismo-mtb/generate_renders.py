import os

render_dir = "/opt/publicidad/media-architect/workspaces/neuro-viral-studio/projects/0004-promo-ciclismo-mtb/render"
os.makedirs(render_dir, exist_ok=True)

char_base = "Adult male in his late 30s, slightly bronzed skin, short dark hair, wearing clean high-end Cross-Country MTB cycling gear: tight dark cycling maillot, black MTB shorts, tall black socks, knee pads, sports gloves, and MTB cycling shoes. Clean clothes, no dirt. He is NOT wearing a helmet. Mouth strictly closed, serious and silent."
char_helmet = "Adult male in his late 30s, slightly bronzed skin, short dark hair, wearing clean high-end Cross-Country MTB cycling gear: tight dark cycling maillot, black MTB shorts, tall black socks, knee pads, sports gloves, and MTB cycling shoes. He is wearing a professional MTB helmet and cycling sunglasses. Clean clothes, no dirt. Mouth strictly closed, serious and silent."

style = "Hyper-realistic cinematic video, vertical 9:16"
safety = "FLOW SAFETY: fictional adults only, safe nonviolent context, respectful natural behavior, no recognizable people, minors, brands, logos, protected characters or readable text."
negative = "NEGATIVE PROMPT: No logos, no text, no letters, no words, no UI elements, no split screens, no mutations, no deformed bikes, no floating faces, no speaking, no talking, no open mouth, no moving lips."

scenes = [
    (1, 2, f"INT. GARAGE. Wide shot. Chiaroscuro lighting. A mountain bike is in the center foreground. The cyclist ({char_helmet}) approaches from the dark background, walking towards the bike, and reaches out to touch the handlebars.", "Static shot or slow creep in."),
    (2, 2, "INT. GARAGE. Close up. A high-end mountain bike illuminated by dramatic top lighting in the dark.", "Slow push-in while the camera orbits smoothly around the bicycle to reveal its details."),
    (3, 3, f"INT. GARAGE. Extreme close up on hands. The cyclist ({char_base}) is putting on his sports gloves, getting ready.", "Zoom in to the hands getting ready."),
    (4, 2, f"INT. GARAGE. Extreme close up of the cyclist ({char_base}) zipping up his cycling jersey.", "Macro detail shot."),
    (5, 3, f"INT. GARAGE. Close up. The cyclist ({char_base}) puts on a professional MTB helmet.", "Dynamic close up."),
    (6, 2, f"INT. GARAGE. Extreme close up of the cyclist's ({char_helmet}) knee, adjusting the fabric of the shorts.", "Macro detail shot."),
    (7, 2, f"INT. GARAGE. Close up of hands with sports gloves adjusting the shorts fabric.", "Macro detail shot."),
    (8, 2, f"INT. GARAGE. Side silhouette of the cyclist's ({char_helmet}) head looking down. Mystery.", "Static silhouette."),
    (9, 2, "INT. GARAGE. Extreme close up of the mountain bike rear derailleur and cassette.", "Static macro."),
    (10, 2, "INT. GARAGE. Extreme close up of the bicycle chain links spinning.", "Slow motion 60fps macro."),
    (11, 2, "INT. GARAGE. Extreme close up of the bicycle rear suspension moving.", "Macro detail."),
    (12, 2, f"INT. GARAGE. Close up of the cyclist ({char_helmet}) buckling the helmet strap under his chin.", "Tight close up."),
    (13, 2, f"INT. GARAGE. Wide shot. The cyclist ({char_helmet}) lifts the bicycle and tilts it forward.", "Whip pan or dynamic follow."),
    (14, 2, "INT. GARAGE. Extreme close up of the front fork moving towards the exit.", "Follow focus."),
    (15, 2, "TRANSITION. Pitch black frame.", "Absolute black frame."),
    (16, 3, f"EXT. MOUNTAIN. High drone shot. The cyclist ({char_helmet}) pedaling fast on a curved dirt trail.", "Drone tracking shot."),
    (17, 2, f"EXT. TRAIL. Tracking shot from the side. The cyclist ({char_helmet}) accelerating on a narrow trail.", "Fast side tracking."),
    (18, 2, f"EXT. FOREST. Low front tracking shot. The cyclist ({char_helmet}) riding directly toward the camera between trees.", "Fast pullback tracking."),
    (19, 2, "EXT. PUDDLE. Extreme close up of a mountain bike rear tire splashing muddy water.", "Slow motion 60fps."),
    (20, 2, f"EXT. ROCKS. Low angle. The cyclist ({char_helmet}) jumps down a small rock step.", "Low angle follow."),
    (21, 2, f"EXT. DENSE FOREST. Rear tracking shot. The cyclist ({char_helmet}) maneuvering tight corners between pine trees.", "Fast rear tracking."),
    (22, 2, f"EXT. MOUNTAIN. Low angle front shot. The cyclist ({char_helmet}) pedaling furiously while standing up on the pedals.", "Aggressive handheld tracking."),
    (23, 2, "EXT. TRAIL. Extreme close up of a cycling shoe and pedal spinning rapidly.", "Macro follow."),
    (24, 2, f"EXT. TRAIL. Rear shot. The cyclist ({char_helmet}) skids aggressively, kicking up a dust cloud.", "Fixed camera on the ground."),
    (25, 2, f"EXT. CORNER. The cyclist ({char_helmet}) taking a berm corner at high speed.", "Fast whip pan following the cyclist."),
    (26, 2, f"EXT. OPEN MOUNTAIN. The cyclist ({char_helmet}) on a fast straight section.", "Drone tracking shot from behind."),
    (27, 2, f"EXT. DROP. Low angle shot. The cyclist ({char_helmet}) jumps directly over the camera lens.", "Static low angle."),
    (28, 2, f"EXT. FOREST. Front shot. The cyclist ({char_helmet}) dodges branches, leaning hard to the left.", "Front tracking shot."),
    (29, 3, f"EXT. RIDGE. Wide drone shot. The cyclist ({char_helmet}) riding along a mountain ridge with a cloudy sky.", "Slow drone tracking."),
    (30, 2, f"EXT. ROCK GARDEN. Side shot of the bicycle. The suspension is working furiously.", "Handheld shaky cam."),
    (31, 2, "EXT. TRAIL. Close up of firm hands gripping the handlebars over rough terrain.", "Handheld action."),
    (32, 2, f"EXT. TIGHT CORNER. Front shot. The cyclist ({char_helmet}) skids and dirt flies directly into the camera lens.", "Impact shot."),
    (33, 2, f"EXT. MOUNTAIN. Side tracking shot, the bicycle gaining massive speed downhill.", "Fast side tracking."),
    (34, 2, f"EXT. FOREST. Medium shot. The cyclist ({char_helmet}) emerges from behind a large pine tree at full speed.", "Static ambush shot."),
    (35, 2, "EXT. NARROW TRAIL. First-person POV from the chest or helmet showing trees rushing by.", "Aggressive POV action."),
    (36, 2, "EXT. HILL. Low rear shot. The rear wheel kicks up a small rock.", "Low angle macro action."),
    (37, 2, f"EXT. FLAT. Side shot. The cyclist ({char_helmet}) does a small manual wheelie.", "Slow motion 60fps tracking."),
    (38, 2, f"EXT. FOREST ZONE. The cyclist ({char_helmet}) rides toward the camera.", "Drone flying backward fast."),
    (39, 2, f"EXT. FINISH LINE. The cyclist ({char_helmet}) brakes hard, skidding to reduce speed.", "Wide side shot."),
    (40, 3, f"EXT. FINISH LINE. Medium close up. The cyclist ({char_base}) stops, breathing heavily. He has just removed his helmet, showing a huge sweaty smile.", "Handheld cinematic."),
    (41, 3, "OUTRO. BLACK SCREEN. Pure black background.", "Static black screen.")
]

for (num, dur, vis, cam) in scenes:
    image_filename = os.path.join(render_dir, f"scene_{num:03d}_image.md")
    video_filename = os.path.join(render_dir, f"scene_{num:03d}_video.md")
    
    if num == 1 or (num >= 5 and num != 40 and num != 41 and num != 15):
        char_desc = char_helmet
    elif num in [2, 9, 10, 11, 14, 15, 19, 23, 41]:
        char_desc = ""
    else:
        char_desc = char_base

    # Image prompt
    with open(image_filename, 'w') as f:
        f.write(f"""---
platform: tiktok_shorts
model: midjourney
---
**SCENE {num:03d} - IMAGE PROMPT**
Cinematic High-End Commercial style. 
{vis}
{char_desc}
CRITICAL: No text, no letters, no UI elements. No split screens.
{negative}
""")

    # Video prompt
    with open(video_filename, 'w') as f:
        f.write(f"""---
platform: tiktok_shorts
model: google_flow_veo
---
**SCENE {num:03d} - VIDEO PROMPT**
{style}, exact duration {dur} seconds. Cinematic High-End Commercial style. {vis}
CAMERA / TIMING: {cam}
CRITICAL: The character must NOT speak under any circumstance. His mouth is completely closed and sealed. Silent action only.
{safety}
{negative}
""")

print("All 41 scenes generated perfectly in render/ using the new media-render standard.")
