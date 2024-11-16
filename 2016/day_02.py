from pathlib import Path
import numpy as np

# Keypad and movement mapping
keypad1 = np.array([
    ["1", "2", "3"],
    ["4", "5", "6"],
    ["7", "8", "9"]
])
keypad2 = np.array([
    [" ", " ", "1", " ", " "],
    [" ", "2", "3", "4", " "],
    ["5", "6", "7", "8", "9"],
    [" ", "A", "B", "C", " "],
    [" ", " ", "D", " ", " "]
])
map_move = {
    "U": np.array([-1, 0]),
    "L": np.array([0, -1]),
    "R": np.array([0, 1]),
    "D": np.array([1, 0])
}


def part1(input_data):
    position = np.array([1, 1])  # Starting position
    bathroom_code = []

    for instruction in input_data.splitlines():
        for move in instruction:
            position = np.clip(position + map_move[move], 0, 2)
        bathroom_code.append(keypad1[tuple(position)])

    return "".join(bathroom_code)


def part2(input_data):
    position = np.array([2, 0])  # Starting position
    bathroom_code = []

    for instruction in input_data.splitlines():
        for move in instruction:
            new_position = np.clip(position + map_move[move], 0, 4)
            if keypad2[tuple(new_position)] != " ":
                position = new_position.copy()
        bathroom_code.append(keypad2[tuple(position)])

    return "".join(bathroom_code)


if __name__ == "__main__":
    input_file = Path(__file__).parent / "day_02_input.txt"
    with open(input_file) as f:
        data = f.read().strip()

    print("Part 1:", part1(data))
    print("Part 2:", part2(data))
