from PIL import Image, ImageDraw

im = Image.open(r"C:\Users\heman\Desktop\devatwal-crane-service\public\images\devatwal_crane_1.jpg")
w, h = im.size

# The crane is in the center: x: 100 to 550, y: 0 to 342
# Center is x ~ 320, y ~ 170
crop_size = 320
center_x = 320
center_y = 170
box = (center_x - crop_size//2, center_y - crop_size//2, center_x + crop_size//2, center_y + crop_size//2)
crop = im.crop(box)

size = 256
crop_resized = crop.resize((size, size), Image.Resampling.LANCZOS)

# Create a clean circular emblem
mask = Image.new('L', (size, size), 0)
draw = ImageDraw.Draw(mask)
draw.ellipse((4, 4, size - 4, size - 4), fill=255)

out = Image.new('RGBA', (size, size), (0, 0, 0, 0))
out.paste(crop_resized, (0, 0), mask=mask)

draw_out = ImageDraw.Draw(out)
# Elegant, clean, professional golden-yellow circular border
draw_out.ellipse((4, 4, size - 4, size - 4), outline=(245, 158, 11, 255), width=4)

out.save(r"C:\Users\heman\Desktop\devatwal-crane-service\public\images\logo_crane_clean_circular.png")
out.save(r"C:\Users\heman\Desktop\devatwal-crane-service\public\images\exact_header_logo.png")
print("Saved clean circular logo: logo_crane_clean_circular.png and exact_header_logo.png!")
