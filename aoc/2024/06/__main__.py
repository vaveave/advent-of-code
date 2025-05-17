import numpy as np
from tqdm import tqdm


DIRECTIONS = [(-1, 0), (0, 1), (1, 0), (0, -1)]  # Up, Right, Down, Left
CHAR_TO_DIRECTION = {"^": 0, ">": 1, "v": 2, "<": 3}
CHAR_TO_BOOL = {".": True, "^": True, ">": True, "v": True, "<": True, "#": False}


class InfiniteLoop(Exception):
    pass


def read_input(input_data):
    input_data = np.array([list(row) for row in input_data.splitlines()])
    start_position = np.where(np.isin(input_data, list(CHAR_TO_DIRECTION.keys())))
    start_position = tuple(p.astype(np.int32)[0] for p in start_position)
    start_direction = CHAR_TO_DIRECTION[input_data[start_position]]
    grid = np.vectorize(CHAR_TO_BOOL.get)(input_data)
    return grid, start_position, start_direction


class Tour:
    def __init__(self, grid, start_position, start_direction):
        self.grid = grid
        self.grid_shape = grid.shape
        self.position = start_position
        self.direction = start_direction

        # self.past_locations: (n, m) matrix tracking if a position (i, j) has been visited.
        # self.past_rotations: (n, m, 4) matrix tracking if a position (i, j) was visited in a specific direction
        # (0=Up, 1=Right, 2=Down, 3=Left).
        self.past_locations = np.zeros(grid.shape, dtype=bool)
        self.past_rotations = np.zeros((*grid.shape, 4), dtype=bool)

    def mark_position(self):
        self.past_locations[self.position] = True
        self.past_rotations[self.position + (self.direction,)] = True

    def move(self):
        """Move in the current direction if possible, rotating right as needed."""
        while True:
            next_position = self.next_position()
            if self.is_valid_position(next_position):
                self.position = next_position
                break
            self.rotate()

    def rotate(self):
        """Rotate the direction clockwise."""
        self.direction = (self.direction + 1) % 4

    def next_position(self):
        """Calculate the next position based on the current direction."""
        dx, dy = DIRECTIONS[self.direction]
        x, y = self.position
        return x + dx, y + dy

    def is_valid_position(self, position):
        """Check if a position is within bounds and traversable."""
        x, y = position
        return (
            0 <= x < self.grid_shape[0]
            and 0 <= y < self.grid_shape[1]
            and self.grid[position]
        )

    def check_infinite_loop(self):
        """Check if the combination of position/direction has already been visited"""
        if (
            self.past_locations[self.position]
            and self.past_rotations[self.position + (self.direction,)]
        ):
            raise InfiniteLoop

    def follow_path(self):
        while not self.is_border_reached():
            self.check_infinite_loop()
            self.mark_position()
            self.move()
        self.mark_position()
        return np.sum(self.past_locations)

    def is_border_reached(self):
        x, y = self.next_position()
        return not (0 <= x < self.grid_shape[0] and 0 <= y < self.grid_shape[1])


def part_1(grid, start_position, start_direction, obstacle=None):
    if obstacle:
        grid = grid.copy()
        grid[obstacle] = False
    tour = Tour(grid, start_position, start_direction)
    tour.follow_path()
    return tour.past_locations


def part_2(grid, start_position, start_direction, past_locations):
    wanna_be_obstacles = np.argwhere(past_locations)
    obstacles = []
    for position in tqdm(wanna_be_obstacles):
        obstacle = tuple(position)
        try:
            part_1(grid, start_position, start_direction, obstacle=obstacle)
        except InfiniteLoop:
            obstacles.append(obstacle)
    return len(set(obstacles))  # Remove duplicates from obstacles


if __name__ == "__main__":
    from aoc.initialize_day import load_input

    raw_input_data = load_input(__file__)
    parsed_grid, initial_position, initial_direction = read_input(raw_input_data)

    visited_positions_grid = part_1(parsed_grid, initial_position, initial_direction)
    print("Part 1:", np.sum(visited_positions_grid))

    loop_obstacles_count = part_2(
        parsed_grid, initial_position, initial_direction, visited_positions_grid
    )
    print("Part 2:", loop_obstacles_count)
