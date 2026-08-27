import os
import glob

# Paths to process
render_dir = "/opt/proyectos/media-architect/workspaces/neuro-viral-studio/projects/0005-curso-ia-mtb-bolivia/render"
files = glob.glob(os.path.join(render_dir, "*.md"))

old_language = "LANGUAGE: All spoken dialogue must be ONLY in neutral Latin American Spanish. Voice Style: Confident and natural female tone, energetic and clear voice that inspires action (Voz femenina joven, segura y enérgica). Do not translate, paraphrase or rewrite the provided dialogue."

new_language = """LANGUAGE: All spoken dialogue must be ONLY in neutral Latin American Spanish. Voice Style: Confident and natural 28-year-old female tone, energetic, articulate and clear voice that inspires action. Maintain exactly the same voice, pitch, and timbre across all scenes (Voz femenina joven de 28 años, segura y enérgica, mismo tono exacto). Do not translate, paraphrase or rewrite the provided dialogue.
AUDIO / SOUND FX: Include immersive background sound effects matching the scene along with the voiceover (e.g., wind, bike tires on dirt for outdoor scenes, or subtle room ambiance for indoor scenes)."""

modified_count = 0

for filepath in files:
    with open(filepath, 'r') as f:
        content = f.read()
    
    if old_language in content:
        content = content.replace(old_language, new_language)
        with open(filepath, 'w') as f:
            f.write(content)
        modified_count += 1
        print(f"Modified: {os.path.basename(filepath)}")

print(f"Total files modified: {modified_count}")
