from PIL import Image, ImageDraw

im = Image.open(r"C:\Users\heman\Desktop\devatwal-crane-service\public\images\exact_reference_hero.jpg")
w, h = im.size
print(f"Image dimensions: {w}x{h}")

# The right side from x=520 to w has the crane, building, sunset, and "Your Trusted Crane Partner"
# The left side from x=0 to 520 has the text overlaid on a dark blue/navy gradient.
# Let's see: what if we take the background from x=0 to 520 and make it a clean dark gradient?
# Let's inspect the colors on the left side:
# At x=0, y=200: dark blue
# At x=0, y=500: dark blue / black
# We can create a version of the image where the left side (0 to 550) has a smooth dark blue gradient that fades into the crane scene at x=550!
bg_clean = im.copy()
draw = ImageDraw.Draw(bg_clean)

# Let's sample colors:
# Top left (x=0, y=0): deep dark navy #070d18
# Mid left (x=0, y=350): #0a1329
# Bottom left (x=0, y=689): #060b14

# Let's create a gradient overlay mask on the left from x=0 to 580
overlay = Image.new('RGBA', (w, h), (0, 0, 0, 0))
for x in range(580):
    # Alpha goes from 1.0 at x=0 to 0.0 at x=550
    alpha = max(0, min(255, int(255 * (1.0 - (x / 550) ** 1.5))))
    for y in range(h):
        # subtle vertical gradient
        y_ratio = y / h
        r = int(7 * (1 - y_ratio) + 4 * y_ratio)
        g = int(14 * (1 - y_ratio) + 8 * y_ratio)
        b = int(28 * (1 - y_ratio) + 16 * y_ratio)
        overlay.putpixel((x, y), (r, g, b, alpha))

bg_composite = Image.alpha_composite(im.convert('RGBA'), overlay)
bg_composite.convert('RGB').save(r"C:\Users\heman\Desktop\devatwal-crane-service\public\images\hero_bg_clean.jpg", quality=95)
print("Created hero_bg_clean.jpg successfully!")
