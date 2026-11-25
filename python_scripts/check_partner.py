from PIL import Image

im = Image.open(r"C:\Users\heman\Desktop\devatwal-crane-service\public\images\devatwal_partner_crane.jpg")
print("devatwal_partner_crane.jpg size:", im.size)
im.resize((500, 250)).save(r"C:\Users\heman\Desktop\devatwal-crane-service\public\images\test_partner.jpg")
