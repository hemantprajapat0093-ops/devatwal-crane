from PIL import Image, ImageOps, ImageDraw

# Let's inspect devatwal_crane_1.jpg and devatwal_crane_2.jpg
im1 = Image.open('C:/Users/heman/Desktop/devatwal-crane-service/public/images/devatwal_crane_1.jpg')
print("im1 size:", im1.size)
im2 = Image.open('C:/Users/heman/Desktop/devatwal-crane-service/public/images/devatwal_crane_2.jpg')
print("im2 size:", im2.size)

# In devatwal_crane_1.jpg, let's see the bounding box of the crane
# To make a full circular logo filled with the crane:
# We crop closely around the crane, scale it so it fills a 512x512 square, and create a circular mask
w, h = im1.size
# Center crop or tight crop on crane
crop_box = (int(w * 0.05), int(h * 0.1), int(w * 0.95), int(h * 0.9))
crane_crop = im1.crop(crop_box)
crane_crop = crane_crop.resize((512, 512), Image.Resampling.LANCZOS)

# Create a circle mask
mask = Image.new('L', (512, 512), 0)
draw = ImageDraw.Draw(mask)
draw.ellipse((0, 0, 512, 512), fill=255)

# Put into RGBA
circle_logo = Image.new('RGBA', (512, 512), (0, 0, 0, 0))
circle_logo.paste(crane_crop, (0, 0), mask=mask)
circle_logo.save('C:/Users/heman/Desktop/devatwal-crane-service/public/images/logo_crane_circle_fill.png', format='PNG')

print("Created logo_crane_circle_fill.png successfully!")
