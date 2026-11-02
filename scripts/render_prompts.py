#!/usr/bin/env python3
"""Fill {{PLACEHOLDERS}} in prompts/*.md with values from config/config.yaml.

Usage:
    pip install pyyaml
    python scripts/render_prompts.py [--config config/config.yaml] [--out build]

The rendered prompts land in build/ (git-ignored). Paste them into your
Claude scheduled tasks / project instructions.
"""
import argparse
import pathlib
import re
import sys

try:
    import yaml
except ImportError:  # pragma: no cover
    sys.exit("Missing dependency: pip install pyyaml")

ROOT = pathlib.Path(__file__).resolve().parent.parent
PLACEHOLDER = re.compile(r"\{\{([A-Z0-9_]+)\}\}")


def indent_block(value: str, key: str) -> str:
    """Multi-line values (PROJECTS) are indented to fit the bullet lists."""
    if key == "PROJECTS":
        return "\n".join("  " + line if line.strip() else line
                         for line in value.strip().splitlines())
    return value.strip()


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--config", default=ROOT / "config" / "config.yaml")
    ap.add_argument("--out", default=ROOT / "build")
    args = ap.parse_args()

    cfg_path = pathlib.Path(args.config)
    if not cfg_path.exists():
        sys.exit(f"{cfg_path} not found. Copy config/config.example.yaml first.")
    cfg = {k: str(v) for k, v in (yaml.safe_load(cfg_path.read_text()) or {}).items()}

    out = pathlib.Path(args.out)
    out.mkdir(exist_ok=True)
    missing = set()
    for src in sorted((ROOT / "prompts").glob("*.md")):
        text = src.read_text()

        def repl(m):
            key = m.group(1)
            if key not in cfg:
                missing.add(key)
                return m.group(0)
            return indent_block(cfg[key], key)

        rendered = PLACEHOLDER.sub(repl, text)
        (out / src.name).write_text(rendered)
        print(f"✓ {out / src.name}  ({len(rendered):,} chars)")

    if missing:
        print("\n⚠ Unfilled placeholders:", ", ".join(sorted(missing)))
        sys.exit(1)


if __name__ == "__main__":
    main()
