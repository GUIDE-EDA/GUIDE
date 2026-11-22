# Makefile for DATE 2025 Conference Paper

# Main LaTeX file (without .tex extension)
MAIN = main

# LaTeX compiler
LATEX = pdflatex

# BibTeX compiler
BIBTEX = bibtex

# Output PDF file
PDF = $(MAIN).pdf

# Auxiliary files generated during compilation
AUX_FILES = $(MAIN).aux $(MAIN).bbl $(MAIN).blg $(MAIN).log $(MAIN).out $(MAIN).toc $(MAIN).lof $(MAIN).lot

.PHONY: all clean cleanall view

# Default target: build the PDF
all: $(PDF)

# Build the PDF with full bibliography processing
$(PDF): $(MAIN).tex references.bib
	@echo "Compiling LaTeX document (first pass)..."
	$(LATEX) $(MAIN).tex
	@echo "Running BibTeX..."
	$(BIBTEX) $(MAIN)
	@echo "Compiling LaTeX document (second pass)..."
	$(LATEX) $(MAIN).tex
	@echo "Compiling LaTeX document (third pass)..."
	$(LATEX) $(MAIN).tex
	@echo "PDF generated: $(PDF)"

# Quick build (single pass, no bibliography update)
quick: $(MAIN).tex
	@echo "Quick compiling LaTeX document..."
	$(LATEX) $(MAIN).tex
	@echo "Quick PDF generated: $(PDF)"

# Clean auxiliary files but keep PDF
clean:
	@echo "Cleaning auxiliary files..."
	rm -f $(AUX_FILES)
	@echo "Clean complete."

# Clean all generated files including PDF
cleanall: clean
	@echo "Removing PDF..."
	rm -f $(PDF)
	@echo "All generated files removed."

# View the PDF (works on systems with xdg-open, open, or evince)
view: $(PDF)
	@if command -v xdg-open > /dev/null; then \
		xdg-open $(PDF); \
	elif command -v open > /dev/null; then \
		open $(PDF); \
	elif command -v evince > /dev/null; then \
		evince $(PDF); \
	else \
		echo "No PDF viewer found. Please open $(PDF) manually."; \
	fi

# Help target
help:
	@echo "Available targets:"
	@echo "  all (default) - Build the complete PDF with bibliography"
	@echo "  quick         - Quick build (single pass, no bibliography)"
	@echo "  clean         - Remove auxiliary files (keep PDF)"
	@echo "  cleanall      - Remove all generated files including PDF"
	@echo "  view          - Open the PDF in default viewer"
	@echo "  help          - Show this help message"
