import re

with open(r"C:\Users\heman\Desktop\devatwal-crane-service\recovered_index.html", "r", encoding="utf-8") as f:
    html = f.read()

# 1. Enhance the brand title in the Hero section next to the crane:
old_hero_title = """          <!-- Highlighted Large Brand Heading -->
          <div class="space-y-3">
            <h1 class="text-4xl sm:text-6xl lg:text-7xl font-black font-heading text-white tracking-tight leading-none">
              DEVATWAL CRANE 
              <span class="block bg-gradient-to-r from-sky-400 via-blue-400 to-indigo-400 bg-clip-text text-transparent">
                SERVICE
              </span>
            </h1>
            <p class="text-xl sm:text-2xl font-extrabold text-sky-300 font-heading tracking-wide">
              Lift Higher. Go Further.
            </p>
            <p class="text-slate-300 text-sm sm:text-base font-semibold max-w-xl">
              Safe Lift... Strong Support... Safe, Powerful, Reliable, On Time.
            </p>
          </div>"""

new_hero_title = """          <!-- Prominently Highlighted Brand Heading Next to Crane -->
          <div class="space-y-3 relative">
            <div class="inline-flex items-center space-x-2 px-4 py-1.5 rounded-full bg-gradient-to-r from-blue-600/30 via-sky-500/20 to-amber-500/20 border border-sky-400/40 shadow-lg shadow-sky-500/20">
              <span class="w-2.5 h-2.5 rounded-full bg-amber-400 animate-pulse"></span>
              <span class="text-xs sm:text-sm font-black tracking-widest text-amber-300 uppercase">★ Certified Heavy Lift Contractor ★</span>
            </div>

            <h1 class="text-4xl sm:text-6xl lg:text-7xl font-black font-heading tracking-tight leading-none">
              <span class="text-white drop-shadow-[0_4px_24px_rgba(56,189,248,0.5)]">DEVATWAL</span> 
              <span class="text-amber-400 drop-shadow-[0_4px_24px_rgba(245,158,11,0.6)]">CRANE</span>
              <span class="block bg-gradient-to-r from-sky-300 via-blue-400 to-amber-400 bg-clip-text text-transparent drop-shadow-[0_6px_28px_rgba(37,99,235,0.7)]">
                SERVICE
              </span>
            </h1>
            
            <p class="text-xl sm:text-2xl font-black text-sky-300 font-heading tracking-wide flex items-center space-x-2">
              <span class="text-amber-400">⚡</span>
              <span>Lift Higher. Go Further.</span>
            </p>
            <p class="text-slate-200 text-sm sm:text-base font-semibold max-w-xl">
              Safe Lift... Strong Support... Safe, Powerful, Reliable, On Time.
            </p>
          </div>"""

if old_hero_title in html:
    html = html.replace(old_hero_title, new_hero_title)
    print("Replaced hero title successfully!")
else:
    print("Warning: old_hero_title not found verbatim, checking regex...")

