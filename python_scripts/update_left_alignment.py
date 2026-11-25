with open(r"C:\Users\heman\Desktop\devatwal-crane-service\public\index.html", "r", encoding="utf-8") as f:
    html = f.read()

# 1. Update Header to be flush to the left with zero wasted space
old_header_container = '<div class="max-w-[96rem] mx-auto px-6 sm:px-10 lg:px-14">'
new_header_container = '<div class="w-full px-3 sm:px-6 lg:px-8">'
html = html.replace(old_header_container, new_header_container, 1)

old_header_brand = '<a href="#hero" class="flex items-center space-x-4 group cursor-pointer focus:outline-none shrink-0">'
new_header_brand = '<a href="#hero" class="flex items-center space-x-3 group cursor-pointer focus:outline-none shrink-0 pl-1 sm:pl-2">'
html = html.replace(old_header_brand, new_header_brand, 1)

# 2. Update Hero Section to be flush to the left with zero wasted space
old_hero_container = '<div class="max-w-[96rem] w-full mx-auto px-6 sm:px-10 lg:px-12 py-14 lg:py-20 relative z-10">'
new_hero_container = '<div class="w-full px-3 sm:px-6 lg:px-8 py-12 lg:py-16 relative z-10">'
html = html.replace(old_hero_container, new_hero_container, 1)

old_hero_col = '<div class="lg:col-span-8 space-y-6 text-left">'
new_hero_col = '<div class="lg:col-span-8 space-y-6 text-left pl-1 sm:pl-2">'
html = html.replace(old_hero_col, new_hero_col, 1)

# Remove any blue glow div spilling upwards into the bottom of the hero
html = html.replace('<div class="lighting-glow-blue -top-20 left-1/3"></div>', '')

with open(r"C:\Users\heman\Desktop\devatwal-crane-service\public\index.html", "w", encoding="utf-8") as f:
    f.write(html)

print("Updated index.html to align logo & hero wording all the way to the left edge!")
