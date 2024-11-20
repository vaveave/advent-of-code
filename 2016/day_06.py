from pathlib import Path
from collections import Counter


def part1(input_data):
    most_common_chr = [Counter(msg).most_common() for msg in zip(*input_data.splitlines())]
    return "".join(x[0][0] for x in most_common_chr)


def part2(input_data):
    most_common_chr = [Counter(msg).most_common() for msg in zip(*input_data.splitlines())]
    return "".join(x[-1][0] for x in most_common_chr)


if __name__ == "__main__":
    # Get the input file path and read the input data
    input_file = Path(__file__).parent / f"day_06_input.txt"
    with open(input_file) as f:
        data = f.read().strip()
    
    print("Part 1:", part1(data))
    print("Part 2:", part2(data))
