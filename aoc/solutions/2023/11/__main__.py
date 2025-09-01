import numpy as np
import itertools

from aoc.cli.utils import load_input


space = "."
galaxy = "#"


def universe_from_str(str_: str):
    return np.array([list(row) for row in str_.split("\n")])


def expand_universe(universe: np.ndarray):
    i_non_galaxy_rows = np.all(universe == space, axis=1)
    universe = np.insert(
        universe, np.where(i_non_galaxy_rows)[0], universe[i_non_galaxy_rows], axis=0
    )
    i_non_galaxy_columns = np.all(universe == space, axis=0)
    universe = np.insert(
        universe,
        np.where(i_non_galaxy_columns)[0],
        universe[:, i_non_galaxy_columns],
        axis=1,
    )
    return universe


def shortest_path_between_galaxies(input_str):
    universe = expand_universe(universe_from_str(input_str))
    i_galaxies = np.where(universe == galaxy)
    galaxies = list(zip(i_galaxies[0], i_galaxies[1]))
    galaxies_pairs = list(itertools.combinations(galaxies, 2))
    return sum(
        [
            abs(gal_1[0] - gal_2[0]) + abs(gal_1[1] - gal_2[1])
            for gal_1, gal_2 in galaxies_pairs
        ]
    )


def read_input(data):
    return data


def part_1(input_data):
    return shortest_path_between_galaxies(input_data)


def expand_universe_n_times(universe: np.ndarray):
    i_non_galaxy_rows = np.all(universe == space, axis=1)
    i_non_galaxy_columns = np.all(universe == space, axis=0)
    universe[i_non_galaxy_rows, :] = "*"
    universe[:, i_non_galaxy_columns] = "*"
    return universe


def shortest_path_between_galaxies_n_times(input_str, age: int):
    universe = expand_universe_n_times(universe_from_str(input_str))
    i_galaxies = np.where(universe == galaxy)
    galaxies = list(zip(i_galaxies[0], i_galaxies[1]))
    galaxies_pairs = list(itertools.combinations(galaxies, 2))
    path_len = 0
    for gal_1, gal_2 in galaxies_pairs:
        min_x = min(gal_1[0], gal_2[0])
        max_x = max(gal_1[0], gal_2[0])
        min_y = min(gal_1[1], gal_2[1])
        max_y = max(gal_1[1], gal_2[1])
        path_len += (
            np.sum(universe[min_x:max_x, min_y] == "*") * (age - 1)
            + np.sum(universe[max_x, min_y:max_y] == "*") * (age - 1)
            + abs(gal_1[0] - gal_2[0])
            + abs(gal_1[1] - gal_2[1])
        )
    return path_len


def part_2(input_data):
    return shortest_path_between_galaxies_n_times(input_data, 1000000)


def main():
    data = load_input(__file__)
    print("Part 1:", part_1(read_input(data)))
    print("Part 2:", part_2(read_input(data)))


if __name__ == "__main__":
    main()
