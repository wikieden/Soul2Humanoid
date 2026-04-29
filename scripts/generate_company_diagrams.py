#!/usr/bin/env python3
"""Generate dark-themed architecture diagrams for Soul2Humanoid reports."""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch
import numpy as np
import os

BG = '#0D1117'
BG_CARD = '#161B22'
BORDER = '#30363D'
TEXT = '#E6EDF3'
TEXT_MUTED = '#8B949E'

C_TESLA = '#CC0000'
C_BD = '#00A4E4'
C_1X = '#00C853'
C_DM = '#9013FE'
C_UNITREE = '#FF6B00'
C_FIGURE = '#F5A623'
C_PI = '#4A90D9'

OUTPUT_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'assets')
os.makedirs(OUTPUT_DIR, exist_ok=True)

plt.rcParams['font.family'] = ['Hiragino Sans GB', 'PingFang SC', 'Arial Unicode MS', 'sans-serif']
plt.rcParams['axes.unicode_minus'] = False

def save_both(fig, name):
    base = os.path.join(OUTPUT_DIR, name)
    fig.savefig(base + '.svg', format='svg', bbox_inches='tight', facecolor=BG, edgecolor='none')
    fig.savefig(base + '.png', format='png', bbox_inches='tight', facecolor=BG, edgecolor='none', dpi=200)
    plt.close(fig)
    print(f"Saved: {base}.svg + .png")

def draw_tesla():
    fig, ax = plt.subplots(figsize=(14, 10))
    ax.set_xlim(0, 14); ax.set_ylim(0, 10); ax.axis('off')
    fig.patch.set_facecolor(BG)
    ax.text(7, 9.6, 'Tesla Optimus End-to-End Architecture', fontsize=20, fontweight='bold',
            ha='center', va='center', color=TEXT)
    ax.text(7, 9.15, 'FSD Tech Stack Transfer + Unified VLA Neural Network', fontsize=13,
            ha='center', va='center', color=TEXT_MUTED, style='italic')
    boxes = [
        (1.5, 7.4, 11.0, 1.2, 'Sensors', C_TESLA,
         '8 Autopilot Cameras  |  IMU  |  Force/Torque Sensors  |  Proprioception'),
        (1.5, 5.7, 11.0, 1.2, 'Vision Foundation Model (Shared with FSD)', '#D32F2F',
         'Occupancy Networks  |  3D Voxel Reconstruction  |  Depth Estimation'),
        (1.5, 4.0, 11.0, 1.2, 'Single End-to-End Neural Network', '#B71C1C',
         'Latent Space Task Decomposition  |  Grok Language Understanding  |  VLA Fusion'),
        (1.5, 2.3, 11.0, 1.2, 'Guardian Network + Force Limiters', '#8B0000',
         'Safety Monitoring  |  Real-Time Force Feedback  |  Collision Avoidance'),
        (1.5, 0.6, 11.0, 1.2, 'Actuators', C_TESLA,
         '28 Body Actuators  |  22-DoF Hand Control  |  78 Total Control Outputs'),
    ]
    for x, y, w, h, title, color, subtitle in boxes:
        b = FancyBboxPatch((x, y), w, h, boxstyle='round,pad=0.03,rounding_size=0.15',
                           facecolor=color, edgecolor=BORDER, linewidth=2, alpha=0.9)
        ax.add_patch(b)
        ax.text(x + w/2, y + h - 0.32, title, fontsize=13, fontweight='bold',
                ha='center', va='center', color='white')
        ax.text(x + w/2, y + 0.32, subtitle, fontsize=10,
                ha='center', va='center', color='white', alpha=0.95)
    for y1 in [7.35, 5.65, 3.95, 2.25]:
        ax.annotate('', xy=(7, y1 - 0.05), xytext=(7, y1 + 0.45),
                    arrowprops=dict(arrowstyle='->', color=TEXT_MUTED, lw=2.5))
    ax.text(13.2, 5.1, 'VLA\nLoop', fontsize=10, fontweight='bold', ha='center', va='center',
            color=TEXT, bbox=dict(boxstyle='round,pad=0.25', facecolor=BG_CARD, edgecolor=C_TESLA, linewidth=2))
    ax.annotate('', xy=(12.55, 5.1), xytext=(13.0, 5.1),
                arrowprops=dict(arrowstyle='->', color=C_TESLA, lw=1.5))
    save_both(fig, 'tesla-end-to-end-architecture')

