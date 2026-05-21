#!/usr/bin/env python3
"""
LLM4Hardware Video Asset Generator

This script generates simple visual assets for the introduction video
including component diagrams, flow charts, and metric visualizations.
"""

import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.patches import FancyBboxPatch
import numpy as np
import os

# Set up the style
plt.style.use('dark_background')
plt.rcParams['font.family'] = 'sans-serif'
plt.rcParams['font.size'] = 12

# Color palette
COLORS = {
    'primary': '#1E3A8A',
    'secondary': '#10B981', 
    'accent': '#F59E0B',
    'background': '#111827',
    'text': '#FFFFFF'
}

def create_component_matrix():
    """Create a visual matrix of all project components"""
    fig, ax = plt.subplots(figsize=(12, 9))
    fig.patch.set_facecolor(COLORS['background'])
    ax.set_facecolor(COLORS['background'])
    
    components = [
        ('AutoChip', 'Functional\nVerilog'),
        ('VeriThoughts', 'Reasoning\n& Formal'),
        ('ROME', 'Hierarchical\nPrompting'),
        ('Veritas', 'CNF-guided\nSynthesis'),
        ('PrefixLLM', 'Prefix\nAdders'),
        ('Testbench', 'Generation\nfor FSM'),
        ('NL2SVA', 'Assertion\nGeneration'),
        ('Security', 'Assertions'),
        ('OpenTitan', 'RAG-SVA\nGenerator'),
        ('LLMPirate', 'IP Security\nAnalysis'),
        ('C2HLSC', 'SW-to-HW\nBridge'),
        ('Masala-CHAI', 'SPICE\nDatasets')
    ]
    
    # Create 3x4 grid
    for i, (title, description) in enumerate(components):
        row = i // 3
        col = i % 3
        
        x = col * 4 + 1
        y = 3 - row * 2
        
        # Create rounded rectangle
        rect = FancyBboxPatch(
            (x, y), 3, 1.5,
            boxstyle="round,pad=0.1",
            facecolor=COLORS['primary'],
            edgecolor=COLORS['secondary'],
            linewidth=2
        )
        ax.add_patch(rect)
        
        # Add title
        ax.text(x + 1.5, y + 1, title, 
                ha='center', va='center', 
                fontsize=14, fontweight='bold',
                color=COLORS['text'])
        
        # Add description
        ax.text(x + 1.5, y + 0.3, description,
                ha='center', va='center',
                fontsize=10, color=COLORS['secondary'])
    
    ax.set_xlim(0, 13)
    ax.set_ylim(-1, 5)
    ax.set_aspect('equal')
    ax.axis('off')
    
    plt.title('LLM4Hardware Research Components', 
              fontsize=20, fontweight='bold',
              color=COLORS['text'], pad=20)
    
    plt.tight_layout()
    plt.savefig('component_matrix.png', 
                facecolor=COLORS['background'],
                dpi=300, bbox_inches='tight')
    plt.close()

def create_design_flow():
    """Create a design flow diagram"""
    fig, ax = plt.subplots(figsize=(10, 12))
    fig.patch.set_facecolor(COLORS['background'])
    ax.set_facecolor(COLORS['background'])
    
    steps = [
        'Natural Language Input',
        'LLM Processing',
        'Hardware Generation', 
        'Formal Verification',
        'Error Feedback Loop',
        'Optimized Implementation'
    ]
    
    y_positions = np.linspace(10, 1, len(steps))
    
    for i, (step, y) in enumerate(zip(steps, y_positions)):
        # Create step box
        rect = FancyBboxPatch(
            (2, y-0.4), 6, 0.8,
            boxstyle="round,pad=0.1",
            facecolor=COLORS['secondary'],
            edgecolor=COLORS['accent'],
            linewidth=2
        )
        ax.add_patch(rect)
        
        # Add step text
        ax.text(5, y, step,
                ha='center', va='center',
                fontsize=12, fontweight='bold',
                color=COLORS['background'])
        
        # Add arrow to next step
        if i < len(steps) - 1:
            ax.arrow(5, y-0.5, 0, -0.6, 
                    head_width=0.2, head_length=0.1,
                    fc=COLORS['accent'], ec=COLORS['accent'],
                    linewidth=3)
    
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 11)
    ax.axis('off')
    
    plt.title('AI-Enhanced Design Flow',
              fontsize=18, fontweight='bold',
              color=COLORS['text'], pad=20)
    
    plt.tight_layout()
    plt.savefig('design_flow.png',
                facecolor=COLORS['background'],
                dpi=300, bbox_inches='tight')
    plt.close()

