"""数据策略对比图 -- 各公司数据飞轮可视化"""
import matplotlib.pyplot as plt
import numpy as np

BG = '#0D1117'
BG_CARD = '#161B22'
BORDER = '#30363D'
TEXT = '#E6EDF3'
TEXT_MUTED = '#8B949E'
GRID = '#21262D'

companies = [
    'Figure AI', 'Physical Intelligence', 'Tesla Optimus',
    'Boston Dynamics', '1X Technologies', 'Unitree',
    'Google DeepMind', 'Agility Robotics', 'Apptronik',
    'NVIDIA Isaac', 'Enchanted Tools'
]

flywheel = [9, 10, 10, 6, 7, 6, 8, 4, 5, 7, 3]
real_world_data =   [8, 7, 10, 5, 8, 5, 4, 6, 5, 3, 4]
synthetic_data =    [9, 8, 7, 6, 5, 7, 8, 3, 6, 10, 3]
teleop_data =       [7, 6, 4, 7, 9, 7, 3, 4, 6, 2, 3]
cross_embodiment =  [3, 10, 2, 4, 2, 2, 9, 1, 7, 6, 1]
human_video =       [4, 9, 5, 3, 3, 2, 5, 1, 3, 4, 2]

x = np.arange(len(companies))
width = 0.15

fig, ax = plt.subplots(figsize=(16, 8), facecolor=BG)
ax.set_facecolor(BG)

ax.bar(x - 2*width, real_world_data, width, label='Real-World Data', color='#58A6FF', edgecolor=BORDER, linewidth=0.5)
ax.bar(x - width, synthetic_data, width, label='Synthetic Data', color='#3FB950', edgecolor=BORDER, linewidth=0.5)
ax.bar(x, teleop_data, width, label='Teleoperation Data', color='#D29922', edgecolor=BORDER, linewidth=0.5)
ax.bar(x + width, cross_embodiment, width, label='Cross-Embodiment', color='#A371F7', edgecolor=BORDER, linewidth=0.5)
ax.bar(x + 2*width, human_video, width, label='Human Video Transfer', color='#F778BA', edgecolor=BORDER, linewidth=0.5)

ax.set_ylabel('Capability / Investment Level (0-10)', fontsize=12, color=TEXT, fontweight='bold')
ax.set_title('Data Strategy Comparison -- Company Data Flywheels', fontsize=18, color=TEXT, fontweight='bold', pad=20)
ax.set_xticks(x)
ax.set_xticklabels(companies, fontsize=9, color=TEXT)
ax.tick_params(axis='y', colors=TEXT)
ax.set_ylim(0, 12)
ax.legend(loc='upper right', fontsize=10, facecolor=BG_CARD, edgecolor=BORDER, labelcolor=TEXT)
ax.grid(axis='y', color=GRID, linestyle='--', alpha=0.7)
for spine in ax.spines.values():
    spine.set_color(BORDER)

for i, (xi, fi) in enumerate(zip(x, flywheel)):
    ax.annotate(f'FW:{fi}', xy=(xi, 11), ha='center', fontsize=7, color=TEXT_MUTED, fontweight='bold')

plt.tight_layout()
plt.savefig('assets/data-strategy-comparison.svg', format='svg', dpi=200, facecolor=BG)
plt.savefig('assets/data-strategy-comparison.png', format='png', dpi=200, facecolor=BG)
print('Saved: assets/data-strategy-comparison.svg + .png')

# 第二个图：数据飞轮流程图
fig2, ax2 = plt.subplots(figsize=(14, 10), facecolor=BG)
ax2.set_facecolor(BG)
ax2.set_xlim(0, 10)
ax2.set_ylim(0, 10)
ax2.axis('off')

examples = [
    ('Tesla / Figure AI (部署驱动型)', 2.5, 8.5,
     ['Deploy in Factory', 'Collect Real Data', 'Retrain Model', 'Deploy Better Robot'],
     ['#58A6FF', '#3FB950', '#D29922', '#58A6FF']),
    ('Physical Intelligence (学习驱动型)', 7.5, 8.5,
     ['Online RL', 'Policy Improvement', 'Deploy', 'More Experience'],
     ['#A371F7', '#F778BA', '#58A6FF', '#A371F7']),
    ('NVIDIA Isaac (仿真驱动型)', 2.5, 3.5,
     ['Omniverse Sim', 'Generate Synthetic Data', 'Train in Isaac Lab', 'Deploy on Jetson'],
     ['#3FB950', '#58A6FF', '#D29922', '#F778BA']),
    ('Agility / Enchanted (传统控制型)', 7.5, 3.5,
     ['Engineer Programs', 'Deploy', 'Monitor Faults', 'Manual Fix'],
     ['#8B949E', '#58A6FF', '#D29922', '#8B949E']),
]

for title, cx, cy, steps, colors in examples:
    ax2.text(cx, cy + 1.2, title, ha='center', va='bottom', fontsize=12, color=TEXT, fontweight='bold')
    angles = np.linspace(0, 2*np.pi, 5)[:-1]
    radius = 1.0
    for i, (angle, step, color) in enumerate(zip(angles, steps, colors)):
        sx = cx + radius * np.cos(angle)
        sy = cy + radius * np.sin(angle)
        circle = plt.Circle((sx, sy), 0.35, color=BG_CARD, ec=color, linewidth=2, zorder=3)
        ax2.add_patch(circle)
        ax2.text(sx, sy, step, ha='center', va='center', fontsize=7, color=TEXT)
        next_angle = angles[(i+1) % len(angles)]
        nx = cx + radius * np.cos(next_angle)
        ny = cy + radius * np.sin(next_angle)
        ax2.annotate('', xy=(nx, ny), xytext=(sx, sy),
                     arrowprops=dict(arrowstyle='->', color=color, lw=1.5, connectionstyle='arc3,rad=0.2'),
                     zorder=2)

ax2.set_title('Data Flywheel Patterns by Company Type', fontsize=18, color=TEXT, fontweight='bold', pad=20)
plt.tight_layout()
plt.savefig('assets/data-flywheel-patterns.svg', format='svg', dpi=200, facecolor=BG)
plt.savefig('assets/data-flywheel-patterns.png', format='png', dpi=200, facecolor=BG)
print('Saved: assets/data-flywheel-patterns.svg + .png')
print('All data strategy charts generated.')
