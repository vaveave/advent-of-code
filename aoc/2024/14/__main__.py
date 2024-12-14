import re
import numpy as np
from tqdm import tqdm


def read_input(input_data):
    coordinate_pattern = re.compile(r"-?\d+")
    coordinates = []
    for line in input_data.splitlines():
        values = list(map(int, coordinate_pattern.findall(line)))
        coordinates.append([(values[1], values[0]), (values[3], values[2])])
    return coordinates


def calculate_grid(coordinates, n_rows, n_columns):
    grid = np.zeros((n_rows, n_columns), dtype=int)
    for (pos, _) in coordinates:
        grid[pos] += 1
    return grid


def update_coordinates(coordinates, n_rows, n_columns):
    for i, [(x, y), (dx, dy)] in enumerate(coordinates):
        coordinates[i][0] = ((x + dx) % n_rows, (y + dy) % n_columns)
    return coordinates


def calculate_safety_factor(grid):
    mid_row, mid_col = grid.shape[0] // 2, grid.shape[1] // 2
    quadrants = [
        grid[:mid_row, :mid_col],
        grid[:mid_row, mid_col+1:],
        grid[mid_row+1:, :mid_col],
        grid[mid_row+1:, mid_col+1:]
    ]
    return np.prod([q.sum() for q in quadrants])


def check_christmas_tree(visual_grid):
    """
    Very rough check: look for a horizontal set of 10 consecutive '#' characters.
    """
    for row in visual_grid:
        if "##########" in "".join(row):
            return True
    return False


def simulate(coordinates, n_rows, n_columns, n_seconds):
    safety_factor_100 = None

    for second in tqdm(range(n_seconds), desc="Simulating"):
        coordinates = update_coordinates(coordinates, n_rows, n_columns)

        if second == 99:  # Capture safety factor at 100 seconds
            grid_100 = calculate_grid(coordinates, n_rows, n_columns)
            safety_factor_100 = calculate_safety_factor(grid_100)

        grid = calculate_grid(coordinates, n_rows, n_columns)
        visual_grid = np.where(grid > 0, "#", " ")

        if check_christmas_tree(visual_grid):
            print("\n".join("".join(row) for row in visual_grid))
            print(f"Seconds elapsed: {second + 1}")

            response = input("Continue searching for the Christmas tree? (y/n): ").strip().lower()
            if response == "n":
                break

    return safety_factor_100


if __name__ == "__main__":
    from aoc.initialize_day import load_input

    data = load_input(__file__)
    initial_coordinates = read_input(data)

    safety_factor = simulate(initial_coordinates, 103, 101, n_seconds=10_000)
    print("Safety Factor after 100 seconds:", safety_factor)
