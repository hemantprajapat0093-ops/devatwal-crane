from PIL import Image

im = Image.open(r"C:\Users\heman\.gemini\antigravity-cli\brain\4864e298-07a5-436c-ad5f-3371b3bb3f27\.user_uploaded\uploaded_media_1795622910081.jpg")
w, h = im.size

# Let's save a copy with a grid overlay so we know EXACT coordinates of every part of the crane!
from PIL import ImageDraw, ImageFont

grid_im = im.copy()
draw = ImageDraw.Draw(grid_im)

for x in range(0, w, 100):
    draw.line([(x, 0), (x, h)], fill=(255, 0, 0), width=1)
    draw.text((x + 2, 10), str(x), fill=(255, 255, 0))

for y in range(0, h, 100):
    draw.line([(0, y), (w, y)], fill=(0, 255, 0), width=1)
    draw.text((10, y + 2), str(y), fill=(0, 255, 255))

grid_im.save(r"C:\Users\heman\Desktop\devatwal-crane-service\public\images\crane_with_grid.jpg")
print("Saved crane_with_grid.jpg!")
