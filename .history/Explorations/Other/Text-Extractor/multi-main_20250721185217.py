# multi_main.py

import os
import time
from pathlib import Path
from concurrent.futures import ProcessPoolExecutor, as_completed
from typing import Tuple

def ocr_image(image_path_str: str) -> Tuple[str, str]:
    """
    Process a single image file path string.
    Returns a tuple of (filename, extracted_text or error message).
    """
    import easyocr
    from pathlib import Path

    reader = easyocr.Reader(['en'], verbose=False)
    img_path = Path(image_path_str)

    try:
        result = reader.readtext(str(img_path), detail=0)
        text = "\n".join(result).strip()
        return (img_path.name, text)
    except Exception as e:
        return (img_path.name, f"[ERROR] {e}")

def main():
    # --- Setup ---
    image_dir = Path("images")
    output_file = Path("multi-output.txt")
    num_workers = 6

    # --- Determine already processed files ---
    if output_file.exists():
        with open(output_file, 'r', encoding='utf-8') as f:
            processed = set(line.strip()[3:] for line in f if line.startswith("## "))
    else:
        processed = set()

    # --- List images to process ---
    images_to_process = [
        str(p) for p in sorted(image_dir.iterdir())
        if p.is_file() and p.suffix.lower() in {".png", ".jpg", ".jpeg"}
        and p.name not in processed
    ]

    # --- Process in parallel ---
    with ProcessPoolExecutor(max_workers=num_workers) as executor:
        futures = {executor.submit(ocr_image, path): path for path in images_to_process}

        with open(output_file, 'a', encoding='utf-8') as f:
            for future in as_completed(futures):
                name, text = future.result()
                print(f"Processed: {name}")
                f.write(f"## {name}\n{text}\n\n")

if __name__ == "__main__":
    overall_start = time.time()
    main()
    overall_end = time.time()
    print(f"Total time: {overall_end - overall_start:.2f} seconds")
