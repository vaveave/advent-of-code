from collections import Counter

from aoc.cli.utils import load_input


def read_input(data):
    return data


def part_1(data):
    most_common_chr = [
        Counter(msg).most_common() for msg in zip(*data.splitlines())
    ]
    return "".join(x[0][0] for x in most_common_chr)


def part_2(data):
    most_common_chr = [
        Counter(msg).most_common() for msg in zip(*data.splitlines())
    ]
    return "".join(x[-1][0] for x in most_common_chr)


def main():
    data = load_input(__file__)
    print("Part 1:", part_1(read_input(data)))
    print("Part 2:", part_2(read_input(data)))


if __name__ == "__main__":
    main()
