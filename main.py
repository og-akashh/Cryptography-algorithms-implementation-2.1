#!/usr/bin/env python3
"""Entry point for the cryptography project.

Running ``python main.py`` launches the interactive menu. Any arguments are
passed to the CLI subcommand parser (see :mod:`crypto_app.cli`).
"""

from __future__ import annotations

import sys
from pathlib import Path

# Make the src/ layout importable without requiring ``pip install -e .``.
_SRC = Path(__file__).resolve().parent / "src"
if str(_SRC) not in sys.path:
    sys.path.insert(0, str(_SRC))

from crypto_app.cli import main  # noqa: E402

if __name__ == "__main__":
    sys.exit(main())
