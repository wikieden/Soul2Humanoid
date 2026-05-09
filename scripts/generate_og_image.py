#!/usr/bin/env python3
"""Generate og-image.png (1200x630) social sharing card for Soul2Humanoid."""
from PIL import Image, ImageDraw, ImageFont
import os

# Palette
BG = (13, 17, 23)          # #0D1117
CARD = (22, 27, 34)        # #161B22
BORDER = (48, 54, 61)      # #30363D
ORANGE = (247, 129, 102)   # #F78166
WHITE = (230, 237, 243)    # #E6EDF3
MUTED = (139, 148, 158)    # #8B949E
BLUE = (88, 166, 255)      # #58A6FF
GREEN = (63, 185, 80)      # #3FB950
PURPLE = (210, 168, 255)   # #D2A8FF
LIGHT_ORANGE = (255, 166, 87)  # #FFA657
LIGHT_BLUE = (121, 192, 255)   # #79C0FF

W, H = 1200, 630

def get_font(size, bold=False):
    """Try CJK font, fallback to system."""
    # macOS CJK fonts
    font_paths = [
        '/System/Library/Fonts/PingFang.ttc',
        '/System/Library/Fonts/Hiragino Sans GB.ttc',
        '/System/Library/Fonts/STHeiti Medium.ttc',
    ]
    for fp in font_paths:
        if os.path.exists(fp):
            try:
                return ImageFont.truetype(fp, size)
            except Exception:
                pass
    try:
        return ImageFont.load_default(size=size)
    except Exception:
        return None

def hex_to_rgb(h):
    h = h.lstrip('#')
    return tuple(int(h[i:i+2], 16) for i in (0, 2, 4))

def draw_rounded_rect(draw, xy, radius, fill, outline=None, width=1):
    x1, y1, x2, y2 = xy
    r = radius
    draw.rectangle([x1+r, y1, x2-r, y2], fill=fill, outline=outline, width=width)
    draw.rectangle([x1, y1+r, x2, y2-r], fill=fill, outline=outline, width=width)
    draw.pieslice([x1, y1, x1+2*r, y1+2*r], 180, 270, fill=fill, outline=fill)
    draw.pieslice([x2-2*r, y1, x2, y1+2*r], 270, 360, fill=fill, outline=fill)
    draw.pieslice([x1, y2-2*r, x1+2*r, y2], 90, 180, fill=fill, outline=fill)
    draw.pieslice([x2-2*r, y2-2*r, x2, y2], 0, 90, fill=fill, outline=fill)

img = Image.new('RGB', (W, H), BG)
draw = ImageDraw.Draw(img)

# Background card
draw_rounded_rect(draw, (14, 14, W-14, H-14), 16, CARD, BORDER, 2)

# Top accent bar
draw.rectangle([14, 14, W-14, 28], fill=ORANGE)

# Title
font_title = get_font(58)
font_sub = get_font(24)
font_tech = get_font(14)
font_muted = get_font(13)
font_bottom = get_font(14)

draw.text((44, 44), 'Soul2Humanoid', fill=WHITE, font=font_title)
draw.text((44, 112), '具身大脑技术方案系统性调研', fill=ORANGE, font=font_sub)

# Divider
draw.line([(44, 155), (W-44, 155)], fill=BORDER, width=2)

# Subtitle tech keywords
kw = '聚焦 VLA 端到端  ·  Flow Matching  ·  数据飞轮  ·  Sim2Real  ·  人形机器人算法架构'
draw.text((44, 168), kw, fill=MUTED, font=font_muted)

# Company grid
companies = [
    ('Figure AI', 'VLA · BotQ · Helix', BLUE),
    ('Physical Intelligence', 'π0.7 · Flow Matching', ORANGE),
    ('Tesla Optimus', 'FSD · End-to-End NN', GREEN),
    ('Boston Dynamics', 'MPC+RL · Atlas', PURPLE),
    ('Unitree', 'Open-source · RL', LIGHT_ORANGE),
    ('1X Technologies', 'NEO · World Model', LIGHT_BLUE),
]

cols, rows = 3, 2
cell_w, cell_h = 370, 110
pad_x, pad_y = 25, 25
start_x, start_y = 44, 215

for i, (name, tech, color) in enumerate(companies):
    col = i % cols
    row = i // cols
    x = start_x + col * (cell_w + pad_x)
    y = start_y + row * (cell_h + pad_y)

    draw_rounded_rect(draw, (x, y, x+cell_w, y+cell_h), 10, (33, 38, 45), BORDER, 1)
    draw.text((x+16, y+14), name, fill=color, font=font_tech)
    draw.text((x+16, y+50), tech, fill=MUTED, font=font_muted)

# Bottom bar
draw.rectangle([14, H-60, W-14, H-14], fill=CARD)
draw.text((44, H-44), '🤖 持续更新中  ·  github.com/wikieden/Soul2Humanoid', fill=ORANGE, font=font_bottom)
draw.text((W-44, H-44), 'wikieden / Soul2Humanoid', fill=MUTED, font=font_bottom, anchor='rt')

OUTPUT = os.path.join(
    os.path.dirname(os.path.abspath(__file__)), '..', 'assets', 'og-image.png'
)
os.makedirs(os.path.dirname(OUTPUT), exist_ok=True)
img.save(OUTPUT, 'PNG', optimize=True)
print(f'Saved: {OUTPUT}')
