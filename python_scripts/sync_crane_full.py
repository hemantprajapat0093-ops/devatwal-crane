from PIL import Image

im = Image.open(r"C:\Users\heman\Desktop\devatwal-crane-service\public\images\hero_exact_master_banner.jpg")
im.save(r"C:\Users\heman\Desktop\devatwal-crane-service\public\images\hero_crane_full_view.jpg", quality=98)
print("Updated hero_crane_full_view.jpg as well!")
