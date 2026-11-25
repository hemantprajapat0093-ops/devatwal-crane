import re

# ==========================================
# 1. UPDATE public/index.html
# ==========================================
with open(r"C:\Users\heman\Desktop\devatwal-crane-service\public\index.html", "r", encoding="utf-8") as f:
    html = f.read()

# A. Remove corner-dock-btn-maps from floating dock
html = re.sub(
    r'\s*<!-- Direct Google Maps Location Pin Trigger.*?<\/a>',
    '',
    html,
    flags=re.DOTALL
)

# B. Update Founder Satyapal's card in Leadership
old_satyapal_contact = """<div><strong class="text-white">Direct Line:</strong> <a href="tel:9414333328" class="text-amber-400 font-bold hover:underline">+91 9414333328</a></div>"""
new_satyapal_contact = """<div><strong class="text-white">Direct Lines:</strong> <a href="tel:9414333328" class="text-amber-400 font-bold hover:underline">+91 9414333328</a> <span class="text-slate-500">/</span> <a href="tel:9950233073" class="text-amber-400 font-bold hover:underline">+91 9950233073</a></div>"""
html = html.replace(old_satyapal_contact, new_satyapal_contact)

# C. Update Maman Prajapat's card in Leadership
old_maman_contact = """<div><strong class="text-white">Direct Line:</strong> <a href="tel:9950233073" class="text-sky-400 font-bold hover:underline">+91 9950233073</a></div>"""
new_maman_contact = """<div><strong class="text-white">Direct Line:</strong> <a href="tel:8003721244" class="text-sky-400 font-bold hover:underline">+91 8003721244</a></div>"""
html = html.replace(old_maman_contact, new_maman_contact)

# D. Update Vishnudat Prajapat -> Dharminder Prajapat in Leadership
old_vishnudat_card = """        <!-- CO-FOUNDER: Vishnudat Prajapat -->
        <div class="box-amber-bright rounded-3xl p-7 group flex flex-col items-center text-center">
          <div class="relative w-32 h-32 rounded-full p-1.5 bg-gradient-to-tr from-slate-700 via-amber-500 to-slate-800 shadow-[0_0_20px_rgba(245,158,11,0.4)] mb-5 group-hover:scale-105 transition-transform duration-300">
            <div class="w-full h-full rounded-full overflow-hidden bg-slate-900 border-2 border-slate-900 flex items-center justify-center text-3xl font-black text-amber-400 font-heading">
              VP
            </div>
          </div>

          <div class="inline-block px-4 py-1 rounded-full bg-slate-800 text-amber-300 text-xs font-bold uppercase mb-2 border border-slate-700">
            Co-Founder & Safety Director
          </div>
          <h3 class="text-2xl font-bold text-white font-heading">
            Vishnudat Prajapat
          </h3>
          <p class="text-xs text-amber-400 font-bold mb-4">
            Technical Safety & Rigging
          </p>
          <p class="text-slate-300 text-xs sm:text-sm leading-relaxed mb-6">
            Oversees hydraulic machinery maintenance, structural slings and rigging integrity, and crane operator safety protocols for elevated building projects.
          </p>

          <div class="w-full space-y-2 border-t border-slate-800/80 pt-4 text-xs text-slate-300 text-left">
            <div><strong class="text-white">Contact:</strong> +91 9414333328 / 9950233073</div>
            <div><strong class="text-white">Specialty:</strong> Heavy Rigging Engineering</div>
          </div>
        </div>"""

new_dharminder_card = """        <!-- CO-FOUNDER: Dharminder Prajapat -->
        <div class="box-amber-bright rounded-3xl p-7 group flex flex-col items-center text-center">
          <div class="relative w-32 h-32 rounded-full p-1.5 bg-gradient-to-tr from-slate-700 via-amber-500 to-slate-800 shadow-[0_0_20px_rgba(245,158,11,0.4)] mb-5 group-hover:scale-105 transition-transform duration-300">
            <div class="w-full h-full rounded-full overflow-hidden bg-slate-900 border-2 border-slate-900 flex items-center justify-center text-3xl font-black text-amber-400 font-heading">
              DP
            </div>
          </div>

          <div class="inline-block px-4 py-1 rounded-full bg-slate-800 text-amber-300 text-xs font-bold uppercase mb-2 border border-slate-700">
            Co-Founder & Operations Director
          </div>
          <h3 class="text-2xl font-bold text-white font-heading">
            Dharminder Prajapat
          </h3>
          <p class="text-xs text-amber-400 font-bold mb-4">
            Technical Safety & Site Operations
          </p>
          <p class="text-slate-300 text-xs sm:text-sm leading-relaxed mb-6">
            Oversees hydraulic machinery maintenance, structural slings and rigging integrity, and crane operator safety protocols for industrial and commercial projects.
          </p>

          <div class="w-full space-y-2 border-t border-slate-800/80 pt-4 text-xs text-slate-300 text-left">
            <div><strong class="text-white">Direct Line:</strong> <a href="tel:9982842357" class="text-amber-400 font-bold hover:underline">+91 9982842357</a></div>
            <div><strong class="text-white">Specialty:</strong> Heavy Rigging & Field Engineering</div>
          </div>
        </div>"""

