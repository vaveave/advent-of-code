import re
import numpy as np
from pathlib import Path


def parse_operation(instruction):
    patterns = {
        "rect": r"^rect (\d+)x(\d+)$",
        "row": r"^rotate row y=(\d+) by (\d+)$",
        "column": r"^rotate column x=(\d+) by (\d+)$"
    }
    for i, key in enumerate(patterns.keys()):
        if match := re.match(patterns[key], instruction):
            return i, tuple(map(int, match.groups()))
    raise ValueError(f"Instruction not recognized: {instruction}")


def apply_operations(input_data, keypad_shape):
    operations = [parse_operation(line) for line in input_data.splitlines()]
    keypad_matrix = np.zeros(keypad_shape, int)
    for operation in operations:
        key, (x, y) = operation
        match key:
            case 0:
                # rect
                keypad_matrix[:y, :x] = 1
            case 1:
                # roll row
                keypad_matrix[x, :] = np.roll(keypad_matrix[x, :], shift=y)
            case 2:
                # roll column
                keypad_matrix[:, x] = np.roll(keypad_matrix[:, x], shift=y)
    return keypad_matrix


def display_keypad(keypad_matrix):
    keypad_display = np.where(keypad_matrix == 1, "o", " ")
    return "\n" + "\n".join(" ".join(row) for row in keypad_display)


input_test = """rect 3x2
rotate column x=1 by 1
rotate row y=0 by 4
rotate column x=1 by 1
"""
shape_test = (3, 7)

if __name__ == "__main__":
    with (Path(__file__).parent / "input.txt").open("r") as f:
        data = f.read()
    shape = (6, 50)
    keypad = apply_operations(data, shape)

    print("Part 1:", np.sum(np.sum(keypad)))
    print("Part 2:", display_keypad(keypad))
