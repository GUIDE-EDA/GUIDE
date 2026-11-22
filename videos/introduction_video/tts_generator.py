#!/usr/bin/env python3
"""
Text-to-Speech Generator for LLM4Hardware Introduction Video

This script converts the video script to audio using text-to-speech.
Requires: pip install pyttsx3

Usage: python tts_generator.py
"""

import re
import os
try:
    import pyttsx3
    TTS_AVAILABLE = True
except ImportError:
    TTS_AVAILABLE = False

def extract_narration_from_script():
    """Extract narration text from the video script"""
    script_path = 'video_script.md'
    
    if not os.path.exists(script_path):
        print(f"Error: {script_path} not found!")
        return None
    
    with open(script_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Extract text between **Narrator:** markers
    narrator_pattern = r'\*\*Narrator:\*\* "(.*?)"'
    narration_blocks = re.findall(narrator_pattern, content, re.DOTALL)
    
    if not narration_blocks:
        print("No narration blocks found in script!")
        return None
    
    # Join all narration with appropriate pauses
    full_narration = ""
    for i, block in enumerate(narration_blocks):
        # Clean up formatting
        clean_block = block.replace('\n', ' ').replace('  ', ' ').strip()
        full_narration += clean_block
        
        # Add pause between sections (except last)
        if i < len(narration_blocks) - 1:
            full_narration += "\n\n[PAUSE]\n\n"
    
    return full_narration

def generate_tts_audio(text, output_file='narration.wav'):
    """Generate text-to-speech audio from the narration text"""
    if not TTS_AVAILABLE:
        print("Error: pyttsx3 not installed!")
        print("Install with: pip install pyttsx3")
        return False
    
    try:
        # Initialize TTS engine
        engine = pyttsx3.init()
        
        # Configure voice settings
        voices = engine.getProperty('voices')
        
        # Try to find a good English voice
        for voice in voices:
            if 'english' in voice.name.lower() or 'en' in voice.id.lower():
                engine.setProperty('voice', voice.id)
                break
        
        # Set speech rate (words per minute)
        engine.setProperty('rate', 180)  # Slightly slower for clarity
        
        # Set volume (0.0 to 1.0)
        engine.setProperty('volume', 0.9)
        
        # Process text with pauses
        processed_text = text.replace('[PAUSE]', '... ')
        
        # Save to file
        engine.save_to_file(processed_text, output_file)
        engine.runAndWait()
        
        print(f"Audio generated: {output_file}")
        return True
        
    except Exception as e:
        print(f"Error generating TTS: {e}")
        return False

def create_narration_segments():
    """Create separate audio files for each section"""
    script_path = 'video_script.md'
    
    if not os.path.exists(script_path):
        print(f"Error: {script_path} not found!")
        return False
    
    with open(script_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Define section patterns and their timings
    sections = [
        ('Opening', r'## Opening.*?\*\*Narrator:\*\* "(.*?)"', '00-15s'),
        ('Introduction', r'## Main Introduction.*?\*\*Narrator:\*\* "(.*?)"', '15-45s'),
        ('Scope', r'## Project Scope.*?\*\*Narrator:\*\* "(.*?)"', '45-90s'),
        ('Innovation', r'## Innovation Highlight.*?\*\*Narrator:\*\* "(.*?)"', '90-120s'),
        ('Impact', r'## Impact Statement.*?\*\*Narrator:\*\* "(.*?)"', '120-150s'),
        ('Closing', r'## Closing.*?\*\*Narrator:\*\* "(.*?)"', '150-180s')
    ]
    
    # Create segments directory
    os.makedirs('audio_segments', exist_ok=True)
    
    if not TTS_AVAILABLE:
        print("TTS not available. Creating text files instead...")
        
        for section_name, pattern, timing in sections:
            match = re.search(pattern, content, re.DOTALL)
            if match:
                text = match.group(1).replace('\n', ' ').replace('  ', ' ').strip()
                filename = f'audio_segments/{section_name.lower()}_{timing.replace("-", "to").replace("s", "sec")}.txt'
                
                with open(filename, 'w', encoding='utf-8') as f:
                    f.write(f"# {section_name} ({timing})\n\n")
                    f.write(text)
                
                print(f"Created: {filename}")
        
        return True
    
    # Generate TTS for each section
    engine = pyttsx3.init()
    
    for section_name, pattern, timing in sections:
        match = re.search(pattern, content, re.DOTALL)
        if match:
            text = match.group(1).replace('\n', ' ').replace('  ', ' ').strip()
            filename = f'audio_segments/{section_name.lower()}_{timing.replace("-", "to").replace("s", "sec")}.wav'
            
            try:
                engine.save_to_file(text, filename)
                engine.runAndWait()
                print(f"Generated: {filename}")
            except Exception as e:
                print(f"Error generating {filename}: {e}")
    
    return True

def create_timing_guide():
    """Create a timing guide for video synchronization"""
    timing_guide = """# Video Timing Guide for LLM4Hardware Introduction

## Audio-Visual Synchronization Guide

### Section 1: Opening (0-15 seconds)
**Audio:** "Welcome to LLM4Hardware - a comprehensive research initiative that's revolutionizing the intersection of artificial intelligence and chip design."
**Visual:** Animated title card with "Generative AI for Chip Design"
**Timing:** Start immediately, fade in title at 2s, hold until 15s

### Section 2: Main Introduction (15-45 seconds)  
**Audio:** "In today's rapidly evolving semiconductor landscape, Large Language Models are transforming how we approach hardware design, verification, and optimization. Our research spans the entire chip design workflow - from high-level behavioral descriptions to low-level circuit implementations."
**Visual:** Montage of circuit designs, AI neural networks, chip layouts
**Timing:** Transition at 15s, show flowing montage throughout

### Section 3: Project Scope (45-90 seconds)
**Audio:** Component overview listing all 12 research projects
**Visual:** Component matrix with progressive reveals
**Timing:** Show matrix at 45s, highlight components as mentioned

### Section 4: Innovation Highlight (90-120 seconds)
**Audio:** Comparison of traditional vs AI-assisted approaches
**Visual:** Split screen comparison diagram
**Timing:** Split screen reveal at 90s, animate differences

### Section 5: Impact Statement (120-150 seconds)
**Audio:** Performance improvements and accessibility benefits
**Visual:** Animated metrics and improvement charts
**Timing:** Charts appear at 120s, animate values progressively

### Section 6: Closing (150-180 seconds)
**Audio:** Call to action and project links
**Visual:** GitHub repository, project website, contact info
**Timing:** Fade to contact info at 150s, hold until end

## Technical Notes:
- Audio files are in /audio_segments/
- Visual assets are in /generated_assets/
- Total video length: 180 seconds (3 minutes)
- Fade transitions: 1-2 seconds each
- Text overlay duration: Minimum 3 seconds for readability

## Export Settings Recommendation:
- Video: 1920x1080, 30fps, H.264
- Audio: 48kHz, 24-bit, stereo
- Bitrate: High quality for presentations
"""
    
    with open('timing_guide.md', 'w', encoding='utf-8') as f:
        f.write(timing_guide)
    
    print("Created: timing_guide.md")

def main():
    """Main function to generate all audio assets"""
    print("LLM4Hardware TTS Generator")
    print("=" * 40)
    
    if not TTS_AVAILABLE:
        print("Warning: pyttsx3 not installed. Text files will be generated instead.")
        print("To install TTS: pip install pyttsx3")
        print()
    
    # Extract narration from script
    print("Extracting narration from script...")
    narration = extract_narration_from_script()
    
    if not narration:
        print("Failed to extract narration!")
        return
    
    # Save extracted narration as text file
    with open('full_narration.txt', 'w', encoding='utf-8') as f:
        f.write(narration)
    print("Saved: full_narration.txt")
    
    # Generate full audio file (if TTS available)
    if TTS_AVAILABLE:
        print("Generating full narration audio...")
        generate_tts_audio(narration, 'full_narration.wav')
    
    # Create individual section files
    print("Creating section-by-section audio/text files...")
    create_narration_segments()
    
    # Create timing guide
    print("Creating timing guide...")
    create_timing_guide()
    
    print("\nGeneration complete!")
    print("\nGenerated files:")
    print("- full_narration.txt (complete script)")
    if TTS_AVAILABLE:
        print("- full_narration.wav (complete audio)")
    print("- audio_segments/ (section-by-section files)")
    print("- timing_guide.md (synchronization guide)")
    
    if not TTS_AVAILABLE:
        print("\nNote: To generate audio files, install pyttsx3 and run again.")

if __name__ == "__main__":
    main()