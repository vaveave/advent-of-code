import numpy as np


def parse_input(disk_map):
    file_lengths = np.array([int(disk_map[i]) for i in range(len(disk_map)) if i % 2 == 0])
    free_space_lengths = np.array([int(disk_map[i]) for i in range(len(disk_map)) if i % 2 == 1])
    return file_lengths, free_space_lengths


def generate_disk_status(file_lengths, free_space_lengths):
    disk_status = []
    for file_id in range(len(file_lengths) - 1):
        disk_status += file_lengths[file_id] * [file_id]
        disk_status += free_space_lengths[file_id] * ['.']

    # Handle the last segment
    if len(file_lengths) >= len(free_space_lengths):
        disk_status += file_lengths[-1] * [len(file_lengths) - 1]
    else:
        disk_status += free_space_lengths[-1] * ['.']
    return disk_status


def calculate_checksum(disk_status):
    return sum(position * int(block) for position, block in enumerate(disk_status) if block != '.')


def part_1(file_lengths, free_space_lengths):
    disk_status = generate_disk_status(file_lengths, free_space_lengths)

    while '.' in disk_status:
        free_space_index = disk_status.index('.')
        block_to_move = disk_status[-1]
        disk_status[free_space_index] = block_to_move
        disk_status.pop()

    return calculate_checksum(disk_status)


def find_next_position(disk_status, start_index, target_char, step):
    position = start_index
    while disk_status[position] == target_char:
        position += step
    return position


def find_consecutive_dots(disk_status, n):
    """
    Finds the first occurrence of n consecutive '.' in the list.
    """
    count = 0
    for i, elem in enumerate(disk_status):
        if elem == '.':
            count += 1
            if count == n:
                return i - n + 1  # Starting index of the sequence
        else:
            count = 0
    return -1  # Not found


def part_2(file_lengths, free_space_lengths):
    disk_status = generate_disk_status(file_lengths, free_space_lengths)
    i = len(disk_status)-1
    while i >= 0:
        file_id = disk_status[i]
        if file_id == ".":
            i -= 1
            continue
        file_id_start = find_next_position(disk_status, i, file_id, -1)
        file_id_len = i - file_id_start
        i_begin_empty_slot = find_consecutive_dots(disk_status[:file_id_start+1], file_id_len)
        if i_begin_empty_slot == -1:
            i = file_id_start
            continue
        else:
            disk_status[i_begin_empty_slot:i_begin_empty_slot+file_id_len], disk_status[file_id_start+1:i+1] = (
                disk_status[file_id_start+1:i+1], disk_status[i_begin_empty_slot:i_begin_empty_slot+file_id_len]
            )
            i = file_id_start

    return calculate_checksum(disk_status)


if __name__ == "__main__":
    from aoc.initialize_day import load_input

    # Load input data
    raw_data = load_input(__file__)
    file_lengths_, free_space_lengths_ = parse_input(raw_data)

    # print("Part 1:", part_1(file_lengths_, free_space_lengths_))
    print("Part 2:", part_2(file_lengths_, free_space_lengths_))
