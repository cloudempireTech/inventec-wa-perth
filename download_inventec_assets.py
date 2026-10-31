import urllib.request
import os
from PIL import Image

output_dir = r"C:\Users\dasan\.gemini\antigravity\scratch\inventec-wa-perth\assets\images"
os.makedirs(output_dir, exist_ok=True)

# Curated high-res Unsplash IDs for precision CNC machining, metal fabrication, welding, CMM
assets = [
    ("cnc-5axis-milling-spindle.jpg", "photo-1581092160607-ee22621dd758"),
    ("heavy-lathe-turning.jpg", "photo-1504917599217-d4dc5ebe6122"),
    ("wire-edm-precision.jpg", "photo-1581092335397-9583fe92d232"),
    ("certified-welding-fabrication.jpg", "photo-1504328345606-18bbc8c9d7d1"),
    ("cmm-inspection-quality.jpg", "photo-1581091226825-a6a2a5aee158"),
    ("mining-heavy-equipment-parts.jpg", "photo-1581092580497-e0d23cbdf1dc"),
    ("machining-workshop-floor.jpg", "photo-1581092795360-fd1ca04f0952"),
    ("custom-metal-flanges-fittings.jpg", "photo-1581092162384-8987c1d64718"),
    ("subsea-oil-gas-machining.jpg", "photo-1581092583537-20d51b4b4f1b"),
    ("surface-grinding-finishing.jpg", "photo-1581092334651-ddf26d9a09d0")
]

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
}

for filename, photo_id in assets:
    target_path = os.path.join(output_dir, filename)
    url = f"https://images.unsplash.com/{photo_id}?auto=format&fit=crop&w=1200&q=80"
    print(f"Downloading {filename}...")
    try:
        req = urllib.request.Request(url, headers=headers)
        tmp_path = target_path + ".tmp"
        with urllib.request.urlopen(req) as resp, open(tmp_path, 'wb') as f:
            f.write(resp.read())
        
        img = Image.open(tmp_path)
        img = img.convert('RGB')
        img.save(target_path, 'JPEG', quality=85, optimize=True)
        if os.path.exists(tmp_path):
            os.remove(tmp_path)
        size_kb = os.path.getsize(target_path) / 1024
        print(f"  Saved {filename} ({size_kb:.1f} KB)")
    except Exception as e:
        print(f"  Error downloading {filename}: {e}")

print("Image download and optimization complete!")
