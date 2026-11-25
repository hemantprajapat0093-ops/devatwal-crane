import re

with open(r"C:\Users\heman\Desktop\devatwal-crane-service\public\index.html", "r", encoding="utf-8") as f:
    html = f.read()

# 1. Update Floating Corner Dock to include Google Maps location pin
old_dock = """  <aside class="fixed-floating-corner-dock" aria-label="Direct Dispatch Dock">
    
    <!-- Direct Phone Call Button (Bright Emerald Glow) -->
    <a href="tel:9414333328" class="corner-dock-btn corner-dock-btn-phone text-white" title="Direct Phone Call">
      <i data-lucide="phone-call" class="w-6 h-6"></i>
      <span class="dock-tooltip">Call +91 9414333328 (Satyapal ji)</span>
    </a>

    <!-- Direct Email Dispatcher Button (Bright Amber Gold Glow) -->
    <button class="corner-dock-btn corner-dock-btn-email btn-send-email text-black font-black" title="Send Email to Satyapal ji">
      <i data-lucide="mail" class="w-6 h-6 text-black"></i>
      <span class="dock-tooltip">Direct Email Satyapal ji</span>
    </button>

    <!-- WhatsApp Direct Trigger (Bright Lime Green Glow) -->
    <button class="corner-dock-btn corner-dock-btn-wa btn-open-whatsapp text-white" title="WhatsApp Chat">
      <i data-lucide="message-circle" class="w-6 h-6"></i>
      <span class="dock-tooltip">WhatsApp Inquiries</span>
    </button>

  </aside>"""

new_dock = """  <aside class="fixed-floating-corner-dock" aria-label="Direct Dispatch Dock">
    
    <!-- Direct Phone Call Button (Bright Emerald Glow) -->
    <a href="tel:9414333328" class="corner-dock-btn corner-dock-btn-phone text-white" title="Direct Phone Call">
      <i data-lucide="phone-call" class="w-6 h-6"></i>
      <span class="dock-tooltip">Call +91 9414333328 (Satyapal ji)</span>
    </a>

    <!-- Direct Email Dispatcher Button (Bright Amber Gold Glow) -->
    <button class="corner-dock-btn corner-dock-btn-email btn-send-email text-black font-black" title="Send Email to Satyapal ji">
      <i data-lucide="mail" class="w-6 h-6 text-black"></i>
      <span class="dock-tooltip">Direct Email Satyapal ji</span>
    </button>

    <!-- WhatsApp Direct Trigger (Bright Lime Green Glow) -->
    <button class="corner-dock-btn corner-dock-btn-wa btn-open-whatsapp text-white" title="WhatsApp Chat">
      <i data-lucide="message-circle" class="w-6 h-6"></i>
      <span class="dock-tooltip">WhatsApp Inquiries</span>
    </button>

    <!-- Direct Google Maps Location Pin Trigger (Official Location) -->
    <a href="https://www.google.com/maps/place/Devatwal+Crane+Service/@28.0604817,76.4195232" target="_blank" rel="noopener noreferrer" class="corner-dock-btn corner-dock-btn-maps text-white" title="Open Google Maps Location">
      <i data-lucide="map-pin" class="w-6 h-6 text-white animate-bounce"></i>
      <span class="dock-tooltip">Google Maps: RIICO Ghiloth Yard</span>
    </a>

  </aside>"""

if old_dock in html:
    html = html.replace(old_dock, new_dock)
    print("Updated floating corner dock!")
else:
    print("Corner dock exact match not found, checking...")

