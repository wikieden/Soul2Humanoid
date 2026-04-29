.PHONY: help charts check clean all

help:
	@echo "Soul2Humanoid — Makefile targets"
	@echo ""
	@echo "  make charts   — Generate all SVG/PNG diagrams from scripts/"
	@echo "  make check    — Check external links in all markdown files"
	@echo "  make clean    — Remove generated chart files"
	@echo "  make all      — Run charts + check"

charts:
	@echo "Generating Physical Intelligence diagrams..."
	@cd scripts && python3 generate_diagrams.py
	@echo ""
	@echo "Generating comparison charts..."
	@cd scripts && python3 generate_comparison_chart.py
	@echo ""
	@echo "All charts generated. Check assets/ for output."

check:
	@echo "Checking external links..."
	@python3 scripts/check_links.py

clean:
	@echo "Cleaning generated assets (preserving source SVGs)..."
	@find assets -name '*.png' -delete
	@echo "PNG files removed. SVG files preserved."

all: charts check
