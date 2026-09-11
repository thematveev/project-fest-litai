#!/usr/bin/env python3
"""Build script: optimizes images, minifies CSS/JS, outputs dist/."""

import os
import re
import shutil
from pathlib import Path
from PIL import Image

SRC = Path(__file__).parent
DIST = SRC / "dist"

IMG_EXTS = {".jpg", ".jpeg", ".png", ".webp", ".gif", ".svg", ".ico"}
CSS_JS_EXTS = {".css", ".js"}


def ensure_dist():
    if DIST.exists():
        shutil.rmtree(DIST)
    DIST.mkdir(parents=True)


def optimize_jpeg(src: Path, dst: Path, max_width=800, quality=78):
    img = Image.open(src)
    if img.width > max_width:
        ratio = max_width / img.width
        new_h = int(img.height * ratio)
        img = img.resize((max_width, new_h), Image.LANCZOS)
    if img.mode == "RGBA":
        img = img.convert("RGB")
    img.save(dst, "JPEG", quality=quality, optimize=True, progressive=True)


def optimize_png(src: Path, dst: Path):
    img = Image.open(src)
    img.save(dst, "PNG", optimize=True)


def optimize_image(src: Path, dst: Path):
    ext = src.suffix.lower()
    if ext in (".jpg", ".jpeg"):
        # Large images (>200KB or >1200px wide): resize aggressively
        img = Image.open(src)
        is_large = src.stat().st_size > 200_000 or img.width > 1200
        if is_large:
            optimize_jpeg(src, dst, max_width=800, quality=75)
        else:
            optimize_jpeg(src, dst, max_width=1200, quality=82)
    elif ext == ".png":
        optimize_png(src, dst)
    elif ext == ".webp":
        img = Image.open(src)
        if img.width > 800:
            ratio = 800 / img.width
            img = img.resize((800, int(img.height * ratio)), Image.LANCZOS)
        img.save(dst, "WEBP", quality=80)
    else:
        shutil.copy2(src, dst)


def minify_css(text: str) -> str:
    # Remove comments
    text = re.sub(r'/\*.*?\*/', '', text, flags=re.DOTALL)
    # Remove newlines and collapse whitespace
    text = re.sub(r'\s*\n\s*', '\n', text)
    text = re.sub(r'\n', ' ', text)
    text = re.sub(r'\s*{\s*', '{', text)
    text = re.sub(r'\s*}\s*', '}', text)
    text = re.sub(r'\s*:\s*', ':', text)
    text = re.sub(r'\s*;\s*', ';', text)
    text = re.sub(r'\s*,\s*', ',', text)
    text = re.sub(r'\s+', ' ', text)
    return text.strip()


def minify_js(text: str) -> str:
    # Remove block comments
    text = re.sub(r'/\*.*?\*/', '', text, flags=re.DOTALL)
    # Remove single-line comments — but NOT // inside strings
    # Process line by line, stripping trailing comments
    lines = []
    for line in text.split('\n'):
        # Simple heuristic: only strip // that is NOT inside a string
        # by counting quote positions
        result = []
        in_str = None
        i = 0
        while i < len(line):
            ch = line[i]
            if in_str:
                result.append(ch)
                if ch == '\\' and i + 1 < len(line):
                    result.append(line[i + 1])
                    i += 2
                    continue
                if ch == in_str:
                    in_str = None
            else:
                if ch in ('"', "'", '`'):
                    in_str = ch
                    result.append(ch)
                elif ch == '/' and i + 1 < len(line) and line[i + 1] == '/':
                    break  # rest is comment
                else:
                    result.append(ch)
            i += 1
        lines.append(''.join(result))
    text = '\n'.join(lines)
    # Collapse whitespace
    text = re.sub(r'\s*\n\s*', '\n', text)
    text = re.sub(r'\n', ' ', text)
    text = re.sub(r'\s+', ' ', text)
    return text.strip()


def copy_assets():
    """Copy and optimize all assets."""
    assets_dist = DIST / "assets"
    assets_dist.mkdir(exist_ok=True)

    for item in SRC.rglob("*"):
        if item.is_dir():
            continue
        rel = item.relative_to(SRC)
        # Skip dist, screenshots, DS_Store, build.py, images/ (not used in site)
        parts = rel.parts
        if parts[0] == "dist" or parts[0] == "images" or parts[0] == ".playwright-mcp":
            continue
        if item.name == ".DS_Store" or item.name == "build.py":
            continue
        if rel.suffix.lower() == ".png" and "screenshot" in item.name:
            continue
        # Skip markdown docs, root-level non-site files
        if rel.suffix.lower() in (".md",):
            continue
        # Only skip root-level logo duplicates, NOT assets/logo/
        if rel.parent == Path(".") and item.name in ("logo.png", "logo3.JPG", "logo.JPG"):
            continue

        dst = DIST / rel
        dst.parent.mkdir(parents=True, exist_ok=True)

        if rel.suffix.lower() in IMG_EXTS and rel.suffix.lower() != ".svg":
            try:
                is_hero = item.stem.lower().startswith("hero") or item.name.lower() == "tikets.jpg"
                if is_hero:
                    shutil.copy2(item, dst)
                    print(f"  {rel.name}: copied ({item.stat().st_size//1024}KB) [hero, no compress]")
                else:
                    optimize_image(item, dst)
                    orig = item.stat().st_size
                    new = dst.stat().st_size
                    saved = (1 - new / orig) * 100 if orig > 0 else 0
                    if saved > 5:
                        print(f"  {rel.name}: {orig//1024}KB -> {new//1024}KB ({saved:.0f}% saved)")
                    else:
                        print(f"  {rel.name}: copied ({new//1024}KB)")
            except Exception as e:
                print(f"  {rel.name}: error ({e}), copying as-is")
                shutil.copy2(item, dst)
        else:
            shutil.copy2(item, dst)


def process_css_js():
    """Minify CSS and JS files in dist."""
    for f in DIST.rglob("*.css"):
        try:
            orig = f.stat().st_size
            text = f.read_text(encoding="utf-8")
            f.write_text(minify_css(text), encoding="utf-8")
            new = f.stat().st_size
            saved = (1 - new / orig) * 100 if orig > 0 else 0
            print(f"  CSS {f.name}: {orig//1024}KB -> {new//1024}KB ({saved:.0f}% saved)")
        except Exception as e:
            print(f"  CSS {f.name}: error ({e})")

    for f in DIST.rglob("*.js"):
        try:
            orig = f.stat().st_size
            text = f.read_text(encoding="utf-8")
            f.write_text(minify_js(text), encoding="utf-8")
            new = f.stat().st_size
            saved = (1 - new / orig) * 100 if orig > 0 else 0
            print(f"  JS {f.name}: {orig//1024}KB -> {new//1024}KB ({saved:.0f}% saved)")
        except Exception as e:
            print(f"  JS {f.name}: error ({e})")


def main():
    print("Building dist/ ...\n")
    ensure_dist()

    print("1. Copying & optimizing images...")
    copy_assets()

    print("\n2. Minifying CSS & JS...")
    process_css_js()

    print(f"\nDone! Output: {DIST}")
    total = sum(f.stat().st_size for f in DIST.rglob("*") if f.is_file())
    print(f"Total dist size: {total // 1024}KB")


if __name__ == "__main__":
    main()
