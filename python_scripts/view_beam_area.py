from PIL import Image

im = Image.open(r"C:\Users\heman\Desktop\devatwal-crane-service\public\images\clean_beam_text_area.png")
print("Size of clean_beam_text_area:", im.size)
# Let's save a 2x zoomed version so we can see every letter clearly
im.resize((im.width * 2, im.height * 2), Image.Resampling.NEAREST).save(r"C:\Users\heman\Desktop\devatwal-crane-service\public\images\clean_beam_text_area_2x.png")
print("Saved clean_beam_text_area_2x.png")
