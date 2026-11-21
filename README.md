# Catppuccin Wallpaper Generator

A small Python script that generates a minimalist [Catppuccin](https://github.com/catppuccin/catppuccin)
wallpaper:

## Features

- All four flavors: Latte, Frappé, Macchiato, Mocha
- Three resolutions: 16:9, 21:9, and 9:19.5 (phone)
- Logo scaled and centered automatically

## Requirements

- Python 3.9+
- [Pillow](https://python-pillow.org/)

## Setup

```bash
git clone 
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Usage

```bash
python3 src/main.py   # run from the project root
```

Pick a flavor and an aspect ratio when prompted. The wallpaper is saved to
`output/background.png` (overwritten on each run).

## Project structure

```
.
├── assets/        # Catppuccin logo used on the wallpaper
├── output/        # Generated wallpapers
├── src/main.py    # The generator
└── requirements.txt
```

## Customizing

Edit the constants at the top of `src/main.py`:

- `FLAVORS`: background color per flavor
- `RESOLUTIONS`: add or change output sizes
- `LOGO_HEIGHT_RATIO`: how large the logo is relative to wallpaper height

## Credits

Colors and logo are from [Catppuccin](https://github.com/catppuccin/catppuccin),
which is MIT licensed.
