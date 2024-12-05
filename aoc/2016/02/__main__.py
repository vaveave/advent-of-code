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


def part_1(input_data):
    position = np.array([1, 1])  # Starting position
    bathroom_code = []

    for instruction in input_data.splitlines():
        for move in instruction:
            position = np.clip(position + map_move[move], 0, 2)
        bathroom_code.append(keypad1[tuple(position)])

    return "".join(bathroom_code)


def part_2(input_data):
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

    from aoc.initialize_day import load_input
    data = load_input(__file__)
    print("Part 1:", part_1(data))
    print("Part 2:", part_2(data))
