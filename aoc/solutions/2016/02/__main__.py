from aoc.cli.utils import load_input
import numpy as np

keypad1 = np.array([["1", "2", "3"], ["4", "5", "6"], ["7", "8", "9"]])
keypad2 = np.array([
    [" ", " ", "1", " ", " "],
    [" ", "2", "3", "4", " "],
    ["5", "6", "7", "8", "9"],
    [" ", "A", "B", "C", " "],
    [" ", " ", "D", " ", " "],
])
map_move = {
    "U": np.array([-1, 0]),
    "L": np.array([0, -1]),
    "R": np.array([0, 1]),
    "D": np.array([1, 0]),
}

def read_input(data):
    return data

def part_1(data):
    position = np.array([1, 1])
    bathroom_code = []
    for instruction in data.splitlines():
        for move in instruction:
            position = np.clip(position + map_move[move], 0, 2)
        bathroom_code.append(keypad1[tuple(position)])
    return "".join(bathroom_code)

def part_2(data):
    position = np.array([2, 0])
    bathroom_code = []
    for instruction in data.splitlines():
        for move in instruction:
            new_pos = position + map_move[move]
            if 0 <= new_pos[0] < 5 and 0 <= new_pos[1] < 5 and keypad2[tuple(new_pos)] != " ":
                position = new_pos
        bathroom_code.append(keypad2[tuple(position)])
    return "".join(bathroom_code)

def main():
    data = load_input(__file__)
    print("Part 1:", part_1(read_input(data)))
    print("Part 2:", part_2(read_input(data)))

if __name__ == "__main__":
    main()