# 2. Update Header
header_pattern = r'<header class="sticky top-0 z-40.*?<\/header>'
new_header = """<header class="sticky top-0 z-40 bg-[#070D18]/95 backdrop-blur-2xl border-b border-slate-800/90 shadow-xl">
    <div class="max-w-[96rem] mx-auto px-6 sm:px-10 lg:px-14">
      <div class="flex items-center justify-between h-24">
        
        <!-- Left: Clean Circular Logo & Two-Line Title -->
        <a href="#hero" class="flex items-center space-x-4 group cursor-pointer focus:outline-none shrink-0">
          <!-- Clean Circular Logo -->
          <div class="w-16 h-16 rounded-full overflow-hidden border-2 border-amber-400 shadow-[0_0_20px_rgba(245,158,11,0.5)] group-hover:scale-105 transition-transform shrink-0 bg-slate-950 flex items-center justify-center">
            <img src="/images/exact_header_logo.png" alt="Devatwal Crane Service Logo" class="w-full h-full object-cover">
          </div>
          
          <!-- Two-Tone Brand Title & Subtitle -->
          <div class="leading-tight">
            <div class="text-xl sm:text-2xl font-black tracking-tight font-heading group-hover:brightness-110 transition-all">
              <span class="text-white">Devatwal </span>
              <span class="text-amber-400">Crane Service</span>
            </div>
            <div class="text-xs sm:text-sm font-semibold text-slate-300 tracking-wide mt-0.5">
              Heavy Lifting Solutions <span class="text-slate-500">|</span> Since 2016
            </div>
          </div>
        </a>

        <!-- Middle Navigation: Home, Book Slot, Leadership, Contact with proper spacing -->
        <nav class="hidden md:flex items-center space-x-10 text-base font-semibold">
          <a href="#hero" class="text-amber-400 font-bold border-b-2 border-amber-400 pb-1 tracking-wider hover:text-amber-300 transition-colors flex items-center space-x-1.5">
            <span>Home</span>
          </a>
          <a href="#booking-section" class="text-slate-200 hover:text-amber-400 transition-colors tracking-wider font-semibold">
            Book Slot
          </a>
          <a href="#leadership" class="text-slate-200 hover:text-amber-400 transition-colors tracking-wider font-semibold">
            Leadership
          </a>
          <a href="#contact" class="text-slate-200 hover:text-amber-400 transition-colors tracking-wider font-semibold">
            Contact
          </a>
        </nav>

        <!-- Right Side: Solid Bright Yellow Reserve Crane Button -->
        <div class="hidden sm:flex items-center space-x-4">
          <a href="#booking-section" class="flex items-center space-x-2 bg-gradient-to-r from-amber-400 to-yellow-400 hover:from-amber-300 hover:to-yellow-300 text-black font-extrabold px-6 py-2.5 rounded-xl text-sm shadow-[0_0_20px_rgba(245,158,11,0.5)] transition-all tracking-wide">
            <i data-lucide="calendar" class="w-4 h-4 text-black"></i>
            <span>Reserve Crane</span>
          </a>
        </div>

        <!-- Mobile Menu Toggle Button -->
        <div class="flex items-center md:hidden">
          <button id="mobile-menu-toggle" class="p-2.5 rounded-xl bg-slate-900 border border-slate-800 text-slate-300 hover:text-white focus:outline-none">
            <i data-lucide="menu" class="w-6 h-6"></i>
          </button>
        </div>

      </div>
    </div>

    <!-- Mobile Navigation Drawer -->
    <div id="mobile-menu-drawer" class="hidden md:hidden bg-[#070D18] border-b border-slate-800 px-6 pt-4 pb-6 space-y-3">
      <div class="flex flex-col space-y-2 text-base font-semibold text-slate-200">
        <a href="#hero" class="py-2.5 px-3 bg-amber-500/20 text-amber-400 rounded-lg font-bold">Home</a>
        <a href="#booking-section" class="py-2.5 px-3 hover:bg-slate-900 rounded-lg">Book Slot</a>
        <a href="#leadership" class="py-2.5 px-3 hover:bg-slate-900 rounded-lg">Leadership</a>
        <a href="#contact" class="py-2.5 px-3 hover:bg-slate-900 rounded-lg">Contact</a>
      </div>
    </div>
  </header>"""

html = re.sub(header_pattern, new_header, html, flags=re.DOTALL)
print("Updated header!")

