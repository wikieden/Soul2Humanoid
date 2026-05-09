.PHONY: help charts check clean all sync build serve deploy

help:
	@echo "Soul2Humanoid — Makefile targets"
	@echo ""
	@echo "  make sync     — Sync markdown + assets to docs/ for MkDocs"
	@echo "  make charts   — Generate all SVG/PNG diagrams from scripts/"
	@echo "  make build    — Sync + mkdocs build"
	@echo "  make serve    — Sync + mkdocs serve (local preview)"
	@echo "  make check    — Check external links in all markdown files"
	@echo "  make clean    — Remove generated chart files"
	@echo "  make deploy   — Sync + git add + commit + push"
	@echo "  make all      — Run charts + check"

sync:
	@echo "Syncing docs/ from root markdown + reports + assets..."
	@python3 scripts/sync_docs.py

charts:
	@echo "Generating Physical Intelligence diagrams..."
	@cd scripts && python3 generate_diagrams.py
	@echo ""
	@echo "Generating comparison charts..."
	@cd scripts && python3 generate_comparison_chart.py
	@echo ""
	@echo "Generating data flywheel charts..."
	@cd scripts && python3 generate_data_flywheel_chart.py
	@echo ""
	@echo "All charts generated. Check assets/ for output."

build: sync
	@echo "Building MkDocs site..."
	@mkdocs build

serve: sync
	@echo "Starting MkDocs dev server..."
	@mkdocs serve

check:
	@echo "Checking external links..."
	@python3 scripts/check_links.py

clean:
	@echo "Cleaning generated assets (preserving source SVGs)..."
	@find assets -name '*.png' -delete
	@echo "PNG files removed. SVG files preserved."

deploy:
	@echo "Syncing docs..."
	@python3 scripts/sync_docs.py
	@echo "Add, commit, push..."
	@git add -A && git commit -m "chore: auto sync docs" && git push origin main

all: charts check
