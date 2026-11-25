from PIL import Image

full = Image.open(r"C:\Users\heman\.gemini\antigravity-cli\brain\4864e298-07a5-436c-ad5f-3371b3bb3f27\.user_uploaded\uploaded_media_1795622910081.jpg")
print("Full size:", full.size)

# Crop around the crane tire in the full image:
# In full image, let's crop x from 500 to 750, y from 400 to 650:
full.crop((500, 400, 750, 650)).save(r"C:\Users\heman\Desktop\devatwal-crane-service\public\images\tire_in_full.png")
print("Saved tire_in_full.png")
