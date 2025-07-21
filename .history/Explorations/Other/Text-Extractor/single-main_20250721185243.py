# single_main.py

import os
import time
from pathlib import Path
import easyocr

def main():
    # --- Setup paths ---
    image_dir = Path("images")
    output_file = Path("single-output.txt")

    # --- Initialize easyocr.Reader ---
    reader = easyocr.Reader(['en'], verbose=False)

    # --- Determine already processed files ---
    if output_file.exists():
        with open(output_file, 'r', encoding='utf-8') as f:
            processed = set(line.strip()[3:] for line in f if line.startswith("## "))
    else:
        processed = set()

    # --- Start timer ---
    start_time = time.time()

    # --- Process images sequentially ---
    with open(output_file, 'a', encoding='utf-8') as f:
        for img_path in sorted(image_dir.iterdir()):
            if not img_path.is_file() or img_path.suffix.lower() not in {'.png', '.jpg', '.jpeg'}:
                continue
            if img_path.name in processed:
                print(f"Skipping {img_path.name} (already processed)")
                continue

            print(f"Processing {img_path.name}...")
            try:
                result = reader.readtext(str(img_path), detail=0)
                text = "\n".join(result).strip()

                f.write(f"## {img_path.name}\n{text}\n\n")
            except Exception as e:
                print(f"Error processing {img_path.name}: {e}")
                f.write(f"## {img_path.name}\n[ERROR] {e}\n\n")

    # --- Finish ---
    end_time = time.time()
    print(f"Total time: {end_time - start_time:.2f} seconds")

if __name__ == "__main__":
    overall_start = time.time()
    main()
    overall_end = time.time()
    print(f"Total time: {overall_end - overall_start:.2f} seconds")
