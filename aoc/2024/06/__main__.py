import numpy as np
from tqdm import tqdm

directions = [
    (-1, 0),
    (0, 1),
    (1, 0),
    (0, -1)
]

map_to_directions = {
    "^": 0,
    ">": 1,
    "v": 2,
    "<": 3
}
char_to_bool = {'.': True, '^': True, '>': True, 'v': True, '<': True, '#': False}

rotate = {
    (1, 0): (0, -1),
    (0, -1): (-1, 0),
    (-1, 0): (0, 1),
    (0, 1): (1, 0),
}


def read_input(input_data):
    input_data = np.array([list(row) for row in input_data.splitlines()])
    start_position = np.where(np.isin(input_data, list(map_to_directions.keys())))
    start_position = tuple(p.astype(np.int32)[0] for p in start_position)
    start_direction = map_to_directions[input_data[start_position]]
    grid = np.vectorize(char_to_bool.get)(input_data)
    return grid, start_position, start_direction


class InfiniteLoop(Exception):
    pass


class Tour:
    def __init__(
            self,
            grid,
            start_position,
            start_direction,
            past_locations=None,
            past_rotations=None
    ):
        self.grid = grid
        self.grid_shape = grid.shape
        self.position = start_position
        self.direction = start_direction

        # Initialize past_locations and past_rotations if not provided
        if past_locations is None:
            self.past_locations = np.zeros((grid.shape[0], grid.shape[1]), dtype=bool)
        else:
            self.past_locations = past_locations

        if past_rotations is None:
            self.past_rotations = np.zeros((grid.shape[0], grid.shape[1], 4), dtype=bool)
        else:
            self.past_rotations = past_rotations

    def mark_position(self):
        """Mark the current position and direction in the past history."""
        self.past_locations[self.position] = True  # Mark position as visited
        self.past_rotations[self.position + (self.direction,)] = True  # Mark direction as visited

    def move(self):
        """Move in the current direction if possible."""
        pos_x, pos_y = self.position
        dir_x, dir_y = directions[self.direction]

        # Rotate if the next cell is not traversable
        while not self.grid[pos_x + dir_x, pos_y + dir_y]:
            self.rotate()
            dir_x, dir_y = directions[self.direction]

        # Update position
        self.position = (pos_x + dir_x, pos_y + dir_y)

    def rotate(self):
        """Rotate the direction clockwise."""
        self.direction = (self.direction + 1) % 4

    def is_border_reached(self):
        """Check if the next move would leave the grid."""
        pos_x, pos_y = self.position
        dir_x, dir_y = directions[self.direction]
        next_pos_x, next_pos_y = pos_x + dir_x, pos_y + dir_y
        return next_pos_x < 0 or next_pos_x >= self.grid_shape[0] or next_pos_y < 0 or next_pos_y >= self.grid_shape[1]

    def check_infinite_loop(self):
        """Check if the current position and direction form an infinite loop."""
        pos_x, pos_y = self.position
        if self.past_locations[pos_x, pos_y] and self.past_rotations[self.position + (self.direction,)]:
            raise InfiniteLoop

    def follow_path(self):
        """Follow the path until a border is reached or a loop is detected."""
        while not self.is_border_reached():
            self.check_infinite_loop()
            self.mark_position()
            self.move()
        self.mark_position()
        return np.sum(self.past_locations)  # Count unique positions visited


def part_1(grid_orig, start_position, start_direction, obstacle=None):
    if obstacle:
        grid = grid_orig.copy()
        grid[obstacle] = False
    else:
        grid = grid_orig
    tour = Tour(grid, start_position, start_direction)
    tour.follow_path()
    return tour.past_locations


def part_2(grid, start_position, start_direction, past_locations):
    wanna_be_obstacles = np.argwhere(past_locations)
    obstacles = []
    for i in tqdm(range(wanna_be_obstacles.shape[0])):
        wanna_be_obstacle = tuple(wanna_be_obstacles[i, :])
        try:
            part_1(grid, start_position, start_direction, obstacle=wanna_be_obstacle)
        except InfiniteLoop:
            obstacles.append(wanna_be_obstacle)
    return len(set(obstacles))


test_data = """....#.....
.........#
..........
..#.......
.......#..
..........
.#..^.....
........#.
#.........
......#..."""


if __name__ == "__main__":
    from aoc.initialize_day import load_input
    data = load_input(__file__)
    grid_, start_position_, start_direction_ = read_input(data)
    past_positions = part_1(grid_, start_position_, start_direction_)

    print("Part 1:", np.sum(past_positions))
    print("Part 2:", part_2(grid_, start_position_, start_direction_, past_positions))
