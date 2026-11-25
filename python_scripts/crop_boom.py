from PIL import Image

im = Image.open(r"C:\Users\heman\Desktop\devatwal-crane-service\public\images\exact_reference_hero.jpg")
# Let's crop from x=600 to 1000, y=100 to 500
im.crop((600, 100, 1000, 500)).save(r"C:\Users\heman\Desktop\devatwal-crane-service\public\images\check_crane_boom_area.jpg")
print("Saved check_crane_boom_area.jpg")
