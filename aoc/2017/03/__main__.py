def read_input(input_data):
    return int(input_data)


def part_1(input_data):
    x, y = 0, 0
    dx, dy = 0, -1
    visited = {(0, 0)}
    for _ in range(input_data - 1):
        dx_new, dy_new = -dy, dx
        x_new, y_new = x + dx_new, y + dy_new
        if (x_new, y_new) not in visited:
            x, y = x_new, y_new
            dx, dy = dx_new, dy_new
        else:
            x, y = x + dx, y + dy
        visited.add((x, y))
    return abs(x) + abs(y)


def part_2(input_data):
    # Implement part 2 solution
    pass


if __name__ == "__main__":
    from aoc.initialize_day import load_input
    data = load_input(__file__)
    print("Part 1:", part_1(read_input(data)))
    print("Part 2:", part_2(read_input(data)))