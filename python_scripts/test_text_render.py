from PIL import Image, ImageDraw, ImageFont
import numpy as np

font_path = r"C:\Windows\Fonts\Nirmala.ttc"

# We want:
# - Blue text: vibrant royal blue, e.g., (16, 75, 200) or (24, 88, 224)
# - White outline: (255, 255, 255), stroke_width=2 or 3
# - Clean Devanagari typography: "क्रेन सर्विस"

for font_size in [20, 22, 24, 26]:
    font = ImageFont.truetype(font_path, size=font_size, index=1) # Bold
    
    # Calculate bounding box
    dummy = Image.new("RGBA", (1, 1))
    draw_dummy = ImageDraw.Draw(dummy)
    bbox = draw_dummy.textbbox((0, 0), "क्रेन सर्विस", font=font, stroke_width=2)
    tw = bbox[2] - bbox[0] + 20
    th = bbox[3] - bbox[1] + 20
    
    txt_im = Image.new("RGBA", (tw, th), (0, 0, 0, 0))
    draw = ImageDraw.Draw(txt_im)
    
    # Draw with stroke (white outline) and fill (blue)
    draw.text((10, 10), "क्रेन सर्विस", font=font, fill=(16, 80, 210, 255), stroke_width=2, stroke_fill=(255, 255, 255, 255))
    
    txt_im.save(rf"C:\Users\heman\Desktop\devatwal-crane-service\public\images\test_rendered_text_size_{font_size}.png")
    print(f"Font size {font_size}: rendered text width={tw}, height={th}")