# 3. Update Hero Section
hero_pattern = r'<section id="hero".*?<\/section>'
new_hero = """<section id="hero" class="hero-exact-banner relative flex items-center overflow-hidden border-b border-slate-800/80">
    <div class="max-w-[96rem] w-full mx-auto px-6 sm:px-10 lg:px-12 py-14 lg:py-20 relative z-10">
      <div class="grid grid-cols-1 lg:grid-cols-12 gap-8 items-center">
        
        <!-- Left Hero Content (Spans wide across left to center with balanced padding) -->
        <div class="lg:col-span-8 space-y-6 text-left">
          
          <!-- Top Row: 3 Rounded Badges/Pills -->
          <div class="flex flex-wrap items-center gap-3">
            <div class="inline-flex items-center space-x-2 px-4 py-2 rounded-full bg-slate-900/90 backdrop-blur-md border border-slate-700 text-xs sm:text-sm font-bold text-white shadow-md">
              <i data-lucide="shield-check" class="w-4 h-4 text-amber-400 shrink-0"></i>
              <span>Trusted Partner</span>
            </div>
            <div class="inline-flex items-center space-x-2 px-4 py-2 rounded-full bg-slate-900/90 backdrop-blur-md border border-slate-700 text-xs sm:text-sm font-bold text-white shadow-md">
              <i data-lucide="cog" class="w-4 h-4 text-amber-400 shrink-0"></i>
              <span>On-Time Service</span>
            </div>
            <div class="inline-flex items-center space-x-2 px-4 py-2 rounded-full bg-slate-900/90 backdrop-blur-md border border-slate-700 text-xs sm:text-sm font-bold text-white shadow-md">
              <i data-lucide="star" class="w-4 h-4 text-amber-400 fill-amber-400 shrink-0"></i>
              <span>5.0+ Client Rating</span>
            </div>
          </div>

          <!-- Angled Yellow Ribbon Parallelogram Badge (Enlarged & Prominent) -->
          <div class="inline-block transform -skew-x-12 bg-amber-400 px-7 py-2 rounded shadow-xl">
            <div class="transform skew-x-12 text-base sm:text-lg font-black text-black italic tracking-wider uppercase">
              Devatwal Crane Service
            </div>
          </div>

          <!-- Slanted Italic Headline: "Lift Higher," / "Go Further." with Swoosh -->
          <div class="space-y-1">
            <h1 class="hero-slanted-main-title text-5xl sm:text-7xl lg:text-8xl leading-tight">
              <span class="text-white block">Lift Higher,</span>
              <span class="text-amber-400 block relative">
                Go Further.
                <span class="block w-56 sm:w-96 h-2 sm:h-2.5 bg-gradient-to-r from-amber-400 via-yellow-300 to-transparent rounded-full mt-1.5 transform -rotate-1"></span>
              </span>
            </h1>
          </div>

          <!-- Tagline -->
          <div>
            <p class="text-lg sm:text-2xl font-black italic text-white tracking-wide flex flex-wrap items-center gap-2.5 drop-shadow">
              <span>Safe Lifting</span>
              <span class="text-amber-400 font-black">•</span>
              <span>Strong Support</span>
              <span class="text-amber-400 font-black">•</span>
              <span>Always Reliable</span>
            </p>
          </div>

          <!-- Description Paragraph -->
          <p class="text-slate-200 text-base sm:text-lg leading-relaxed max-w-2xl font-normal drop-shadow">
            Operating since 2016, Devatwal Crane Service delivers industrial-grade heavy lifting solutions across India. Stationed at RIICO Industrial Area Ghiloth and serving the entire 301705 Neemrana industrial corridor 24/7 with precision hydraulic power.
          </p>

          <!-- Two Action Buttons -->
          <div class="flex flex-col sm:flex-row items-stretch sm:items-center gap-4 pt-3">
            <a href="#booking-section" class="flex items-center justify-center space-x-3 bg-gradient-to-r from-amber-400 to-yellow-400 hover:from-amber-300 hover:to-yellow-300 text-black font-extrabold px-8 py-4 rounded-full text-base shadow-[0_4px_25px_rgba(245,158,11,0.5)] transition-all transform hover:-translate-y-0.5">
              <i data-lucide="calendar" class="w-5 h-5 text-black"></i>
              <span>Book Crane Slot Online</span>
              <i data-lucide="arrow-right" class="w-4 h-4 text-black"></i>
            </a>

            <button class="btn-send-email flex items-center justify-center space-x-2.5 bg-slate-900/80 hover:bg-slate-800 text-white font-bold border-2 border-slate-600 hover:border-slate-400 px-8 py-4 rounded-full text-base backdrop-blur-md transition-all shadow-lg transform hover:-translate-y-0.5">
              <i data-lucide="mail" class="w-5 h-5 text-white"></i>
              <span>Get a Quote</span>
            </button>
          </div>

        </div>

        <!-- Right Side Spacer (Showcases the clean authentic crane hoisting slab) -->
        <div class="hidden lg:block lg:col-span-4 h-[560px] pointer-events-none"></div>

      </div>
    </div>
  </section>"""

