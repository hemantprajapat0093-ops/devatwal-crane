from PIL import Image, ImageDraw, ImageFont

font = ImageFont.truetype(r"C:\Windows\Fonts\Nirmala.ttc", 36, index=0)
im = Image.new("RGBA", (400, 100), (0, 0, 0, 0))
draw = ImageDraw.Draw(im)
draw.text((20, 20), "देवतवाल क्रेन सर्विस प्रजापति", font=font, fill=(255, 0, 0, 255))
im.save(r"C:\Users\heman\Desktop\devatwal-crane-service\public\images\test_hindi_render.png")
print("Successfully rendered Hindi text with Nirmala.ttc!")
