import re

from pathlib import Path


def read_input(input_data):
    return input_data


def part_1(input_data):
    non_corrupted_pairs = [
        tuple(map(int, x)) for x in re.findall(r"mul\((\d+),(\d+)\)", input_data)
    ]
    return sum(x[0]*x[1] for x in non_corrupted_pairs)


def part_2(input_data):
    # Implement part 2 solution
    pass


if __name__ == "__main__":
    with (Path(__file__).parent / "input.txt").open("r") as f:
        data = f.read()

    print("Part 1:", part_1(data))
    print("Part 2:", part_2(read_input(data)))
