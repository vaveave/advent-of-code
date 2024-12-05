import numpy as np
from pathlib import Path


adjacents = np.array([
    (-1, 1),  (0, 1),  (1, 1),
    (-1, 0),           (1, 0),
    (-1, -1), (0, -1), (1, -1)
])


def read_input(input_data):
    return np.array([np.array(list(x), dtype=str) for x in input_data.splitlines()])


def is_within_bounds(arr, x, y):
    return (0 <= x < arr.shape[0]) & (0 <= y < arr.shape[1])


def count_adjacents(arr, x, y):
    counter = 0
    for dx, dy in adjacents:
        if is_within_bounds(arr, x + dx*3, y + dy*3):
            if "".join([arr[x + k*dx, y + k*dy][0] for k in range(4)]) == "XMAS":
                counter += 1
    return counter


def part_1(input_data):
    start_indexes = np.argwhere(input_data == "X")
    return sum(count_adjacents(input_data, x, y) for x, y in start_indexes)


def check_mas_diagonals(arr, x, y):
    diagonals = [
        [(x - 1, y - 1), (x, y), (x + 1, y + 1)],  # Top-left to bottom-right
        [(x - 1, y + 1), (x, y), (x + 1, y - 1)],  # Top-right to bottom-left
    ]
    top_left_bottom_right = [arr[dx, dy] for dx, dy in diagonals[0] if is_within_bounds(arr, dx, dy)]
    top_right_bottom_left = [arr[dx, dy] for dx, dy in diagonals[1] if is_within_bounds(arr, dx, dy)]
    if all(
            x in ["MAS", "SAM"] for x in ["".join(top_left_bottom_right), "".join(top_right_bottom_left)]
    ):
        return True
    return False


def part_2(input_data):
    start_indexes = np.argwhere(input_data == "A")
    counter = 0
    for x, y in start_indexes:
        if check_mas_diagonals(input_data, x, y):
            counter += 1

    return counter


if __name__ == "__main__":

    from aoc.initialize_day import load_input

    folder = Path(__file__).parent
    try:
        year = int(folder.parts[-2])
        day = int(folder.parts[-1])
    except ValueError:
        print("Failed to determine year and day from folder structure.")
        raise SystemExit(1)

    data = load_input(year, day)

    print("Part 1:", part_1(read_input(data)))
    print("Part 2:", part_2(read_input(data)))
