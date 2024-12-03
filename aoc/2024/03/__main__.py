import re

from pathlib import Path


def part_1(input_data):
    non_corrupted_pairs = [
        tuple(map(int, x)) for x in re.findall(r"mul\((\d+),(\d+)\)", input_data)
    ]
    return sum(x[0]*x[1] for x in non_corrupted_pairs)


def part_2(input_data):
    remaining_string = input_data
    indexes = [remaining_string.find("do()"), remaining_string.find("don't()")]
    result = part_1(input_data[:(min(indexes))])
    while True:
        indexes = [remaining_string.find("do()"), remaining_string.find("don't()")]
        if all(ind==-1 for ind in indexes):
            return result
        indexes.sort()
        if indexes[0] == -1:
            indexes = [indexes[1], len(remaining_string)]
        if not remaining_string[indexes[0]:].startswith("don't()"):
            result += part_1(remaining_string[indexes[0]:indexes[1]])
        remaining_string = remaining_string[indexes[1]:]


if __name__ == "__main__":
    with (Path(__file__).parent / "input.txt").open("r") as f:
        data = f.read()

    print("Part 1:", part_1(data))
    print("Part 2:", part_2(data))
