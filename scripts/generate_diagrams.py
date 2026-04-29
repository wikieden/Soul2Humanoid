#!/usr/bin/env python3
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, Arc
import numpy as np
import os

# Dark theme palette
BG = '#0D1117'
BG_CARD = '#161B22'
BORDER = '#30363D'
TEXT = '#E6EDF3'
TEXT_MUTED = '#8B949E'

PI_ORANGE = '#F5A623'
PI_BLUE = '#4A90D9'
PI_GREEN = '#7ED321'
PI_PURPLE = '#9013FE'
PI_RED = '#D0021B'

OUTPUT_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'assets', 'physical-intelligence')
os.makedirs(OUTPUT_DIR, exist_ok=True)

def save_both(fig, name):
    base = os.path.join(OUTPUT_DIR, name)
    fig.savefig(base, format='svg', bbox_inches='tight', facecolor=BG, edgecolor='none')
    fig.savefig(base.replace('.svg', '.png'), format='png', bbox_inches='tight', facecolor=BG, edgecolor='none', dpi=200)
    plt.close(fig)
    print(f"Saved: {base} + .png")

def draw_diagram1():
    fig, ax = plt.subplots(figsize=(14, 8))
    ax.set_xlim(0, 14); ax.set_ylim(0, 8); ax.axis('off'); fig.patch.set_facecolor(BG)
    ax.text(7, 7.6, 'Physical Intelligence VLA System Architecture', fontsize=20, fontweight='bold', ha='center', va='center', color=TEXT)
    ax.text(7, 7.2, 'General-Purpose Vision-Language-Action Foundation Model', fontsize=13, ha='center', va='center', color=TEXT_MUTED, style='italic')
    left_box = FancyBboxPatch((0.5, 4.2), 3.2, 2.2, boxstyle="round,pad=0.05,rounding_size=0.15", facecolor=PI_BLUE, edgecolor=BORDER, linewidth=2, alpha=0.9)
    ax.add_patch(left_box)
    ax.text(2.1, 5.95, 'Multimodal Input', fontsize=13, fontweight='bold', ha='center', va='center', color='white')
    ax.text(2.1, 5.55, 'Camera Images', fontsize=10, ha='center', va='center', color='white')
    ax.text(2.1, 5.25, 'Language Instructions', fontsize=10, ha='center', va='center', color='white')
    ax.text(2.1, 4.95, 'Action History', fontsize=10, ha='center', va='center', color='white')
    ax.text(2.1, 4.65, 'Visual Subgoals', fontsize=10, ha='center', va='center', color='white')
    ax.annotate('', xy=(4.8, 5.3), xytext=(3.8, 5.3), arrowprops=dict(arrowstyle='->', color=TEXT_MUTED, lw=2))
    center_box = FancyBboxPatch((4.8, 4.0), 4.4, 2.6, boxstyle="round,pad=0.05,rounding_size=0.15", facecolor=PI_ORANGE, edgecolor=BORDER, linewidth=2, alpha=0.9)
    ax.add_patch(center_box)
    ax.text(7.0, 6.15, 'Pre-trained VLM Backbone', fontsize=13, fontweight='bold', ha='center', va='center', color='white')
    ax.text(7.0, 5.75, 'Internet-Scale Vision-Language', fontsize=10, ha='center', va='center', color='white')
    ax.text(7.0, 5.50, 'Pretraining (3B params)', fontsize=10, ha='center', va='center', color='white')
    ax.text(7.0, 5.15, 'Semantic Understanding', fontsize=10, ha='center', va='center', color='white')
    ax.text(7.0, 4.85, 'Cross-Embodiment Knowledge', fontsize=10, ha='center', va='center', color='white')
    ax.annotate('', xy=(10.0, 5.3), xytext=(9.3, 5.3), arrowprops=dict(arrowstyle='->', color=TEXT_MUTED, lw=2))
    right_box = FancyBboxPatch((10.0, 4.2), 3.5, 2.2, boxstyle="round,pad=0.05,rounding_size=0.15", facecolor=PI_GREEN, edgecolor=BORDER, linewidth=2, alpha=0.9)
    ax.add_patch(right_box)
    ax.text(11.75, 5.95, 'Action Expert', fontsize=13, fontweight='bold', ha='center', va='center', color='white')
    ax.text(11.75, 5.55, 'Flow Matching / Diffusion', fontsize=10, ha='center', va='center', color='white')
    ax.text(11.75, 5.25, 'Continuous Action Output', fontsize=10, ha='center', va='center', color='white')
    ax.text(11.75, 4.95, '50Hz High-Frequency Control', fontsize=10, ha='center', va='center', color='white')
    bottom_outer = FancyBboxPatch((0.5, 0.8), 13.0, 2.6, boxstyle="round,pad=0.05,rounding_size=0.1", facecolor=BG_CARD, edgecolor=TEXT_MUTED, linewidth=1.5, linestyle='--', alpha=0.6)
    ax.add_patch(bottom_outer)
    ax.text(7.0, 3.0, 'Cross-Embodiment Training Data', fontsize=12, fontweight='bold', ha='center', va='center', color=TEXT)
    datasets = [('Open X-Embodiment', PI_BLUE), ('DROID Dataset', PI_GREEN), ('Human Videos', PI_PURPLE), ('Autonomous Episodes', PI_ORANGE), ('pi Dataset\n(8 Robots)', PI_RED)]
    box_w = 2.2; gap = 0.3; start_x = (14 - (5*box_w + 4*gap)) / 2
    for i, (name, color) in enumerate(datasets):
        bx = start_x + i*(box_w+gap)
        b = FancyBboxPatch((bx, 1.0), box_w, 1.5, boxstyle="round,pad=0.02,rounding_size=0.08", facecolor=color, edgecolor=BORDER, linewidth=1.5, alpha=0.85)
        ax.add_patch(b)
        ax.text(bx + box_w/2, 1.75, name, fontsize=9, fontweight='bold', ha='center', va='center', color='white')
    out_box = FancyBboxPatch((10.0, 1.0), 3.5, 1.5, boxstyle="round,pad=0.05,rounding_size=0.15", facecolor=PI_RED, edgecolor=BORDER, linewidth=2, alpha=0.9)
    ax.add_patch(out_box)
    ax.text(11.75, 2.1, 'Motor Commands', fontsize=12, fontweight='bold', ha='center', va='center', color='white')
    ax.text(11.75, 1.7, 'Joint Angles / EEF Pose', fontsize=9, ha='center', va='center', color='white')
    ax.text(11.75, 1.4, 'Gripper Control', fontsize=9, ha='center', va='center', color='white')
    ax.text(11.75, 1.1, 'Base Velocity', fontsize=9, ha='center', va='center', color='white')
    ax.annotate('', xy=(11.75, 2.6), xytext=(11.75, 4.15), arrowprops=dict(arrowstyle='->', color=TEXT_MUTED, lw=1.5))
    save_both(fig, 'pi-vla-architecture.svg')

