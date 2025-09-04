import sys
import argparse
import importlib
from typing import Literal, Annotated
from pydantic import BaseModel, Field, ValidationError


class CLIArgs(BaseModel):
    command: Literal["run", "init"]
    year: Annotated[int, Field(strict=True, gt=2014, le=2100)]
    day: Annotated[int, Field(strict=True, gt=0, le=25)]


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


def build_parser() -> argparse.ArgumentParser:
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
    parser = build_parser()
    args = parser.parse_args()

    try:
        cli_args = CLIArgs(**vars(args))
    except ValidationError as e:
        print("❌ Invalid arguments:\n", e)
        sys.exit(1)

    if cli_args.command == "run":
        run_solution(cli_args.year, cli_args.day)
    elif cli_args.command == "init":
        init_day(cli_args.year, cli_args.day)


if __name__ == "__main__":
    main()
