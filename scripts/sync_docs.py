#!/usr/bin/env python3
"""Sync root-level markdown and assets to docs/ for MkDocs build."""
import os
import shutil
import glob

ROOT = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(ROOT)  # go up from scripts/ to repo root
DOCS = os.path.join(ROOT, 'docs')

MD_FILES = [
    'README.md', 'comparisons.md', 'papers.md', 'resources.md',
    'people.md', 'funding.md', 'tags.md', 'podcasts-videos.md',
    'latest-news.md', 'CHANGELOG.md', 'open-source-tracking.md',
    'CONTRIBUTING.md',
]

def ensure_dir(path):
    os.makedirs(path, exist_ok=True)

def copy_and_fix_paths(src, dst):
    """Copy markdown file and fix relative image paths for docs/ context."""
    with open(src, 'r', encoding='utf-8') as f:
        content = f.read()
    # Fix paths that reference parent dirs from docs/
    content = content.replace('](../../assets/', '](../assets/')
    content = content.replace('](./assets/', '](assets/')
    content = content.replace('](./reports/', '](reports/')
    content = content.replace('](../reports/', '](../reports/')
    with open(dst, 'w', encoding='utf-8') as f:
        f.write(content)

def sync():
    ensure_dir(DOCS)
    ensure_dir(os.path.join(DOCS, 'reports'))
    ensure_dir(os.path.join(DOCS, 'assets'))
    ensure_dir(os.path.join(DOCS, 'stylesheets'))

    # 1. Top-level markdown files
    for fname in MD_FILES:
        src = os.path.join(ROOT, fname)
        if not os.path.exists(src):
            continue
        dst_name = 'index.md' if fname == 'README.md' else fname
        dst = os.path.join(DOCS, dst_name)
        copy_and_fix_paths(src, dst)
        print(f"  sync: {fname} -> docs/{dst_name}")

    # 2. Company reports
    for report_dir in glob.glob(os.path.join(ROOT, 'reports', '*')):
        if not os.path.isdir(report_dir):
            continue
        company = os.path.basename(report_dir)
        src = os.path.join(report_dir, 'README.md')
        if os.path.exists(src):
            dst = os.path.join(DOCS, 'reports', f'{company}.md')
            copy_and_fix_paths(src, dst)
            print(f"  sync: reports/{company}/README.md -> docs/reports/{company}.md")

    # 3. Assets (top-level SVG/PNG)
    for ext in ['svg', 'png']:
        for src in glob.glob(os.path.join(ROOT, 'assets', f'*.{ext}')):
            dst = os.path.join(DOCS, 'assets', os.path.basename(src))
            shutil.copy2(src, dst)
        # Subdirectories
        for src in glob.glob(os.path.join(ROOT, 'assets', '*', f'*.{ext}')):
            rel = os.path.relpath(src, os.path.join(ROOT, 'assets'))
            dst = os.path.join(DOCS, 'assets', rel)
            ensure_dir(os.path.dirname(dst))
            shutil.copy2(src, dst)
    print("  sync: assets/ -> docs/assets/")

    # 4. Stylesheets
    for src in glob.glob(os.path.join(ROOT, 'docs', 'stylesheets', '*')):
        pass  # already in docs/

    print("\nDocs sync complete.")

if __name__ == '__main__':
    sync()