def draw_diagram2():
    fig, ax = plt.subplots(figsize=(16, 10))
    ax.set_xlim(0, 16); ax.set_ylim(0, 10); ax.axis('off'); fig.patch.set_facecolor(BG)
    ax.text(8, 9.6, 'Physical Intelligence Technology Roadmap', fontsize=20, fontweight='bold', ha='center', va='center', color=TEXT)
    ax.text(8, 9.2, 'From pi0 to pi0.7: 18 Months of Rapid Evolution', fontsize=13, ha='center', va='center', color=TEXT_MUTED, style='italic')
    ax.plot([1.5, 14.5], [5, 5], color=TEXT, linewidth=3, zorder=1)
    milestones = [
        ('2024.10', 'pi0', 'First Generalist Policy', 'VLM + Flow Matching, 8-Robot Cross-Embodiment', PI_BLUE, 1),
        ('2025.01', 'FAST', 'Efficient Action Tokenization', 'DCT + BPE, 5x Faster Training', PI_GREEN, -1),
        ('2025.02', 'Open Source', 'pi0 + pi0-FAST', 'Weights & Code Released', PI_PURPLE, 1),
        ('2025.04', 'pi0.5', 'Open-World Generalization', 'New Kitchen/Bedroom Zero-Shot', PI_ORANGE, -1),
        ('2025.05', 'Knowledge Insulation', 'Train Fast, Run Fast', 'Preserve Internet-Scale Knowledge', PI_BLUE, 1),
        ('2025.06', 'Real-Time Chunking', 'Low-Latency Control', 'High-Frequency Real-Time Action Execution', PI_GREEN, -1),
        ('2025.11', 'pi*0.6/Recap', 'RL from Experience', 'Self-Improvement via Online RL', PI_RED, 1),
        ('2025.12', 'Human->Robot', 'Transfer Emergence', 'Human Video to Robot Task Transfer', PI_PURPLE, -1),
        ('2026.02', 'PI Layer', 'Real-World Deployment', 'Partner Applications & Scaling', PI_ORANGE, 1),
        ('2026.03', 'MEM + RLT', 'Memory & Efficient RL', '15-Min Long-Horizon + Fast Online RL', PI_BLUE, -1),
        ('2026.04', 'pi0.7', 'Compositional Generalization', 'Steerable Model with Emergent Capabilities', PI_RED, 1),
    ]
    n = len(milestones); xs = np.linspace(1.5, 14.5, n)
    for i, (date, label, title, desc, color, direction) in enumerate(milestones):
        x = xs[i]
        ax.scatter([x], [5], s=120, color=color, zorder=3, edgecolors=BORDER, linewidths=2)
        if direction == 1:
            y_box = 6.2; ax.plot([x, x], [5.15, y_box], color=color, linewidth=1.5, linestyle='-')
        else:
            y_box = 2.0; ax.plot([x, x], [4.85, y_box + 1.1], color=color, linewidth=1.5, linestyle='-')
        box = FancyBboxPatch((x - 0.55, y_box), 1.1, 1.1, boxstyle="round,pad=0.02,rounding_size=0.08", facecolor=color, edgecolor=BORDER, linewidth=1.5, alpha=0.9)
        ax.add_patch(box)
        ax.text(x, y_box + 0.75, date, fontsize=8, fontweight='bold', ha='center', va='center', color='white')
        ax.text(x, y_box + 0.45, label, fontsize=9, fontweight='bold', ha='center', va='center', color='white')
        ax.text(x, y_box + 0.15, title, fontsize=7, ha='center', va='center', color='white')
        ax.text(x, y_box - 0.25, desc, fontsize=8, ha='center', va='top', color=TEXT)
    ax.text(4.0, 5.4, '2024', fontsize=15, fontweight='bold', ha='center', va='center', color=TEXT_MUTED, alpha=0.5)
    ax.text(8.0, 5.4, '2025', fontsize=15, fontweight='bold', ha='center', va='center', color=TEXT_MUTED, alpha=0.5)
    ax.text(12.5, 5.4, '2026', fontsize=15, fontweight='bold', ha='center', va='center', color=TEXT_MUTED, alpha=0.5)
    save_both(fig, 'pi-timeline.svg')

