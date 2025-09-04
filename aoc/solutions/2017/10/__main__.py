from aoc.cli.utils import load_input


def read_input(data):
    return [int(d) for d in data.split(",")]


def part_1(data, size):
    curr_list = list(range(size))
    curr_pos = 0
    for skip_size, length in enumerate(data):
        indices = [(curr_pos + i) % size for i in range(length)]
        values = [curr_list[i] for i in indices][::-1]
        for idx, val in zip(indices, values):
            curr_list[idx] = val
        curr_pos = (length + curr_pos + skip_size) % size
    return curr_list[0] * curr_list[1]


def part_2(data):
    # Implement part 2 solution
    pass


def main():
    data = load_input(__file__)
    list_size = 256
    print("Part 1:", part_1(read_input(data), list_size))
    print("Part 2:", part_2(read_input(data)))


if __name__ == "__main__":
    main()
