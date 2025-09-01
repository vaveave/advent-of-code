import numpy as np

from aoc.cli.utils import load_input


MAP_DIRECTION = {"^": (-1, 0), ">": (0, 1), "v": (1, 0), "<": (0, -1)}


def parse_input(input_data):
    grid_data, directions = input_data.split("\n\n")
    grid = np.array([list(line) for line in grid_data.splitlines()])
    return grid, directions


def preprocess_input_for_large_boxes(input_data):
    modified_data = (
        input_data.replace("#", "##")
        .replace("O", "[]")
        .replace(".", "..")
        .replace("@", "@.")
    )
    return parse_input(modified_data)


def calculate_gps(grid):
    positions = np.argwhere((grid == "[") | (grid == "O"))
    return sum(100 * x + y for x, y in positions)


def check_and_make_to_be_moved(pos, to_be_moved):
    if pos not in to_be_moved:
        to_be_moved.append(pos)


def move_boxes(input_data):
    grid, directions = input_data
    start_x, start_y = tuple(np.argwhere(grid == "@")[0])

    for direction in directions.replace("\n", ""):
        dx, dy = MAP_DIRECTION[direction]
        to_be_moved = [(start_x, start_y)]
        i = 0
        jump_to_next = False

        while i < len(to_be_moved):
            x, y = to_be_moved[i]
            new_x, new_y = x + dx, y + dy
            if grid[new_x, new_y] in "O[]":
                check_and_make_to_be_moved((new_x, new_y), to_be_moved)
                if grid[new_x, new_y] == "[":
                    check_and_make_to_be_moved((new_x, new_y + 1), to_be_moved)
                if grid[new_x, new_y] == "]":
                    check_and_make_to_be_moved((new_x, new_y - 1), to_be_moved)
            elif grid[new_x, new_y] == "#":
                jump_to_next = True
                break
            i += 1

        if jump_to_next:
            continue

        new_grid = grid.copy()

        for x, y in to_be_moved:
            new_grid[x, y] = "."
        for x, y in to_be_moved:
            new_grid[x + dx, y + dy] = grid[x, y]

        grid = new_grid

        start_x, start_y = start_x + dx, start_y + dy

    return calculate_gps(grid)


def main():
    data = load_input(__file__)
    print("Part 1:", move_boxes(parse_input(data)))
    print("Part 2:", move_boxes(preprocess_input_for_large_boxes(data)))


if __name__ == "__main__":
    main()
