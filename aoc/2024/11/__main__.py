import numpy as np
from collections import Counter
from itertools import chain


def read_input(input_data):
    return [int(x) for x in input_data.split(" ")]


def transform_rules(stone):
    if stone == 0:
        return [1]
    elif (len(str(stone)) % 2) == 0:
        str_stone = str(stone)
        mid = len(str_stone) // 2
        return [int(str_stone[:mid]), int(str_stone[mid:])]
    else:
        return [stone * 2024]


def part_1(input_data, blinks):
    stones_counters = []
    stones_counters.append(Counter(input_data))
    for blink in range(blinks):
        new_counter = Counter(
            list(chain.from_iterable([transform_rules(stone)*count for stone, count in stones_counters[blink].items()]))
        )
        stones_counters.append(new_counter)
    return sum(stones_counters[-1].values())


if __name__ == "__main__":

    from aoc.initialize_day import load_input
    data = load_input(__file__)
    print("Part 1:", part_1(read_input(data), 25))
    # print("Part 2:", part_1(read_input(data), 75))