html = html.replace(old_vishnudat_card, new_dharminder_card)

# E. Update Yard Address box in Contact Section to be Clickable
old_yard_box = """          <div class="box-amber-bright p-5 rounded-2xl flex items-start space-x-4">
            <div class="p-3 rounded-xl bg-amber-500/20 text-amber-400 shrink-0">
              <i data-lucide="map-pin" class="w-6 h-6"></i>
            </div>
            <div>
              <div class="text-xs text-amber-400 font-bold uppercase">Yard Address:</div>
              <div class="text-white font-bold text-sm sm:text-base mt-0.5">
                RIICO Industrial Area, Ghiloth, Neemrana, Alwar, Rajasthan - 301705
              </div>
            </div>
          </div>"""

new_yard_box = """          <a href="https://www.google.com/maps/place/Devatwal+Crane+Service/@28.0604817,76.4195232" target="_blank" rel="noopener noreferrer" class="box-amber-bright p-5 rounded-2xl flex items-start justify-between space-x-4 group cursor-pointer hover:border-amber-400 transition-all block text-left" title="Click to Open Devatwal Crane Service Yard on Google Maps">
            <div class="flex items-start space-x-4">
              <div class="p-3 rounded-xl bg-amber-500/20 text-amber-400 shrink-0 group-hover:bg-amber-500/30 group-hover:scale-110 transition-all">
                <i data-lucide="map-pin" class="w-6 h-6 text-amber-400"></i>
              </div>
              <div>
                <div class="text-xs text-amber-400 font-bold uppercase flex items-center space-x-2">
                  <span>Yard Address:</span>
                  <span class="text-[10px] bg-amber-500/25 text-amber-300 px-2 py-0.5 rounded-full border border-amber-500/40">📍 Click to Open Google Maps ↗</span>
                </div>
                <div class="text-white font-bold text-sm sm:text-base mt-1 group-hover:text-amber-300 transition-colors">
                  RIICO Industrial Area, Ghiloth, Neemrana, Alwar, Rajasthan - 301705
                </div>
                <div class="text-xs text-slate-400 mt-1">
                  Stationed Yard • Immediate Crane Dispatch across 301705
                </div>
              </div>
            </div>
            <div class="shrink-0 p-1 text-slate-400 group-hover:text-amber-400 transition-colors">
              <i data-lucide="external-link" class="w-5 h-5"></i>
            </div>
          </a>"""

html = html.replace(old_yard_box, new_yard_box)

# F. Update Direct Calling Lines in Contact Section
old_call_box = """          <div class="tech-card-bright p-5 rounded-2xl flex items-start space-x-4">
            <div class="p-3 rounded-xl bg-emerald-600/20 text-emerald-400 shrink-0">
              <i data-lucide="phone-call" class="w-6 h-6"></i>
            </div>
            <div>
              <div class="text-xs text-emerald-400 font-bold uppercase">Direct Calling Lines:</div>
              <div class="flex flex-wrap gap-3 mt-1 text-sm sm:text-base font-mono font-bold">
                <a href="tel:9414333328" class="text-white hover:text-amber-400 transition-colors">
                  +91 9414333328 (Satyapal ji)
                </a>
                <span class="text-slate-500">|</span>
                <a href="tel:9950233073" class="text-white hover:text-amber-400 transition-colors">
                  +91 9950233073 (Maman ji)
                </a>
              </div>
            </div>
          </div>"""

new_call_box = """          <div class="tech-card-bright p-5 rounded-2xl flex items-start space-x-4">
            <div class="p-3 rounded-xl bg-emerald-600/20 text-emerald-400 shrink-0">
              <i data-lucide="phone-call" class="w-6 h-6"></i>
            </div>
            <div class="w-full">
              <div class="text-xs text-emerald-400 font-bold uppercase mb-1">Direct Calling Lines:</div>
              <div class="grid grid-cols-1 sm:grid-cols-3 gap-2 text-xs sm:text-sm font-mono font-bold">
                <div class="p-2 rounded-lg bg-slate-900/80 border border-slate-800">
                  <div class="text-[10px] text-slate-400 font-sans font-medium uppercase">Founder:</div>
                  <a href="tel:9414333328" class="text-white hover:text-amber-400 transition-colors block">+91 9414333328</a>
                  <a href="tel:9950233073" class="text-white hover:text-amber-400 transition-colors block text-xs mt-0.5">+91 9950233073</a>
                  <span class="text-amber-400 text-[10px] font-sans font-semibold">Satyapal ji</span>
                </div>
                <div class="p-2 rounded-lg bg-slate-900/80 border border-slate-800">
                  <div class="text-[10px] text-slate-400 font-sans font-medium uppercase">Co-Founder:</div>
                  <a href="tel:8003721244" class="text-white hover:text-sky-400 transition-colors block">+91 8003721244</a>
                  <span class="text-sky-400 text-[10px] font-sans font-semibold mt-1 block">Maman ji</span>
                </div>
                <div class="p-2 rounded-lg bg-slate-900/80 border border-slate-800">
                  <div class="text-[10px] text-slate-400 font-sans font-medium uppercase">Co-Founder:</div>
                  <a href="tel:9982842357" class="text-white hover:text-amber-400 transition-colors block">+91 9982842357</a>
                  <span class="text-amber-400 text-[10px] font-sans font-semibold mt-1 block">Dharminder ji</span>
                </div>
              </div>
            </div>
          </div>"""

