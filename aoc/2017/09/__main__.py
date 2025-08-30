import re

from aoc.initialize_day import load_input


def clean_data(data: str) -> str:
    # Remove canceled characters: any "!" followed by one character
    return re.sub(r"!.", "", data)


def part_1_and_2(data):
    data = clean_data(data)
    score = depth = garbage = ind = 0
    while ind < len(data):
        if data[ind] == "<":
            new_garbage = data[ind:].find(">")
            ind += new_garbage + 1
            garbage += new_garbage - 1
            continue
        if data[ind] == "{":
            depth += 1
        elif data[ind] == "}":
            score += depth
            depth -= 1
        ind += 1
    return score, garbage


input_data = load_input(__file__)
part_1, part_2 = part_1_and_2(input_data)
print("Part 1:", part_1)
print("Part 2:", part_2)
