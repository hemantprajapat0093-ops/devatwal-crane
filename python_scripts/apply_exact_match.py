import re

# Read current index.html
with open(r"C:\Users\heman\Desktop\devatwal-crane-service\public\index.html", "r", encoding="utf-8") as f:
    current_html = f.read()

# Header and Hero replacement block
new_header_and_hero = """  <!-- ================= SLEEK WIDE NAVBAR (EXACT MATCH TO REFERENCE SCREENSHOT) ================= -->
  <!-- Left: Circular Crane Logo | "Devatwal" (white) "Crane Service" (yellow) + "Heavy Lifting Solutions | Since 2016" -->
  <!-- Center: Home (active with yellow underline), Book Slot, Leadership, Contact -->
  <!-- Right: [Calendar] Reserve Crane (solid bright yellow rounded pill button) -->
  <header class="sticky top-0 z-40 bg-[#070D18]/95 backdrop-blur-2xl border-b border-slate-800/90 shadow-xl">
    <div class="max-w-[96rem] mx-auto px-6 sm:px-10 lg:px-14">
      <div class="flex items-center justify-between h-24">
        
        <!-- Left: Logo & Two-Line Title -->
        <a href="#hero" class="flex items-center space-x-4 group cursor-pointer focus:outline-none shrink-0">
          <!-- Circular Logo (Exact from Reference) -->
          <div class="w-16 h-16 rounded-full p-0.5 bg-gradient-to-tr from-amber-400 via-yellow-300 to-amber-500 shadow-[0_0_20px_rgba(245,158,11,0.5)] group-hover:scale-105 transition-transform shrink-0">
            <div class="w-full h-full rounded-full overflow-hidden bg-slate-950 flex items-center justify-center border border-slate-800">
              <img src="/images/exact_header_logo.png" alt="Devatwal Crane Service" class="w-full h-full object-cover">
            </div>
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

        <!-- Middle Navigation: Home, Book Slot, Leadership, Contact -->
        <nav class="hidden md:flex items-center space-x-10 text-base font-medium">
          <a href="#hero" class="text-amber-400 font-bold border-b-2 border-amber-400 pb-1 tracking-wide">
            Home
          </a>
          <a href="#booking-section" class="text-white hover:text-amber-400 transition-colors tracking-wide font-medium">
            Book Slot
          </a>
          <a href="#leadership" class="text-white hover:text-amber-400 transition-colors tracking-wide font-medium">
            Leadership
          </a>
          <a href="#contact" class="text-white hover:text-amber-400 transition-colors tracking-wide font-medium">
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
        <a href="#fleet" class="py-2.5 px-3 hover:bg-slate-900 rounded-lg">Crane Fleet</a>
        <a href="#leadership" class="py-2.5 px-3 hover:bg-slate-900 rounded-lg">Leadership</a>
        <a href="#contact" class="py-2.5 px-3 hover:bg-slate-900 rounded-lg">Contact</a>
      </div>
    </div>
  </header>

  <!-- ================= HERO SECTION (EXACT MATCH TO REFERENCE SCREENSHOT) ================= -->
  <!-- Left: 3 Pills (Trusted Partner, On-Time Service, 5.0+ Rating) -->
  <!-- Skewed Yellow Parallelogram: Devatwal Crane Service -->
  <!-- Slanted Headline: Lift Higher, (white) / Go Further. (yellow with curved swoosh) -->
  <!-- Tagline: Safe Lifting • Strong Support • Always Reliable -->
  <!-- Paragraph: Operating since 2016... -->
  <!-- Buttons: [Calendar] Book Crane Slot Online -> | [Mail] Get a Quote -->
  <!-- Right: Authentic ACE 12XW Unit 7 Crane hoisting concrete slab at sunset with cursive "Your Trusted Crane Partner" -->
  <section id="hero" class="hero-exact-banner relative flex items-center overflow-hidden border-b border-slate-800/80">
    
    <div class="max-w-[96rem] w-full mx-auto px-6 sm:px-10 lg:px-14 py-12 lg:py-20 relative z-10">
      <div class="grid grid-cols-1 lg:grid-cols-12 gap-8 items-center">
        
        <!-- Left Hero Content -->
        <div class="lg:col-span-7 space-y-6 text-left">
          
          <!-- Top Row: 3 Rounded Badges/Pills -->
          <div class="flex flex-wrap items-center gap-3">
            <div class="inline-flex items-center space-x-2 px-4 py-2 rounded-full bg-slate-950/75 backdrop-blur-md border border-slate-700/80 text-xs sm:text-sm font-semibold text-white shadow-md">
              <i data-lucide="shield-check" class="w-4 h-4 text-amber-400 shrink-0"></i>
              <span>Trusted Partner</span>
            </div>
            <div class="inline-flex items-center space-x-2 px-4 py-2 rounded-full bg-slate-950/75 backdrop-blur-md border border-slate-700/80 text-xs sm:text-sm font-semibold text-white shadow-md">
              <i data-lucide="cog" class="w-4 h-4 text-amber-400 shrink-0"></i>
              <span>On-Time Service</span>
            </div>
            <div class="inline-flex items-center space-x-2 px-4 py-2 rounded-full bg-slate-950/75 backdrop-blur-md border border-slate-700/80 text-xs sm:text-sm font-semibold text-white shadow-md">
              <i data-lucide="star" class="w-4 h-4 text-amber-400 fill-amber-400 shrink-0"></i>
              <span>5.0+ Client Rating</span>
            </div>
          </div>

          <!-- Angled Yellow Ribbon Parallelogram Badge -->
          <div class="inline-block transform -skew-x-12 bg-amber-400 px-5 py-1.5 rounded shadow-lg">
            <div class="transform skew-x-12 text-sm sm:text-base font-black text-black italic tracking-wide">
              Devatwal Crane Service
            </div>
          </div>

          <!-- Slanted Italic Headline: "Lift Higher," / "Go Further." with Swoosh -->
          <div class="space-y-1">
            <h1 class="hero-slanted-main-title text-5xl sm:text-7xl lg:text-8xl leading-tight">
              <span class="text-white block">Lift Higher,</span>
              <span class="text-amber-400 block relative">
                Go Further.
                <span class="block w-48 sm:w-80 h-2 sm:h-2.5 bg-gradient-to-r from-amber-400 via-yellow-300 to-transparent rounded-full mt-1.5 transform -rotate-1"></span>
              </span>
            </h1>
          </div>

          <!-- Tagline -->
          <div>
            <p class="text-base sm:text-xl font-bold italic text-white tracking-wide flex flex-wrap items-center gap-2 drop-shadow">
              <span>Safe Lifting</span>
              <span class="text-amber-400 font-black">•</span>
              <span>Strong Support</span>
              <span class="text-amber-400 font-black">•</span>
              <span>Always Reliable</span>
            </p>
          </div>

          <!-- Description Paragraph -->
          <p class="text-slate-200 text-sm sm:text-base leading-relaxed max-w-xl font-normal drop-shadow">
            Operating since 2016, Devatwal Crane Service delivers industrial-grade heavy lifting solutions across India. From construction to industrial projects, our powerful cranes get the job done — safely and efficiently.
          </p>

          <!-- Two Buttons: Book Crane Slot Online -> | Get a Quote -->
          <div class="flex flex-col sm:flex-row items-stretch sm:items-center gap-4 pt-3">
            <a href="#booking-section" class="flex items-center justify-center space-x-3 bg-gradient-to-r from-amber-400 to-yellow-400 hover:from-amber-300 hover:to-yellow-300 text-black font-extrabold px-8 py-4 rounded-full text-sm sm:text-base shadow-[0_4px_25px_rgba(245,158,11,0.5)] transition-all transform hover:-translate-y-0.5">
              <i data-lucide="calendar" class="w-5 h-5 text-black"></i>
              <span>Book Crane Slot Online</span>
              <i data-lucide="arrow-right" class="w-4 h-4 text-black"></i>
            </a>

            <button class="btn-send-email flex items-center justify-center space-x-2.5 bg-slate-950/70 hover:bg-slate-900 text-white font-bold border-2 border-slate-500 hover:border-slate-300 px-8 py-4 rounded-full text-sm sm:text-base backdrop-blur-md transition-all shadow-lg transform hover:-translate-y-0.5">
              <i data-lucide="mail" class="w-5 h-5 text-white"></i>
              <span>Get a Quote</span>
            </button>
          </div>

        </div>

        <!-- Right Side Spacer (Allows the background crane & sunset to shine brilliantly on desktop) -->
        <div class="hidden lg:block lg:col-span-5 h-[560px] pointer-events-none"></div>

      </div>
    </div>
  </section>
"""

# Find where <header starts and where </section> for hero ends in current_html
header_start = current_html.find("<header")
hero_end = current_html.find("</section>") + len("</section>")

if header_start != -1 and hero_end != -1:
    final_html = current_html[:header_start] + new_header_and_hero + current_html[hero_end:]
    with open(r"C:\Users\heman\Desktop\devatwal-crane-service\public\index.html", "w", encoding="utf-8") as out:
        out.write(final_html)
    print("public/index.html updated successfully with exact match header & hero!")
else:
    print("Error locating header or hero section!")
