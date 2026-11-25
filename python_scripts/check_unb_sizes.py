from PIL import Image

for name in ["orig_unblurred_trusted", "orig_unblurred_arm", "orig_unblurred_boom"]:
    im = Image.open(rf"C:\Users\heman\Desktop\devatwal-crane-service\public\images\{name}.jpg")
    print(name, im.size)
