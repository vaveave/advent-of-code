import numpy as np


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
        # If the level is 9, record the current position as reachable and stop recursion
        if level == 9:
            self.reachable_locations.append(pos)
            return
        # Explore all possible directions
        for dx, dy in DIRECTIONS:
            next_pos = (pos[0] + dx, pos[1] + dy)
            # Skip if out of bound
            if self.is_out_of_bounds(next_pos):
                continue
            # If the next position matches the expected level, continue following the path
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


if __name__ == "__main__":
    from aoc.initialize_day import load_input

    data = load_input(__file__)
    island = read_input(data)
    all_trailheads = initialize_and_process_trailheads(island)

    print("Part 1:", part_1(all_trailheads))
    print("Part 2:", part_2(all_trailheads))
