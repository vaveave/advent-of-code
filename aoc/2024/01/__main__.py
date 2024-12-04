import numpy as np
from pathlib import Path


def read_input(input_data):
    return np.fromstring(input_data, sep=' ', dtype=int).reshape(-1, 2).T


def part_1(location_ids):
    list_1, list_2 = -np.sort(-location_ids)
    return np.sum(abs(list_2 - list_1))


def part_2(location_ids):
    list_1, list_2 = location_ids
    return sum(location * np.count_nonzero(list_2 == location) for location in list_1)


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
