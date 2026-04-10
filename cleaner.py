import sys
import os
from PIL import Image
import string
import random
import pathlib

# ── ANSI styles ───────────────────────────────────────────────────────────────
RESET  = "\033[0m";  BOLD  = "\033[1m";
BLUE   = "\033[38;5;39m"

folder_input = "inputs"
folder_output = "outputs"

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

def name_generator(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

def get_image_extension(path):
    return pathlib.Path(path).suffix

def remove_data(path):
    image = Image.open(path)
    name = name_generator()
    ogExtension = get_image_extension(path)
    
    # next 3 lines strip exif
    data = list(image.get_flattened_data())
    image_without_exif = Image.new(image.mode, image.size)
    image_without_exif.putdata(data)
    
    image_without_exif.save(folder_output + '/' + name + ogExtension)

    # as a good practice, close the file handler after saving the image.
    image_without_exif.close()

def get_images():
    images = []
    valid_extensions = (".jpg", ".jpeg", ".png", ".gif", ".tiff", ".heic", ".heif", ".webp")

    for filename in os.listdir(folder_input):
        if filename.lower().endswith(valid_extensions):
            remove_data(folder_input + "/" + filename)

    print("Done!")

# ── main menu ─────────────────────────────────────────────────────────────────
def main_menu() -> None:
    print_header()
    get_images()

# ── entrypoint ────────────────────────────────────────────────────────────────
if __name__ == "__main__":
    main_menu()