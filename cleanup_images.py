#!/usr/bin/env python3
"""
Trova le immagini in static/img/ non referenziate da nessun .md in content/
e le cancella dopo conferma.
"""

import re
import sys
from pathlib import Path

CONTENT_DIR = Path("/Users/barno/Documents/lavori/corsobitcoin/content")
STATIC_DIR  = Path("/Users/barno/Documents/lavori/corsobitcoin/static/img")

IMG_EXTS = {".jpg", ".jpeg", ".png", ".gif", ".webp", ".svg", ".avif"}

# Pattern che cattura path immagine nei .md
# Copre: ![alt](/img/...), cover: "/img/...", src="/img/..."
IMG_REF_RE = re.compile(
    r'(?:'
    r'!\[[^\]]*\]\((/img/[^\s)]+)\)'   # ![alt](/img/...)
    r'|cover:\s*["\']?(/img/[^\s"\']+)'  # cover: "/img/..."
    r'|src=["\']?(/img/[^\s"\'>\)]+)'   # src="/img/..."
    r')'
)

# ── 1. Raccoglie tutti i path immagine referenziati nei .md ──────────────────

referenced: set[str] = set()
md_files = list(CONTENT_DIR.rglob("*.md"))
print(f"File .md scansionati: {len(md_files)}")

for md in md_files:
    text = md.read_text(encoding="utf-8", errors="ignore")
    for m in IMG_REF_RE.finditer(text):
        path = m.group(1) or m.group(2) or m.group(3)
        if path:
            # Normalizza: rimuovi query string o anchor
            path = path.split('?')[0].split('#')[0].rstrip('"\')')
            referenced.add(path)

print(f"Path immagine referenziati nei .md: {len(referenced)}")

# ── 2. Raccoglie tutti i file immagine in static/img/ ────────────────────────

static_files = [
    f for f in STATIC_DIR.rglob("*")
    if f.is_file() and f.suffix.lower() in IMG_EXTS
]
print(f"File immagine in static/img/: {len(static_files)}\n")

# ── 3. Trova le immagini non usate ───────────────────────────────────────────

# Converte i path statici in /img/... per confronto
def to_web_path(p: Path) -> str:
    """static/img/posts/foo.webp → /img/posts/foo.webp"""
    parts = p.parts
    # Cerca "img" nei parts e ricostruisce da lì
    try:
        idx = parts.index("img")
        return "/" + "/".join(parts[idx:])
    except ValueError:
        return "/" + p.name

unused: list[Path] = []
for f in sorted(static_files):
    web = to_web_path(f)
    if web not in referenced:
        unused.append(f)

# ── 4. Stampa la lista ────────────────────────────────────────────────────────

if not unused:
    print("Nessuna immagine non utilizzata trovata.")
    sys.exit(0)

total_size = sum(f.stat().st_size for f in unused)
total_kb   = total_size / 1024
total_mb   = total_kb / 1024

print("=" * 60)
print(f"IMMAGINI NON REFERENZIATE ({len(unused)} file, {total_mb:.1f} MB)")
print("=" * 60)
for f in unused:
    kb = f.stat().st_size / 1024
    web = to_web_path(f)
    print(f"  {web:60s}  {kb:7.1f} KB")

print()
print(f"Totale: {len(unused)} file  |  {total_mb:.2f} MB ({total_kb:.0f} KB)")

# ── 5. Conferma ───────────────────────────────────────────────────────────────

print()
risposta = input("Cancellare questi file? [s/N] ").strip().lower()
if risposta not in ("s", "si", "sì", "y", "yes"):
    print("Annullato. Nessun file cancellato.")
    sys.exit(0)

# ── 6. Cancellazione ──────────────────────────────────────────────────────────

deleted = 0
freed   = 0
errors  = 0

for f in unused:
    size = f.stat().st_size
    try:
        f.unlink()
        deleted += 1
        freed   += size
        print(f"  [DEL] {to_web_path(f)}")
    except Exception as e:
        errors += 1
        print(f"  [ERR] {to_web_path(f)}: {e}", file=sys.stderr)

print()
print("=" * 60)
print(f"Cancellati : {deleted} file")
print(f"Spazio lib.: {freed/1024/1024:.2f} MB ({freed/1024:.0f} KB)")
if errors:
    print(f"Errori     : {errors}")
