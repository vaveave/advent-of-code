import re
from itertools import product
from pathlib import Path


def generate_strings_with_nans(s):
    unknown_indices = [i for i, char in enumerate(s) if char == "?"]

    possible_values = [".", "#"]
    replacements = list(product(possible_values, repeat=len(unknown_indices)))

    result_strings = []

    for replacement in replacements:
        temp_str = list(s)
        for index, value in zip(unknown_indices, replacement):
            temp_str[index] = value
        result_strings.append("".join(temp_str))

    return result_strings


def map_string_to_tuple(s):
    pattern = re.compile(r'#*')
    matches = pattern.findall(s)
    result_tuple = tuple(len(match) for match in matches if match)
    return result_tuple


def check_springs(full_spring: str):
    spring_str, check_str = full_spring.split(" ")
    spring_str, check_str = spring_str*5, check_str*5
    check_errors = tuple(int(i) for i in check_str.split(","))
    all_strings = generate_strings_with_nans(spring_str)
    cnt = 0
    for s in all_strings:
        if map_string_to_tuple(s) == check_errors:
            cnt += 1
    return cnt


def part_1(input_data):
    return sum([check_springs(str_) for str_ in input_data.splitlines()])


def part_2(input_data):
    # Implement part 2 solution
    pass


if __name__ == "__main__":
    with (Path(__file__).parent / "input.txt").open("r") as f:
        data = f.read()

    print("Part 1:", part_1(data))
    print("Part 2:", part_2(data))
