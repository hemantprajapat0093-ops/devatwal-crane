from PIL import Image

im = Image.open(r"C:\Users\heman\Desktop\devatwal-crane-service\public\images\hero_bg_clean.jpg")
left_crop = im.crop((0, 140, 500, 689))
left_crop.save(r"C:\Users\heman\Desktop\devatwal-crane-service\public\images\check_left_clean.jpg")
print("Saved check_left_clean.jpg")
