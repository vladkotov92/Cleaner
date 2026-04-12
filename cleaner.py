import os
import string
import random
from pathlib import Path
from PIL import Image

# ── ANSI styles ───────────────────────────────────────────────────────────────
RESET  = "\033[0m";  BOLD  = "\033[1m";
BLUE   = "\033[38;5;39m"

folder_input  = Path("inputs")
folder_output = Path("outputs")

VALID_EXTENSIONS = (".jpg", ".jpeg", ".png", ".gif", ".tiff", ".heic", ".heif", ".webp")

def print_header() -> None:
    clear_screen()
    print(f"{BLUE}{BOLD}")
    print(r"""
   ________    _________    _   ____________
  / ____/ /   / ____/   |  / | / / ____/ __ \
 / /   / /   / __/ / /| | /  |/ / __/ / /_/ /
/ /___/ /___/ /___/ ___ |/ /|  / /___/ _, _/
\____/_____/_____/_/  |_/_/ |_/_____/_/ |_|

                     Developer: A Russian Boy
    """)
    print(f"{RESET}{BOLD}")
    print("* GitHub: https://github.com/vladkotov92")
    print()

def clear_screen() -> None:
    os.system("clear")

def name_generator(size=10, chars=string.ascii_uppercase + string.digits) -> str:
    return ''.join(random.choice(chars) for _ in range(size))

def remove_data(path: Path) -> None:
    with Image.open(path) as image:
        data = list(image.getdata())
        image_without_exif = Image.new(image.mode, image.size)
        image_without_exif.putdata(data)
        output_path = folder_output / (name_generator() + path.suffix)
        image_without_exif.save(output_path)

def process_images() -> None:
    if not folder_input.exists():
        print(f"Error: folder '{folder_input}' does not exist.")
        return

    folder_output.mkdir(parents=True, exist_ok=True)

    images = [f for f in folder_input.iterdir() if f.suffix.lower() in VALID_EXTENSIONS]

    if not images:
        print("No images found in the inputs folder.")
        return

    ok = 0
    for image_path in images:
        try:
            remove_data(image_path)
            print(f"  [OK] {image_path.name}")
            ok += 1
        except Exception as e:
            print(f"  [ERROR] {image_path.name}: {e}")

    print(f"\nDone! {ok}/{len(images)} images processed.")

# ── entrypoint ────────────────────────────────────────────────────────────────
def main() -> None:
    print_header()
    process_images()

if __name__ == "__main__":
    main()