html = html.replace(old_call_box, new_call_box)

# G. Update Footer Contacts and Credits
old_footer_contacts = """            <li class="flex items-center space-x-1.5">
              <i data-lucide="phone" class="w-3.5 h-3.5 text-emerald-400"></i>
              <a href="tel:9414333328" class="text-white hover:text-amber-400 font-mono">+91 9414333328 (Satyapal ji)</a>
            </li>
            <li class="flex items-center space-x-1.5">
              <i data-lucide="phone" class="w-3.5 h-3.5 text-emerald-400"></i>
              <a href="tel:9950233073" class="text-white hover:text-amber-400 font-mono">+91 9950233073 (Maman ji)</a>
            </li>"""

new_footer_contacts = """            <li class="flex items-center space-x-1.5">
              <i data-lucide="phone" class="w-3.5 h-3.5 text-emerald-400"></i>
              <a href="tel:9414333328" class="text-white hover:text-amber-400 font-mono">+91 9414333328 / 9950233073 (Satyapal ji)</a>
            </li>
            <li class="flex items-center space-x-1.5">
              <i data-lucide="phone" class="w-3.5 h-3.5 text-emerald-400"></i>
              <a href="tel:8003721244" class="text-white hover:text-amber-400 font-mono">+91 8003721244 (Maman ji)</a>
            </li>
            <li class="flex items-center space-x-1.5">
              <i data-lucide="phone" class="w-3.5 h-3.5 text-emerald-400"></i>
              <a href="tel:9982842357" class="text-white hover:text-amber-400 font-mono">+91 9982842357 (Dharminder ji)</a>
            </li>"""

html = html.replace(old_footer_contacts, new_footer_contacts)

# Credits:
html = html.replace(
    '<strong class="text-white">Maman Prajapat & Vishnudat Prajapat</strong>',
    '<strong class="text-white">Maman Prajapat & Dharminder Prajapat</strong>'
)

with open(r"C:\Users\heman\Desktop\devatwal-crane-service\public\index.html", "w", encoding="utf-8") as f:
    f.write(html)

print("Updated public/index.html successfully!")


# ==========================================
# 2. UPDATE public/js/app.js
# ==========================================
with open(r"C:\Users\heman\Desktop\devatwal-crane-service\public\js\app.js", "r", encoding="utf-8") as f:
    app_js = f.read()

old_owner_cfg = """const OWNER_CONFIG = {
  phone1: '9414333328',
  phone2: '9950233073',
  email: 'satyapaldevatwal@gmail.com',
  pincode: '301705',
  yardLocation: 'RIICO Industrial Area Ghiloth, Neemrana, Alwar, Rajasthan - 301705',
};"""

new_owner_cfg = """const OWNER_CONFIG = {
  phone1: '9414333328', // Satyapal ji
  phone2: '9950233073', // Satyapal ji
  phoneMaman: '8003721244', // Maman ji
  phoneDharminder: '9982842357', // Dharminder ji
  email: 'satyapaldevatwal@gmail.com',
  pincode: '301705',
  yardLocation: 'RIICO Industrial Area Ghiloth, Neemrana, Alwar, Rajasthan - 301705',
};"""

app_js = app_js.replace(old_owner_cfg, new_owner_cfg)

with open(r"C:\Users\heman\Desktop\devatwal-crane-service\public\js\app.js", "w", encoding="utf-8") as f:
    f.write(app_js)

print("Updated public/js/app.js successfully!")


# ==========================================
# 3. UPDATE server.js
# ==========================================
with open(r"C:\Users\heman\Desktop\devatwal-crane-service\server.js", "r", encoding="utf-8") as f:
    server_js = f.read()

server_js = server_js.replace(
    "const PRIMARY_PHONE_2 = '9950233073';",
    "const PRIMARY_PHONE_2 = '9950233073'; // Satyapal ji\nconst MAMAN_PHONE = '8003721244';\nconst DHARMINDER_PHONE = '9982842357';"
)

server_js = server_js.replace(
    "console.log(`📞 Direct Contact: +91 9414333328 / +91 9950233073`);",
    "console.log(`📞 Direct Contact: Satyapal (+91 9414333328, 9950233073), Maman (+91 8003721244), Dharminder (+91 9982842357)`);"
)

with open(r"C:\Users\heman\Desktop\devatwal-crane-service\server.js", "w", encoding="utf-8") as f:
    f.write(server_js)

print("Updated server.js successfully!")