def draw_diagram3():
    fig, ax = plt.subplots(figsize=(14, 10))
    ax.set_xlim(0, 14); ax.set_ylim(0, 10); ax.axis('off'); fig.patch.set_facecolor(BG)
    ax.text(7, 9.6, 'pi0.7: Steerable Model with Diverse Multimodal Prompting', fontsize=18, fontweight='bold', ha='center', va='center', color=TEXT)
    inputs = [('Language Instructions', PI_BLUE, 'Fold the shirt\nneatly on the table'), ('Metadata Conditioning', PI_GREEN, 'Quality: High\nSpeed: Fast'), ('Control Modality Labels', PI_PURPLE, 'Joint Control\nEEF Control'), ('Visual Subgoal Images', PI_ORANGE, 'Generated by\nWorld Model')]
    box_w = 2.8; gap = 0.4; start_x = (14 - (4*box_w + 3*gap)) / 2
    for i, (title, color, text) in enumerate(inputs):
        bx = start_x + i*(box_w+gap)
        b = FancyBboxPatch((bx, 7.2), box_w, 1.6, boxstyle="round,pad=0.02,rounding_size=0.1", facecolor=color, edgecolor=BORDER, linewidth=2, alpha=0.9)
        ax.add_patch(b)
        ax.text(bx + box_w/2, 8.45, title, fontsize=11, fontweight='bold', ha='center', va='center', color='white')
        ax.text(bx + box_w/2, 7.85, text, fontsize=9, ha='center', va='center', color='white')
    mid_x = 7.0; mid_y = 5.8
    for i in range(4):
        bx = start_x + i*(box_w+gap) + box_w/2
        ax.annotate('', xy=(mid_x, mid_y + 0.6), xytext=(bx, 7.15), arrowprops=dict(arrowstyle='->', color=TEXT_MUTED, lw=1.5, connectionstyle="arc3,rad=0.1"))
    mid_box = FancyBboxPatch((4.0, mid_y - 0.3), 6.0, 1.0, boxstyle="round,pad=0.02,rounding_size=0.1", facecolor=PI_ORANGE, edgecolor=BORDER, linewidth=2, alpha=0.9)
    ax.add_patch(mid_box)
    ax.text(mid_x, mid_y + 0.2, 'Diverse Context Prompting Framework', fontsize=13, fontweight='bold', ha='center', va='center', color='white')
    ax.annotate('', xy=(mid_x, 4.5), xytext=(mid_x, mid_y - 0.35), arrowprops=dict(arrowstyle='->', color=TEXT_MUTED, lw=2))
    center_box = FancyBboxPatch((3.0, 2.5), 8.0, 2.0, boxstyle="round,pad=0.05,rounding_size=0.15", facecolor=PI_BLUE, edgecolor=BORDER, linewidth=2, alpha=0.9)
    ax.add_patch(center_box)
    ax.text(mid_x, 4.1, 'pi0.7 VLA Model', fontsize=15, fontweight='bold', ha='center', va='center', color='white')
    ax.text(mid_x, 3.6, 'Composable Skill Recombination | Cross-Embodiment Transfer | Emergent Capabilities', fontsize=10, ha='center', va='center', color='white')
    ax.text(mid_x, 3.2, 'In-Context Adaptation | Long-Horizon Planning | Real-Time Control', fontsize=10, ha='center', va='center', color='white')
    outputs = [('Action Expert', PI_GREEN, 'Continuous Actions\n50Hz Control'), ('High-Level Policy', PI_PURPLE, 'Subgoal Planning\nSkill Selection'), ('World Model', PI_ORANGE, 'Visual Subgoal\nGeneration')]
    box_w2 = 3.0; gap2 = 0.5; start_x2 = (14 - (3*box_w2 + 2*gap2)) / 2
    for i, (title, color, text) in enumerate(outputs):
        bx = start_x2 + i*(box_w2+gap2)
        ax.annotate('', xy=(bx + box_w2/2, 2.3), xytext=(mid_x, 2.45), arrowprops=dict(arrowstyle='->', color=TEXT_MUTED, lw=1.5, connectionstyle="arc3,rad=0.1"))
        b = FancyBboxPatch((bx, 0.6), box_w2, 1.4, boxstyle="round,pad=0.02,rounding_size=0.1", facecolor=color, edgecolor=BORDER, linewidth=2, alpha=0.9)
        ax.add_patch(b)
        ax.text(bx + box_w2/2, 1.6, title, fontsize=11, fontweight='bold', ha='center', va='center', color='white')
        ax.text(bx + box_w2/2, 1.05, text, fontsize=9, ha='center', va='center', color='white')
    save_both(fig, 'pi-pi07-prompting.svg')