def draw_boston_dynamics():
    fig, ax = plt.subplots(figsize=(14, 10))
    ax.set_xlim(0, 14); ax.set_ylim(0, 10); ax.axis('off')
    fig.patch.set_facecolor(BG)
    ax.text(7, 9.6, 'Boston Dynamics Atlas Hybrid Architecture', fontsize=20, fontweight='bold',
            ha='center', va='center', color=TEXT)
    ax.text(7, 9.15, 'MPC + RL + Neural Networks: Layered Reliability with Learned Edge Cases',
            fontsize=13, ha='center', va='center', color=TEXT_MUTED, style='italic')
    layers = [
        (0.8, 7.2, 12.4, 1.4, 'Layer 4  —  High-Level Perception & Decision',
         'Vision Foundation Model  +  VLA  |  Object Detection  |  Semantic Understanding  |  Task Reasoning',
         C_BD),
        (0.8, 5.4, 12.4, 1.4, 'Layer 3  —  Manipulation Execution',
         'Diffusion Transformer (LBM)  |  Flow Matching Loss  |  30Hz Control  |  Language-Conditioned Behavior',
         '#0077A8'),
        (0.8, 3.6, 12.4, 1.4, 'Layer 2  —  Motion Planning',
         'Optimization + Learning  |  Whole-Body Coordination  |  Self-Collision Avoidance  |  Obstacle Avoidance',
         '#005F85'),
        (0.8, 1.8, 12.4, 1.4, 'Layer 1  —  Balance & Gait',
         'MPC (Model Predictive Control)  +  RL Policy  |  Real-Time Stability  |  Slip Recovery  |  Dynamic Response',
         '#004662'),
    ]
    for x, y, w, h, title, subtitle, color in layers:
        b = FancyBboxPatch((x, y), w, h, boxstyle='round,pad=0.03,rounding_size=0.15',
                           facecolor=color, edgecolor=BORDER, linewidth=2, alpha=0.9)
        ax.add_patch(b)
        ax.text(x + w/2, y + h - 0.38, title, fontsize=13, fontweight='bold',
                ha='center', va='center', color='white')
        ax.text(x + w/2, y + 0.35, subtitle, fontsize=10,
                ha='center', va='center', color='white', alpha=0.95)
    for y1 in [7.15, 5.35, 3.55]:
        ax.annotate('', xy=(7, y1 - 0.05), xytext=(7, y1 + 0.45),
                    arrowprops=dict(arrowstyle='->', color=TEXT_MUTED, lw=2.5))
    note = ('Philosophy: Preserve MPC as trustworthy physical foundation;\n'
            'introduce learning where MPC cannot cover edge cases;\n'
            'gradually migrate high-level behavior toward data-driven,\n'
            'language-conditioned control.')
    ax.text(7, 0.7, note, fontsize=10, ha='center', va='center', color=TEXT_MUTED,
            style='italic', linespacing=1.4,
            bbox=dict(boxstyle='round,pad=0.4', facecolor=BG_CARD, edgecolor=BORDER, linewidth=1.5))
    save_both(fig, 'boston-dynamics-hybrid-architecture')

