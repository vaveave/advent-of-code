from pathlib import Path


def change_floor(char_):
    match char_:
        case "(":
            return 1
        case ")":
            return -1
        case _:
            f"Instruction {char_} non recognised. Ignoring it."


def part_1(input_data):
    floor = 0
    for char in input_data:
        floor += change_floor(char)
    return str(floor)


def part_2(input_data):
    i = 0
    floor = 0
    for i, char in enumerate(input_data):
        floor += change_floor(char)
        if floor == -1:
            break
    return str(i+1)


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