def draw_diagram4():
    fig, ax = plt.subplots(figsize=(16, 6))
    ax.set_xlim(0, 16); ax.set_ylim(0, 6); ax.axis('off'); fig.patch.set_facecolor(BG)
    ax.text(8, 5.6, 'FAST: Efficient Robot Action Tokenization', fontsize=20, fontweight='bold', ha='center', va='center', color=TEXT)
    steps = [('Raw Action\nChunk', BG_CARD), ('DCT', PI_BLUE), ('Quantize', PI_GREEN), ('Sparse Frequency\nMatrix', PI_PURPLE), ('Flatten', PI_ORANGE), ('BPE', PI_RED), ('Compressed Action\nTokens', PI_BLUE), ('VLA\nTraining', PI_GREEN)]
    box_w = 1.6; gap = 0.35; start_x = (16 - (8*box_w + 7*gap)) / 2
    for i, (title, color) in enumerate(steps):
        bx = start_x + i*(box_w+gap)
        b = FancyBboxPatch((bx, 2.5), box_w, 1.4, boxstyle="round,pad=0.02,rounding_size=0.08", facecolor=color, edgecolor=BORDER, linewidth=2, alpha=0.9)
        ax.add_patch(b)
        ax.text(bx + box_w/2, 3.2, title, fontsize=9, fontweight='bold', ha='center', va='center', color='white')
        if i < len(steps) - 1:
            ax.annotate('', xy=(bx + box_w + 0.05, 3.2), xytext=(bx + box_w - 0.05, 3.2), arrowprops=dict(arrowstyle='->', color=TEXT_MUTED, lw=1.5))
    ax.text(4.5, 1.5, '10x Compression', fontsize=13, fontweight='bold', ha='center', va='center', color=PI_ORANGE, bbox=dict(boxstyle='round,pad=0.3', facecolor=BG_CARD, edgecolor=PI_ORANGE, linewidth=2))
    ax.text(11.5, 1.5, '5x Faster Training', fontsize=13, fontweight='bold', ha='center', va='center', color=PI_GREEN, bbox=dict(boxstyle='round,pad=0.3', facecolor=BG_CARD, edgecolor=PI_GREEN, linewidth=2))
    save_both(fig, 'pi-fast-tokenization.svg')

