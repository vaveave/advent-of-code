import re
from aoc.cli.utils import load_input


def isolate_part(row: str, pos: int):
    start_pos = pos
    end_pos = pos

    # Move left to find the starting position of the digits
    while start_pos >= 0 and row[start_pos].isdigit():
        start_pos -= 1

    # Move right to find the ending position of the digits
    while end_pos < len(row) and row[end_pos].isdigit():
        end_pos += 1

    # Extract the digits from the string
    extracted_digits = row[start_pos + 1 : end_pos]
    return int(extracted_digits)


def get_all_possible_engine_parts(engine):
    possible_engine_parts = []
    for row in engine:
        row_engine_parts = []
        for match in re.finditer(r"\d+", row):
            row_engine_parts.append(
                (match.start(), match.start() + len(match.group()) - 1, match.group())
            )
        possible_engine_parts.append(row_engine_parts)
    return possible_engine_parts


def get_engine_parts(engine):
    engine_parts = []
    parts_candidates = get_all_possible_engine_parts(engine)
    for i, row in enumerate(engine):
        for j, char in enumerate(row):
            if not re.match(r"[0-9.]", char):
                close_candidates = [
                    item
                    for sublist in parts_candidates[i - 1 : i + 2]
                    for item in sublist
                ]
                for candidate in close_candidates:
                    if abs(candidate[0] - j) <= 1 or abs(candidate[1] - j) <= 1:
                        engine_parts.append(candidate)
    return engine_parts


def read_input(data):
    return data


def part_1(input_data):
    engine_parts = get_engine_parts(input_data.splitlines())
    return sum([int(part[2]) for part in engine_parts])


def get_engine_gears(engine):
    engine_gears = []
    parts_candidates = get_all_possible_engine_parts(engine)
    for i, row in enumerate(engine):
        for j, char in enumerate(row):
            if char == "*":
                close_candidates = [
                    item
                    for sublist in parts_candidates[i - 1 : i + 2]
                    for item in sublist
                ]
                adjacent_parts = [
                    candidate
                    for candidate in close_candidates
                    if abs(candidate[0] - j) <= 1 or abs(candidate[1] - j) <= 1
                ]
                if len(adjacent_parts) == 2:
                    engine_gears.append(adjacent_parts)
    return engine_gears


def part_2(input_data):
    engine_gears = get_engine_gears(input_data.splitlines())
    return sum([int(parts[0][2]) * int(parts[1][2]) for parts in engine_gears])


def main():
    data = load_input(__file__)
    print("Part 1:", part_1(read_input(data)))
    print("Part 2:", part_2(read_input(data)))


if __name__ == "__main__":
    main()
