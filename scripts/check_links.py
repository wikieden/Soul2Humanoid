#!/usr/bin/env python3
"""Check external links in markdown files."""
import os
import re
import sys
import urllib.request
from concurrent.futures import ThreadPoolExecutor, as_completed

SKIP_DIRS = {'.git', '.opencode', 'node_modules'}
SKIP_URLS = {
    'https://aistudio.google.com',
    'https://docs.google.com/forms',
}

def find_markdown_files(root_dir):
    md_files = []
    for dirpath, dirnames, filenames in os.walk(root_dir):
        dirnames[:] = [d for d in dirnames if d not in SKIP_DIRS]
        for f in filenames:
            if f.endswith('.md'):
                md_files.append(os.path.join(dirpath, f))
    return md_files

def extract_urls(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    result = []
    seen = set()

    # Markdown links: [text](url)
    md_pattern = re.compile(r'\[([^\]]+)\]\((https?://[^\s)]+(?:\)[^\s)]+)*)\)')
    for text, url in md_pattern.findall(content):
        while url and url[-1] in '.,;:!?\'"':
            url = url[:-1]
        if url not in seen:
            seen.add(url)
            result.append((filepath, url, text))

    # Bare URLs on their own line or in lists - allow parentheses in URL
    bare_pattern = re.compile(r'(?<![\[\(])(https?://[^\s\]]+)')
    for url in bare_pattern.findall(content):
        while url and url[-1] in '.,;:!?\'"':
            url = url[:-1]
        # Remove trailing unmatched parenthesis
        if url.count('(') < url.count(')'):
            url = url[:-1]
        if url not in seen:
            seen.add(url)
            result.append((filepath, url, ''))

    return result

def check_url(url, timeout=15):
    if any(url.startswith(skip) for skip in SKIP_URLS):
        return True, "skipped"
    try:
        req = urllib.request.Request(url, method='HEAD', headers={
            'User-Agent': 'Mozilla/5.0 (compatible; LinkChecker/1.0)'
        })
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            return True, resp.status
    except urllib.error.HTTPError as e:
        if e.code in (301, 302, 307, 308, 403):
            return True, f"HTTP {e.code}"
        try:
            req = urllib.request.Request(url, method='GET', headers={
                'User-Agent': 'Mozilla/5.0 (compatible; LinkChecker/1.0)'
            })
            with urllib.request.urlopen(req, timeout=timeout) as resp:
                return True, resp.status
        except urllib.error.HTTPError as e2:
            if e2.code in (301, 302, 307, 308, 403):
                return True, f"HTTP {e2.code}"
            return False, f"HTTP {e2.code}"
        except Exception:
            return False, f"HTTP {e.code}"
    except urllib.error.URLError as e:
        err_str = str(e.reason)
        if 'CERTIFICATE_VERIFY_FAILED' in err_str or 'SSL' in err_str or 'EOF occurred' in err_str:
            return True, f"SSL issue (likely false positive)"
        return False, str(e.reason)
    except Exception as e:
        return False, str(e)

def main():
    root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    md_files = find_markdown_files(root)
    print(f"Found {len(md_files)} markdown files")

    all_urls = []
    for md_file in md_files:
        urls = extract_urls(md_file)
        all_urls.extend(urls)

    unique_urls = {}
    for filepath, url, text in all_urls:
        if url not in unique_urls:
            unique_urls[url] = (filepath, text)

    print(f"Checking {len(unique_urls)} unique URLs...\n")

    results = {'ok': [], 'failed': [], 'skipped': []}

    with ThreadPoolExecutor(max_workers=10) as executor:
        future_to_url = {executor.submit(check_url, url): url for url in unique_urls}
        for future in as_completed(future_to_url):
            url = future_to_url[future]
            filepath, text = unique_urls[url]
            rel_path = os.path.relpath(filepath, root)
            try:
                ok, status = future.result()
                if status == "skipped":
                    results['skipped'].append((rel_path, url))
                    print(f"  SKIP  {url}")
                elif ok:
                    results['ok'].append((rel_path, url, status))
                    print(f"  OK    {url} ({status})")
                else:
                    results['failed'].append((rel_path, url, status))
                    print(f"  FAIL  {url} -> {status}")
            except Exception as e:
                results['failed'].append((rel_path, url, str(e)))
                print(f"  FAIL  {url} -> {e}")

    print(f"\n{'='*60}")
    print(f"Results: {len(results['ok'])} OK, {len(results['failed'])} FAILED, {len(results['skipped'])} SKIPPED")

    if results['failed']:
        print(f"\nFailed links:")
        for rel_path, url, status in results['failed']:
            print(f"  [{rel_path}] {url} -> {status}")
        sys.exit(1)
    else:
        print("\nAll links OK!")
        sys.exit(0)

if __name__ == '__main__':
    main()