def draw_diagram5():
    fig, ax = plt.subplots(figsize=(14, 9))
    ax.set_xlim(0, 14); ax.set_ylim(0, 9); ax.axis('off'); fig.patch.set_facecolor(BG)
    ax.text(7, 8.6, 'MEM: Multi-Scale Embodied Memory', fontsize=20, fontweight='bold', ha='center', va='center', color=TEXT)
    center_box = FancyBboxPatch((4.5, 4.5), 5.0, 2.2, boxstyle="round,pad=0.05,rounding_size=0.15", facecolor=PI_BLUE, edgecolor=BORDER, linewidth=2, alpha=0.9)
    ax.add_patch(center_box)
    ax.text(7.0, 6.0, 'pi0.6 + MEM VLA', fontsize=15, fontweight='bold', ha='center', va='center', color='white')
    ax.text(7.0, 5.4, 'Multi-Scale Embodied Memory System', fontsize=11, ha='center', va='center', color='white')
    left_box1 = FancyBboxPatch((0.5, 5.0), 3.0, 1.4, boxstyle="round,pad=0.02,rounding_size=0.1", facecolor=PI_GREEN, edgecolor=BORDER, linewidth=2, alpha=0.9)
    ax.add_patch(left_box1)
    ax.text(2.0, 5.95, 'Short-Term Memory', fontsize=11, fontweight='bold', ha='center', va='center', color='white')
    ax.text(2.0, 5.45, 'Efficient Video Encoder', fontsize=9, ha='center', va='center', color='white')
    ax.annotate('', xy=(4.45, 5.7), xytext=(3.55, 5.7), arrowprops=dict(arrowstyle='->', color=TEXT_MUTED, lw=2))
    left_box2 = FancyBboxPatch((0.5, 2.8), 3.0, 1.4, boxstyle="round,pad=0.02,rounding_size=0.1", facecolor=BG_CARD, edgecolor=PI_GREEN, linewidth=2, alpha=0.8)
    ax.add_patch(left_box2)
    ax.text(2.0, 3.75, 'Frame-based History', fontsize=11, fontweight='bold', ha='center', va='center', color=TEXT)
    ax.text(2.0, 3.25, 'Raw observations from\nrecent timesteps', fontsize=9, ha='center', va='center', color=TEXT)
    ax.annotate('', xy=(2.0, 4.95), xytext=(2.0, 4.25), arrowprops=dict(arrowstyle='->', color=TEXT_MUTED, lw=1.5))
    right_box1 = FancyBboxPatch((10.5, 5.0), 3.0, 1.4, boxstyle="round,pad=0.02,rounding_size=0.1", facecolor=PI_PURPLE, edgecolor=BORDER, linewidth=2, alpha=0.9)
    ax.add_patch(right_box1)
    ax.text(12.0, 5.95, 'Long-Term Memory', fontsize=11, fontweight='bold', ha='center', va='center', color='white')
    ax.text(12.0, 5.45, 'Language-based Memory', fontsize=9, ha='center', va='center', color='white')
    ax.annotate('', xy=(9.55, 5.7), xytext=(10.45, 5.7), arrowprops=dict(arrowstyle='->', color=TEXT_MUTED, lw=2))
    right_box2 = FancyBboxPatch((10.5, 2.8), 3.0, 1.4, boxstyle="round,pad=0.02,rounding_size=0.1", facecolor=BG_CARD, edgecolor=PI_PURPLE, linewidth=2, alpha=0.8)
    ax.add_patch(right_box2)
    ax.text(12.0, 3.75, 'Abstract Concepts', fontsize=11, fontweight='bold', ha='center', va='center', color=TEXT)
    ax.text(12.0, 3.25, 'Natural language descriptions\nof task knowledge', fontsize=9, ha='center', va='center', color=TEXT)
    ax.annotate('', xy=(12.0, 4.95), xytext=(12.0, 4.25), arrowprops=dict(arrowstyle='->', color=TEXT_MUTED, lw=1.5))
    bottom_box = FancyBboxPatch((3.5, 0.5), 7.0, 1.4, boxstyle="round,pad=0.02,rounding_size=0.1", facecolor=PI_ORANGE, edgecolor=BORDER, linewidth=2, alpha=0.9)
    ax.add_patch(bottom_box)
    ax.text(7.0, 1.35, 'Active Reasoning Mechanism', fontsize=13, fontweight='bold', ha='center', va='center', color='white')
    ax.text(7.0, 0.85, 'Selects what to remember + High-level subtask planning', fontsize=10, ha='center', va='center', color='white')
    ax.annotate('', xy=(5.5, 1.95), xytext=(2.0, 2.75), arrowprops=dict(arrowstyle='->', color=TEXT_MUTED, lw=1.5, connectionstyle="arc3,rad=0.2"))
    ax.annotate('', xy=(8.5, 1.95), xytext=(12.0, 2.75), arrowprops=dict(arrowstyle='->', color=TEXT_MUTED, lw=1.5, connectionstyle="arc3,rad=-0.2"))
    ax.annotate('', xy=(7.0, 4.45), xytext=(7.0, 1.95), arrowprops=dict(arrowstyle='->', color=TEXT_MUTED, lw=2))
    ax.text(7.0, 0.15, 'Supports up to 15-minute tasks | Handles partial observability | In-context adaptation', fontsize=10, ha='center', va='center', color=TEXT_MUTED, style='italic')
    save_both(fig, 'pi-mem-memory.svg')

