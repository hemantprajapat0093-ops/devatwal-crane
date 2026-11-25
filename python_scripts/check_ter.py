from PIL import Image

im = Image.open(r"C:\Users\heman\Desktop\devatwal-crane-service\public\images\exact_reference_hero.jpg")
# Where is "ter." located exactly?
# Let's crop from x=650 to 850, y=250 to 420
ter_crop = im.crop((650, 250, 850, 420))
ter_crop.save(r"C:\Users\heman\Desktop\devatwal-crane-service\public\images\crop_ter.jpg")
print("Saved crop_ter.jpg")
