import numpy as np


def read_input(input_data):
    len_blocks = np.array([int(input_data[i]) for i in range(len(input_data)) if (i%2) == 0])
    len_empty = np.array([int(input_data[i]) for i in range(len(input_data)) if (i%2) == 1])
    return [len_blocks, len_empty]


def calc_disc_status(input_data):
    len_blocks, len_empty = input_data
    disk_status = []
    for i in range(len(len_blocks)-1):
        disk_status += len_blocks[i] * [i] + len_empty[i] * ["."]
    if len(len_blocks) >= len(len_empty):
        disk_status += len_blocks[-1] * [len(len_blocks)-1]
    else:
        disk_status += len_empty[-1] * ["."]
    return disk_status


def part_1(input_data):
    disk_status = calc_disc_status(input_data)
    while "." in disk_status:
        to_be_mapped = disk_status[-1]
        ind = disk_status.index(".")
        disk_status[ind] = to_be_mapped
        disk_status = disk_status[:-1]
    return sum([i * int(disk_status[i]) for i in range(len(disk_status))])


def read_forward_backward(disk_status, pos_start, char, direction):
    pos = pos_start
    while disk_status[pos] == char:
        pos += direction
    return pos


def part_2(input_data):
    pass


if __name__ == "__main__":

    from aoc.initialize_day import load_input
    data = load_input(__file__)
    print("Part 1:", part_1(read_input(data)))
    print("Part 2:", part_2(read_input(data)))
