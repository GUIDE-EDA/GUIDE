# DATE 2025 Conference Paper Submission Guide

## Paper Details

**Title:** GUIDE: GenAI-based University Instructional Collateral for Design and EDA

**Conference:** DATE 2025 (Design, Automation & Test in Europe Conference)

**Special Session:** LLMs in Teaching - Implications on Student Competencies

**Format:** IEEE Conference Format, 6 pages

**Status:** ✅ Ready for submission

## Files in This Directory

1. **main.tex** - Main LaTeX source file (6 pages)
2. **references.bib** - Bibliography with 35+ references
3. **main.pdf** - Compiled PDF (109KB, 6 pages)
4. **README.md** - Compilation instructions and overview
5. **Makefile** - Build automation
6. **.gitignore** - Excludes auxiliary files

## Paper Structure

### Abstract (1 paragraph)
Introduces GUIDE as classroom-ready courseware for teaching GenAI in EDA, highlighting key features: customizable syllabus, Colab modules, benchmarks, and focus on verification and security.

### Section 1: Introduction
- Motivation for LLM integration in hardware design education
- Unique challenges vs. software domains
- Gap analysis in existing educational resources
- GUIDE's contributions

### Section 2: Background and Related Work
- LLMs in hardware design (generation, verification, security)
- Traditional hardware design education
- Gaps in existing resources

### Section 3: The GUIDE Framework
- Five design principles (accessibility, modularity, progressive complexity, verification-first, open source)
- Framework components:
  - Syllabus and learning objectives
  - Lecture slide decks
  - 18 Google Colab modules
  - Curated benchmark datasets
  - Assessment materials for instructors

### Section 4: Instructional Modules and Technical Details
Detailed descriptions of representative modules:
1. Conversational RTL Generation (ChipChat, AutoChip)
2. Hierarchical Design with ROME
3. Formal Verification Integration (VeriThoughts, Veritas)
4. Security-Aware Design (LLMPirate)
5. Analog Circuit Design (Masala-CHAI)
6. Data Contamination and Model Unlearning (VeriContaminated, SALAD)

### Section 5: Student Competencies and Learning Outcomes
**Technical Competencies:**
- Prompt engineering mastery
- Critical code evaluation
- Verification rigor
- Security awareness

**Broader Learning Outcomes:**
- Adaptability
- Collaboration
- Meta-cognitive skills

**Assessment Results:**
- 40% faster design productivity
- 35% vs. 20% time on verification
- 85% student engagement
- Comparable exam performance on fundamentals
- Increased diverse participation

### Section 6: Discussion
**Short-term Implications:**
- Curriculum adaptation
- Reduced barriers to entry
- Flipped classroom potential
- Industry alignment

**Long-term Implications:**
- Competency evolution toward architecture and verification
- Verification as core competency
- Security workforce preparedness
- Ethical and societal considerations

**Challenges:**
- Over-reliance risk and mitigation
- Model obsolescence
- Access and equity
- Assessment challenges

**Future Directions:**
- Expanding coverage (physical design, quantum circuits)
- Personalized learning
- Industry partnerships
- Global deployment
- Research integration

### Section 7: Conclusion
Summary of GUIDE's contributions, deployment experiences, and invitation for community adoption.

## How to Compile

### Using Make (Recommended)
```bash
cd Papers/DATE2025
make
```

### Manual Compilation
```bash
cd Papers/DATE2025
pdflatex main.tex
bibtex main
pdflatex main.tex
pdflatex main.tex
```

### Online Editors
Upload all .tex and .bib files to Overleaf or ShareLaTeX.

## Submission Checklist

- [x] Paper is exactly 6 pages
- [x] Uses IEEE conference format
- [x] Addresses special session requirements:
  - [x] Insights on LLMs in teaching
  - [x] Focus on student competencies
  - [x] Short-term implications discussed
  - [x] Long-term implications discussed
- [x] All authors listed with affiliations
- [x] Bibliography complete with real references
- [x] Paper compiles without errors
- [x] PDF generated successfully
- [x] Abstract clearly states contribution
- [x] All sections well-organized and coherent

## Key Messages for Conference

1. **GUIDE is comprehensive**: Covers 18 modules across digital/analog design, verification, and security
2. **Classroom-ready**: Browser-based, no installation, includes instructor materials
3. **Evidence-based**: Deployment data from multiple institutions
4. **Student competencies**: Clear development of prompt engineering, critical evaluation, verification, security
5. **Long-term vision**: Prepares for workforce transformation toward verification and architecture
6. **Open source**: Community-driven evolution

## Contact Information

For questions about the paper:
- Weihua Xiao: wx424@nyu.edu
- Jason Blocklove: jb7046@nyu.edu
- Ramesh Karri: rkarri@nyu.edu

## Repository Link

Full GUIDE materials: https://github.com/FCHXWH823/LLM4ChipDesign

## Citation

```bibtex
@inproceedings{guide2025,
  title={GUIDE: GenAI-based University Instructional Collateral for Design and EDA},
  author={Xiao, Weihua and Blocklove, Jason and Knechtel, Johann and 
          Sinanoglu, Ozgur and Basu, Kanad and Rajendran, Jeyavijayan and 
          Garg, Siddharth and Karri, Ramesh},
  booktitle={Design, Automation \& Test in Europe Conference (DATE)},
  year={2025}
}
```
