from PIL import Image, ImageDraw, ImageFont

# Test rendering "क्रेन सर्विस" using Nirmala.ttc
font_path = r"C:\Windows\Fonts\Nirmala.ttc"
# Test both regular and bold (index 0 or index 1 in ttc)
for idx in [0, 1]:
    try:
        font = ImageFont.truetype(font_path, size=36, index=idx)
        test_im = Image.new("RGBA", (300, 80), (255, 255, 255, 0))
        draw = ImageDraw.Draw(test_im)
        draw.text((10, 10), "क्रेन सर्विस", font=font, fill=(30, 64, 175, 255))
        test_im.save(rf"C:\Users\heman\Desktop\devatwal-crane-service\public\images\test_nirmala_{idx}.png")
        print(f"Rendered Nirmala index {idx} successfully!")
    except Exception as e:
        print(f"Error index {idx}: {e}")
