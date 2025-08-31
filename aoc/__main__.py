"""
Advent of Code CLI dispatcher.

Usage:
    py -m aoc <year> <day>         # Run solution for given year and day
    py -m aoc <year> <day> -init   # Initialize folder and template for given year and day
"""

import argparse
import importlib

def main():
    """
    Parses CLI arguments and dispatches to either run a day's solution or initialize a day.
    """
    parser = argparse.ArgumentParser(
        description="Run or initialize Advent of Code solutions."
    )
    parser.add_argument("year", type=int, help="Year of the challenge")
    parser.add_argument("day", type=int, help="Day of the challenge")
    parser.add_argument(
        "-init", action="store_true", help="Initialize the folder and template for the day"
    )
    args = parser.parse_args()

    year_str = str(args.year)
    day_str = f"{args.day:02d}"

    if args.init:
        # Dispatch to initialize_day
        from aoc import initialize_day
        initialize_day.initialize_day.initialize_day(args.year, args.day)
    else:
        # Run the solution for the given day
        module_name = f"aoc.{year_str}.{day_str}.__main__"
        try:
            module = importlib.import_module(module_name)
            if hasattr(module, "main"):
                module.main()
            else:
                # If no main(), run as script
                if hasattr(module, "__file__"):
                    with open(module.__file__, "r") as f:
                        code = f.read()
                    exec(code, {"__name__": "__main__", "__file__": module.__file__})
                else:
                    print(f"No entry point found in {module_name}")
        except ModuleNotFoundError:
            print(f"Module {module_name} not found.")

if __name__ == "__main__":
    main()
