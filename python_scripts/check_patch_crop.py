from PIL import Image

im = Image.open(r"C:\Users\heman\Desktop\devatwal-crane-service\public\images\hero_perfect_clean_backdrop.jpg")
im.crop((680, 230, 890, 470)).save(r"C:\Users\heman\Desktop\devatwal-crane-service\public\images\verify_patch_smooth.jpg")
print("Saved verify_patch_smooth.jpg")
