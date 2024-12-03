from pathlib import Path
from collections import Counter


def part_1(input_data):
    most_common_chr = [Counter(msg).most_common() for msg in zip(*input_data.splitlines())]
    return "".join(x[0][0] for x in most_common_chr)


def part_2(input_data):
    most_common_chr = [Counter(msg).most_common() for msg in zip(*input_data.splitlines())]
    return "".join(x[-1][0] for x in most_common_chr)


if __name__ == "__main__":
    
    from aoc.initialize_day import load_input

    folder = Path(__file__).parent
    try:
        year = int(folder.parts[-2])
        day = int(folder.parts[-1])
    except ValueError:
        print("Failed to determine year and day from folder structure.")
        raise SystemExit(1)

    data = load_input(year, day)

    print("Part 1:", part_1(data))
    print("Part 2:", part_2(data))
