import numpy as np
from pathlib import Path


def part_1(input_data):
    list_1, list_2 = -np.sort(-np.fromstring(input_data, sep=' ', dtype=int).reshape(-1, 2).T)
    return np.sum(abs(list_2 - list_1))


def part_2(input_data):
    list_1, list_2 = np.fromstring(input_data, sep=' ', dtype=int).reshape(-1, 2).T
    return sum(location * np.count_nonzero(list_2 == location) for location in list_1)


test_data = """3   4
4   3
2   5
1   3
3   9
3   3"""


if __name__ == "__main__":
    with (Path(__file__).parent / "input.txt").open("r") as f:
        data = f.read()

    print("Part 1:", part_1(data))
    print("Part 2:", part_2(data))
