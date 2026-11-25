from PIL import Image
import os

path = r"C:\Users\heman\.gemini\antigravity-cli\brain\4864e298-07a5-436c-ad5f-3371b3bb3f27\.user_uploaded\uploaded_media_1795628364577.jpg"
im = Image.open(path)
w, h = im.size
print(f"Uploaded banner dimensions: {w}x{h}, mode: {im.mode}")
