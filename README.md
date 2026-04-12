# Cleaner

**Batch EXIF metadata remover — straight from your terminal.**

```
   ________    _________    _   ____________
  / ____/ /   / ____/   |  / | / / ____/ __ \
 / /   / /   / __/ / /| | /  |/ / __/ / /_/ /
/ /___/ /___/ /___/ ___ |/ /|  / /___/ _, _/
\____/_____/_____/_/  |_/_/ |_/_____/_/ |_|
```

---

## What it does

Cleaner scans the `inputs/` folder, strips all EXIF metadata from every image, and saves clean copies with randomised filenames into the `outputs/` folder. The original files are never modified.

**Supported formats:** JPG, JPEG, PNG, GIF, TIFF, HEIC, HEIF, WEBP

---

## Requirements

- Python 3.7+
- [Pillow](https://python-pillow.org/)

---

## Installation

```bash
git clone https://github.com/vladkotov92/cleaner.git
cd cleaner
pip install pillow
```

---

## Usage

1. Drop the images you want to clean into the `inputs/` folder.
2. Run the script:

```bash
python3 cleaner.py
```

3. Retrieve the cleaned images from the `outputs/` folder.

The script will print a per-file status and a final summary:

```
  [OK] photo1.jpg
  [OK] photo2.png
  [ERROR] corrupt.jpg: cannot identify image file

Done! 2/3 images processed.
```

> The `outputs/` folder is created automatically if it does not exist.

---

## Developer

**A Russian Boy**
GitHub: [vladkotov92](https://github.com/vladkotov92)

---

## License

MIT — see [LICENSE](LICENSE)
