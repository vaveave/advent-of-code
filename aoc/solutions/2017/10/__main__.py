from aoc.cli.utils import load_input


def rearrange_list(curr_list, curr_pos, length, size):
    indices = [(curr_pos + i) % size for i in range(length)]
    values = [curr_list[i] for i in indices][::-1]
    for idx, val in zip(indices, values):
        curr_list[idx] = val
    return curr_list


def part_1(data, size):
    lengths = [int(d) for d in data.split(",")]
    curr_list = list(range(size))
    curr_pos = 0
    for skip_size, length in enumerate(lengths):
        curr_list = rearrange_list(curr_list, curr_pos, length, size)
        curr_pos = (length + curr_pos + skip_size) % size
    return curr_list[0] * curr_list[1]


def part_2(data, size):
    lengths = [ord(d) for d in data] + [17, 31, 73, 47, 23]
    curr_list = list(range(size))
    curr_pos = 0
    skip_size = 0

    for _ in range(64):
        for length in lengths:
            indices = [(curr_pos + i) % size for i in range(length)]
            values = [curr_list[i] for i in indices][::-1]
            for idx, val in zip(indices, values):
                curr_list[idx] = val
            curr_pos = (curr_pos + length + skip_size) % size
            skip_size += 1

    dense = []
    for i in range(0, size, 16):
        x = 0
        for v in curr_list[i:i + 16]:
            x ^= v
        dense.append(x)

    return "".join(f"{x:02x}" for x in dense)


def main():
    data = load_input(__file__)
    list_size = 256
    print("Part 1:", part_1(data, list_size))
    print("Part 2:", part_2(data, list_size))


if __name__ == "__main__":
    main()