def draw_diagram6():
    fig, ax = plt.subplots(figsize=(10, 10))
    ax.set_xlim(0, 10); ax.set_ylim(0, 10); ax.axis('off'); fig.patch.set_facecolor(BG)
    ax.text(5, 9.6, 'RL Self-Improvement Loop', fontsize=20, fontweight='bold', ha='center', va='center', color=TEXT)
    center_x, center_y = 5.0, 5.0; radius = 3.0
    angles = [90, 0, 270, 180]
    labels = ['Generalist Policy (pi0)', 'Recap / RLT Training', 'Experience Generation', 'Distillation']
    sublabels = ['Base VLA Model', 'Online RL Optimization', 'Autonomous Episodes + Metadata', 'RL Experience -> Generalist\nwith Strategy Metadata']
    colors = [PI_BLUE, PI_RED, PI_ORANGE, PI_PURPLE]
    for i in range(4):
        angle_start = angles[i]; angle_end = angles[(i+1) % 4]
        arc = Arc((center_x, center_y), radius*2.4, radius*2.4, angle=0, theta1=angle_end+20, theta2=angle_start-20, color=colors[i], linewidth=4, zorder=1)
        ax.add_patch(arc)
        arrow_angle = np.radians(angle_end + 20)
        ax_x = center_x + radius * 1.2 * np.cos(arrow_angle)
        ax_y = center_y + radius * 1.2 * np.sin(arrow_angle)
        dx = -np.sin(arrow_angle) * 0.2
        dy = np.cos(arrow_angle) * 0.2
        ax.annotate('', xy=(ax_x, ax_y), xytext=(ax_x - dx, ax_y - dy), arrowprops=dict(arrowstyle='->', color=colors[i], lw=3))
        label_angle = np.radians((angle_start + angle_end) / 2)
        lx = center_x + (radius + 0.9) * np.cos(label_angle)
        ly = center_y + (radius + 0.9) * np.sin(label_angle)
        box = FancyBboxPatch((lx - 1.3, ly - 0.5), 2.6, 1.0, boxstyle="round,pad=0.02,rounding_size=0.08", facecolor=colors[i], edgecolor=BORDER, linewidth=2, alpha=0.9)
        ax.add_patch(box)
        ax.text(lx, ly + 0.15, labels[i], fontsize=10, fontweight='bold', ha='center', va='center', color='white')
        ax.text(lx, ly - 0.2, sublabels[i], fontsize=8, ha='center', va='center', color='white')
    center_box = FancyBboxPatch((center_x - 1.4, center_y - 0.5), 2.8, 1.0, boxstyle="round,pad=0.02,rounding_size=0.1", facecolor=TEXT, edgecolor=BORDER, linewidth=2, alpha=0.95)
    ax.add_patch(center_box)
    ax.text(center_x, center_y + 0.1, 'Closed-Loop', fontsize=12, fontweight='bold', ha='center', va='center', color='white')
    ax.text(center_x, center_y - 0.25, 'Self-Improvement', fontsize=12, fontweight='bold', ha='center', va='center', color='white')
    enh_box = FancyBboxPatch((center_x - 1.4, center_y + 1.4), 2.8, 0.7, boxstyle="round,pad=0.02,rounding_size=0.08", facecolor=PI_GREEN, edgecolor=BORDER, linewidth=2, alpha=0.9)
    ax.add_patch(enh_box)
    ax.text(center_x, center_y + 1.75, 'Enhanced Generalist (pi0.7)', fontsize=10, fontweight='bold', ha='center', va='center', color='white')
    save_both(fig, 'pi-rl-loop.svg')

