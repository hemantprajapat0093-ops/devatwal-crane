from PIL import Image

im = Image.open(r"C:\Users\heman\Desktop\devatwal-crane-service\public\images\exact_reference_hero.jpg")
# Where is the slab?
# The slab is hoisted at the right top: x: 1050 to 1400, y: 150 to 400
slab_crop = im.crop((1050, 150, 1400, 400))
slab_crop.save(r"C:\Users\heman\Desktop\devatwal-crane-service\public\images\debug_slab_detail.jpg")
print("Saved debug_slab_detail.jpg")
