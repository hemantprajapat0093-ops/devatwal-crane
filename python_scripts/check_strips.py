from PIL import Image

for i in [1, 2, 3, 4]:
    im = Image.open(rf"C:\Users\heman\Desktop\devatwal-crane-service\public\images\rh_strip{i}.jpg")
    print(f"Strip {i}: {im.size}")
