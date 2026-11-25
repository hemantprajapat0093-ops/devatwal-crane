from PIL import Image

im = Image.open(r"C:\Users\heman\Desktop\devatwal-crane-service\public\images\hero_crane_featured_large.jpg")
print("hero_crane_featured_large size:", im.size)
im.crop((0, 0, 400, 300)).save(r"C:\Users\heman\Desktop\devatwal-crane-service\public\images\feat_crop.jpg")
print("Saved feat_crop.jpg")
