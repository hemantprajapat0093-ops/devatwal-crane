import urllib.request

html = urllib.request.urlopen("http://127.0.0.1:3000/").read().decode("utf-8")
print("Header full width (w-full):", 'header class="sticky top-0 z-40 bg-[#070D18]/95 backdrop-blur-2xl border-b border-slate-800/90 shadow-xl w-full"' in html or 'div class="w-full px-3 sm:px-6 lg:px-8"' in html)
print("Hero full width:", 'div class="w-full px-3 sm:px-6 lg:px-8 py-12 lg:py-16 relative z-10"' in html)
print("Flush left alignment:", 'pl-1 sm:pl-2' in html)
print("HTML length:", len(html))
