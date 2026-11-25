from PIL import Image, ImageDraw

# In uploaded_media_1795622910081.jpg:
# Header logo is around x: 90 to 190, y: 30 to 130
im = Image.open(r"C:\Users\heman\Desktop\devatwal-crane-service\public\images\exact_reference_hero.jpg")
# let's find the circle:
logo_crop = im.crop((92, 34, 182, 124))
logo_crop.save(r"C:\Users\heman\Desktop\devatwal-crane-service\public\images\header_ref_logo.png")

# Let's make it a clean high-res circle with smooth transparent background
size = 180
logo_resized = logo_crop.resize((size, size), Image.Resampling.LANCZOS)
mask = Image.new('L', (size, size), 0)
draw = ImageDraw.Draw(mask)
draw.ellipse((2, 2, size - 2, size - 2), fill=255)

out = Image.new('RGBA', (size, size), (0, 0, 0, 0))
out.paste(logo_resized, (0, 0), mask=mask)
draw_out = ImageDraw.Draw(out)
draw_out.ellipse((2, 2, size - 2, size - 2), outline=(255, 255, 255, 200), width=3)
out.save(r"C:\Users\heman\Desktop\devatwal-crane-service\public\images\exact_header_logo.png")

print("Created exact_header_logo.png!")
