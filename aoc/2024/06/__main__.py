import numpy as np

map_to_directions = {
    "^": (-1, 0),
    ">": (0, 1),
    "v": (1, 0),
    "<": (0, -1)
}
map_to_symbols = {tuple(value): key for key, value in map_to_directions.items()}


rotate = {
    (1, 0): (0, -1),
    (0, -1): (-1, 0),
    (-1, 0): (0, 1),
    (0, 1): (1, 0),
}


class InfiniteLoop(Exception):
    pass


def read_input(input_data):
    return np.array([list(row) for row in input_data.splitlines()])


def next_position_direction(grid, position, direction):
    position = np.array(position)
    direction = np.array(direction)
    while grid[tuple(position + direction)] == "#":
        direction = np.array(rotate[tuple(direction)])
    new_position = position + direction
    return tuple(new_position), tuple(direction)


def is_bound_reached(grid, next_position):
    is_outside = any([
        (next_position[0] == 0),
        (next_position[0] == grid.shape[0]-1),
        (next_position[1] == 0),
        (next_position[1] == grid.shape[1]-1)
    ])
    return is_outside


def follow_path(grid, hist_steps):
    hist_steps = hist_steps.copy()
    curr_position, curr_direction = hist_steps[-1]
    while not is_bound_reached(grid, curr_position):
        next_step = next_position_direction(grid, curr_position, curr_direction)
        if next_step in set(hist_steps):
            raise InfiniteLoop
        curr_position, curr_direction = next_step
        # grid[curr_position] = map_to_symbols[curr_direction]  # to be removed
        hist_steps.append(next_step)
    return len(set(pos for pos, _ in hist_steps))


def part_1(grid):
    start_position = np.where(np.isin(grid, list(map_to_directions.keys())))
    start_position = tuple(p[0] for p in start_position)
    start_direction = map_to_directions[grid[start_position]]
    return follow_path(grid, [(start_position, start_direction)])


def try_path(grid, hist_steps):
    try:
        follow_path(grid, hist_steps)
        return False
    except InfiniteLoop:
        return True


def follow_what_if_path(grid, hist_steps):
    curr_position, curr_direction = hist_steps[-1]
    obstacles_counter = 0
    while not is_bound_reached(grid, curr_position):
        next_step = next_position_direction(grid, curr_position, curr_direction)
        # grid[next_step[0]] = "0"
        grid_to_be_tested = grid.copy()
        grid_to_be_tested[next_step[0]] = "#"
        if try_path(grid_to_be_tested, hist_steps):
            obstacles_counter += 1
        curr_position, curr_direction = next_step
        # grid[curr_position] = map_to_symbols[curr_direction]  # to be removed
        hist_steps.append(next_step)
    return obstacles_counter


def part_2(grid):
    start_position = np.where(np.isin(grid, list(map_to_directions.keys())))
    start_position = tuple(p[0] for p in start_position)
    start_direction = map_to_directions[grid[start_position]]
    return follow_what_if_path(grid, [(start_position, start_direction)])


test_data = """....#.....
.........#
..........
..#.......
.......#..
..........
.#..^.....
........#.
#.........
......#..."""


if __name__ == "__main__":

    from aoc.initialize_day import load_input
    data = load_input(__file__)
    print("Part 1:", part_1(read_input(data)))
    #print("Part 2:", part_2(read_input(data)))
