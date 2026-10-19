SHELL := /bin/sh

IVERILOG ?= iverilog
VVP      ?= vvp
COVERED  ?= covered

BUILD   := build
DUT     := src/simple_alu.v
TB      := tb/simple_alu_tb.v
SIM     := $(BUILD)/simple_alu.vvp
RAW_VCD := $(BUILD)/simple_alu_raw.vcd
VCD     := $(BUILD)/simple_alu.vcd
CDD     := $(BUILD)/simple_alu.cdd
SUMMARY := $(BUILD)/coverage_summary.rpt
DETAIL  := $(BUILD)/coverage_detail.rpt
SLIDES_TEX := slides/coverage_flow_slides.tex
SLIDES_PDF := slides/coverage_flow_slides.pdf

.PHONY: all sim coverage report view slides check-tools clean clean-slides

all: report

$(BUILD):
	mkdir -p $(BUILD)

check-tools:
	@command -v $(IVERILOG) >/dev/null 2>&1 || { echo "ERROR: iverilog not found"; exit 1; }
	@command -v $(VVP) >/dev/null 2>&1 || { echo "ERROR: vvp not found"; exit 1; }
	@command -v $(COVERED) >/dev/null 2>&1 || { echo "ERROR: covered not found (see README.md)"; exit 1; }

$(SIM): $(DUT) $(TB) | $(BUILD)
	$(IVERILOG) -g2001 -Wall -s simple_alu_tb -o $@ $(DUT) $(TB)

$(RAW_VCD): $(SIM)
	$(VVP) $(SIM)

# Remove the VCD comment rejected by Covered 0.7.10.  Also put the 1ps
# timescale on one line so Fliplot displays the unit correctly.
$(VCD): $(RAW_VCD)
	perl -0pe 's/^\$$comment [^\n]*\n//mg; s/\$$timescale\s+1ps\s+\$$end/\$$timescale 1ps \$$end/' $< > $@.tmp
	mv $@.tmp $@

sim: $(VCD)

$(CDD): $(VCD) $(DUT)
	$(COVERED) score \
		-t simple_alu \
		-i simple_alu_tb.dut \
		-v $(DUT) \
		-vcd $(VCD) \
		-o $(CDD)

coverage: check-tools $(CDD)

$(SUMMARY): $(CDD)
	$(COVERED) report -m ltc -d s -o $@ $(CDD)

$(DETAIL): $(CDD)
	$(COVERED) report -m ltc -d v -i -o $@ $(CDD)

report: check-tools $(SUMMARY) $(DETAIL)
	@echo "Generated:"
	@echo "  $(SUMMARY)"
	@echo "  $(DETAIL)"

$(SLIDES_PDF): $(SLIDES_TEX)
	@command -v latexmk >/dev/null 2>&1 || { echo "ERROR: latexmk not found"; exit 1; }
	latexmk -pdf -interaction=nonstopmode -halt-on-error -outdir=slides $(SLIDES_TEX)

slides: $(SLIDES_PDF)
	@echo "Generated: $(SLIDES_PDF)"

# Optional Tcl/Tk GUI; only works if Covered was compiled with GUI support.
view: coverage
	$(COVERED) report -view $(CDD)

clean:
	rm -rf $(BUILD)

clean-slides:
	latexmk -C -outdir=slides $(SLIDES_TEX)
