from PIL import Image
import os

src = "weather/static/images/pinkcloud.png"
out = "weather/static/images/icons"
os.makedirs(out, exist_ok=True)

img = Image.open(src).convert("RGBA")
side = max(img.size)
canvas = Image.new("RGBA", (side, side), (0, 0, 0, 0))
canvas.paste(img, ((side - img.width) // 2, (side - img.height) // 2))

for s in (192, 512):
    canvas.resize((s, s), Image.LANCZOS).save(f"{out}/icon-{s}.png")