def draw_1x():
    fig, ax = plt.subplots(figsize=(14, 10))
    ax.set_xlim(0, 14); ax.set_ylim(0, 10); ax.axis('off')
    fig.patch.set_facecolor(BG)
    ax.text(7, 9.6, '1X NEO System Architecture', fontsize=20, fontweight='bold',
            ha='center', va='center', color=TEXT)
    ax.text(7, 9.15, 'World Model + Redwood VLA + Tendon-Driven Safe Actuation',
            fontsize=13, ha='center', va='center', color=TEXT_MUTED, style='italic')
    inputs = [
        ('Stereo Camera\n8.85MP 90Hz', C_1X),
        ('Microphone\n4-Array Beamforming', '#2E7D32'),
        ('Tactile Sensors\nHand IP68', '#388E3C'),
        ('Proprioception\nFull-Body State', '#43A047'),
    ]
    box_w = 2.6; gap = 0.5
    start_x = (14 - (4*box_w + 3*gap)) / 2
    for i, (label, color) in enumerate(inputs):
        bx = start_x + i*(box_w+gap)
        b = FancyBboxPatch((bx, 7.2), box_w, 1.2, boxstyle='round,pad=0.02,rounding_size=0.1',
                           facecolor=color, edgecolor=BORDER, linewidth=2, alpha=0.9)
        ax.add_patch(b)
        ax.text(bx + box_w/2, 7.8, label, fontsize=10, fontweight='bold',
                ha='center', va='center', color='white', linespacing=1.3)
    vla_box = FancyBboxPatch((3.5, 4.6), 7.0, 2.0, boxstyle='round,pad=0.05,rounding_size=0.15',
                             facecolor=C_1X, edgecolor=BORDER, linewidth=2.5, alpha=0.95)
    ax.add_patch(vla_box)
    ax.text(7, 6.0, 'Redwood VLA', fontsize=16, fontweight='bold', ha='center', va='center', color='white')
    ax.text(7, 5.35, 'Vision Understanding  |  Language Understanding  |  Action Generation  |  Memory System',
            fontsize=10, ha='center', va='center', color='white')
    for i in range(4):
        bx = start_x + i*(box_w+gap) + box_w/2
        ax.annotate('', xy=(bx, 6.65), xytext=(bx, 7.15),
                    arrowprops=dict(arrowstyle='->', color=TEXT_MUTED, lw=1.8))
    side_left = FancyBboxPatch((0.5, 4.8), 2.5, 1.6, boxstyle='round,pad=0.02,rounding_size=0.1',
                               facecolor='#1B5E20', edgecolor=BORDER, linewidth=2, alpha=0.9)
    ax.add_patch(side_left)
    ax.text(1.75, 5.85, '1X World Model', fontsize=11, fontweight='bold', ha='center', va='center', color='white')
    ax.text(1.75, 5.25, 'Physics-Based\nVideo Prediction', fontsize=9, ha='center', va='center', color='white')
    ax.annotate('', xy=(3.45, 5.6), xytext=(3.05, 5.6),
                arrowprops=dict(arrowstyle='->', color=TEXT_MUTED, lw=2))
    side_right = FancyBboxPatch((11.0, 4.8), 2.5, 1.6, boxstyle='round,pad=0.02,rounding_size=0.1',
                                facecolor='#2E7D32', edgecolor=BORDER, linewidth=2, alpha=0.9)
    ax.add_patch(side_right)
    ax.text(12.25, 5.85, 'Built-in LLM', fontsize=11, fontweight='bold', ha='center', va='center', color='white')
    ax.text(12.25, 5.25, 'OpenAI GPT\nLanguage Interaction', fontsize=9, ha='center', va='center', color='white')
    ax.annotate('', xy=(10.55, 5.6), xytext=(10.95, 5.6),
                arrowprops=dict(arrowstyle='->', color=TEXT_MUTED, lw=2))
    out_box = FancyBboxPatch((4.5, 2.2), 5.0, 1.6, boxstyle='round,pad=0.05,rounding_size=0.15',
                             facecolor='#004D40', edgecolor=BORDER, linewidth=2.5, alpha=0.95)
    ax.add_patch(out_box)
    ax.text(7, 3.3, 'Tendon Drive Actuators', fontsize=14, fontweight='bold', ha='center', va='center', color='white')
    ax.text(7, 2.7, '95% Backdrivability  |  22 dB Ultra-Quiet  |  2% Torque Precision  |  Collision-Safe',
            fontsize=10, ha='center', va='center', color='white')
    ax.annotate('', xy=(7, 3.85), xytext=(7, 4.55),
                arrowprops=dict(arrowstyle='->', color=TEXT_MUTED, lw=2.5))
    # Expert mode note
    ax.text(7, 1.0, 'Expert Mode: Remote expert teleoperates to teach new tasks while NEO learns from demonstrations',
            fontsize=10, ha='center', va='center', color=TEXT_MUTED, style='italic',
            bbox=dict(boxstyle='round,pad=0.3', facecolor=BG_CARD, edgecolor=BORDER, linewidth=1.5))
    save_both(fig, '1x-neo-system-architecture')

