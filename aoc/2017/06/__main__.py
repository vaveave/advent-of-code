from math import ceil


def read_input(input_data):
    return [int(line) for line in input_data.split("\t")]


def part_1_and_2(all_blocks: list[int]):
    length = len(all_blocks)
    cnt = 0
    seen = {}
    while True:
        cnt += 1
        seen[tuple(all_blocks)] = cnt
        # Find the index of the largest block
        argmax, max_val = max(enumerate(all_blocks), key=lambda x: x[1])
        # Distribute blocks
        blocks_to_distribute = ceil(max_val / length)
        distributed = max_val
        for i in range(length - 1):
            ind = (argmax + i + 1) % length
            new_val = min(blocks_to_distribute, distributed)
            # Distribute blocks to the next index
            all_blocks[ind] += new_val
            distributed -= new_val
        all_blocks[argmax] = distributed
        if tuple(all_blocks) in seen:
            break
    return cnt, cnt - seen[tuple(all_blocks)] + 1


if __name__ == "__main__":
    from aoc.initialize_day import load_input

    data = load_input(__file__)
    cnt, cycle_length = part_1_and_2(read_input(data))
    print("Part 1:", cnt)
    print("Part 2:", cycle_length)
