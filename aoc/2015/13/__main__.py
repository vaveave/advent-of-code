import re


def read_input(input_data):
    first_name_pattern = re.compile(r"^([\w\-]+)")
    last_name_pattern = re.compile(r"\b(\w+).$")
    score_pattern = re.compile(r"\d+")
    return {
        (first_name_pattern.findall(x)[0], last_name_pattern.findall(x)[0]):
            int(score_pattern.findall(x)[0]) for x in input_data.splitlines()
    }


def part_1(input_data):
    # Implement part 1 solution
    pass


def part_2(input_data):
    # Implement part 2 solution
    pass


if __name__ == "__main__":

    from aoc.initialize_day import load_input
    data = load_input(__file__)
    print("Part 1:", part_1(read_input(data)))
    print("Part 2:", part_2(read_input(data)))