html = re.sub(hero_pattern, new_hero, html, flags=re.DOTALL)
print("Updated hero section!")

# 4. Update Booking Section
booking_pattern = r'<section id="booking-section".*?<\/section>'
new_booking = """<section id="booking-section" class="py-20 lg:py-28 max-w-[96rem] mx-auto px-6 sm:px-8 lg:px-12 relative">
    <div class="lighting-glow-blue top-1/4 right-0"></div>

    <div class="text-center max-w-3xl mx-auto mb-14 relative z-10">
      <div class="inline-flex items-center space-x-2 px-4 py-1.5 rounded-full text-xs font-bold bg-amber-500/15 text-amber-400 border border-amber-500/30 mb-3 shadow-[0_0_15px_rgba(245,158,11,0.2)]">
        <i data-lucide="calendar" class="w-4 h-4 text-amber-400"></i>
        <span>Direct Crane Reservation System</span>
      </div>
      <h2 class="text-3xl sm:text-5xl font-black font-heading text-white tracking-tight">
        Book Your Crane Slot Online
      </h2>
      <p class="text-slate-300 text-base sm:text-lg mt-3 font-normal">
        Choose your required crane model, job specifications, and date below. An automated dispatch booking is routed directly to <strong>satyapaldevatwal@gmail.com</strong>.
      </p>
    </div>

    <!-- Redesigned High-Tech Dark Obsidian Booking Card -->
    <div class="max-w-4xl mx-auto bg-slate-900/95 backdrop-blur-2xl border border-slate-700/80 rounded-3xl p-6 sm:p-10 shadow-[0_20px_50px_rgba(0,0,0,0.85)] relative z-10">
      
      <form id="crane-booking-form" class="space-y-8">
        
        <!-- STEP 1: Select Crane Variety -->
        <div>
          <label class="block text-xs sm:text-sm font-bold text-amber-400 uppercase tracking-wider mb-3 flex items-center space-x-2">
            <span class="w-6 h-6 rounded-full bg-amber-400 text-black flex items-center justify-center text-xs font-black">1</span>
            <span>Select Crane Variety *</span>
          </label>
          <input type="hidden" id="selected-crane-type" value="ACE 12XW Hydra (Window AC Cabin)">
          
          <div class="grid grid-cols-1 sm:grid-cols-3 gap-4">
            
            <div class="crane-option-card selected p-4 rounded-2xl border-2 border-amber-400 bg-slate-950/90 cursor-pointer transition-all shadow-[0_0_20px_rgba(245,158,11,0.2)]" data-crane-val="ACE 12XW Hydra (Window AC Cabin)" data-preset="12xw">
              <div class="flex items-center justify-between mb-2">
                <span class="text-xs font-black text-amber-400">12 TON</span>
                <span class="text-[11px] bg-amber-500/20 text-amber-300 px-2 py-0.5 rounded-full border border-amber-500/40 font-bold">❄️ Window AC</span>
              </div>
              <div class="font-bold text-base text-white font-heading">ACE 12XW Hydra</div>
              <div class="text-xs text-slate-400 mt-1">Machinery shifts, columns, building slabs & trusses</div>
            </div>

            <div class="crane-option-card p-4 rounded-2xl border border-slate-700 bg-slate-950/80 cursor-pointer transition-all hover:border-slate-500" data-crane-val="ACE 14XW High-Reach (Window AC Cabin)" data-preset="14xw">
              <div class="flex items-center justify-between mb-2">
                <span class="text-xs font-black text-amber-400">14 TON</span>
                <span class="text-[11px] bg-amber-500/20 text-amber-300 px-2 py-0.5 rounded-full border border-amber-500/40 font-bold">❄️ Window AC</span>
              </div>
              <div class="font-bold text-base text-white font-heading">ACE 14XW High-Reach</div>
              <div class="text-xs text-slate-400 mt-1">Multi-story framework, heavy high-elevation lifting</div>
            </div>

            <div class="crane-option-card p-4 rounded-2xl border border-slate-700 bg-slate-950/80 cursor-pointer transition-all hover:border-slate-500" data-crane-val="Indus Heavy Industrial Crane (High Workload)" data-preset="indus">
              <div class="flex items-center justify-between mb-2">
                <span class="text-xs font-black text-sky-400">HEAVY TITAN</span>
                <span class="text-[11px] bg-blue-500/20 text-sky-300 px-2 py-0.5 rounded-full border border-blue-500/40 font-bold">🏭 Indus Grade</span>
              </div>
              <div class="font-bold text-base text-white font-heading">Indus Heavy Industrial</div>
              <div class="text-xs text-slate-400 mt-1">Extreme industrial workloads, plant vessels & boilers</div>
            </div>

          </div>
        </div>

        <!-- STEP 2: Work Scope & Weight -->
        <div class="grid grid-cols-1 sm:grid-cols-2 gap-6">
          <div>
            <label class="block text-xs sm:text-sm font-bold text-amber-400 uppercase tracking-wider mb-2 flex items-center space-x-2">
              <span class="w-6 h-6 rounded-full bg-amber-400 text-black flex items-center justify-center text-xs font-black">2</span>
              <span>Nature of Work *</span>
            </label>
            <select id="bk-work-type" required class="w-full bg-slate-950 border border-slate-700 rounded-xl px-4 py-3 text-white text-sm focus:outline-none focus:border-amber-400">
              <option value="Building Construction & Precast Slab Placement">🏢 Building Construction & Precast Slab Placement</option>
              <option value="Heavy Industrial Machinery Loading & Unloading">⚙️ Heavy Machinery Loading & Unloading</option>
              <option value="Industrial Shed Erection & Steel Trusses">🏭 Industrial Shed Erection & Steel Trusses</option>
              <option value="Chemical Tank & Reactor Vessel Placement">🧪 Chemical Tank & Reactor Vessel Placement</option>
              <option value="Shipping Container Handling & Yard Logistics">📦 Shipping Container Handling & Logistics</option>
              <option value="Commercial Vehicle & Automobile Hoisting">🚗 Commercial Vehicle & Automobile Hoisting</option>
              <option value="Emergency 24/7 Breakdown & Site Recovery">🚨 Emergency Breakdown & Site Recovery</option>
              <option value="Other Heavy Industrial Lift">🏗️ General Heavy Duty Lifting Work</option>
            </select>
          </div>

          <div>
            <label class="block text-xs sm:text-sm font-bold text-amber-400 uppercase tracking-wider mb-2 flex items-center space-x-2">
              <span class="w-6 h-6 rounded-full bg-amber-400 text-black flex items-center justify-center text-xs font-black">3</span>
              <span>Estimated Load Weight</span>
            </label>
            <select id="bk-load-weight" class="w-full bg-slate-950 border border-slate-700 rounded-xl px-4 py-3 text-white text-sm focus:outline-none focus:border-amber-400">
              <option value="Up to 5 Tons">Up to 5 Tons (Light-Medium Duty)</option>
              <option value="5 to 10 Tons">5 to 10 Tons (Standard Heavy Lift)</option>
              <option value="10 to 14 Tons">10 to 14 Tons (ACE Window AC Cabin Capacity)</option>
              <option value="15 to 25+ Tons">15 to 25+ Tons (Indus Industrial Titan Capacity)</option>
              <option value="On-Site Assessment Needed">On-Site Assessment Required</option>
            </select>
          </div>
        </div>

        <!-- STEP 3: Date, Shift Slot, Pincode -->
        <div class="grid grid-cols-1 sm:grid-cols-3 gap-6">
          <div>
            <label class="block text-xs font-bold text-slate-300 uppercase tracking-wider mb-2">
              Required Date *
            </label>
            <input type="date" id="bk-date" required class="w-full bg-slate-950 border border-slate-700 rounded-xl px-4 py-3 text-white text-sm focus:outline-none focus:border-amber-400">
          </div>

          <div>
            <label class="block text-xs font-bold text-slate-300 uppercase tracking-wider mb-2">
              Time Shift Slot *
            </label>
            <select id="bk-time-slot" required class="w-full bg-slate-950 border border-slate-700 rounded-xl px-4 py-3 text-white text-sm focus:outline-none focus:border-amber-400">
              <option value="Immediate Emergency Dispatch">⚡ Immediate Dispatch (Within 30-45 mins)</option>
              <option value="Morning Shift (08:00 AM - 12:00 PM)">🌅 Morning Shift (08:00 AM - 12:00 PM)</option>
              <option value="Afternoon Shift (12:00 PM - 04:00 PM)">☀️ Afternoon Shift (12:00 PM - 04:00 PM)</option>
              <option value="Evening Shift (04:00 PM - 08:00 PM)">🌆 Evening Shift (04:00 PM - 08:00 PM)</option>
              <option value="Night Full Shift (08:00 PM - 08:00 AM)">🌙 Night / Over-Time Shift (Full Night)</option>
            </select>
          </div>

          <div>
            <label class="block text-xs font-bold text-slate-300 uppercase tracking-wider mb-2">
              Service Pincode
            </label>
            <input type="text" id="bk-pincode" value="301705" class="w-full bg-slate-950 border border-slate-700 rounded-xl px-4 py-3 text-white text-sm font-mono font-bold focus:outline-none" readonly title="Complete coverage across 301705 postal zone">
          </div>
        </div>

        <!-- Site Location Address -->
        <div>
          <label class="block text-xs font-bold text-slate-300 uppercase tracking-wider mb-2">
            Project Site Location Address (301705 Industrial Zone) *
          </label>
          <input type="text" id="bk-location" required placeholder="e.g. RIICO Industrial Area Ghiloth, Plot No... / Japanese Zone Neemrana" class="w-full bg-slate-950 border border-slate-700 rounded-xl px-4 py-3 text-white text-sm focus:outline-none focus:border-amber-400">
        </div>

        <!-- STEP 4: Contact Information -->
        <div class="grid grid-cols-1 sm:grid-cols-3 gap-6">
          <div>
            <label class="block text-xs font-bold text-slate-300 uppercase tracking-wider mb-2">
              Contact Person / Company Name *
            </label>
            <input type="text" id="bk-name" required placeholder="Your Name or Company" class="w-full bg-slate-950 border border-slate-700 rounded-xl px-4 py-3 text-white text-sm focus:outline-none focus:border-amber-400">
          </div>

          <div>
            <label class="block text-xs font-bold text-slate-300 uppercase tracking-wider mb-2">
              Mobile Phone Number *
            </label>
            <input type="tel" id="bk-phone" required placeholder="98XXXXXXXX" class="w-full bg-slate-950 border border-slate-700 rounded-xl px-4 py-3 text-white text-sm font-mono focus:outline-none focus:border-amber-400">
          </div>

          <div>
            <label class="block text-xs font-bold text-slate-300 uppercase tracking-wider mb-2">
              Email Address
            </label>
            <input type="email" id="bk-email" placeholder="client@company.com" class="w-full bg-slate-950 border border-slate-700 rounded-xl px-4 py-3 text-white text-sm focus:outline-none focus:border-amber-400">
          </div>
        </div>

        <div>
          <label class="block text-xs font-bold text-slate-300 uppercase tracking-wider mb-2">
            Special Instructions / Job Scope
          </label>
          <textarea id="bk-notes" rows="3" placeholder="Provide dimensions, terrain condition, safety specifications, or lifting clearances..." class="w-full bg-slate-950 border border-slate-700 rounded-xl px-4 py-3 text-white text-sm focus:outline-none focus:border-amber-400"></textarea>
        </div>

        <div class="pt-2">
          <button type="submit" id="btn-submit-booking" class="w-full bg-gradient-to-r from-amber-400 via-yellow-400 to-amber-500 hover:from-amber-300 hover:to-yellow-300 text-black font-black py-4 rounded-xl text-base tracking-wider uppercase shadow-[0_0_25px_rgba(245,158,11,0.5)] flex items-center justify-center space-x-2 transition-all">
            <i data-lucide="check-circle" class="w-5 h-5 text-black"></i>
            <span>Confirm Crane Slot & Transmit Booking</span>
          </button>
          <p class="text-center text-xs text-slate-400 mt-2">
            🔒 Booking notification is automatically logged and sent to <strong>satyapaldevatwal@gmail.com</strong>.
          </p>
        </div>

      </form>
    </div>
  </section>"""

