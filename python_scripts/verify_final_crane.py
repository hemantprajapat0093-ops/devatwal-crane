from PIL import Image
import numpy as np

im = Image.open(r"C:\Users\heman\Desktop\devatwal-crane-service\public\images\hero_crane_full_view.jpg")
w, h = im.size
arr = np.array(im)

# Check top left (where "...t Rating" was):
top_white = np.sum((arr[int(30*h/603):int(115*h/603), :int(60*w/832), 0] > 190) & 
                   (arr[int(30*h/603):int(115*h/603), :int(60*w/832), 1] > 190) & 
                   (arr[int(30*h/603):int(115*h/603), :int(60*w/832), 2] > 190))
print("White pixels in top left:", top_white)

# Check mid left (where yellow "...r." was):
mid_yellow = np.sum((arr[int(365*h/603):int(435*h/603), :int(45*w/832), 0] > 220) & 
                    (arr[int(365*h/603):int(435*h/603), :int(45*w/832), 1] > 180) & 
                    (arr[int(365*h/603):int(435*h/603), :int(45*w/832), 2] < 60))
print("Yellow text pixels in mid left:", mid_yellow)

# Check bottom left (where "...le" was):
bot_white = np.sum((arr[int(560*h/603):, :int(35*w/832), 0] > 190) & 
                   (arr[int(560*h/603):, :int(35*w/832), 1] > 190) & 
                   (arr[int(560*h/603):, :int(35*w/832), 2] > 190))
print("White pixels in bot left:", bot_white)
