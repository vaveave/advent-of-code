from itertools import chain


def read_input(input_data):
    return input_data.split(" ")


def transform_rules(stone: str):
    if stone == "0":
        return ["1"]
    elif (len(stone) % 2) == 0:
        new_len = int(len(stone)/2)
        return [str(int(stone[:new_len])), str(int(stone[new_len:]))]
    else:
        return [str(int(stone) * 2024)]


def part_1(input_data, blinks):
    stones_pattern = input_data
    for blink in range(1, blinks+1):
        stones_pattern = list(
            chain.from_iterable([transform_rules(stone) for stone in stones_pattern])
        )
    return len(stones_pattern)


def part_2(input_data):
    # Implement part 2 solution
    pass


if __name__ == "__main__":

    from aoc.initialize_day import load_input
    data = load_input(__file__)
    print("Part 1:", part_1(read_input(data), 75))
    # print("Part 2:", part_1(read_input(data), 75))
