import re

with open(r"C:\Users\heman\Desktop\devatwal-crane-service\reconstructed_prev_index.html", encoding="utf-8") as f:
    text = f.read()

# find all class names
classes = set(re.findall(r'class="([^"]+)"', text))
custom_classes = set()
for c in classes:
    for word in c.split():
        if not any(word.startswith(p) for p in ['bg-', 'text-', 'p-', 'px-', 'py-', 'pt-', 'pb-', 'm-', 'mx-', 'my-', 'mt-', 'mb-', 'flex', 'grid-', 'w-', 'h-', 'max-w', 'min-h', 'rounded', 'border', 'shadow', 'items-', 'justify-', 'space-', 'relative', 'absolute', 'overflow', 'hover:', 'focus:', 'hidden', 'block', 'inline', 'group', 'transition', 'cursor-', 'select-', 'truncate', 'leading-', 'tracking-', 'font-', 'duration-', 'col-', 'lg:', 'sm:', 'md:', 'uppercase', 'lowercase', 'z-']):
            custom_classes.add(word)

print("Custom classes in reconstructed_prev_index.html:")
for c in sorted(custom_classes):
    print("-", c)
