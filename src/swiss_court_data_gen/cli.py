"""Command-line interface for Swiss Federal Court Data Generation."""

from __future__ import annotations

import sys

from swiss_court_data_gen import __version__


def main() -> int:
    """Main entry point for the CLI."""
    print(f"Swiss Court Data Generation v{__version__}")
    print("Hello World!")
    print("CLI implementation coming soon...")
    return 0


if __name__ == "__main__":
    sys.exit(main())
