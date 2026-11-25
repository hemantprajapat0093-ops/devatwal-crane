from PIL import Image

p0 = r"C:/Users/heman/.gemini/antigravity-cli/brain/4864e298-07a5-436c-ad5f-3371b3bb3f27/.user_uploaded/uploaded_media_0_1795620538745.jpg"
p1 = r"C:/Users/heman/.gemini/antigravity-cli/brain/4864e298-07a5-436c-ad5f-3371b3bb3f27/.user_uploaded/uploaded_media_1_1795620538745.jpg"

im0 = Image.open(p0)
im1 = Image.open(p1)

print(f"Media 0 size: {im0.size}")
print(f"Media 1 size: {im1.size}")
