import functools
from collections import Counter

from aoc.cli.utils import load_input


def read_input(input_data):
    return list(map(int, input_data.split()))


@functools.lru_cache(maxsize=None)
def transform_rules(stone):
    if stone == 0:
        return [1]
    str_stone = str(stone)
    mid = len(str_stone) // 2
    return (
        [int(str_stone[:mid]), int(str_stone[mid:])]
        if len(str_stone) % 2 == 0
        else [stone * 2024]
    )


def transform_stones(input_data, blinks_part_1, blinks_part_2):
    stones_counters = Counter(input_data)
    part_1_out = None

    for blink in range(1, blinks_part_2 + 1):
        new_counter = Counter()
        for stone, count in stones_counters.items():
            for new_stone in transform_rules(stone):
                new_counter[new_stone] += count
        stones_counters = new_counter

        if blink == blinks_part_1:
            part_1_out = sum(stones_counters.values())

    part_2_out = sum(stones_counters.values())
    return part_1_out, part_2_out


def main():
    data = load_input(__file__)
    input_stones = read_input(data)
    part_1, part_2 = transform_stones(input_stones, 25, 75)
    print("Part 1:", part_1)
    print("Part 2:", part_2)


if __name__ == "__main__":
    main()
