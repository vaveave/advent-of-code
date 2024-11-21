from pathlib import Path
from collections import Counter


def part_1(input_data):
    most_common_chr = [Counter(msg).most_common() for msg in zip(*input_data.splitlines())]
    return "".join(x[0][0] for x in most_common_chr)


def part_2(input_data):
    most_common_chr = [Counter(msg).most_common() for msg in zip(*input_data.splitlines())]
    return "".join(x[-1][0] for x in most_common_chr)


if __name__ == "__main__":
    with (Path(__file__).parent / "input.txt").open("r") as f:
        data = f.read()

    print("Part 1:", part_1(data))
    print("Part 2:", part_2(data))
