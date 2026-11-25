from PIL import Image, ImageEnhance, ImageDraw, ImageFilter

im = Image.open('C:/Users/heman/Desktop/devatwal-crane-service/public/images/devatwal_crane_1.jpg')
# Enhance color vibrancy and sharpness
enhancer = ImageEnhance.Color(im)
im = enhancer.enhance(1.25)
enhancer = ImageEnhance.Sharpness(im)
im = enhancer.enhance(1.3)
enhancer = ImageEnhance.Contrast(im)
im = enhancer.enhance(1.15)

# Tight center crop on the yellow crane body and boom
w, h = im.size
# Crop to square centered on crane
size = min(w, h)
left = int((w - size) * 0.45)
top = int((h - size) * 0.5)
square_crop = im.crop((left, 0, left + h, h))
square_crop = square_crop.resize((600, 600), Image.Resampling.LANCZOS)

# Create circular mask
mask = Image.new('L', (600, 600), 0)
draw = ImageDraw.Draw(mask)
draw.ellipse((4, 4, 596, 596), fill=255)

# Save high-res circular logo
output = Image.new('RGBA', (600, 600), (0, 0, 0, 0))
output.paste(square_crop, (0, 0), mask=mask)

# Add a vibrant glowing gold border to the circular image directly
border_draw = ImageDraw.Draw(output)
border_draw.ellipse((4, 4, 596, 596), outline=(245, 158, 11, 255), width=8)

output.save('C:/Users/heman/Desktop/devatwal-crane-service/public/images/logo_crane_full_circle.png', format='PNG')
print("Successfully created logo_crane_full_circle.png!")