def draw_diagram7():
    fig, ax = plt.subplots(figsize=(14, 7))
    ax.set_xlim(0, 14); ax.set_ylim(0, 7); ax.axis('off'); fig.patch.set_facecolor(BG)
    ax.text(7, 6.6, 'Cross-Embodiment Transfer', fontsize=20, fontweight='bold', ha='center', va='center', color=TEXT)
    left_box = FancyBboxPatch((0.5, 2.5), 3.5, 3.0, boxstyle="round,pad=0.05,rounding_size=0.15", facecolor=PI_BLUE, edgecolor=BORDER, linewidth=2, alpha=0.9)
    ax.add_patch(left_box)
    ax.text(2.25, 5.0, 'Source Robot Data', fontsize=13, fontweight='bold', ha='center', va='center', color='white')
    ax.text(2.25, 4.5, 'Bi-ARX Robot', fontsize=11, ha='center', va='center', color='white')
    ax.text(2.25, 4.0, 'Folding Task', fontsize=11, ha='center', va='center', color='white')
    ax.text(2.25, 3.3, 'Multimodal demonstrations\nfrom source embodiment', fontsize=9, ha='center', va='center', color='white')
    ax.annotate('', xy=(5.5, 4.0), xytext=(4.1, 4.0), arrowprops=dict(arrowstyle='->', color=TEXT_MUTED, lw=2))
    pipeline_box = FancyBboxPatch((5.5, 3.0), 3.0, 2.0, boxstyle="round,pad=0.05,rounding_size=0.15", facecolor=PI_ORANGE, edgecolor=BORDER, linewidth=2, alpha=0.9)
    ax.add_patch(pipeline_box)
    ax.text(7.0, 4.55, 'Training Pipeline', fontsize=12, fontweight='bold', ha='center', va='center', color='white')
    ax.text(7.0, 4.05, 'Cross-Embodiment', fontsize=10, ha='center', va='center', color='white')
    ax.text(7.0, 3.65, 'VLA Pre-training', fontsize=10, ha='center', va='center', color='white')
    ax.text(7.0, 3.25, 'Knowledge Distillation', fontsize=10, ha='center', va='center', color='white')
    ax.annotate('', xy=(9.5, 4.0), xytext=(8.6, 4.0), arrowprops=dict(arrowstyle='->', color=TEXT_MUTED, lw=2))
    center_box = FancyBboxPatch((9.5, 3.0), 3.0, 2.0, boxstyle="round,pad=0.05,rounding_size=0.15", facecolor=PI_PURPLE, edgecolor=BORDER, linewidth=2, alpha=0.9)
    ax.add_patch(center_box)
    ax.text(11.0, 4.55, 'pi0.7 Model', fontsize=13, fontweight='bold', ha='center', va='center', color='white')
    ax.text(11.0, 4.05, 'Generalist Policy', fontsize=10, ha='center', va='center', color='white')
    ax.text(11.0, 3.65, 'Compositional Skills', fontsize=10, ha='center', va='center', color='white')
    ax.text(11.0, 3.25, 'Cross-Embodiment', fontsize=10, ha='center', va='center', color='white')
    right_box = FancyBboxPatch((10.0, 0.5), 3.0, 1.8, boxstyle="round,pad=0.05,rounding_size=0.15", facecolor=PI_GREEN, edgecolor=BORDER, linewidth=2, alpha=0.9)
    ax.add_patch(right_box)
    ax.text(11.5, 1.75, 'Target Robot', fontsize=12, fontweight='bold', ha='center', va='center', color='white')
    ax.text(11.5, 1.25, 'UR5e Bimanual', fontsize=10, ha='center', va='center', color='white')
    ax.text(11.5, 0.85, 'Zero-Shot Transfer', fontsize=10, ha='center', va='center', color='white')
    ax.annotate('', xy=(11.5, 2.35), xytext=(11.5, 2.95), arrowprops=dict(arrowstyle='->', color=TEXT_MUTED, lw=2))
    ax.text(7.0, 1.5, 'No training data on target robot', fontsize=11, ha='center', va='center', color=TEXT, fontweight='bold', bbox=dict(boxstyle='round,pad=0.3', facecolor=BG_CARD, edgecolor=TEXT_MUTED, linewidth=1.5))
    ax.text(7.0, 0.9, 'Different size, morphology, control', fontsize=10, ha='center', va='center', color=TEXT_MUTED)
    ax.text(7.0, 0.5, 'Matches expert human zero-shot success rate', fontsize=10, ha='center', va='center', color=TEXT_MUTED)
    save_both(fig, 'pi-cross-embodiment.svg')