def draw_deepmind():
    fig, ax = plt.subplots(figsize=(14, 10))
    ax.set_xlim(0, 14); ax.set_ylim(0, 10); ax.axis('off')
    fig.patch.set_facecolor(BG)
    ax.text(7, 9.6, 'Google DeepMind Gemini Robotics Dual-Model Architecture', fontsize=20, fontweight='bold',
            ha='center', va='center', color=TEXT)
    ax.text(7, 9.15, 'VLA Perception-Action Loop + ER Embodied Reasoning for Complex Task Planning',
            fontsize=13, ha='center', va='center', color=TEXT_MUTED, style='italic')

    # Left: ER Model
    er_box = FancyBboxPatch((0.8, 4.2), 5.0, 4.0, boxstyle='round,pad=0.05,rounding_size=0.15',
                            facecolor=C_DM, edgecolor=BORDER, linewidth=2.5, alpha=0.95)
    ax.add_patch(er_box)
    ax.text(3.3, 7.9, 'Gemini Robotics-ER 1.6', fontsize=15, fontweight='bold', ha='center', va='center', color='white')
    ax.text(3.3, 7.35, 'Embodied Reasoning Model', fontsize=11, ha='center', va='center', color='white', alpha=0.9)
    er_items = [
        'Complex Task Planning',
        'Logic & Physical Reasoning',
        'Tool Use (Search, APIs)',
        'Dynamic Environment Adaptation',
        'Step-by-Step Subgoal Generation',
    ]
    for i, item in enumerate(er_items):
        ax.text(3.3, 6.75 - i*0.42, f'  {item}', fontsize=10, ha='center', va='center', color='white')

    # Right: VLA Model
    vla_box = FancyBboxPatch((8.2, 4.2), 5.0, 4.0, boxstyle='round,pad=0.05,rounding_size=0.15',
                             facecolor='#5E35B1', edgecolor=BORDER, linewidth=2.5, alpha=0.95)
    ax.add_patch(vla_box)
    ax.text(10.7, 7.9, 'Gemini Robotics 1.5', fontsize=15, fontweight='bold', ha='center', va='center', color='white')
    ax.text(10.7, 7.35, 'VLA Foundation Model', fontsize=11, ha='center', va='center', color='white', alpha=0.9)
    vla_items = [
        'Vision-Language-Action Fusion',
        'Cross-Embodiment Generalization',
        'Fine Manipulation (Folding, Packing)',
        'Multi-Step Autonomous Execution',
        'Natural Language Interaction',
    ]
    for i, item in enumerate(vla_items):
        ax.text(10.7, 6.75 - i*0.42, f'  {item}', fontsize=10, ha='center', va='center', color='white')

    # Collaboration arrows
    ax.annotate('', xy=(8.1, 6.6), xytext=(5.9, 6.6),
                arrowprops=dict(arrowstyle='<->', color=TEXT_MUTED, lw=2.5))
    ax.text(7.0, 6.9, 'Collaborate', fontsize=10, fontweight='bold', ha='center', va='center', color=TEXT,
            bbox=dict(boxstyle='round,pad=0.2', facecolor=BG_CARD, edgecolor=BORDER, linewidth=1.5))

    ax.annotate('', xy=(7.0, 4.95), xytext=(7.0, 5.6),
                arrowprops=dict(arrowstyle='->', color=TEXT_MUTED, lw=2.5))

    # Bottom: Any robot embodiment
    bot_box = FancyBboxPatch((3.5, 3.0), 7.0, 1.6, boxstyle='round,pad=0.05,rounding_size=0.15',
                             facecolor=BG_CARD, edgecolor=C_DM, linewidth=2.5, alpha=0.95)
    ax.add_patch(bot_box)
    ax.text(7.0, 4.1, 'Any Robot Embodiment', fontsize=14, fontweight='bold', ha='center', va='center', color=TEXT)
    ax.text(7.0, 3.5, 'Bimanual Arms  |  Humanoid Robots  |  Mobile Manipulators  |  Quadrupeds',
            fontsize=10, ha='center', va='center', color=TEXT_MUTED)

    # On-device note
    ax.text(7.0, 1.8, 'Gemini Robotics On-Device: Local VLA execution for low latency, privacy, and offline operation',
            fontsize=10, ha='center', va='center', color=TEXT_MUTED, style='italic',
            bbox=dict(boxstyle='round,pad=0.3', facecolor=BG_CARD, edgecolor=BORDER, linewidth=1.5))

    save_both(fig, 'google-deepmind-gemini-robotics-architecture')

