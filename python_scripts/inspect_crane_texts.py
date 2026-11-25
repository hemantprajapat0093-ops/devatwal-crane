from PIL import Image

# 1. In uploaded_media_1795622910081.jpg:
im_mockup = Image.open(r"C:\Users\heman\.gemini\antigravity-cli\brain\4864e298-07a5-436c-ad5f-3371b3bb3f27\.user_uploaded\uploaded_media_1795622910081.jpg")
print("im_mockup:", im_mockup.size)

# Where is the crane in im_mockup?
# The boom is roughly x: 700 to 1400, y: 150 to 650
# Let's crop:
# a) The boom text: "ACE 12XW प्रजापति"
# b) The lower arm text: "देवतवाल क्रेन सर्विस"
# c) Near "Your Trusted Crane Partner" (where blur was noted)
# d) Bottom right area (near call/email logo dock)

# Let's crop the crane from im_mockup:
im_mockup.crop((700, 150, 1400, 689)).save(r"C:\Users\heman\Desktop\devatwal-crane-service\public\images\test_mockup_crane.jpg")

# 2. In uploaded_media_1_1795616151709.jpg:
im1 = Image.open(r"C:\Users\heman\.gemini\antigravity-cli\brain\4864e298-07a5-436c-ad5f-3371b3bb3f27\.user_uploaded\uploaded_media_1_1795616151709.jpg")
print("im1:", im1.size)
im1.save(r"C:\Users\heman\Desktop\devatwal-crane-service\public\images\test_orig_crane.jpg")

# 3. In uploaded_media_0_1795616151709.jpg:
im0 = Image.open(r"C:\Users\heman\.gemini\antigravity-cli\brain\4864e298-07a5-436c-ad5f-3371b3bb3f27\.user_uploaded\uploaded_media_0_1795616151709.jpg")
print("im0:", im0.size)
im0.save(r"C:\Users\heman\Desktop\devatwal-crane-service\public\images\test_orig_crane_road.jpg")

print("Saved test crane images for comparison!")
