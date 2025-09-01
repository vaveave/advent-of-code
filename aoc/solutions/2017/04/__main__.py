from aoc.cli.utils import load_input


def read_input(input_data):
    return [line.split(" ") for line in input_data.splitlines()]


def part_1(data):
    return sum(1 for line in data if len(line) == len(set(line)))


def part_2(data):
    data = [["".join(sorted(word)) for word in line] for line in data]
    return part_1(data)


def main():
    data = load_input(__file__)
    print("Part 1:", part_1(read_input(data)))
    print("Part 2:", part_2(read_input(data)))


if __name__ == "__main__":
    main()