def draw_unitree():
    fig, ax = plt.subplots(figsize=(14, 10))
    ax.set_xlim(0, 14); ax.set_ylim(0, 10); ax.axis('off')
    fig.patch.set_facecolor(BG)
    ax.text(7, 9.6, 'Unitree RL + Imitation Learning Pipeline', fontsize=20, fontweight='bold',
            ha='center', va='center', color=TEXT)
    ax.text(7, 9.15, 'Simulation-Driven RL + Human Demonstration for Agile Dynamic Motion',
            fontsize=13, ha='center', va='center', color=TEXT_MUTED, style='italic')

    # Left branch: RL
    rl_box = FancyBboxPatch((0.5, 5.5), 5.5, 3.2, boxstyle='round,pad=0.05,rounding_size=0.15',
                            facecolor=C_UNITREE, edgecolor=BORDER, linewidth=2.5, alpha=0.95)
    ax.add_patch(rl_box)
    ax.text(3.25, 8.2, 'Reinforcement Learning', fontsize=14, fontweight='bold', ha='center', va='center', color='white')
    ax.text(3.25, 7.6, 'Isaac Sim / MuJoCo / Gym', fontsize=11, ha='center', va='center', color='white')
    rl_items = [
        'Millions of simulated episodes',
        'PPO / SAC policy optimization',
        'Domain randomization',
        'Gait & dynamic motion discovery',
    ]
    for i, item in enumerate(rl_items):
        ax.text(3.25, 7.05 - i*0.45, f'  {item}', fontsize=10, ha='center', va='center', color='white')

    # Right branch: Imitation Learning
    il_box = FancyBboxPatch((8.0, 5.5), 5.5, 3.2, boxstyle='round,pad=0.05,rounding_size=0.15',
                            facecolor='#E65100', edgecolor=BORDER, linewidth=2.5, alpha=0.95)
    ax.add_patch(il_box)
    ax.text(10.75, 8.2, 'Imitation Learning', fontsize=14, fontweight='bold', ha='center', va='center', color='white')
    ax.text(10.75, 7.6, 'Motion Capture / Teleoperation', fontsize=11, ha='center', va='center', color='white')
    il_items = [
        'Human demonstration recording',
        'Behavior cloning (BC)',
        'Dance & gymnastics skills',
        'Teleoperated task sequences',
    ]
    for i, item in enumerate(il_items):
        ax.text(10.75, 7.05 - i*0.45, f'  {item}', fontsize=10, ha='center', va='center', color='white')

    # Center merge: Sim2Real
    merge_box = FancyBboxPatch((4.5, 3.5), 5.0, 1.6, boxstyle='round,pad=0.05,rounding_size=0.15',
                               facecolor='#BF360C', edgecolor=BORDER, linewidth=2.5, alpha=0.95)
    ax.add_patch(merge_box)
    ax.text(7.0, 4.5, 'Sim2Real Transfer', fontsize=14, fontweight='bold', ha='center', va='center', color='white')
    ax.text(7.0, 3.9, 'Domain Adaptation  |  Dynamics Randomization  |  Policy Distillation',
            fontsize=10, ha='center', va='center', color='white')

    ax.annotate('', xy=(5.8, 4.55), xytext=(4.5, 5.45),
                arrowprops=dict(arrowstyle='->', color=TEXT_MUTED, lw=2.5))
    ax.annotate('', xy=(8.2, 4.55), xytext=(9.5, 5.45),
                arrowprops=dict(arrowstyle='->', color=TEXT_MUTED, lw=2.5))

    # Bottom: Deployment
    dep_box = FancyBboxPatch((4.0, 1.2), 6.0, 1.8, boxstyle='round,pad=0.05,rounding_size=0.15',
                             facecolor=BG_CARD, edgecolor=C_UNITREE, linewidth=2.5, alpha=0.95)
    ax.add_patch(dep_box)
    ax.text(7.0, 2.4, 'Deployment on H1 / G1', fontsize=14, fontweight='bold', ha='center', va='center', color=TEXT)
    ax.text(7.0, 1.8, 'Real-Time Control  |  3.3 m/s Speed Record  |  189 N.m/Kg Torque Density',
            fontsize=10, ha='center', va='center', color=TEXT_MUTED)

    ax.annotate('', xy=(7.0, 3.05), xytext=(7.0, 3.45),
                arrowprops=dict(arrowstyle='->', color=TEXT_MUTED, lw=2.5))

    save_both(fig, 'unitree-rl-pipeline')

