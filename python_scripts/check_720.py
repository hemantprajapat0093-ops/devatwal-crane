from PIL import Image

im = Image.open(r"C:\Users\heman\Desktop\devatwal-crane-service\public\images\exact_reference_hero.jpg")
im.crop((720, 260, 870, 460)).save(r"C:\Users\heman\Desktop\devatwal-crane-service\public\images\crop_720_870.jpg")
print("Saved crop_720_870.jpg")
