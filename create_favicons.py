import os
from PIL import Image, ImageDraw

base_dir = r"C:\Users\dasan\.gemini\antigravity\scratch\inventec-wa-perth\assets\images"
os.makedirs(base_dir, exist_ok=True)

# 1. Create SVG Logo & Favicon
svg_logo = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512" width="512" height="512">
  <defs>
    <linearGradient id="cyanGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#38BDF8"/>
      <stop offset="50%" stop-color="#0284C7"/>
      <stop offset="100%" stop-color="#0369A1"/>
    </linearGradient>
    <radialGradient id="darkBg" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#1e293b"/>
      <stop offset="100%" stop-color="#0a0f1d"/>
    </radialGradient>
  </defs>
  <rect width="512" height="512" rx="110" fill="url(#darkBg)"/>
  <circle cx="256" cy="256" r="210" fill="none" stroke="url(#cyanGrad)" stroke-width="8" stroke-dasharray="16 12"/>
  
  <!-- Precision Machining Hex Nut & Spindle Icon -->
  <polygon points="256,90 380,162 380,306 256,378 132,306 132,162" fill="none" stroke="url(#cyanGrad)" stroke-width="14" stroke-linejoin="round"/>
  <circle cx="256" cy="234" r="62" fill="none" stroke="#F59E0B" stroke-width="12"/>
  
  <!-- Stylized "I" Gear Spindle -->
  <rect x="242" y="140" width="28" height="188" rx="8" fill="#FFFFFF"/>
  <rect x="216" y="140" width="80" height="26" rx="6" fill="#FFFFFF"/>
  <rect x="216" y="302" width="80" height="26" rx="6" fill="#FFFFFF"/>
</svg>'''

with open(os.path.join(base_dir, "logo.svg"), "w", encoding="utf-8") as f:
    f.write(svg_logo)

with open(os.path.join(base_dir, "favicon.svg"), "w", encoding="utf-8") as f:
    f.write(svg_logo)

# 2. Render PNG 512x512
size = 512
img = Image.new("RGBA", (size, size), (0, 0, 0, 0))
draw = ImageDraw.Draw(img)

# Background
draw.rounded_rectangle([16, 16, 496, 496], radius=110, fill=(10, 15, 29, 255))
draw.ellipse([36, 36, 476, 476], outline=(2, 132, 199, 180), width=8)

# Hexagon
cyan = (56, 189, 248, 255)
hex_points = [(256, 100), (380, 172), (380, 316), (256, 388), (132, 316), (132, 172)]
draw.polygon(hex_points, outline=cyan, fill=None)
draw.line(hex_points + [hex_points[0]], fill=cyan, width=12)

# Central amber circle
draw.ellipse([200, 188, 312, 300], outline=(245, 158, 11, 255), width=10)

# Machining I-pillar
white = (255, 255, 255, 255)
draw.rounded_rectangle([242, 140, 270, 348], radius=6, fill=white)
draw.rounded_rectangle([216, 140, 296, 166], radius=6, fill=white)
draw.rounded_rectangle([216, 322, 296, 348], radius=6, fill=white)

logo_512_path = os.path.join(base_dir, "logo-512.png")
img.save(logo_512_path, "PNG")

# 3. Apple touch icon 180x180
apple_icon = img.resize((180, 180), Image.Resampling.LANCZOS)
apple_icon.save(os.path.join(base_dir, "apple-touch-icon.png"), "PNG")

# 4. Favicon 32x32
fav_32 = img.resize((32, 32), Image.Resampling.LANCZOS)
fav_32.save(os.path.join(base_dir, "favicon-32x32.png"), "PNG")

# 5. Favicon ico
img.resize((32, 32), Image.Resampling.LANCZOS).save(os.path.join(base_dir, "favicon.ico"), format="ICO")

print("All Inventec favicons successfully generated!")
