"""
Advent of Code CLI dispatcher.

Usage:
    uv run aoc run <year> <day>    # Run solution for given year and day
    uv run aoc init <year> <day>   # Initialize folder and template for given year and day
"""

import sys

from aoc.cli.app import main


if __name__ == "__main__":
    sys.exit(main())
