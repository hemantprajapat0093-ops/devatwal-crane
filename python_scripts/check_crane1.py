from PIL import Image

im = Image.open(r"C:\Users\heman\Desktop\devatwal-crane-service\public\images\devatwal_crane_1.jpg")
print("devatwal_crane_1 size:", im.size)
# The whole crane is centered in devatwal_crane_1.jpg
# Let's crop a perfect square around the crane
w, h = im.size
print("w, h:", w, h)
