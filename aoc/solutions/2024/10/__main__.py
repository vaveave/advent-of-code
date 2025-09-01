import numpy as np

from aoc.cli.utils import load_input


DIRECTIONS = [
    (-1, 0),  # Up
    (0, 1),  # Right
    (1, 0),  # Down
    (0, -1),  # Left
]


def read_input(input_data):
    return np.array([list(line) for line in input_data.splitlines()], dtype=int)


class Trailhead:
    def __init__(self, island_map, start_pos):
        self.island_map = island_map
        self.rows, self.columns = island_map.shape
        self.start_pos = tuple(start_pos)
        self.reachable_locations = []

    def calc_score(self):
        return len(set(self.reachable_locations))

    def calc_rating(self):
        return len(self.reachable_locations)

    def is_out_of_bounds(self, pos):
        row, col = pos
        return not ((0 <= row < self.rows) & (0 <= col < self.columns))

    def follow_path(self, pos, level):
        if level == 9:
            self.reachable_locations.append(pos)
            return
        for dx, dy in DIRECTIONS:
            next_pos = (pos[0] + dx, pos[1] + dy)
            if self.is_out_of_bounds(next_pos):
                continue
            next_level = level + 1
            if self.island_map[next_pos] == next_level:
                self.follow_path(next_pos, next_level)

    def find_reachable_locations(self):
        self.follow_path(self.start_pos, 0)


def initialize_and_process_trailheads(island_map):
    start_locations = np.argwhere(island_map == 0)
    trailheads = [Trailhead(island_map, pos) for pos in start_locations]
    for trailhead in trailheads:
        trailhead.find_reachable_locations()
    return trailheads


def part_1(trailheads):
    return sum(trailhead.calc_score() for trailhead in trailheads)


def part_2(trailheads):
    return sum(trailhead.calc_rating() for trailhead in trailheads)


def main():
    data = load_input(__file__)
    island = read_input(data)
    all_trailheads = initialize_and_process_trailheads(island)
    print("Part 1:", part_1(all_trailheads))
    print("Part 2:", part_2(all_trailheads))


if __name__ == "__main__":
    main()
