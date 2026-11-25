from PIL import Image

# Let's save a preview of loc_arm, loc_left_body, loc_trusted, loc_boom_slab
for n in ["loc_trusted", "loc_arm", "loc_left_body", "loc_boom_slab"]:
    im = Image.open(rf"C:\Users\heman\Desktop\devatwal-crane-service\public\images\{n}.jpg")
    print(n, im.size)
