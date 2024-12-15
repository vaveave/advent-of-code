import numpy as np

MAP_DIRECTION = {"^": (-1, 0), ">": (0, 1), "v": (1, 0), "<": (0, -1)}


def read_input(input_data):
    grid, directions = input_data.split("\n\n")
    grid = np.array([list(line) for line in grid.splitlines()])
    return grid, directions


def read_doubled_input(input_data):
    input_data = input_data.replace("#", "##").replace("O", "[]").replace(".", "..").replace("@", "@.")
    grid, directions = input_data.split("\n\n")
    grid = np.array([list(line) for line in grid.splitlines()])
    return grid, directions


def calc_gps(grid, are_boxes_large):
    if are_boxes_large:
        raise NotImplementedError
    else:
        positions = np.argwhere(grid == "O")
        all_gps = sum([100*x + y for x, y in positions])
    return all_gps


def move_boxes(input_data):
    grid, directions = input_data
    x, y = tuple(np.argwhere(grid == "@")[0])
    for direction in directions.replace("\n", ""):
        dx, dy = MAP_DIRECTION[direction]
        k = 1
        while grid[x+k*dx, y+k*dy] not in ("#", "."):
            k += 1
        if grid[x+k*dx, y+k*dy] == "#":
            continue
        if dx != 0:
            grid[x:x+(k+1)*dx:dx, y:y+1] = np.insert(
                grid[x:x+k*dx:dx, y:y+1], 0, "."
            ).reshape(-1, 1)
        else:
            grid[x:x+1, y:y+(k+1)*dy:dy] = np.insert(
                grid[x:x+1, y:y+k*dy:dy], 0, "."
            )
        x, y = x+dx, y+dy

    return calc_gps(grid, False)


def try_locate_large_boxes(grid, axis, min_pos, max_pos, pos, increment):
    x, y = pos
    if axis == 0:  # move along rows
        if np.any(grid[x, min_pos:max_pos+1] == "#"):
            return 0, None, None
        if np.all(grid[x, min_pos:max_pos+1] == "."):
            return 1, None, None
        min_indices = np.where(grid[x, :y+1] == ".")
        max_indices = np.where(grid[x, y+1:] == ".")
        not_wall_indices = np.where(grid[x, :] != "#")
        if min_indices[0].size > 0:
            i_min = min_indices[0][-1]+1
        else:  # only "[" or "]" characters
            i_min = not_wall_indices[0][0]
        if max_indices[0].size > 0:
            i_max = y+max_indices[0][0]
        else:  # only "[" or "]" characters
            i_max = not_wall_indices[0][-1]
    else:  # move along columns
        if np.any(grid[min_pos:max_pos, y] == "#"):
            return 0, None, None
        if np.all(grid[min_pos:max_pos, y] == "."):
            return 1, None, None
        i_min = x
        i_max = x+1
    return 2, i_min, i_max


def update_grid(grid, curr_pos, min_pos, max_pos, increment, tot_moves, axis):
    x, y = curr_pos
    dx, dy = increment
    if axis == 1:  # move along columns
        grid[x:x+1, y:y+(tot_moves+1)*dy:dy] = np.insert(
            grid[x:x+1, y:y+tot_moves*dy:dy], 0, "."
        )
    else:
        new_grid = np.full(grid.shape, ".", dtype=grid.dtype)

        for row in range(x+tot_moves*dx, x-dx, -dx):
            _, min_pos_row, max_pos_row = (
                try_locate_large_boxes(grid, axis, y, y+1, (row, y), increment)
            )
            new_grid[row-dx, min_pos_row:max_pos_row+1] = grid[row, min_pos_row:max_pos_row+1]
        grid[x+dx:x + (tot_moves+2) * dx:dx, min_pos:max_pos + 1] = new_grid[x-dx:x + tot_moves * dx:dx, min_pos:max_pos + 1]
        grid[x, y] = "."
        # grid[i_walls] = "#"
    return grid


def move_large_boxes(input_data):
    grid, directions = input_data
    x, y = tuple(np.argwhere(grid == "@")[0])
    for i, direction in enumerate(directions.replace("\n", "")):
        print(f"Step {i}:")
        print("\n".join("".join(row) for row in grid))
        print(f"Move: {direction}\n")
        dx, dy = MAP_DIRECTION[direction]
        curr_pos = (x, y)
        if dx != 0:
            min_pos, max_pos = y, y + 1
            axis = 0
            increment = dx
        else:
            min_pos, max_pos = x, x + 1
            axis = 1
            increment = dy
        tot_moves = 0
        result = 2
        new_min_pos, new_max_pos = min_pos, max_pos
        while result not in [0, 1]:
            tot_moves += 1
            min_pos = min(min_pos, new_min_pos)
            max_pos = max(max_pos, new_max_pos)
            result, new_min_pos, new_max_pos = (
                try_locate_large_boxes(grid, axis, min_pos, max_pos, (x+dx*tot_moves, y+dy*tot_moves), increment)
            )
        if dx != 0:
            tot_moves -= 1
        if result == 0:
            # We found a wall, no moves
            continue
        grid = update_grid(grid, curr_pos, min_pos, max_pos, (dx, dy), tot_moves, axis)
        x, y = x+dx, y+dy

    return calc_gps(grid, True)


if __name__ == "__main__":

    from aoc.initialize_day import load_input
    data = load_input(__file__)
    # print("Part 1:", move_boxes(read_input(data)))
    print("Part 2:", move_large_boxes(read_doubled_input(data)))
