# Advent of Code: Year {{year}}, Day {{day}}
# Usage: python {{year}}/day_{{day}}.py

from pathlib import Path


def part1(input_data):
    # Implement part 1 solution
    pass


def part2(input_data):
    # Implement part 2 solution
    pass


if __name__ == "__main__":
    # Get the input file path and read the input data
    input_file = Path(__file__).parent / f"day_{{day}}_input.txt"
    with open(input_file) as f:
        data = f.read().strip()

    print("Part 1:", part1(data))
    print("Part 2:", part2(data))
