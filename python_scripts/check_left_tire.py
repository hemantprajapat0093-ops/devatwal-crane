from PIL import Image

full = Image.open(r"C:\Users\heman\.gemini\antigravity-cli\brain\4864e298-07a5-436c-ad5f-3371b3bb3f27\.user_uploaded\uploaded_media_1795622910081.jpg")
# Crop x from 450 to 650, y from 400 to 680
full.crop((450, 400, 650, 680)).save(r"C:\Users\heman\Desktop\devatwal-crane-service\public\images\left_of_tire.png")
print("Saved left_of_tire.png")
