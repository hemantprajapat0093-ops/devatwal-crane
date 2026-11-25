from PIL import Image

im = Image.open(r"C:\Users\heman\.gemini\antigravity-cli\brain\4864e298-07a5-436c-ad5f-3371b3bb3f27\.user_uploaded\uploaded_media_1795622910081.jpg")

# Let's inspect the un-blurred crane in uploaded_media_1795622910081.jpg:
# Area under "Your Trusted": (750, 150, 1100, 450)
im.crop((750, 150, 1100, 450)).save(r"C:\Users\heman\Desktop\devatwal-crane-service\public\images\orig_unblurred_trusted.jpg")

# Lower arm / tire area: (650, 400, 950, 680)
im.crop((650, 400, 950, 680)).save(r"C:\Users\heman\Desktop\devatwal-crane-service\public\images\orig_unblurred_arm.jpg")

# Upper boom area: (850, 200, 1300, 450)
im.crop((850, 200, 1300, 450)).save(r"C:\Users\heman\Desktop\devatwal-crane-service\public\images\orig_unblurred_boom.jpg")

print("Saved unblurred crops from original user upload!")