def draw_timeline():
    fig, ax = plt.subplots(figsize=(20, 10))
    ax.set_xlim(0, 20); ax.set_ylim(0, 10); ax.axis('off')
    fig.patch.set_facecolor(BG)
    ax.text(10, 9.6, 'Embodied AI Technology Evolution Timeline (2023-2026)', fontsize=20, fontweight='bold',
            ha='center', va='center', color=TEXT)
    ax.text(10, 9.15, 'Key Milestones in Vision-Language-Action, World Models, and Humanoid Robotics',
            fontsize=13, ha='center', va='center', color=TEXT_MUTED, style='italic')

    # Main timeline axis
    ax.plot([1.5, 18.5], [5, 5], color=TEXT, linewidth=3, zorder=1)

    milestones = [
        # 2023
        ('2023.07', 'RT-2', 'DeepMind', 'First large-scale VLA model\nVision-Language -> Action', C_DM, 1),
        ('2023.10', 'RT-X / OXE', 'DeepMind', 'Cross-embodiment dataset\n20+ institutions', C_DM, -1),
        # 2024
        ('2024.04', 'Electric Atlas', 'Boston Dynamics', 'Full-electric Atlas debut\nHydraulic retired', C_BD, 1),
        ('2024.08', 'Gemini Robotics', 'DeepMind', 'Gemini-based VLA system\nMulti-modal robotics', C_DM, -1),
        ('2024.10', 'pi0', 'Physical Intelligence', 'First generalist policy\n8-robot cross-embodiment', C_PI, 1),
        ('2024.11', 'Figure 01', 'Figure AI', 'Helix early demonstrations\nBMW factory pilot', C_FIGURE, -1),
        # 2025
        ('2025.02', 'Helix VLA', 'Figure AI', 'End-to-end humanoid VLA\nReal-time dual-system', C_FIGURE, 1),
        ('2025.03', 'Gemini 1.5', 'DeepMind', 'Stronger VLA model\nComplex physical interaction', C_DM, -1),
        ('2025.04', 'pi0.5 + FAST', 'Physical Intelligence', 'Open-world generalization\nEfficient action tokenization', C_PI, 1),
        ('2025.05', 'FSD v12 Transfer', 'Tesla', 'Human video learning breakthrough\nDigital Dreams synthetic data', C_TESLA, -1),
        ('2025.08', 'GTC Robotics', 'NVIDIA + Ecosystem', 'Isaac Sim/Gym explosion\nGR00T humanoid foundation', '#76B900', 1),
        ('2025.11', 'pi0.6 / Recap', 'Physical Intelligence', 'RL from experience\nSelf-improvement loop', C_PI, -1),
        # 2026
        ('2026.01', 'Atlas Product', 'Boston Dynamics', 'CES product launch\nHyundai Mobis supply chain', C_BD, 1),
        ('2026.02', 'pi0.7 / MEM', 'Physical Intelligence', 'Compositional generalization\n15-min long-horizon memory', C_PI, -1),
        ('2026.03', 'Figure 03 / BotQ', 'Figure AI', 'Next-gen humanoid\nAutonomous data flywheel', C_FIGURE, 1),
        ('2026.04', 'Gemini-ER 1.6', 'DeepMind', 'Enhanced embodied reasoning\nComplex task planning', C_DM, -1),
    ]

    n = len(milestones)
    xs = np.linspace(1.5, 18.5, n)
    for i, (date, label, company, desc, color, direction) in enumerate(milestones):
        x = xs[i]
        ax.scatter([x], [5], s=120, color=color, zorder=3, edgecolors=BORDER, linewidths=2)
        if direction == 1:
            y_box = 6.2
            ax.plot([x, x], [5.15, y_box], color=color, linewidth=1.5, linestyle='-')
        else:
            y_box = 2.0
            ax.plot([x, x], [4.85, y_box + 1.1], color=color, linewidth=1.5, linestyle='-')
        box = FancyBboxPatch((x - 0.55, y_box), 1.1, 1.1, boxstyle='round,pad=0.02,rounding_size=0.08',
                             facecolor=color, edgecolor=BORDER, linewidth=1.5, alpha=0.9)
        ax.add_patch(box)
        ax.text(x, y_box + 0.75, date, fontsize=8, fontweight='bold', ha='center', va='center', color='white')
        ax.text(x, y_box + 0.48, label, fontsize=9, fontweight='bold', ha='center', va='center', color='white')
        ax.text(x, y_box + 0.18, company, fontsize=7, ha='center', va='center', color='white')
        ax.text(x, y_box - 0.25, desc, fontsize=8, ha='center', va='top', color=TEXT)

    # Year labels
    ax.text(3.5, 5.4, '2023', fontsize=15, fontweight='bold', ha='center', va='center', color=TEXT_MUTED, alpha=0.5)
    ax.text(7.5, 5.4, '2024', fontsize=15, fontweight='bold', ha='center', va='center', color=TEXT_MUTED, alpha=0.5)
    ax.text(12.0, 5.4, '2025', fontsize=15, fontweight='bold', ha='center', va='center', color=TEXT_MUTED, alpha=0.5)
    ax.text(16.5, 5.4, '2026', fontsize=15, fontweight='bold', ha='center', va='center', color=TEXT_MUTED, alpha=0.5)

    save_both(fig, 'embodied-ai-timeline-overview')

if __name__ == '__main__':
    draw_tesla()
    draw_boston_dynamics()
    draw_1x()
    draw_deepmind()
    draw_unitree()
    draw_timeline()
    print('All 6 diagrams generated successfully!')
