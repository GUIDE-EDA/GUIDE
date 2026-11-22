# LLM4ChipDesign Poster

This directory contains the comprehensive poster for the LLM4Hardware repository.

## Poster Overview

**Title**: LLM4ChipDesign  
**Subtitle**: Comprehensive Research Framework for LLM-based Hardware Design

## Three Main Research Areas

### 1. LLM4Verilog Generation
- **AutoChip**: Functional Verilog from prompts
- **VeriThoughts**: Reasoning-based generation
- **ROME**: Hierarchical prompting
- **Veritas**: CNF-based synthesis
- **PrefixLLM**: Prefix circuit design

### 2. LLM4Security
- **LLMPirate**: IP piracy detection
- **Security Assertions**: LLM-generated SVA
- **Hybrid-NL2SVA**: Enhanced NL2SVA
- **OpenTitan RAG**: SVA for IP blocks

### 3. LLM4C2HLS
- **C2HLSC**: Software-to-hardware gap
- Automated C code refactoring
- HLS-compatible transformation
- Iterative LLM feedback

## Featured Submodules

### 1. AutoChip
- Generates functional Verilog modules with iterative error feedback
- **Slides**: [ETS 2025 Tutorial.pptx](slides/ETS%202025%20Tutorial.pptx)
- **Paper**: https://arxiv.org/abs/2311.04887
- **Code**: https://github.com/shailja-thakur/AutoChip.git

### 2. C2HLS
- Bridges software-to-hardware design gap with LLM guidance
- **Slides**: [C2HLSC - Neurips Tutorial.pptx](slides/C2HLSC%20-%20Neurips%20Tutorial.pptx)
- **Paper**: https://arxiv.org/abs/2412.00214
- **Code**: https://github.com/Lucaz97/c2hlsc

### 3. Security Assertion Generation
- Generates SystemVerilog assertions for security verification
- **Slides**: [llm_assertion_slides.pptx](slides/llm_assertion_slides.pptx)
- **Paper**: https://arxiv.org/abs/2306.14027

## Key Framework Features

- End-to-end automated pipelines for hardware design
- Iterative feedback mechanisms with EDA tools
- Security-focused verification and assertion generation
- Multi-modal LLM integration (text, code, schematics)
- Comprehensive evaluation frameworks and benchmarks
- Hierarchical design methodologies for complex systems

## Files

- `LLM4ChipDesign_poster.pdf` - High-resolution PDF version (recommended for printing)
- `LLM4ChipDesign_poster.png` - PNG version for web display
- `create_poster.py` - Python script used to generate the poster

## Usage

The poster can be used for:
- Conference presentations
- Research demonstrations
- Project overviews
- Academic publications
- Grant proposals

## Technical Details

- **Size**: A1 format (594 x 841 mm / 23.4 x 33.1 inches)
- **Resolution**: 300 DPI
- **Generated using**: Python matplotlib library
- **Fonts**: System default fonts for maximum compatibility