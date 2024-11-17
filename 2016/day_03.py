import re
import numpy as np
from pathlib import Path


def part1(input_data):
    shapes = np.array(
        re.findall(r'\d+', input_data), dtype=int
    ).reshape(-1, 3)
    # Sorting each row we can check only the first combination
    shapes = np.sort(shapes, axis=1)
    return str(sum(shapes[:, 0] + shapes[:, 1] > shapes[:, 2]))


def part2(input_data):
    shapes = np.array(
        re.findall(r'\d+', input_data), dtype=int
    ).reshape(-1, 3)
    shapes = shapes.T.reshape(-1).reshape(-1, 3)
    shapes = np.sort(shapes, axis=1)
    return str(sum(shapes[:, 0] + shapes[:, 1] > shapes[:, 2]))


if __name__ == "__main__":
    # Get the input file path and read the input data
    input_file = Path(__file__).parent / f"day_03_input.txt"
    with open(input_file) as f:
        data = f.read().strip()

    print("Part 1:", part1(data))
    print("Part 2:", part2(data))
