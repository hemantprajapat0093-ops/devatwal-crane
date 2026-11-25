from PIL import Image

im = Image.open(r"C:\Users\heman\Desktop\devatwal-crane-service\public\images\test_right_half.jpg")
print("Size:", im.size)
# Where is the crane in test_right_half.jpg (which is x=550..1419, y=100..689)?
# Let's crop strips:
# 1. x: 50..250 (original 600..800)
im.crop((50, 0, 250, im.height)).save(r"C:\Users\heman\Desktop\devatwal-crane-service\public\images\rh_strip1.jpg")
# 2. x: 250..450 (original 800..1000)
im.crop((250, 0, 450, im.height)).save(r"C:\Users\heman\Desktop\devatwal-crane-service\public\images\rh_strip2.jpg")
# 3. x: 450..650 (original 1000..1200)
im.crop((450, 0, 650, im.height)).save(r"C:\Users\heman\Desktop\devatwal-crane-service\public\images\rh_strip3.jpg")
# 4. x: 650..869 (original 1200..1419)
im.crop((650, 0, im.width, im.height)).save(r"C:\Users\heman\Desktop\devatwal-crane-service\public\images\rh_strip4.jpg")

print("Saved strips!")
