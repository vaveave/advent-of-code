def read_input(input_data):
    return [int(line) for line in input_data.splitlines()]


def move_pointer(instructions, jump_cap=None):
    cnt = 0
    curr_pos = 0
    length = len(instructions)
    while 0 <= curr_pos < length:
        jump = instructions[curr_pos]
        if jump_cap is not None:
            instructions[curr_pos] += 1 if jump < jump_cap else -1
        else:
            instructions[curr_pos] += 1
        curr_pos += jump
        cnt += 1
    return cnt


def part_1(input_data):
    return move_pointer(input_data)


def part_2(input_data):
    return move_pointer(input_data, 3)


if __name__ == "__main__":
    from aoc.initialize_day import load_input

    data = load_input(__file__)
    print("Part 1:", part_1(read_input(data)))
    print("Part 2:", part_2(read_input(data)))
