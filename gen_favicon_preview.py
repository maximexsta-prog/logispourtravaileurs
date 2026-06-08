from PIL import Image, ImageDraw

def draw_icon(size, bg_color="#FFFFFF"):
    s = size / 32
    img = Image.new("RGBA", (size, size), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)

    # White background
    d.rectangle([0, 0, size, size], fill=bg_color)

    # Chimney (drawn first so roof overlaps its base)
    cx = [22*s, 4*s, 25*s, 14*s]
    d.rectangle(cx, fill="#1A2744")

    # Roof: wide angular chevron with thickness
    # Outer: (0,19) -> (16,6) -> (32,19)
    # Inner: (29,21) -> (16,10) -> (3,21)
    roof = [
        (0*s,  19*s),
        (16*s,  6*s),
        (32*s, 19*s),
        (29*s, 21*s),
        (16*s, 10*s),
        (3*s,  21*s),
    ]
    d.polygon(roof, fill="#1A2744")

    # 2x2 gold windows centered below roof
    wc = "#C4982A"
    d.rectangle([12*s, 22*s, 15*s, 25*s], fill=wc)
    d.rectangle([17*s, 22*s, 20*s, 25*s], fill=wc)
    d.rectangle([12*s, 26*s, 15*s, 29*s], fill=wc)
    d.rectangle([17*s, 26*s, 20*s, 29*s], fill=wc)

    return img

# --- Preview sheet ---
sizes   = [180, 64, 32, 16]
padding = 32
margin  = 40
max_h   = 180
label_h = 22

sheet_w = sum(s + padding for s in sizes) + padding
sheet_h = max_h + margin * 2 + label_h

sheet = Image.new("RGB", (sheet_w, sheet_h), "#E8E8E8")
d = ImageDraw.Draw(sheet)

x = padding
for sz in sizes:
    icon = draw_icon(sz)
    y = margin + (max_h - sz) // 2
    sheet.paste(icon, (x, y), icon)
    label = f"{sz}px"
    d.text((x + sz // 2 - len(label) * 3, margin + max_h + 6), label, fill="#666666")
    x += sz + padding

out = r"C:\Users\Main\Documents\GitHub\logispourtravailleurs\favicon-preview.png"
sheet.save(out)
print("saved:", out)
