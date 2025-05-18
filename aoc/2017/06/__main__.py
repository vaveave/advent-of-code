from math import ceil


def read_input(input_data):
    return [int(line) for line in input_data.split("\t")]


def redistribute_blocks(memory_banks: list[int]) -> tuple[int, int]:
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


if __name__ == "__main__":
    from aoc.initialize_day import load_input

    data = load_input(__file__)
    total_cycles, loop_size = redistribute_blocks(read_input(data))
    print("Part 1:", total_cycles)
    print("Part 2:", loop_size)