html = re.sub(booking_pattern, new_booking, html, flags=re.DOTALL)
print("Updated booking section!")

# 5. Update Map Section to High-Tech Interactive Satellite Google Map
map_box_pattern = r'<div class="lg:col-span-6 bg-slate-950 rounded-3xl border-2 border-slate-800.*?<\/div>\s*<\/div>\s*<\/section>'
new_map_box = """<div class="lg:col-span-6 bg-slate-950 rounded-3xl border border-slate-700/80 overflow-hidden shadow-2xl flex flex-col">
        
        <!-- Header Bar with Google Maps Badge & Direct Link -->
        <div class="p-4 bg-slate-900/95 border-b border-slate-800 flex flex-wrap items-center justify-between gap-3">
          <div class="flex items-center space-x-2.5">
            <div class="w-8 h-8 rounded-lg bg-blue-600/20 border border-blue-500/40 flex items-center justify-center">
              <i data-lucide="map-pin" class="w-5 h-5 text-blue-400"></i>
            </div>
            <div>
              <span class="text-xs sm:text-sm font-bold text-white block">Devatwal Crane Service Yard</span>
              <span class="text-[11px] text-amber-400 font-medium">RIICO Industrial Area Ghiloth, Neemrana (301705)</span>
            </div>
          </div>
          <a href="https://www.google.com/maps/place/Devatwal+Crane+Service/@28.0604817,76.4195232" target="_blank" rel="noopener noreferrer" class="flex items-center space-x-1.5 bg-blue-600 hover:bg-blue-500 text-white text-xs font-bold px-3.5 py-2 rounded-lg shadow-md transition-all">
            <span>Open in Maps</span>
            <i data-lucide="external-link" class="w-3.5 h-3.5"></i>
          </a>
        </div>

        <!-- Interactive Satellite Google Map (t=k for Satellite Imagery, z=17 for high-detail zoom) -->
        <div class="h-96 w-full bg-slate-950 relative">
          <iframe 
            id="satellite-crane-map"
            src="https://maps.google.com/maps?q=28.0604817,76.4195232+(Devatwal+Crane+Service)&t=k&z=17&ie=UTF8&iwloc=B&output=embed" 
            width="100%" 
            height="100%" 
            style="border:0;" 
            allowfullscreen="" 
            loading="lazy" 
            referrerpolicy="no-referrer-when-downgrade"
            title="Devatwal Crane Service Satellite Location Map">
          </iframe>
        </div>

        <!-- Footer Coordinates & Direct App Link -->
        <div class="p-4 bg-slate-900/95 border-t border-slate-800 flex flex-col sm:flex-row items-center justify-between gap-3 text-xs">
          <div class="text-slate-300 flex items-center space-x-2">
            <span class="w-2.5 h-2.5 rounded-full bg-emerald-400 animate-pulse"></span>
            <span><strong>GPS Coordinates:</strong> 28.0604817° N, 76.4195232° E</span>
          </div>
          <a href="https://www.google.com/maps/place/Devatwal+Crane+Service/@28.0604817,76.4195232" target="_blank" rel="noopener noreferrer" class="text-amber-400 hover:text-amber-300 font-bold flex items-center space-x-1">
            <span>Official Google Maps Listing</span>
            <i data-lucide="arrow-up-right" class="w-3.5 h-3.5"></i>
          </a>
        </div>

      </div>

    </div>
  </section>"""

html = re.sub(map_box_pattern, new_map_box, html, flags=re.DOTALL)
print("Updated map section!")

with open(r"C:\Users\heman\Desktop\devatwal-crane-service\public\index.html", "w", encoding="utf-8") as f:
    f.write(html)

print("Saved public/index.html successfully!")
