from PIL import Image

im = Image.open(r"C:\Users\heman\Desktop\devatwal-crane-service\public\images\user_crane_exact.jpg")

im.crop((0, 0, 80, 120)).save(r"C:\Users\heman\Desktop\devatwal-crane-service\public\images\snippet_rating.jpg")
im.crop((0, 200, 80, 330)).save(r"C:\Users\heman\Desktop\devatwal-crane-service\public\images\snippet_r.jpg")
im.crop((0, 330, 80, 420)).save(r"C:\Users\heman\Desktop\devatwal-crane-service\public\images\snippet_le.jpg")
im.crop((0, 420, 150, 603)).save(r"C:\Users\heman\Desktop\devatwal-crane-service\public\images\snippet_tire.jpg")

print("Saved snippet crops!")
