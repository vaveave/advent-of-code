import argparse

from .initialize_day import initialize_day


def main():
    """Parse command-line arguments and initialize the day."""
    parser = argparse.ArgumentParser(description="Initialize Advent of Code day folder, script, and input.")
    parser.add_argument("year", type=int, help="The year of the Advent of Code challenge.")
    parser.add_argument("day", type=int, help="The day of the Advent of Code challenge (1-25).")

    args = parser.parse_args()

    if not (1 <= args.day <= 25):
        parser.error("Day must be between 1 and 25.")

    try:
        initialize_day(args.year, args.day)
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
