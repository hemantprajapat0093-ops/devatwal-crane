from PIL import Image

for name in ["uploaded_media_0_1795620538745.jpg", "uploaded_media_1_1795620538745.jpg", "uploaded_media_1795622910081.jpg"]:
    p = rf"C:\Users\heman\.gemini\antigravity-cli\brain\4864e298-07a5-436c-ad5f-3371b3bb3f27\.user_uploaded\{name}"
    im = Image.open(p)
    print(name, im.size)
    # save 500px wide preview
    ratio = 500 / im.width
    im.resize((500, int(im.height * ratio))).save(rf"C:\Users\heman\Desktop\devatwal-crane-service\public\images\preview_{name}")
print("Saved previews!")
