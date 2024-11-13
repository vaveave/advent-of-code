# Advent of Code: Year {{year}}, Day {{day}}
# Usage: python {{year}}/days/day_{{day}}.py

from pathlib import Path


def part1(input_data):
    # Implement part 1 solution
    pass


def part2(input_data):
    # Implement part 2 solution
    pass


if __name__ == "__main__":
    # You can modify this manually or use a script to auto-generate it
    year = "{{year}}"
    day = "{{day}}"

    # Get the directory of the current script
    script_dir = Path(__file__).parent

    # Read input data from the corresponding file in the script directory
    input_file = script_dir / f"day_{day}.txt"
    with open(input_file) as f:
        data = f.read().strip()

    # Print results for part 1 and part 2
    print("Part 1:", part1(data))
    print("Part 2:", part2(data))
