from PIL import Image

im_trust = Image.open(r"C:\Users\heman\Desktop\devatwal-crane-service\public\images\loc_trusted.jpg")
print("loc_trusted size:", im_trust.size)
# What text is on loc_trusted?
# Is "Your Trusted Crane Partner" cursive white/yellow?
# Yes!
im_arm = Image.open(r"C:\Users\heman\Desktop\devatwal-crane-service\public\images\loc_arm.jpg")
print("loc_arm size:", im_arm.size)
