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
    with (Path(__file__).parent / "input.txt").open("r") as f:
        data = f.read()

    print("Part 1:", part_1(read_input(data)))
    print("Part 2:", part_2(read_input(data)))
