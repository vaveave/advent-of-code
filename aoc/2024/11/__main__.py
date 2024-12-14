import functools
from tqdm import tqdm
from collections import Counter


def read_input(input_data):
    return [int(x) for x in input_data.split(" ")]


@functools.lru_cache(maxsize=None)
def transform_rules(stone):
    if stone == 0:
        return [1]
    elif (len(str(stone)) % 2) == 0:
        str_stone = str(stone)
        mid = len(str_stone) // 2
        return [int(str_stone[:mid]), int(str_stone[mid:])]
    else:
        return [stone * 2024]


def transform_stones(input_data, blinks_part_1, blinks_part_2):
    stones_counters = Counter(input_data)
    part_1 = 0
    for blink in tqdm(range(blinks_part_2)):
        new_counter = Counter()
        for stone, count in stones_counters.items():
            for new_stone in transform_rules(stone):
                new_counter[new_stone] += count
        stones_counters = new_counter
        if blink == blinks_part_1:
            part_1 = sum(stones_counters.values())
    part_2 = sum(stones_counters.values())
    return part_1, part_2


if __name__ == "__main__":

    from aoc.initialize_day import load_input
    data = load_input(__file__)
    part_1, part_2 = transform_stones(read_input(data), 25, 75)
    print("Part 1:", part_1)
    print("Part 2:", part_2)
