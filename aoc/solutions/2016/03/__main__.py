import re
import numpy as np

from aoc.cli.utils import load_input


def read_input(data):
    return data

def part_1(data):
    shapes = np.array(re.findall(r"\d+", data), dtype=int).reshape(-1, 3)
    shapes = np.sort(shapes, axis=1)
    return str(sum(shapes[:, 0] + shapes[:, 1] > shapes[:, 2]))

def part_2(data):
    shapes = np.array(re.findall(r"\d+", data), dtype=int).reshape(-1, 3)
    shapes = shapes.T.reshape(-1).reshape(-1, 3)
    shapes = np.sort(shapes, axis=1)
    return str(sum(shapes[:, 0] + shapes[:, 1] > shapes[:, 2]))

def main():
    data = load_input(__file__)
    print("Part 1:", part_1(read_input(data)))
    print("Part 2:", part_2(read_input(data)))

if __name__ == "__main__":
    main()
