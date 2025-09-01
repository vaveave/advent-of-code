from math import ceil

from aoc.cli.utils import load_input


def read_input(input_data):
    return [int(line) for line in input_data.split("\t")]


def redistribute_blocks(memory_banks):
    num_banks = len(memory_banks)
    cycle_count = 0
    seen_configs = {}
    while True:
        cycle_count += 1
        seen_configs[tuple(memory_banks)] = cycle_count
        max_index, blocks = max(enumerate(memory_banks), key=lambda x: x[1])
        base_blocks = ceil(blocks / num_banks)
        remaining_blocks = blocks
        for i in range(num_banks - 1):
            target_index = (max_index + i + 1) % num_banks
            give = min(base_blocks, remaining_blocks)
            memory_banks[target_index] += give
            remaining_blocks -= give
        memory_banks[max_index] = remaining_blocks
        if tuple(memory_banks) in seen_configs:
            break
    return cycle_count, cycle_count - seen_configs[tuple(memory_banks)] + 1


def part_1(data):
    total_cycles, _ = redistribute_blocks(data.copy())
    return total_cycles


def part_2(data):
    _, loop_size = redistribute_blocks(data.copy())
    return loop_size


def main():
    data = load_input(__file__)
    parsed = read_input(data)
    print("Part 1:", part_1(parsed))
    print("Part 2:", part_2(parsed))


if __name__ == "__main__":
    main()
