import numpy as np


pipes = "|-LJ7F"
move_map = {
    "L": {(+1, 0): (0, +1), (0, -1): (-1, 0)},
    "J": {(+1, 0): (0, -1), (0, +1): (-1, 0)},
    "7": {(-1, 0): (0, -1), (0, +1): (+1, 0)},
    "F": {(-1, 0): (0, +1), (0, -1): (+1, 0)},
    "|": {(-1, 0): (-1, 0), (+1, 0): (+1, 0)},
    "-": {(0, -1): (0, -1), (0, +1): (0, +1)},
}


def do_move(move: tuple, current_pos: tuple, pipes_array: np.append):
    next_pos = tuple(a+b for a, b in zip(current_pos, move))
    next_val = pipes_array[next_pos[0], next_pos[1]]
    return next_pos, next_val


def explore_path(input_str):
    pipes_array = np.array([list(row) for row in input_str.split("\n")])
    current_pos = tuple(el[0] for el in np.where(pipes_array == "S"))
    path = {0: [current_pos, "S"]}
    for move in [(0, +1), (0, -1), (+1, 0), (-1, 0)]:
        current_pos, current_val = do_move(move, current_pos, pipes_array)
        if current_val in pipes:
            path[1] = [current_pos, current_val]
            break
    i = 1
    while current_val != "S":
        move = move_map[current_val][move]
        current_pos, current_val = do_move(move, current_pos, pipes_array)
        i += 1
        path[i] = [current_pos, current_val]
    return path


def part_1(input_data):
    path = explore_path(input_data)
    return int(len(path)/2)


def part_2(input_data):
    return None


if __name__ == "__main__":

    from aoc.initialize_day import load_input
    data = load_input(__file__)
    print("Part 1:", part_1(data))
    print("Part 2:", part_2(data))