# 2. Add the Email Dispatcher Modal before </body>
modal_html = """
  <!-- ================= MODAL 3: EMAIL DISPATCH CENTER ================= -->
  <!-- Direct launcher for Gmail, Default Client, Yahoo, Outlook & Copying -->
  <div id="email-dispatcher-modal" class="fixed inset-0 z-50 bg-black/85 backdrop-blur-md hidden items-center justify-center p-4">
    <div class="tech-card rounded-3xl max-w-lg w-full p-6 sm:p-8 shadow-2xl relative overflow-hidden bg-slate-900 border-sky-400/50">
      
      <button id="close-email-modal" class="absolute top-4 right-4 p-2 text-slate-400 hover:text-white bg-slate-800 rounded-full border border-slate-700">
        <i data-lucide="x" class="w-5 h-5"></i>
      </button>

      <div class="flex items-center space-x-3 mb-4">
        <div class="w-12 h-12 rounded-2xl bg-blue-600/20 text-sky-400 border border-sky-400/30 flex items-center justify-center shrink-0">
          <i data-lucide="mail" class="w-6 h-6"></i>
        </div>
        <div>
          <h3 class="text-xl font-black text-white font-heading">
            Direct Email Inquiries
          </h3>
          <p class="text-xs text-sky-400 font-semibold font-mono">
            satyapaldevatwal@gmail.com
          </p>
        </div>
      </div>

      <p class="text-xs text-slate-300 mb-5 leading-relaxed">
        Choose your preferred email service provider below. We have automatically pre-filled the inquiry subject and project requirements for you:
      </p>

      <!-- Provider 1-Click Launchers -->
      <div class="space-y-2.5 mb-5">
        <!-- 1. Gmail Web Launcher -->
        <a id="btn-launch-gmail" href="#" target="_blank" class="w-full flex items-center justify-between px-4 py-3 bg-red-600 hover:bg-red-500 text-white rounded-xl font-bold text-sm shadow-md transition-all group">
          <div class="flex items-center space-x-3">
            <span class="text-lg">🔴</span>
            <span>Open in Gmail (Web Browser)</span>
          </div>
          <i data-lucide="external-link" class="w-4 h-4 text-white/80 group-hover:translate-x-0.5 transition-transform"></i>
        </a>

        <!-- 2. Default System Mail App (mailto) -->
        <a id="btn-launch-mailto" href="#" class="w-full flex items-center justify-between px-4 py-3 bg-blue-600 hover:bg-blue-500 text-white rounded-xl font-bold text-sm shadow-md transition-all group">
          <div class="flex items-center space-x-3">
            <span class="text-lg">💻</span>
            <span>Open in Default Mail App (Outlook / Apple Mail)</span>
          </div>
          <i data-lucide="arrow-right" class="w-4 h-4 text-white/80 group-hover:translate-x-0.5 transition-transform"></i>
        </a>

        <!-- 3. Outlook.com Web -->
        <a id="btn-launch-outlook" href="#" target="_blank" class="w-full flex items-center justify-between px-4 py-3 bg-slate-800 hover:bg-slate-700 text-sky-300 border border-slate-700 rounded-xl font-semibold text-xs sm:text-sm transition-all group">
          <div class="flex items-center space-x-3">
            <span class="text-lg">🔷</span>
            <span>Open in Outlook.com / Office 365 Web</span>
          </div>
          <i data-lucide="external-link" class="w-4 h-4 text-slate-400 group-hover:translate-x-0.5 transition-transform"></i>
        </a>

        <!-- 4. Yahoo Mail Web -->
        <a id="btn-launch-yahoo" href="#" target="_blank" class="w-full flex items-center justify-between px-4 py-3 bg-slate-800 hover:bg-slate-700 text-purple-300 border border-slate-700 rounded-xl font-semibold text-xs sm:text-sm transition-all group">
          <div class="flex items-center space-x-3">
            <span class="text-lg">🟣</span>
            <span>Open in Yahoo Mail</span>
          </div>
          <i data-lucide="external-link" class="w-4 h-4 text-slate-400 group-hover:translate-x-0.5 transition-transform"></i>
        </a>
      </div>

      <!-- Copy Email & Text Section -->
      <div class="border-t border-slate-800 pt-4">
        <button id="btn-copy-email-text" class="w-full flex items-center justify-center space-x-2 bg-slate-950 hover:bg-slate-800 text-slate-200 border border-slate-700 hover:border-sky-400 py-2.5 rounded-xl text-xs font-bold transition-all">
          <i data-lucide="copy" class="w-4 h-4 text-sky-400"></i>
          <span>Copy Inquiry Message & Email Address to Clipboard</span>
        </button>
      </div>

      <!-- Direct In-Modal Quick Message Form -->
      <div class="border-t border-slate-800 mt-4 pt-4">
        <details class="text-xs text-slate-300">
          <summary class="cursor-pointer font-bold text-sky-400 hover:underline">
            Or send message directly from this webpage (No email app needed) ▾
          </summary>
          <form id="quick-inmodal-email-form" class="mt-3 space-y-2.5">
            <input type="text" id="modal-name" required placeholder="Your Name or Company" class="w-full bg-slate-950 border border-slate-800 rounded-lg px-3 py-2 text-white text-xs">
            <input type="tel" id="modal-phone" required placeholder="Your Mobile Phone Number" class="w-full bg-slate-950 border border-slate-800 rounded-lg px-3 py-2 text-white text-xs">
            <textarea id="modal-message" rows="2" placeholder="Tell us your lifting requirements..." class="w-full bg-slate-950 border border-slate-800 rounded-lg px-3 py-2 text-white text-xs"></textarea>
            <button type="submit" id="btn-send-modal-msg" class="w-full btn-tech-primary text-white py-2 rounded-lg text-xs font-bold">
              Send Message Directly
            </button>
          </form>
        </details>
      </div>

    </div>
  </div>
"""

html = html.replace("</body>", modal_html + "\n</body>")

with open(r"C:\Users\heman\Desktop\devatwal-crane-service\public\index.html", "w", encoding="utf-8") as out:
    out.write(html)

print("public/index.html updated successfully!")
