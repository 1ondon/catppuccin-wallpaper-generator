from PIL import Image

# Catppuccin flavors
flavors = ["Latte", "Frappe", "Macchiato", "Mocha"]

# Background colors
backgrounds = [
    "#eff1f5",
    "#303446",
    "#24273a",
    "#1e1e2e"
]

# Flavor menu
print("Select a flavor:")

i = 0
while i < len(flavors):
    print(f"{i + 1}. {flavors[i]}")
    i += 1

flavorChoice = input("Select a flavor (1-4): ")

if flavorChoice not in ["1", "2", "3", "4"]:
    print("Invalid flavor!")
    raise SystemExit

flavorIndex = int(flavorChoice) - 1

backgroundColor = backgrounds[flavorIndex]

# Aspect ratio menu
aspectRatios = ["16:9", "21:9", "9:19.5"]

sizes = [
    [1920, 1080],
    [2560, 1080],
    [1320, 2868]
]

print("\nSelect an aspect ratio:")

i = 0
while i < len(aspectRatios):
    print(f"{i + 1}. {aspectRatios[i]}")
    i += 1

ratioChoice = input("Select an aspect ratio (1-3): ")

if ratioChoice not in ["1", "2", "3"]:
    print("Invalid aspect ratio!")
    raise SystemExit

ratio = sizes[int(ratioChoice) - 1]

# Create wallpaper
image = Image.new("RGBA", (ratio[0], ratio[1]), color=backgroundColor)

# Load cat logo (run this from the project root)
try:
    cat = Image.open("assets/1544x1544_circle.png").convert("RGBA")
except FileNotFoundError:
    print("Logo not found! Run this from the project root.")
    raise SystemExit

# Resize logo
catSize = int(ratio[1] * 0.17)
cat.thumbnail((catSize, catSize), Image.Resampling.LANCZOS)

# Center logo
x = (ratio[0] - cat.width) // 2
y = (ratio[1] - cat.height) // 2

image.alpha_composite(cat, (x, y))

# Save wallpaper (the output folder must already exist)
image.convert("RGB").save("output/background.png")

print("\nWallpaper created!")
print("Flavor:", flavors[flavorIndex])
print("Resolution:", ratio[0], "x", ratio[1])
print("Saved to: output/background.png")