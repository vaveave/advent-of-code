import re
import numpy as np
from pathlib import Path


def part_1(input_data):
    shapes = np.array(
        re.findall(r'\d+', input_data), dtype=int
    ).reshape(-1, 3)
    # Sorting each row we can check only the first combination
    shapes = np.sort(shapes, axis=1)
    return str(sum(shapes[:, 0] + shapes[:, 1] > shapes[:, 2]))


def part_2(input_data):
    shapes = np.array(
        re.findall(r'\d+', input_data), dtype=int
    ).reshape(-1, 3)
    shapes = shapes.T.reshape(-1).reshape(-1, 3)
    shapes = np.sort(shapes, axis=1)
    return str(sum(shapes[:, 0] + shapes[:, 1] > shapes[:, 2]))


if __name__ == "__main__":
    with (Path(__file__).parent / "input.txt").open("r") as f:
        data = f.read()

    print("Part 1:", part_1(data))
    print("Part 2:", part_2(data))
