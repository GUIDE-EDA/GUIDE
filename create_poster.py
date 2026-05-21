#!/usr/bin/env python3
"""
LLM4ChipDesign Poster Generator
Creates a comprehensive poster showcasing the three main research areas of LLM4Hardware
"""

import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.patches import FancyBboxPatch, Rectangle
import numpy as np

def create_llm4chipdesign_poster():
    # Create a large figure for the poster (A1 size: 594 x 841 mm, converted to inches)
    fig = plt.figure(figsize=(23.4, 33.1))
    ax = fig.add_subplot(111)
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 140)
    ax.axis('off')
    
    # Define colors
    primary_blue = '#1f4e79'
    secondary_blue = '#4a90a4'
    light_blue = '#87ceeb'
    orange = '#ff7f00'
    green = '#228b22'
    gray = '#f5f5f5'
    dark_gray = '#333333'
    
    # Title Section
    title_box = FancyBboxPatch((5, 125), 90, 12, 
                              boxstyle="round,pad=1", 
                              facecolor=primary_blue, 
                              edgecolor='black', 
                              linewidth=2)
    ax.add_patch(title_box)
    
    ax.text(50, 131, 'LLM4ChipDesign', 
            fontsize=48, fontweight='bold', color='white', 
            ha='center', va='center')
    
    ax.text(50, 127, 'Comprehensive Research Framework for LLM-based Hardware Design', 
            fontsize=18, color='white', ha='center', va='center')
    
    # Subtitle with three main areas
    ax.text(50, 120, 'Three Main Research Areas: LLM4Verilog Generation • LLM4Security • LLM4C2HLS', 
            fontsize=16, color=dark_gray, ha='center', va='center', fontweight='bold')
    
    # Main Research Areas Section
    areas_y_start = 115
    area_height = 35
    area_spacing = 2
    
    # Area 1: LLM4Verilog Generation
    area1_box = FancyBboxPatch((2, areas_y_start - area_height), 30, area_height, 
                              boxstyle="round,pad=0.5", 
                              facecolor=light_blue, 
                              edgecolor=primary_blue, 
                              linewidth=2)
    ax.add_patch(area1_box)
    
    ax.text(17, areas_y_start - 3, 'LLM4Verilog Generation', 
            fontsize=16, fontweight='bold', color=primary_blue, 
            ha='center', va='center')
    
    verilog_projects = [
        '• AutoChip: Functional Verilog from prompts',
        '• VeriThoughts: Reasoning-based generation', 
        '• ROME: Hierarchical prompting',
        '• Veritas: CNF-based synthesis',
        '• PrefixLLM: Prefix circuit design'
    ]
    
    for i, project in enumerate(verilog_projects):
        ax.text(4, areas_y_start - 8 - i*4, project, 
                fontsize=11, color=dark_gray, ha='left', va='center')
    
    # Area 2: LLM4Security  
    area2_box = FancyBboxPatch((35, areas_y_start - area_height), 30, area_height, 
                              boxstyle="round,pad=0.5", 
                              facecolor='#ffeeee', 
                              edgecolor=orange, 
                              linewidth=2)
    ax.add_patch(area2_box)
    
    ax.text(50, areas_y_start - 3, 'LLM4Security', 
            fontsize=16, fontweight='bold', color=orange, 
            ha='center', va='center')
    
    security_projects = [
        '• LLMPirate: IP piracy detection',
        '• Security Assertions: LLM-generated SVA',
        '• Hybrid-NL2SVA: Enhanced NL2SVA',
        '• OpenTitan RAG: SVA for IP blocks'
    ]
    
    for i, project in enumerate(security_projects):
        ax.text(37, areas_y_start - 8 - i*4, project, 
                fontsize=11, color=dark_gray, ha='left', va='center')
    
    # Area 3: LLM4C2HLS
    area3_box = FancyBboxPatch((68, areas_y_start - area_height), 30, area_height, 
                              boxstyle="round,pad=0.5", 
                              facecolor='#eeffee', 
                              edgecolor=green, 
                              linewidth=2)
    ax.add_patch(area3_box)
    
    ax.text(83, areas_y_start - 3, 'LLM4C2HLS', 
            fontsize=16, fontweight='bold', color=green, 
            ha='center', va='center')
    
    c2hls_projects = [
        '• C2HLSC: Software-to-hardware gap',
        '• Automated C code refactoring',
        '• HLS-compatible transformation',
        '• Iterative LLM feedback'
    ]
    
    for i, project in enumerate(c2hls_projects):
        ax.text(70, areas_y_start - 8 - i*4, project, 
                fontsize=11, color=dark_gray, ha='left', va='center')
    
    # Featured Submodules Section
    featured_y_start = 75
    ax.text(50, featured_y_start + 2, 'Featured Submodules', 
            fontsize=24, fontweight='bold', color=primary_blue, 
            ha='center', va='center')
    
    # Submodule 1: AutoChip
    submod1_box = FancyBboxPatch((2, featured_y_start - 25), 30, 22, 
                                boxstyle="round,pad=0.5", 
                                facecolor=gray, 
                                edgecolor=primary_blue, 
                                linewidth=2)
    ax.add_patch(submod1_box)
    
    ax.text(17, featured_y_start - 5, 'AutoChip', 
            fontsize=18, fontweight='bold', color=primary_blue, 
            ha='center', va='center')
    
    # Add a simple diagram for AutoChip
    # Input arrow
    ax.arrow(4, featured_y_start - 10, 6, 0, head_width=1, head_length=1, fc=green, ec=green)
    ax.text(7, featured_y_start - 12, 'Design\nPrompt', fontsize=8, ha='center', va='center')
    
    # LLM box
    llm_box = Rectangle((12, featured_y_start - 12), 10, 4, facecolor=secondary_blue, edgecolor='black')
    ax.add_patch(llm_box)
    ax.text(17, featured_y_start - 10, 'LLM', fontsize=10, fontweight='bold', color='white', ha='center', va='center')
    
    # Output arrow
    ax.arrow(22, featured_y_start - 10, 6, 0, head_width=1, head_length=1, fc=green, ec=green)
    ax.text(25, featured_y_start - 12, 'Functional\nVerilog', fontsize=8, ha='center', va='center')
    
    ax.text(17, featured_y_start - 18, 'Generates functional Verilog modules\nwith iterative error feedback', 
            fontsize=10, color=dark_gray, ha='center', va='center')
    
    # Submodule 2: C2HLS
    submod2_box = FancyBboxPatch((35, featured_y_start - 25), 30, 22, 
                                boxstyle="round,pad=0.5", 
                                facecolor=gray, 
                                edgecolor=green, 
                                linewidth=2)
    ax.add_patch(submod2_box)
    
    ax.text(50, featured_y_start - 5, 'C2HLS', 
            fontsize=18, fontweight='bold', color=green, 
            ha='center', va='center')
    
    # Add a simple diagram for C2HLS
    # C Code box
    c_box = Rectangle((37, featured_y_start - 12), 8, 4, facecolor='#ffdddd', edgecolor='black')
    ax.add_patch(c_box)
    ax.text(41, featured_y_start - 10, 'C Code', fontsize=9, fontweight='bold', ha='center', va='center')
    
    # Arrow
    ax.arrow(45, featured_y_start - 10, 6, 0, head_width=1, head_length=1, fc=green, ec=green)
    
    # HLS box
    hls_box = Rectangle((53, featured_y_start - 12), 10, 4, facecolor='#ddffdd', edgecolor='black')
    ax.add_patch(hls_box)
    ax.text(58, featured_y_start - 10, 'HLS-Ready\nC Code', fontsize=8, fontweight='bold', ha='center', va='center')
    
    ax.text(50, featured_y_start - 18, 'Bridges software-to-hardware\ndesign gap with LLM guidance', 
            fontsize=10, color=dark_gray, ha='center', va='center')
    
    # Submodule 3: Security Assertion Generation
    submod3_box = FancyBboxPatch((68, featured_y_start - 25), 30, 22, 
                                boxstyle="round,pad=0.5", 
                                facecolor=gray, 
                                edgecolor=orange, 
                                linewidth=2)
    ax.add_patch(submod3_box)
    
    ax.text(83, featured_y_start - 5, 'Security Assertions', 
            fontsize=16, fontweight='bold', color=orange, 
            ha='center', va='center')
    
    # Add a simple diagram for Security Assertions
    # Natural Language box
    nl_box = Rectangle((70, featured_y_start - 12), 10, 4, facecolor='#ffffdd', edgecolor='black')
    ax.add_patch(nl_box)
    ax.text(75, featured_y_start - 10, 'Natural\nLanguage', fontsize=8, fontweight='bold', ha='center', va='center')
    
    # Arrow
    ax.arrow(80, featured_y_start - 10, 6, 0, head_width=1, head_length=1, fc=orange, ec=orange)
    
    # SVA box
    sva_box = Rectangle((88, featured_y_start - 12), 8, 4, facecolor='#ffddff', edgecolor='black')
    ax.add_patch(sva_box)
    ax.text(92, featured_y_start - 10, 'SVA\nCode', fontsize=8, fontweight='bold', ha='center', va='center')
    
    ax.text(83, featured_y_start - 18, 'Generates SystemVerilog assertions\nfor security verification', 
            fontsize=10, color=dark_gray, ha='center', va='center')
    
    # Key Features Section
    features_y_start = 45
    features_box = FancyBboxPatch((5, features_y_start - 20), 90, 18, 
                                 boxstyle="round,pad=1", 
                                 facecolor='#f8f9fa', 
                                 edgecolor=primary_blue, 
                                 linewidth=2)
    ax.add_patch(features_box)
    
    ax.text(50, features_y_start - 2, 'Key Framework Features', 
            fontsize=20, fontweight='bold', color=primary_blue, 
            ha='center', va='center')
    
    features = [
        '• End-to-end automated pipelines for hardware design',
        '• Iterative feedback mechanisms with EDA tools', 
        '• Security-focused verification and assertion generation',
        '• Multi-modal LLM integration (text, code, schematics)',
        '• Comprehensive evaluation frameworks and benchmarks',
        '• Hierarchical design methodologies for complex systems'
    ]
    
    # Split features into two columns
    left_features = features[:3]
    right_features = features[3:]
    
    for i, feature in enumerate(left_features):
        ax.text(10, features_y_start - 8 - i*3, feature, 
                fontsize=12, color=dark_gray, ha='left', va='center')
    
    for i, feature in enumerate(right_features):
        ax.text(55, features_y_start - 8 - i*3, feature, 
                fontsize=12, color=dark_gray, ha='left', va='center')
    
    # Footer with links
    footer_box = FancyBboxPatch((5, 2), 90, 8, 
                               boxstyle="round,pad=0.5", 
                               facecolor=primary_blue, 
                               edgecolor='black', 
                               linewidth=1)
    ax.add_patch(footer_box)
    
    ax.text(50, 7, 'Repository: github.com/FCHXWH823/LLM4Hardware', 
            fontsize=16, fontweight='bold', color='white', 
            ha='center', va='center')
    
    ax.text(50, 4, 'Papers • Code • Tutorials • Collaborative Research Framework', 
            fontsize=14, color='white', ha='center', va='center')
    
    plt.tight_layout()
    return fig

# Generate and save the poster
if __name__ == "__main__":
    print("Creating LLM4ChipDesign poster...")
    fig = create_llm4chipdesign_poster()
    
    # Save as high-resolution PDF and PNG
    fig.savefig('/home/runner/work/LLM4Hardware/LLM4Hardware/LLM4ChipDesign_poster.pdf', 
                dpi=300, bbox_inches='tight', facecolor='white')
    fig.savefig('/home/runner/work/LLM4Hardware/LLM4Hardware/LLM4ChipDesign_poster.png', 
                dpi=300, bbox_inches='tight', facecolor='white')
    
    print("Poster saved as:")
    print("- LLM4ChipDesign_poster.pdf")
    print("- LLM4ChipDesign_poster.png")
    
    plt.show()