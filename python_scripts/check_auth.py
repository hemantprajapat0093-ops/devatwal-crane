from PIL import Image

im = Image.open(r"C:\Users\heman\Desktop\devatwal-crane-service\public\images\hero_crane_authentic.jpg")
print("hero_crane_authentic size:", im.size)
# What text or pixels are in hero_crane_authentic?
# Let's crop left, center, right
im.crop((0, 0, 200, im.height)).save(r"C:\Users\heman\Desktop\devatwal-crane-service\public\images\auth_left.jpg")
im.crop((200, 0, 450, im.height)).save(r"C:\Users\heman\Desktop\devatwal-crane-service\public\images\auth_mid.jpg")
im.crop((450, 0, im.width, im.height)).save(r"C:\Users\heman\Desktop\devatwal-crane-service\public\images\auth_right.jpg")
print("Saved auth slices!")
