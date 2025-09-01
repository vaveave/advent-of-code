import re
import numpy as np

from aoc.cli.utils import load_input


def read_input(data):
    return data


def parse_operation(instruction):
    patterns = {
        "rect": r"^rect (\d+)x(\d+)$",
        "row": r"^rotate row y=(\d+) by (\d+)$",
        "column": r"^rotate column x=(\d+) by (\d+)$",
    }
    for i, key in enumerate(patterns.keys()):
        if match := re.match(patterns[key], instruction):
            return i, tuple(map(int, match.groups()))
    raise ValueError(f"Instruction not recognized: {instruction}")


def apply_operations(data, keypad_shape):
    operations = [parse_operation(line) for line in data.splitlines()]
    keypad_matrix = np.zeros(keypad_shape, int)
    for operation in operations:
        key, (x, y) = operation
        match key:
            case 0:
                keypad_matrix[:y, :x] = 1
            case 1:
                keypad_matrix[x, :] = np.roll(keypad_matrix[x, :], shift=y)
            case 2:
                keypad_matrix[:, x] = np.roll(keypad_matrix[:, x], shift=y)
    return keypad_matrix


def display_keypad(keypad_matrix):
    keypad_display = np.where(keypad_matrix == 1, "o", " ")
    return "\n" + "\n".join(" ".join(row) for row in keypad_display)


def part_1(data):
    keypad_matrix = apply_operations(data, (6, 50))
    return int(np.sum(keypad_matrix))

def part_2(data):
    keypad_matrix = apply_operations(data, (6, 50))
    return display_keypad(keypad_matrix)


def main():
    data = load_input(__file__)
    print("Part 1:", part_1(read_input(data)))
    print("Part 2:", part_2(read_input(data)))


if __name__ == "__main__":
    main()
