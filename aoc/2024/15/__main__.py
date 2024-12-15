import numpy as np

MAP_DIRECTION = {"^": (-1, 0), ">": (0, 1), "v": (1, 0), "<": (0, -1)}


def read_input(input_data):
    grid, directions = input_data.split("\n\n")
    grid = np.array([list(line) for line in grid.splitlines()])
    return grid, directions


def part_1(input_data):
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

    positions = np.argwhere(grid == "O")
    all_gps = sum([100*x + y for x,y in positions])
    return all_gps


def part_2(input_data):
    # Implement part 2 solution
    pass


if __name__ == "__main__":

    from aoc.initialize_day import load_input
    data = load_input(__file__)
    print("Part 1:", part_1(read_input(data)))
    print("Part 2:", part_2(read_input(data)))