def create_impact_metrics():
    """Create impact metrics visualization"""
    fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(12, 8))
    fig.patch.set_facecolor(COLORS['background'])
    
    metrics = [
        ('Design Time\nReduction', 70, '%'),
        ('Error Detection\nImprovement', 3, 'x faster'),
        ('Accessibility\nIncrease', 85, '% more users'),
        ('Verification\nCoverage', 90, '% coverage')
    ]
    
    axes = [ax1, ax2, ax3, ax4]
    
    for ax, (title, value, unit) in zip(axes, metrics):
        ax.set_facecolor(COLORS['background'])
        
        # Create circular progress
        circle = plt.Circle((0.5, 0.5), 0.4, 
                           fill=False, color=COLORS['secondary'], 
                           linewidth=8)
        ax.add_patch(circle)
        
        # Add progress arc based on value
        if isinstance(value, int) and value <= 100:
            progress = value / 100 * 360
            wedge = patches.Wedge((0.5, 0.5), 0.4, 0, progress,
                                 facecolor=COLORS['accent'], alpha=0.8)
            ax.add_patch(wedge)
        
        # Add value text
        ax.text(0.5, 0.6, str(value),
                ha='center', va='center',
                fontsize=24, fontweight='bold',
                color=COLORS['text'])
        
        ax.text(0.5, 0.4, unit,
                ha='center', va='center',
                fontsize=12, color=COLORS['secondary'])
        
        # Add title
        ax.text(0.5, 0.1, title,
                ha='center', va='center',
                fontsize=12, fontweight='bold',
                color=COLORS['text'])
        
        ax.set_xlim(0, 1)
        ax.set_ylim(0, 1)
        ax.set_aspect('equal')
        ax.axis('off')
    
    plt.suptitle('Measurable Impact', 
                 fontsize=20, fontweight='bold',
                 color=COLORS['text'], y=0.95)
    
    plt.tight_layout()
    plt.savefig('impact_metrics.png',
                facecolor=COLORS['background'],
                dpi=300, bbox_inches='tight')
    plt.close()

def create_comparison_chart():
    """Create traditional vs LLM approach comparison"""
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 8))
    fig.patch.set_facecolor(COLORS['background'])
    
    traditional = [
        'Manual HDL coding',
        'Separate verification',
        'Expert-only access',
        'Time-intensive debug'
    ]
    
    llm_approach = [
        'Natural language input',
        'Integrated verification', 
        'All skill levels',
        'Automated correction'
    ]
    
    # Traditional approach
    ax1.set_facecolor(COLORS['background'])
    ax1.text(0.5, 0.9, 'Traditional Approach',
             ha='center', va='center',
             fontsize=16, fontweight='bold',
             color='#EF4444')
    
    for i, item in enumerate(traditional):
        ax1.text(0.1, 0.7 - i*0.15, f'• {item}',
                ha='left', va='center',
                fontsize=12, color=COLORS['text'])
    
    # LLM approach
    ax2.set_facecolor(COLORS['background'])
    ax2.text(0.5, 0.9, 'LLM4Hardware Approach',
             ha='center', va='center',
             fontsize=16, fontweight='bold',
             color=COLORS['secondary'])
    
    for i, item in enumerate(llm_approach):
        ax2.text(0.1, 0.7 - i*0.15, f'• {item}',
                ha='left', va='center',
                fontsize=12, color=COLORS['text'])
    
    # Add border
    for ax, color in [(ax1, '#EF4444'), (ax2, COLORS['secondary'])]:
        rect = patches.Rectangle((0, 0), 1, 1,
                               linewidth=3, edgecolor=color,
                               facecolor='none')
        ax.add_patch(rect)
        ax.set_xlim(0, 1)
        ax.set_ylim(0, 1)
        ax.axis('off')
    
    plt.tight_layout()
    plt.savefig('comparison_chart.png',
                facecolor=COLORS['background'],
                dpi=300, bbox_inches='tight')
    plt.close()

def main():
    """Generate all visual assets"""
    print("Generating visual assets for LLM4Hardware introduction video...")
    
    # Create output directory if it doesn't exist
    os.makedirs('generated_assets', exist_ok=True)
    os.chdir('generated_assets')
    
    try:
        print("Creating component matrix...")
        create_component_matrix()
        
        print("Creating design flow diagram...")
        create_design_flow()
        
        print("Creating impact metrics...")
        create_impact_metrics()
        
        print("Creating comparison chart...")
        create_comparison_chart()
        
        print("All assets generated successfully!")
        print("Files saved in: generated_assets/")
        print("- component_matrix.png")
        print("- design_flow.png") 
        print("- impact_metrics.png")
        print("- comparison_chart.png")
        
    except Exception as e:
        print(f"Error generating assets: {e}")
        print("Make sure matplotlib is installed: pip install matplotlib")

if __name__ == "__main__":
    main()