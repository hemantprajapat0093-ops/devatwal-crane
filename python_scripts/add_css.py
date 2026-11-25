import re

css_additions = """
/* Exact Match Hero Banner Styling (From Reference Screenshot) */
.hero-exact-banner {
  position: relative;
  min-height: 640px;
  background-color: #070d18;
  background-image: 
    linear-gradient(to right, rgba(7, 13, 24, 0.98) 0%, rgba(7, 13, 24, 0.88) 40%, rgba(7, 13, 24, 0.3) 65%, transparent 100%),
    url('/images/hero_perfect_clean_backdrop.jpg');
  background-position: right center;
  background-size: cover;
  background-repeat: no-repeat;
}

@media (max-width: 1024px) {
  .hero-exact-banner {
    background-image: 
      linear-gradient(to bottom, rgba(7, 13, 24, 0.95) 0%, rgba(7, 13, 24, 0.85) 60%, rgba(7, 13, 24, 0.95) 100%),
      url('/images/hero_perfect_clean_backdrop.jpg');
    background-position: center top;
  }
}

.hero-slanted-main-title {
  font-family: 'Plus Jakarta Sans', sans-serif;
  font-style: italic;
  font-weight: 900;
  letter-spacing: -0.025em;
  text-shadow: 0 4px 20px rgba(0, 0, 0, 0.8);
}
"""

with open(r"C:\Users\heman\Desktop\devatwal-crane-service\public\css\style.css", "a", encoding="utf-8") as f:
    f.write("\n" + css_additions)

print("Updated style.css with hero-exact-banner styles!")
