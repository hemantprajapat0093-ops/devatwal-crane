from PIL import Image

im1 = Image.open(r"C:\Users\heman\.gemini\antigravity-cli\brain\4864e298-07a5-436c-ad5f-3371b3bb3f27\.user_uploaded\uploaded_media_1795622910081.jpg")
print("im1 size:", im1.size)

# Where does the crane start in im1?
# In im1, is the whole heading and navbar present?
# Let's save a reduced version or inspect regions
im1.save(r"C:\Users\heman\Desktop\devatwal-crane-service\public\images\ref_mockup.jpg")
print("Saved ref_mockup.jpg")
