#!/usr/bin/env python3
"""Generate data collection method comparison charts."""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
import os

# Dark theme palette matching project style
BG = '#0D1117'
BG_CARD = '#161B22'
BORDER = '#30363D'
TEXT = '#E6EDF3'
TEXT_MUTED = '#8B949E'

OUTPUT_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'assets')
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Color palette
COLORS = {
    'ego_mocap': '#F5A623',      # Orange
    'aloha': '#4A90D9',          # Blue
    'vr': '#7ED321',             # Green
    'exoskeleton': '#9013FE',    # Purple
    'simulation': '#50E3C2',     # Cyan
    'internet': '#FF6B35',       # Coral
}

METHODS = ['Ego+MoCap+Gloves', 'ALOHA', 'VR Teleop', 'Exoskeleton', 'Simulation', 'Internet Video']
METHOD_KEYS = ['ego_mocap', 'aloha', 'vr', 'exoskeleton', 'simulation', 'internet']


def setup_dark_figure(figsize=(14, 8)):
    """Create figure with dark theme."""
    fig, ax = plt.subplots(figsize=figsize)
    fig.patch.set_facecolor(BG)
    ax.set_facecolor(BG_CARD)
    ax.tick_params(colors=TEXT)
    ax.xaxis.label.set_color(TEXT)
    ax.yaxis.label.set_color(TEXT)
    ax.title.set_color(TEXT)
    for spine in ax.spines.values():
        spine.set_color(BORDER)
    return fig, ax


def chart_1_cost_comparison():
    """Chart 1: Hardware cost vs per-demo cost."""
    fig, ax = setup_dark_figure((14, 8))
    
    # Data
    hardware_costs = [100000, 3000, 500, 25000, 2000, 0]  # median estimates
    per_demo_costs = [50, 12, 2.5, 30, 0.5, 0.1]
    
    x = np.arange(len(METHODS))
    width = 0.35
    
    bars1 = ax.bar(x - width/2, hardware_costs, width, label='Hardware Cost ($)', 
                   color=[COLORS[k] for k in METHOD_KEYS], alpha=0.85, edgecolor=BORDER)
    
    ax2 = ax.twinx()
    ax2.set_facecolor(BG_CARD)
    ax2.tick_params(colors=TEXT)
    ax2.yaxis.label.set_color(TEXT)
    bars2 = ax2.bar(x + width/2, per_demo_costs, width, label='Per-Demo Cost ($)', 
                    color=[COLORS[k] for k in METHOD_KEYS], alpha=0.5, edgecolor=BORDER, hatch='//')
    
    ax.set_xlabel('Data Collection Method', fontsize=12, color=TEXT)
    ax.set_ylabel('Hardware Cost (USD, log scale)', fontsize=12, color=TEXT)
    ax2.set_ylabel('Per-Demo Cost (USD, log scale)', fontsize=12, color=TEXT)
    ax.set_title('Robot Data Collection: Hardware vs Per-Demo Cost', fontsize=16, fontweight='bold', color=TEXT, pad=20)
    ax.set_xticks(x)
    ax.set_xticklabels(METHODS, rotation=15, ha='right', color=TEXT)
    ax.set_yscale('log')
    ax2.set_yscale('log')
    ax.set_ylim(1, 500000)
    ax2.set_ylim(0.01, 500)
    
    # Combined legend
    lines1, labels1 = ax.get_legend_handles_labels()
    lines2, labels2 = ax2.get_legend_handles_labels()
    ax.legend(lines1 + lines2, labels1 + labels2, loc='upper right', 
              facecolor=BG_CARD, edgecolor=BORDER, labelcolor=TEXT)
    
    ax.grid(True, alpha=0.2, color=BORDER)
    plt.tight_layout()
    
    for ext in ['svg', 'png']:
        fig.savefig(os.path.join(OUTPUT_DIR, f'data-collection-cost-comparison.{ext}'), 
                    facecolor=BG, dpi=150 if ext == 'png' else 300)
    plt.close(fig)
    print("Chart 1 generated: data-collection-cost-comparison")


def chart_2_evolution_timeline():
    """Chart 2: Method evolution timeline."""
    fig, ax = setup_dark_figure((16, 7))
    
    # Timeline data: (year, method, maturity 1-10)
    timeline = [
        (2015, 'Simulation', 6),
        (2017, 'Internet Video', 4),
        (2019, 'ALOHA', 3),
        (2020, 'VR Teleop', 4),
        (2021, 'Ego+MoCap+Gloves', 7),
        (2022, 'Exoskeleton', 5),
        (2024, 'ALOHA', 8),
        (2025, 'VR Teleop', 7),
        (2025, 'Ego+MoCap+Gloves', 9),
        (2026, 'Exoskeleton', 7),
        (2026, 'Simulation', 9),
    ]
    
    method_y = {m: i for i, m in enumerate(METHODS)}
    
    for year, method, maturity in timeline:
        y = method_y[method]
        size = 100 + maturity * 80
        color = COLORS[METHOD_KEYS[y]]
        ax.scatter(year, y, s=size, c=color, alpha=0.7, edgecolors=TEXT, linewidth=1.5, zorder=5)
        ax.annotate(f'{year}', (year, y), textcoords="offset points", xytext=(0, 15), 
                   ha='center', fontsize=8, color=TEXT_MUTED)
    
    # Draw connecting lines per method
    for method in METHODS:
        y = method_y[method]
        points = [(year, maturity) for year, m, maturity in timeline if m == method]
        if len(points) > 1:
            years = [p[0] for p in points]
            ax.plot(years, [y]*len(years), '--', color=COLORS[METHOD_KEYS[y]], alpha=0.3, linewidth=1.5)
    
    ax.set_yticks(range(len(METHODS)))
    ax.set_yticklabels(METHODS, color=TEXT)
    ax.set_xlabel('Year', fontsize=12, color=TEXT)
    ax.set_title('Data Collection Methods: Evolution Timeline', fontsize=16, fontweight='bold', color=TEXT, pad=20)
    ax.set_xlim(2014, 2027)
    ax.set_ylim(-0.5, len(METHODS)-0.5)
    ax.grid(True, alpha=0.2, color=BORDER, axis='x')
    
    # Legend for bubble size
    legend_sizes = [200, 500, 900]
    legend_labels = ['Maturity: Low', 'Medium', 'High']
    legend_elements = [plt.scatter([], [], s=s, c=TEXT_MUTED, alpha=0.6, edgecolors=TEXT) for s in legend_sizes]
    ax.legend(legend_elements, legend_labels, loc='lower right', 
              facecolor=BG_CARD, edgecolor=BORDER, labelcolor=TEXT, title='Maturity')
    
    plt.tight_layout()
    for ext in ['svg', 'png']:
        fig.savefig(os.path.join(OUTPUT_DIR, f'data-collection-timeline.{ext}'), 
                    facecolor=BG, dpi=150 if ext == 'png' else 300)
    plt.close(fig)
    print("Chart 2 generated: data-collection-timeline")