def draw_diagram8():
    fig, ax = plt.subplots(figsize=(14, 8))
    fig.patch.set_facecolor(BG)
    tasks = ['Bussing Easy (UR5e)', 'Bussing Hard (UR5e)', 'Shirt Folding (Bi-ARX)', 'Grocery Bagging (UR5e)', 'Toast out of Toaster (Bi-Trossen)']
    models = ['pi0', 'pi0-small', 'OpenVLA', 'OpenVLA(UR5e only)', 'Octo']
    colors = [PI_BLUE, PI_GREEN, PI_ORANGE, PI_PURPLE, TEXT_MUTED]
    data = {
        'Bussing Easy (UR5e)': [0.971, 0.443, 0.0, 0.343, 0.043],
        'Bussing Hard (UR5e)': [0.875, 0.333, 0.0, 0.0, 0.0],
        'Shirt Folding (Bi-ARX)': [1.0, 0.5, 0.0, 0.0, 0.0],
        'Grocery Bagging (UR5e)': [0.786, 0.271, 0.0, 0.0, 0.0],
        'Toast out of Toaster (Bi-Trossen)': [0.750, 0.0, 0.0, 0.0, 0.0]
    }
    n_tasks = len(tasks); n_models = len(models)
    bar_height = 0.12; group_gap = 0.35; model_gap = 0.02
    ax.set_xlim(0, 1.1)
    ax.set_ylim(-0.3, n_tasks * (n_models * bar_height + group_gap + 0.1) + 0.5)
    for i, task in enumerate(tasks):
        base_y = i * (n_models * bar_height + group_gap + 0.1)
        for j, model in enumerate(models):
            y = base_y + j * (bar_height + model_gap)
            val = data[task][j]
            if val > 0:
                ax.barh(y, val, height=bar_height, color=colors[j], edgecolor=BORDER, linewidth=0.5, alpha=0.9)
                ax.text(val + 0.02, y, f'{val:.3f}', va='center', ha='left', fontsize=8, color=TEXT)
        ax.text(-0.02, base_y + (n_models * bar_height) / 2, task, va='center', ha='right', fontsize=10, fontweight='bold', color=TEXT)
    ax.set_yticks([])
    ax.set_xlabel('Normalized Success Rate', fontsize=12, color=TEXT)
    ax.set_title('Performance Benchmark: pi0 vs OpenVLA vs Octo', fontsize=18, fontweight='bold', color=TEXT, pad=20)
    legend_patches = [mpatches.Patch(color=colors[i], label=models[i]) for i in range(n_models)]
    ax.legend(handles=legend_patches, loc='upper right', fontsize=10, frameon=True, facecolor=BG, edgecolor=TEXT_MUTED)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_visible(False)
    ax.tick_params(axis='y', which='both', left=False)
    plt.tight_layout()
    save_both(fig, 'pi-benchmark.svg')

if __name__ == '__main__':
    draw_diagram1()
    draw_diagram2()
    draw_diagram3()
    draw_diagram4()
    draw_diagram5()
    draw_diagram6()
    draw_diagram7()
    draw_diagram8()
    print("All 8 diagrams generated successfully!")
