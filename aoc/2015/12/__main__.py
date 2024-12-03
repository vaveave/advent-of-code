import re
import json
from pathlib import Path


def part_1(input_data):
    pattern = re.compile(r"[-+]?[0-9]+")
    return sum(map(int, pattern.findall(input_data)))


def sum_excluding_reds(input_data):
    if isinstance(input_data, list):
        return sum(sum_excluding_reds(sub_json) for sub_json in input_data)
    elif isinstance(input_data, dict):
        values = input_data.values()
        if any(value == "red" for value in values):
            return 0
        return sum(sum_excluding_reds(value) for value in values)
    elif isinstance(input_data, int):
        return input_data
    elif isinstance(input_data, str):
        return 0
    else:
        raise ValueError(f"Unexpected data type: {type(input_data)}")


def part_2(input_data):
    input_data = json.loads(input_data)
    return sum_excluding_reds(input_data)


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
