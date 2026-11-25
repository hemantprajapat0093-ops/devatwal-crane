from PIL import Image

# uploaded_media_0_1795616151709.jpg is the photo of the real crane on the road
im0 = Image.open(r"C:\Users\heman\.gemini\antigravity-cli\brain\4864e298-07a5-436c-ad5f-3371b3bb3f27\.user_uploaded\uploaded_media_0_1795616151709.jpg")
print("im0 size:", im0.size)

# In im0:
# On the upper boom: "ACE 12XW प्रजापति"
# On the lower slant arm: "देवतवाल क्रेन सर्विस"
# "देवतवाल" is in RED, "क्रेन सर्विस" is in BLUE!
# On the cabin: "7"
# On top of the cabin: "Devatwal Crane Service"
# Let's crop the lower slant arm from im0:
# w=745, h=342
# lower arm is roughly x: 200 to 450, y: 150 to 300
im0.crop((200, 150, 450, 300)).save(r"C:\Users\heman\Desktop\devatwal-crane-service\public\images\arm_real_im0.jpg")

# upper boom: x: 300 to 600, y: 30 to 150
im0.crop((300, 30, 600, 150)).save(r"C:\Users\heman\Desktop\devatwal-crane-service\public\images\boom_real_im0.jpg")
print("Saved arm_real_im0.jpg and boom_real_im0.jpg")
