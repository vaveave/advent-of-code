import re


mul_pattern = re.compile(r"mul\((\d+),(\d+)\)")
do_dont_pattern = re.compile(r"do\(\)|don't\(\)")


def part_1(input_data):
    non_corrupted_pairs = [
        tuple(map(int, x)) for x in mul_pattern.findall(input_data)
    ]
    return sum(x[0]*x[1] for x in non_corrupted_pairs)


def part_2(input_data):
    boundaries = [match.start() for match in do_dont_pattern.finditer(input_data)]
    boundaries = [0] + boundaries + [len(input_data)]
    total = 0
    for i in range(len(boundaries)-1):
        segment = input_data[boundaries[i]:boundaries[i + 1]]
        if segment.startswith("don't"):
            continue
        total += part_1(segment)
    return total


if __name__ == "__main__":

    from aoc.initialize_day import load_input
    data = load_input(__file__)
    print("Part 1:", part_1(data))
    print("Part 2:", part_2(data))