def chart_3_decision_matrix():
    """Chart 3: Effectiveness vs Efficiency decision matrix."""
    fig, ax = setup_dark_figure((14, 10))
    
    # Data: (efficiency_score, effectiveness_score, flexibility_score, method)
    # Efficiency: lower cost = higher score (1-10)
    # Effectiveness: data quality (1-10)
    # Flexibility: bubble size
    matrix_data = [
        (2, 10, 6, 'Ego+MoCap+Gloves', 'ego_mocap'),
        (6, 7, 5, 'ALOHA', 'aloha'),
        (9, 5, 7, 'VR Teleop', 'vr'),
        (5, 8, 7, 'Exoskeleton', 'exoskeleton'),
        (10, 4, 9, 'Simulation', 'simulation'),
        (10, 3, 4, 'Internet Video', 'internet'),
    ]
    
    # Quadrant lines
    ax.axhline(y=6.5, color=BORDER, linestyle='--', alpha=0.5, linewidth=1)
    ax.axvline(x=6.5, color=BORDER, linestyle='--', alpha=0.5, linewidth=1)
    
    # Quadrant labels
    ax.text(3.5, 9, 'High Quality\nLow Efficiency', fontsize=10, color=TEXT_MUTED, 
            ha='center', va='center', style='italic', alpha=0.7)
    ax.text(9, 9, 'High Quality\nHigh Efficiency\n(IDEAL)', fontsize=10, color='#7ED321', 
            ha='center', va='center', fontweight='bold', alpha=0.8)
    ax.text(3.5, 3, 'Low Quality\nLow Efficiency', fontsize=10, color=TEXT_MUTED, 
            ha='center', va='center', style='italic', alpha=0.7)
    ax.text(9, 3, 'Low Quality\nHigh Efficiency', fontsize=10, color=TEXT_MUTED, 
            ha='center', va='center', style='italic', alpha=0.7)
    
    for eff, effect, flex, name, key in matrix_data:
        size = 300 + flex * 150
        color = COLORS[key]
        ax.scatter(eff, effect, s=size, c=color, alpha=0.75, edgecolors=TEXT, linewidth=2, zorder=5)
        
        # Offset labels to avoid overlap
        offsets = {
            'Ego+MoCap+Gloves': (-35, 25),
            'ALOHA': (30, 20),
            'VR Teleop': (30, -25),
            'Exoskeleton': (-40, -20),
            'Simulation': (30, 20),
            'Internet Video': (30, -25),
        }
        ox, oy = offsets[name]
        ax.annotate(name, (eff, effect), textcoords="offset points", xytext=(ox, oy),
                   ha='center', fontsize=10, color=TEXT, fontweight='bold',
                   bbox=dict(boxstyle='round,pad=0.3', facecolor=BG_CARD, edgecolor=color, alpha=0.9))
    
    ax.set_xlabel('Efficiency (Cost-effectiveness) →', fontsize=12, color=TEXT)
    ax.set_ylabel('Effectiveness (Data Quality) →', fontsize=12, color=TEXT)
    ax.set_title('Data Collection Decision Matrix\nEffectiveness vs Efficiency', 
                 fontsize=16, fontweight='bold', color=TEXT, pad=20)
    ax.set_xlim(0, 11)
    ax.set_ylim(0, 11)
    ax.grid(True, alpha=0.2, color=BORDER)
    
    # Legend for bubble size (flexibility)
    legend_sizes = [450, 1050, 1650]
    legend_labels = ['Low Flex', 'Medium', 'High Flex']
    legend_elements = [plt.scatter([], [], s=s, c=TEXT_MUTED, alpha=0.6, edgecolors=TEXT) for s in legend_sizes]
    ax.legend(legend_elements, legend_labels, loc='lower right', 
              facecolor=BG_CARD, edgecolor=BORDER, labelcolor=TEXT, title='Flexibility')
    
    plt.tight_layout()
    for ext in ['svg', 'png']:
        fig.savefig(os.path.join(OUTPUT_DIR, f'data-collection-decision-matrix.{ext}'), 
                    facecolor=BG, dpi=150 if ext == 'png' else 300)
    plt.close(fig)
    print("Chart 3 generated: data-collection-decision-matrix")


if __name__ == '__main__':
    chart_1_cost_comparison()
    chart_2_evolution_timeline()
    chart_3_decision_matrix()
    print(f"\nAll charts saved to: {OUTPUT_DIR}")
