from itertools import combinations


def read_input(input_data):
    lines = input_data.strip().splitlines()
    data = [list(map(int, line.split("\t"))) for line in lines]
    return data


def part_1(input_data):
    return sum([max(row) - min(row) for row in input_data])


def part_2(input_data):
    tot = 0
    for row in input_data:
        for a, b in combinations(row, 2):
            if a % b == 0 or b % a == 0:
                tot += abs(a // b) if a > b else abs(b // a)
    return tot


if __name__ == "__main__":

    from aoc.initialize_day import load_input
    data = load_input(__file__)
    print("Part 1:", part_1(read_input(data)))
    print("Part 2:", part_2(read_input(data)))
