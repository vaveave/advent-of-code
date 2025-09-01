from aoc.cli.utils import load_input


def read_input(input_data):
    return input_data


def calculate_sum(input_data, offset):
    length = len(input_data)
    return sum(
        int(input_data[i])
        for i in range(length)
        if input_data[i] == input_data[(i + offset) % length]
    )


def part_1(data):
    return calculate_sum(data, 1)


def part_2(data):
    return calculate_sum(data, len(data) // 2)


def main():
    data = load_input(__file__)
    print("Part 1:", part_1(read_input(data)))
    print("Part 2:", part_2(read_input(data)))


if __name__ == "__main__":
    main()
