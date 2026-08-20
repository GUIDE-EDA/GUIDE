# DATE 2025 Conference Paper: GUIDE

This directory contains the LaTeX source for the DATE 2025 conference paper on GUIDE (GenAI-based University Instructional collateral for Design and EDA).

## Files

- `main.tex`: Main LaTeX document (6 pages)
- `references.bib`: BibTeX bibliography file
- `Makefile`: Build automation
- `README.md`: This file

## Paper Abstract

GUIDE is a classroom-ready courseware for teaching GenAI in EDA. It packages customizable syllabus, slide decks, stackable Colab modules, and benchmark datasets spanning digital and analog flows: NL→RTL synthesis, assertion/testbench generation, hierarchical prompting, formal and property checks, and security (e.g., hardware Trojans, IP risks). Students run prompts, simulation, and verification in the browser against curated benchmarks; instructors get rubrics, project prompts, and assessment aids. GUIDE drops cleanly into VLSI/EDA courses, bootcamps, or upskilling modules, scaffolding skills from prompt engineering to verification and security analysis using open-sourced resources.

## Authors

- Weihua Xiao (NYU)
- Jason Blocklove (NYU)
- Johann Knechtel (NYU-AD)
- Ozgur Sinanoglu (NYU-AD)
- Kanad Basu (RPI)
- Jeyavijayan Rajendran (TAMU)
- Siddharth Garg (NYU)
- Ramesh Karri (NYU)

## Compilation Instructions

### Prerequisites

You need a LaTeX distribution installed on your system:

- **Linux/macOS**: Install TeX Live
  ```bash
  # Ubuntu/Debian
  sudo apt-get install texlive-full
  
  # macOS with Homebrew
  brew install --cask mactex
  ```

- **Windows**: Install MiKTeX or TeX Live

### Building the Paper

#### Option 1: Using Make (Recommended)

```bash
make
```

This will compile the paper and generate `main.pdf`.

To clean up auxiliary files:
```bash
make clean
```

To remove all generated files including the PDF:
```bash
make cleanall
```

#### Option 2: Manual Compilation

```bash
pdflatex main.tex
bibtex main
pdflatex main.tex
pdflatex main.tex
```

The multiple runs are necessary to resolve cross-references and bibliography citations.

#### Option 3: Using Online LaTeX Editors

You can also compile this paper using online services:

- **Overleaf**: Upload all files to a new project
- **ShareLaTeX**: Upload all files to a new project

## Conference Information

**Conference**: DATE 2025 (Design, Automation & Test in Europe Conference)

**Special Session**: LLMs in Teaching - Implications on Student Competencies

**Focus**: The conference is particularly interested in:
- Insights and comments on the use of LLMs in teaching
- Implications on the competences students develop
- Possible impacts not only in the short but also long-term

## Paper Structure

1. **Introduction**: Motivation and challenges of integrating LLMs into hardware design education
2. **Background and Related Work**: Review of LLMs in hardware design and hardware design education
3. **The GUIDE Framework**: Architecture and design principles
4. **Instructional Modules and Technical Details**: Detailed description of teaching modules
5. **Student Competencies and Learning Outcomes**: Analysis of skills developed through GUIDE
6. **Discussion**: Short-term and long-term implications for education and workforce
7. **Conclusion**: Summary and future directions

## Related Resources

- **GUIDE Repository**: https://github.com/FCHXWH823/LLM4ChipDesign
- **Colab Notebooks**: Available in the `colab-scripts/` directory
- **Slides**: Available in the `slides/` directory
- **Syllabus**: Available in the `Syllabus/` directory
- **Papers**: Individual project papers available in the `Papers/` directory

## License

This paper and associated materials are open-sourced for educational purposes. Please cite appropriately if you use or adapt these materials.

## Contact

For questions or feedback, please contact:
- Weihua Xiao: wx424@nyu.edu
- Jason Blocklove: jb7046@nyu.edu
- Ramesh Karri: rkarri@nyu.edu

## Citation

If you use GUIDE in your teaching or research, please cite:

```bibtex
@inproceedings{guide2025,
  title={GUIDE: GenAI-based University Instructional Collateral for Design and EDA},
  author={Xiao, Weihua and Blocklove, Jason and Knechtel, Johann and Sinanoglu, Ozgur and Basu, Kanad and Rajendran, Jeyavijayan and Garg, Siddharth and Karri, Ramesh},
  booktitle={Design, Automation \& Test in Europe Conference (DATE)},
  year={2025}
}
```
