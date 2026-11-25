from PIL import Image

im = Image.open(r"C:\Users\heman\Desktop\devatwal-crane-service\public\images\exact_reference_hero.jpg")
print("Image dimensions:", im.size)

# Let's crop vertical strips to see the crane
for x_start in range(500, 1400, 150):
    box = (x_start, 0, min(x_start + 150, im.width), im.height)
    crop = im.crop(box)
    crop.save(rf"C:\Users\heman\Desktop\devatwal-crane-service\public\images\crane_pos_{x_start}.jpg")

print("Positions saved")
