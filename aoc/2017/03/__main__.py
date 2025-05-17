def read_input(input_data):
    return int(input_data)


def spiral_move(x, y, dx, dy, visited):
    """
    Moves a point (x, y) in a spiral pattern, updating its direction and position.
    The function attempts to turn left (counterclockwise) from the current direction (dx, dy).
    If the new position has not been visited, it moves to that position and updates the direction.
    Otherwise, it continues moving in the current direction.
    Args:
        x (int): Current x-coordinate.
        y (int): Current y-coordinate.
        dx (int): Current x-direction increment.
        dy (int): Current y-direction increment.
        visited (set of tuple): Set of (x, y) tuples representing visited positions.
    Returns:
        tuple: Updated (x, y, dx, dy) after moving in the spiral.
    """
    dx_new, dy_new = -dy, dx
    x_new, y_new = x + dx_new, y + dy_new
    if (x_new, y_new) not in visited:
        x, y = x_new, y_new
        dx, dy = dx_new, dy_new
    else:
        x, y = x + dx, y + dy
    return x, y, dx, dy


def part_1(input_data):
    x, y = 0, 0
    dx, dy = 0, -1
    visited = {(0, 0)}
    for _ in range(input_data - 1):
        x, y, dx, dy = spiral_move(x, y, dx, dy, visited)
        visited.add((x, y))
    return abs(x) + abs(y)


def part_2(input_data):
    x, y = 0, 0
    dx, dy = 0, -1
    visited = {(0, 0): 1}
    neighbors = [(0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]
    while True:
        if visited[(x, y)] > input_data:
            return visited[(x, y)]
        x, y, dx, dy = spiral_move(x, y, dx, dy, visited)
        visited[(x, y)] = sum(visited.get((x + dx, y + dy), 0) for dx, dy in neighbors)


if __name__ == "__main__":
    from aoc.initialize_day import load_input

    data = load_input(__file__)
    print("Part 1:", part_1(read_input(data)))
    print("Part 2:", part_2(read_input(data)))
