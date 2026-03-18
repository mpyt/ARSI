import cv2
import json
import numpy as np
import os
import glob


def mask_polygons(image_path, json_path, output_dir, color=(0, 0, 0), output_suffix="_masked"):

    img_array = np.fromfile(image_path, dtype=np.uint8)
    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
    if img is None:
        print(f"  Nelze načíst obrázek: {image_path}")
        return False

    with open(json_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    for shape in data["shapes"]:
        points = np.array(shape["points"], dtype=np.int32)
        cv2.fillPoly(img, [points], color)

    name, ext = os.path.splitext(os.path.basename(image_path))
    output_path = os.path.join(output_dir, f"{name}{output_suffix}{ext}")
    success, encoded = cv2.imencode(ext, img)
    if success:
        encoded.tofile(output_path)
        return True
    return False


def process_input(input_path, json_path, output_dir, color=(0, 0, 0), output_suffix="_masked"):
    os.makedirs(output_dir, exist_ok=True)
    extensions = ("*.jpg", "*.jpeg", "*.png", "*.bmp")

    # Jeden soubor
    if os.path.isfile(input_path):
        print(f"Zpracovávám soubor: {input_path}")
        if mask_polygons(input_path, json_path, output_dir, color, output_suffix):
            print(f"Hotovo! Výstup v '{output_dir}'")
        return

    # Složka
    if os.path.isdir(input_path):
        files = []
        for ext in extensions:
            files.extend(glob.glob(os.path.join(input_path, ext)))
        files.sort()

        if not files:
            print(f"Ve složce '{input_path}' nebyly nalezeny žádné obrázky.")
            return

        print(f"Nalezeno {len(files)} obrázků ve složce '{input_path}'")
        saved = 0
        for i, file_path in enumerate(files, 1):
            print(f"  [{i}/{len(files)}] {os.path.basename(file_path)}", end="")
            if mask_polygons(file_path, json_path, output_dir, color, output_suffix):
                saved += 1
                print(" ✓")
            else:
                print(" ✗")

        print(f"Hotovo! Úspěšně zpracováno {saved}/{len(files)} do '{output_dir}'")
        return

    print(f"Cesta neexistuje: {input_path}")


if __name__ == "__main__":
    INPUT_PATH = r"C:\Users\micha\Desktop\VŠB\Projekty\ARSI\photo_samples\1762-1"          # Cesta k obrázku NEBO složce
    JSON_PATH = r"C:\Users\micha\Desktop\VŠB\Projekty\ARSI\photo_samples\maska_mustr.json"       # Cesta k LabelMe JSON
    OUTPUT_DIR = r"C:\Users\micha\Desktop\VŠB\Projekty\ARSI\photo_samples\test"   # Výstupní složka
    COLOR = (0, 0, 0)                    # Černá (BGR)
    OUTPUT_SUFFIX = "_masked"            # Přípona výstupních souborů

    process_input(INPUT_PATH, JSON_PATH, OUTPUT_DIR, COLOR, OUTPUT_SUFFIX)