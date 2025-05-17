
def read_input(input_data):
    return [line.split(" ") for line in input_data.splitlines()]


def part_1(input_data):
    return sum(1 for line in input_data if len(line) == len(set(line)))


def part_2(input_data):
    input_data = [
        ["".join(sorted(word)) for word in line] for line in input_data
    ]
    return part_1(input_data)


if __name__ == "__main__":

    from aoc.initialize_day import load_input
    data = load_input(__file__)
    print("Part 1:", part_1(read_input(data)))
    print("Part 2:", part_2(read_input(data)))
