import numpy as np
from itertools import combinations

from aoc.cli.utils import load_input


def read_input(input_data):
    grid = np.array([list(row) for row in input_data.splitlines()])
    unique_frequencies = np.unique(grid[grid != "."])
    frequencies_locations = [np.argwhere(grid == freq) for freq in unique_frequencies]
    return grid, frequencies_locations


def calculate_antinodes(grid, frequencies_locations, with_resonance=False):
    antinodes = np.zeros(grid.shape, dtype=bool)
    for locations in frequencies_locations:
        location_pairs = list(combinations(locations, 2))
        for pair in location_pairs:
            for j in range(2):
                dx = pair[(j + 1) % 2][0] - pair[j][0]
                dy = pair[(j + 1) % 2][1] - pair[j][1]
                node_x = pair[(j + 1) % 2][0] + dx
                node_y = pair[(j + 1) % 2][1] + dy
                while (0 <= node_x < grid.shape[0]) and (0 <= node_y < grid.shape[1]):
                    antinodes[node_x, node_y] = True
                    if not with_resonance:
                        break
                    node_x += dx
                    node_y += dy
    return antinodes


def part_1(grid, frequencies_locations):
    antinodes = calculate_antinodes(grid, frequencies_locations)
    return np.sum(np.sum(antinodes))


def part_2(grid, frequencies_locations):
    antinodes = calculate_antinodes(grid, frequencies_locations, with_resonance=True)
    grid[antinodes] = "#"
    return np.sum(np.sum(grid != "."))


def main():
    data = load_input(__file__)
    grid_, frequencies_locations_ = read_input(data)
    print("Part 1:", part_1(grid_, frequencies_locations_))
    print("Part 2:", part_2(grid_, frequencies_locations_))


if __name__ == "__main__":
    main()
