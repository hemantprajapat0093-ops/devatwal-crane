from PIL import Image

im = Image.open(r"C:\Users\heman\Desktop\devatwal-crane-service\public\images\user_crane_clean.jpg")
im.crop((0, 0, 150, im.height)).save(r"C:\Users\heman\Desktop\devatwal-crane-service\public\images\verify_cleaned_left.jpg")
print("Saved verify_cleaned_left.jpg")
