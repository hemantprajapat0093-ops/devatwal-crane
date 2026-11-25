from PIL import Image

im = Image.open(r"C:\Users\heman\Desktop\devatwal-crane-service\public\images\exact_reference_hero.jpg")
w, h = im.size

# Let's crop:
# 1. The crane cabin
# 2. The lifted concrete slab
# 3. The ground / tires
# 4. Where the yellow text "Go Futer." was located
crop_text = im.crop((400, 200, 850, 400))
crop_text.save(r"C:\Users\heman\Desktop\devatwal-crane-service\public\images\debug_text_gofuter.jpg")

# Where is the cabin?
crop_cabin = im.crop((550, 400, 750, 650))
crop_cabin.save(r"C:\Users\heman\Desktop\devatwal-crane-service\public\images\debug_cabin.jpg")

print("Saved debug_text_gofuter.jpg and debug_cabin.jpg")
