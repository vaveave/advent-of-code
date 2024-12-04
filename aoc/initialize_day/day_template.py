from pathlib import Path


def read_input(input_data):
    return input_data


def part_1(input_data):
    # Implement part 1 solution
    pass


def part_2(input_data):
    # Implement part 2 solution
    pass


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

    print("Part 1:", part_1(read_input(data)))
    print("Part 2:", part_2(read_input(data)))
