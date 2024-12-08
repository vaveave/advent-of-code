import numpy as np
from itertools import combinations


def read_input(input_data):
    grid = np.array([list(row) for row in input_data.splitlines()])
    unique_frequencies = np.unique(grid[grid != "."])
    frequencies_locations = []
    for freq in unique_frequencies:
        frequencies_locations.append(np.argwhere(grid == freq))
    return grid, unique_frequencies, frequencies_locations


def part_1(grid, unique_frequencies, frequencies_locations):
    antinodes = np.zeros(grid.shape, dtype=bool)
    for i, frequency in enumerate(unique_frequencies):
        locations = frequencies_locations[i]
        row_indices = list(combinations(range(locations.shape[0]), 2))
        row_combinations = [(locations[i], locations[j]) for i, j in row_indices]
        for combo in row_combinations:
            for j in range(2):
                node_x = 2 * combo[(j+1) % 2][0] - combo[j][0]
                node_y = 2 * combo[(j+1) % 2][1] - combo[j][1]
                if (0 <= node_x < grid.shape[0]) and (0 <= node_y < grid.shape[1]):
                    antinodes[node_x, node_y] = True
    return np.sum(np.sum(antinodes))


def part_2(grid, unique_frequencies, frequencies_locations):
    antinodes = np.zeros(grid.shape, dtype=bool)
    for i, frequency in enumerate(unique_frequencies):
        locations = frequencies_locations[i]
        row_indices = list(combinations(range(locations.shape[0]), 2))
        row_combinations = [(locations[i], locations[j]) for i, j in row_indices]
        for combo in row_combinations:
            for j in range(2):
                dx = combo[(j+1) % 2][0] - combo[j][0]
                dy = combo[(j+1) % 2][1] - combo[j][1]
                node_x = combo[(j+1) % 2][0] + dx
                node_y = combo[(j+1) % 2][1] + dy
                while (0 <= node_x < grid.shape[0]) and (0 <= node_y < grid.shape[1]):
                    antinodes[node_x, node_y] = True
                    node_x += dx
                    node_y += dy
    grid[antinodes] = "#"
    return np.sum(np.sum(grid != "."))


if __name__ == "__main__":

    from aoc.initialize_day import load_input
    data = load_input(__file__)
    grid_, unique_frequencies_, frequencies_locations_ = read_input(data)

    print("Part 1:", part_1(grid_, unique_frequencies_, frequencies_locations_))
    print("Part 2:", part_2(grid_, unique_frequencies_, frequencies_locations_))
