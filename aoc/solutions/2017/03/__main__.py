from aoc.cli.utils import load_input


def read_input(input_data):
    return int(input_data)



def spiral_move(x, y, dx, dy, visited):
    dx_new, dy_new = -dy, dx
    x_new, y_new = x + dx_new, y + dy_new
    if (x_new, y_new) not in visited:
        x, y = x_new, y_new
        dx, dy = dx_new, dy_new
    else:
        x, y = x + dx, y + dy
    return x, y, dx, dy



def part_1(data):
    x, y = 0, 0
    dx, dy = 0, -1
    visited = {(0, 0)}
    for _ in range(data - 1):
        x, y, dx, dy = spiral_move(x, y, dx, dy, visited)
        visited.add((x, y))
    return abs(x) + abs(y)



def part_2(data):
    x, y = 0, 0
    dx, dy = 0, -1
    visited = {(0, 0): 1}
    neighbors = [(0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]
    while True:
        if visited[(x, y)] > data:
            return visited[(x, y)]
        x, y, dx, dy = spiral_move(x, y, dx, dy, visited)
        visited[(x, y)] = sum(visited.get((x + dx, y + dy), 0) for dx, dy in neighbors)



def main():
    data = load_input(__file__)
    print("Part 1:", part_1(read_input(data)))
    print("Part 2:", part_2(read_input(data)))


if __name__ == "__main__":
    main()
