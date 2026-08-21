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

def optimize_image(image_path: Path, force_recompress: bool = False):
    if not force_recompress and image_path.suffix.lower() == f".{FORMAT}":
        return
    
    try:
        with Image.open(image_path) as img:
            # Convertir a RGB si es PNG con transparencia para JPG
            if img.mode in ("RGBA", "P"):
                img = img.convert("RGB")
            
            new_path = image_path.with_suffix(f".{FORMAT}")
            
            if new_path == image_path:
                # Evitar sobreescribir mientras el archivo está abierto
                temp_path = image_path.with_suffix(f".tmp_opt")
                img.save(temp_path, format="JPEG" if FORMAT == "jpg" else FORMAT.upper(), quality=QUALITY, optimize=True)
                os.replace(temp_path, new_path)
                print(f"Re-optimizado: {image_path.name} (Quality: {QUALITY}%)")
            else:
                img.save(new_path, format="JPEG" if FORMAT == "jpg" else FORMAT.upper(), quality=QUALITY, optimize=True)
                print(f"Optimizado: {image_path.name} -> {new_path.name} (Quality: {QUALITY}%)")
                
                # Eliminar el original pesado para no subirlo a git
                os.remove(image_path)
    except Exception as e:
        print(f"Error procesando {image_path}: {e}")

def main():
    parser = argparse.ArgumentParser(description="Media Architect Image Optimizer")
    parser.add_argument("target_path", type=str, help="Directorio a escanear o archivo a optimizar")
    args = parser.parse_args()

    target_path = Path(args.target_path)
    if not target_path.exists():
        print(f"Error: La ruta {target_path} no existe.")
        sys.exit(1)

    count = 0
    if target_path.is_file():
        print(f"Optimizando archivo específico: {target_path}...")
        optimize_image(target_path, force_recompress=True)
        count += 1
    elif target_path.is_dir():
        print(f"Escaneando {target_path} para optimizar imágenes...")
        for img_file in target_path.glob("*.png"):
            optimize_image(img_file)
            count += 1
    
    print(f"Proceso completado. {count} imágenes procesadas a .{FORMAT} al {QUALITY}%")

if __name__ == "__main__":
    main()
