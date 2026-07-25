import os
import sys
import argparse
from pathlib import Path
from PIL import Image
from dotenv import load_dotenv

# Cargar variables de entorno desde la raíz del proyecto
root_dir = Path(__file__).parent.parent
load_dotenv(root_dir / ".env")

FORMAT = os.getenv("IMAGE_COMPRESSION_FORMAT", "jpg").lower()
QUALITY = int(os.getenv("IMAGE_COMPRESSION_QUALITY", "95"))

def optimize_image(image_path: Path):
    if image_path.suffix.lower() == f".{FORMAT}":
        return
    
    try:
        with Image.open(image_path) as img:
            # Convertir a RGB si es PNG con transparencia para JPG
            if img.mode in ("RGBA", "P"):
                img = img.convert("RGB")
            
            new_path = image_path.with_suffix(f".{FORMAT}")
            img.save(new_path, format="JPEG" if FORMAT == "jpg" else FORMAT.upper(), quality=QUALITY, optimize=True)
            print(f"Optimizado: {image_path.name} -> {new_path.name} (Quality: {QUALITY}%)")
            
            # Eliminar el original pesado para no subirlo a git
            os.remove(image_path)
    except Exception as e:
        print(f"Error procesando {image_path}: {e}")

def main():
    parser = argparse.ArgumentParser(description="Media Architect Image Optimizer")
    parser.add_argument("target_dir", type=str, help="Directorio a escanear")
    args = parser.parse_args()

    target_path = Path(args.target_dir)
    if not target_path.exists() or not target_path.is_dir():
        print(f"Error: El directorio {target_path} no existe.")
        sys.exit(1)

    print(f"Escaneando {target_path} para optimizar imágenes...")
    count = 0
    for img_file in target_path.glob("*.png"):
        optimize_image(img_file)
        count += 1
    
    print(f"Proceso completado. {count} imágenes optimizadas a .{FORMAT} al {QUALITY}%")

if __name__ == "__main__":
    main()
