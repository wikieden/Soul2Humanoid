#!/usr/bin/env python3
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
import os

# Dark theme palette
BG = '#0D1117'
BG_CARD = '#161B22'
BORDER = '#30363D'
TEXT = '#E6EDF3'
TEXT_MUTED = '#8B949E'

OUTPUT_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'assets')
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Data: companies and their scores across dimensions (1-10)
companies = ['Figure AI', 'Physical\nIntelligence', 'Tesla', 'Boston\nDynamics', '1X Tech', 'Unitree', 'Google\nDeepMind', 'Agility\nRobotics', 'Apptronik', 'NVIDIA\nIsaac', 'Enchanted\nTools']

# Dimensions
categories = ['AI Maturity', 'Hardware\nMaturity', 'Commercial\nProgress', 'Openness\n(Open Source)', 'Cost\nEfficiency', 'Data\nStrategy']
N = len(categories)

# Scores (subjective assessment based on research)
scores = {
    'Figure AI':          [9, 8, 6, 4, 5, 8],
    'Physical\nIntelligence': [10, 5, 6, 9, 6, 8],
    'Tesla':              [8, 7, 5, 5, 7, 10],
    'Boston\nDynamics':   [7, 10, 7, 5, 4, 7],
    '1X Tech':            [8, 7, 4, 5, 5, 6],
    'Unitree':            [5, 7, 8, 8, 10, 5],
    'Google\nDeepMind':   [9, 4, 3, 7, 6, 8],
    'Agility\nRobotics':  [3, 7, 6, 2, 6, 4],
    'Apptronik':          [5, 8, 3, 6, 4, 5],
    'NVIDIA\nIsaac':      [8, 9, 8, 5, 3, 7],
    'Enchanted\nTools':   [4, 5, 2, 2, 5, 3],
}

colors = ['#F5A623', '#4A90D9', '#D0021B', '#9013FE', '#7ED321', '#50E3C2', '#4285F4', '#FF6B35', '#00CED1', '#76B900', '#E8A0BF']

# Create radar chart
fig, ax = plt.subplots(figsize=(12, 10), subplot_kw=dict(polar=True))

angles = [n / float(N) * 2 * np.pi for n in range(N)]
angles += angles[:1]

for i, (company, score) in enumerate(scores.items()):
    values = score + score[:1]
    ax.plot(angles, values, 'o-', linewidth=2, label=company, color=colors[i])
    ax.fill(angles, values, alpha=0.08, color=colors[i])

ax.set_xticks(angles[:-1])
ax.set_xticklabels(categories, size=12, fontweight='bold')
ax.set_ylim(0, 10)
ax.set_yticks([2, 4, 6, 8, 10])
ax.set_yticklabels(['2', '4', '6', '8', '10'], size=11, color=TEXT_MUTED)
ax.grid(True, linestyle='--', alpha=0.5)

plt.title('Embodied AI Companies: Multi-Dimensional Comparison', size=18, fontweight='bold', pad=30)
plt.legend(loc='upper right', bbox_to_anchor=(1.35, 1.1), fontsize=13, frameon=True, fancybox=True, shadow=True)
plt.tight_layout()

base = os.path.join(OUTPUT_DIR, 'company-comparison-radar')
fig.savefig(base + '.svg', format='svg', bbox_inches='tight', facecolor=BG, edgecolor='none')
fig.savefig(base + '.png', format='png', bbox_inches='tight', facecolor=BG, edgecolor='none', dpi=200)
plt.close(fig)
print(f"Saved: {base}.svg + .png")

# Create a horizontal bar chart for specific metrics
fig2, ax2 = plt.subplots(figsize=(14, 8))
metrics = ['AI Maturity', 'Hardware Maturity', 'Commercial Progress', 'Openness', 'Cost Efficiency', 'Data Strategy']
company_list = ['Figure AI', 'PI', 'Tesla', 'BD', '1X Tech', 'Unitree', 'DeepMind', 'Agility', 'Apptronik', 'NVIDIA', 'Enchanted']
data_matrix = [
    [9, 8, 6, 4, 5, 8],   # Figure AI
    [10, 5, 6, 9, 6, 8],  # PI
    [8, 7, 5, 5, 7, 10],  # Tesla
    [7, 10, 7, 5, 4, 7],  # Boston Dynamics
    [8, 7, 4, 5, 5, 6],   # 1X Tech
    [5, 7, 8, 8, 10, 5],  # Unitree
    [9, 4, 3, 7, 6, 8],   # DeepMind
    [3, 7, 6, 2, 6, 4],   # Agility
    [5, 8, 3, 6, 4, 5],   # Apptronik
    [8, 9, 8, 5, 3, 7],   # NVIDIA Isaac
    [4, 5, 2, 2, 5, 3],   # Enchanted Tools
]

y_pos = np.arange(len(metrics))
bar_height = 0.07
for i, (company, color) in enumerate(zip(company_list, colors)):
    ax2.barh(y_pos + i * bar_height, data_matrix[i], bar_height, label=company, color=color, alpha=0.85, edgecolor='white', linewidth=0.5)

ax2.set_yticks(y_pos + bar_height * 5)
ax2.set_yticklabels(metrics, fontsize=13, fontweight='bold')
ax2.set_xlim(0, 11)
ax2.set_xlabel('Score (1-10)', fontsize=13)
ax2.set_title('Embodied AI Companies: Capability Comparison by Dimension', fontsize=18, fontweight='bold', pad=20)
ax2.legend(loc='lower right', fontsize=13, frameon=True, fancybox=True)
ax2.spines['top'].set_visible(False)
ax2.spines['right'].set_visible(False)
ax2.grid(axis='x', linestyle='--', alpha=0.3)

plt.tight_layout()
base2 = os.path.join(OUTPUT_DIR, 'company-comparison-bars')
fig2.savefig(base2 + '.svg', format='svg', bbox_inches='tight', facecolor=BG, edgecolor='none')
fig2.savefig(base2 + '.png', format='png', bbox_inches='tight', facecolor=BG, edgecolor='none', dpi=200)
plt.close(fig2)
print(f"Saved: {base2}.svg + .png")

print("All comparison charts generated successfully!")
