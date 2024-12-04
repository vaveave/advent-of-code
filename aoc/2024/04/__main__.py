import numpy as np
from pathlib import Path


ADJACENTS = {
    (-1, 1), (0, 1), (1, 1),
    (-1, 0), (1, 0), (-1, -1),
    (0, -1), (1, -1)
}


def read_input(input_data):
    return np.array([np.array(list(x), dtype=str) for x in input_data.splitlines()])


def count_adjacents(arr, i, j):
    counter = 0
    for dx, dy in ADJACENTS:
        if (0 <= i+dx*3 < arr.shape[0]) & (0 <= j+dy*3 < arr.shape[1]):
            if "".join([arr[i+k*dx, j+k*dy][0] for k in range(4)]) == "XMAS":
                counter += 1
    return counter


def part_1(input_data):
    i_start = input_data == "X"
    counter = 0
    for i in range(input_data.shape[0]):
        for j in range(input_data.shape[1]):
            if i_start[i,j]:
                counter += count_adjacents(input_data, i, j)
    return counter


def part_2(input_data):
    i_start = input_data == "A"
    counter = 0
    for i in range(1, input_data.shape[0]-1):
        for j in range(1, input_data.shape[1]-1):
            if i_start[i,j]:
                if ((input_data[i-1,j-1] == "M") & (input_data[i+1,j+1] == "S") & (input_data[i-1,j+1] == "M") & (input_data[i+1,j-1] == "S")):
                    counter += 1
                if ((input_data[i-1,j-1] == "S") & (input_data[i+1,j+1] == "M") & (input_data[i-1,j+1] == "M") & (input_data[i+1,j-1] == "S")):
                    counter += 1
                if ((input_data[i-1,j-1] == "M") & (input_data[i+1,j+1] == "S") & (input_data[i-1,j+1] == "S") & (input_data[i+1,j-1] == "M")):
                    counter += 1
                if ((input_data[i-1,j-1] == "S") & (input_data[i+1,j+1] == "M") & (input_data[i-1,j+1] == "S") & (input_data[i+1,j-1] == "M")):
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

    data = read_input(load_input(year, day))

    print("Part 1:", part_1(data))
    print("Part 2:", part_2(data))
