import numpy as np

# Define direction mappings for movement
MAP_DIRECTION = {"^": (-1, 0), ">": (0, 1), "v": (1, 0), "<": (0, -1)}


def parse_input(input_data):
    """Parse the input data into a grid and directions."""
    grid_data, directions = input_data.split("\n\n")
    grid = np.array([list(line) for line in grid_data.splitlines()])
    return grid, directions


def preprocess_input_for_large_boxes(input_data):
    """Modify the input data for processing large boxes."""
    modified_data = (
        input_data
        .replace("#", "##")
        .replace("O", "[]")
        .replace(".", "..")
        .replace("@", "@.")
    )
    return parse_input(modified_data)


def calculate_gps(grid, has_large_boxes):
    """Calculate GPS score based on grid and box size."""
    if has_large_boxes:
        positions = np.argwhere(grid == "[")
    else:
        positions = np.argwhere(grid == "O")
    return sum(100 * x + y for x, y in positions)


def move_small_boxes(input_data):
    """Move small boxes based on directions and calculate GPS."""
    grid, directions = input_data
    x, y = tuple(np.argwhere(grid == "@")[0])

    for direction in directions.replace("\n", ""):
        dx, dy = MAP_DIRECTION[direction]
        steps = 1

        # Find the next obstacle or empty cell
        while grid[x + steps * dx, y + steps * dy] not in ("#", "."):
            steps += 1

        if grid[x + steps * dx, y + steps * dy] == "#":
            continue  # Hit a wall, skip move

        # Move boxes horizontally or vertically
        if dx != 0:
            grid[x:x + (steps + 1) * dx:dx, y:y + 1] = np.insert(
                grid[x:x + steps * dx:dx, y:y + 1], 0, "."
            ).reshape(-1, 1)
        else:
            grid[x:x + 1, y:y + (steps + 1) * dy:dy] = np.insert(
                grid[x:x + 1, y:y + steps * dy:dy], 0, "."
            )

        x, y = x + dx, y + dy

    return calculate_gps(grid, has_large_boxes=False)


def move_large_boxes(input_data):
    """Move large boxes based on directions and calculate GPS."""
    grid, directions = input_data
    x, y = tuple(np.argwhere(grid == "@")[0])

    for step, direction in enumerate(directions.replace("\n", "")):

        # if ("[." in "\n".join("".join(row) for row in grid)) | (".]" in "\n".join("".join(row) for row in grid)):
        #    raise ValueError(f"Error at step {step}")

        dx, dy = MAP_DIRECTION[direction]

        grid_temp = np.full(grid.shape, ".", dtype=grid.dtype)
        grid_temp[x+dx, y] = "@"

        n_steps = 0

        if dx != 0:
            next_level_min = y
            next_level_max = y
            next_level = x
            exit_level = False
            while not exit_level:
                next_level += dx
                if np.any(grid[next_level, next_level_min:next_level_max+1] == "#"):
                    # Found a stone, no action needed
                    exit_level = True
                elif np.all(grid[next_level, next_level_min:next_level_max+1] == "."):
                    # We can move boxes
                    grid[grid_temp != "."] = grid_temp[grid_temp != "."]
                    grid[grid == "x"] = "."
                    grid[x, y] = "."
                    x += dx
                    exit_level = True
                else:
                    # Moving to the next level
                    if next_level == x+dx:
                        if grid[next_level, y] == "]":
                            next_level_min -= 1
                            grid_temp[next_level, y-1] = "x"
                        else:
                            next_level_max += 1
                            grid_temp[next_level, y+1] = "x"
                    else:
                        if (grid[next_level, next_level_min] == "]") & (grid[next_level, next_level_max] == "."):
                            next_level_min -= 1
                            next_level_max -= 1
                            grid_temp[next_level, next_level_min] = "x"
                        elif (grid[next_level, next_level_min] == "]") & (grid[next_level, next_level_max] == "["):
                            next_level_min -= 1
                            next_level_max += 1
                            grid_temp[next_level, next_level_min] = "x"
                            grid_temp[next_level, next_level_max] = "x"
                        elif (grid[next_level, next_level_min] == ".") & (grid[next_level, next_level_max] == "["):
                            next_level_min += 1
                            next_level_max += 1
                            grid_temp[next_level, next_level_max] = "x"
                    grid_temp[next_level+dx, next_level_min:next_level_max+1] = grid[next_level, next_level_min:next_level_max+1]

        else:  # dy != 0

            # Find the next obstacle or empty cell
            while grid[x + n_steps * dx, y + n_steps * dy] not in ("#", "."):
                n_steps += 1
            if grid[x + n_steps * dx, y + n_steps * dy] == "#":
                continue  # Hit a wall, skip move
            grid[x:x + 1, y:y + (n_steps + 1) * dy:dy] = np.insert(
                grid[x:x + 1, y:y + n_steps * dy:dy], 0, "."
            )
            y = y + dy

    print("\n".join("".join(row) for row in grid))
    return calculate_gps(grid, has_large_boxes=True)


if __name__ == "__main__":
    from aoc.initialize_day import load_input

    data = load_input(__file__)
    # Uncomment for Part 1
    print("Part 1:", move_small_boxes(parse_input(data)))

    # Part 2
    print("Part 2:", move_large_boxes(preprocess_input_for_large_boxes(data)))
