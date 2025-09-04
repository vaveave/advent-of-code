import argparse
import importlib

def run_solution(year: int, day: int):
    """Run the solution script for the given year and day."""
    module_name = f"aoc.solutions.{year}.{day:02d}.__main__"
    try:
        module = importlib.import_module(module_name)
        if hasattr(module, "main"):
            module.main()
    except ModuleNotFoundError:
        print(f"❌ Module not found: {module_name}")


def init_day(year: int, day: int):
    """Initialize folder and template for the given year and day."""
    from aoc.cli.utils import initialize_day
    initialize_day(year, day)


def build_parser():
    parser = argparse.ArgumentParser(description="Run or initialize Advent of Code solutions.")
    subparsers = parser.add_subparsers(dest="command", required=True)

    # Run command
    run_parser = subparsers.add_parser("run", help="Run the solution for a given year and day")
    run_parser.add_argument("year", type=int)
    run_parser.add_argument("day", type=int)

    # Init command
    init_parser = subparsers.add_parser("init", help="Initialize folder and template for a given year and day")
    init_parser.add_argument("year", type=int)
    init_parser.add_argument("day", type=int)

    return parser


def main():
    args = build_parser().parse_args()

    if args.command == "run":
        run_solution(args.year, args.day)
    elif args.command == "init":
        init_day(args.year, args.day)
    else:
        print(f"❌ Unknown command '{args.command}'")

