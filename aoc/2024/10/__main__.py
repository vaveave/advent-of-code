import numpy as np


DIRECTIONS = [
    (-1, 0),
    (0, 1),
    (1, 0),
    (0, -1)
]


def read_input(input_data):
    input_data = np.array([list(line) for line in input_data.splitlines()], dtype=str)
    input_data = np.array([[float(x) if x != "." else np.nan for x in row] for row in input_data])
    return input_data


class Trailhead:
    def __init__(self, island_map, start_pos):
        self.island_map = island_map
        self.island_rows = island_map.shape[0]
        self.island_columns = island_map.shape[1]
        self.start_pos = start_pos
        self.reachable_locations = []

    def calc_score(self):
        return len(set(self.reachable_locations))

    def is_bored_reached(self, pos):
        return not((0 <= pos[0] < self.island_rows) & (0 <= pos[1] < self.island_columns))

    def follow_path(self, pos, level):
        if level == 9:
            self.reachable_locations.append(pos)
        else:
            for dx, dy in DIRECTIONS:
                next_pos = (pos[0] + dx, pos[1] + dy)
                if self.is_bored_reached(next_pos):
                    continue
                next_level = level + 1
                if self.island_map[next_pos] == next_level:
                    self.follow_path(next_pos, next_level)

    def find_reachable_locations(self):
        self.follow_path(self.start_pos, 0)


def part_1(island_map):
    start_locations = np.argwhere(island_map == 0)
    cnt = 0
    for pos in start_locations:
        wanna_be_trailhead = Trailhead(island_map, pos)
        wanna_be_trailhead.find_reachable_locations()
        cnt += wanna_be_trailhead.calc_score()
    return cnt


def part_2(input_data):
    # Implement part 2 solution
    pass


if __name__ == "__main__":

    from aoc.initialize_day import load_input
    data = load_input(__file__)
    print("Part 1:", part_1(read_input(data)))
    print("Part 2:", part_2(read_input(data)))
