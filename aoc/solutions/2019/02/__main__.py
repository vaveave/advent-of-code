from itertools import product

from aoc.cli.utils import load_input


def read_input(data):
    return [int(i) for i in data.split(",")]


def part_1(data, noun=12, verb=2):
    curr_pos = 0
    data[1] = noun
    data[2] = verb
    opp_code, pos_param_1, pos_param_2, pos_result = data[curr_pos: curr_pos + 4]
    while data[curr_pos] != 99:
        match opp_code:
            case 1:
                data[pos_result] = data[pos_param_1] + data[pos_param_2]
            case 2:
                data[pos_result] = data[pos_param_1] * data[pos_param_2]
        curr_pos += 4
        opp_code, pos_param_1, pos_param_2, pos_result = data[curr_pos: curr_pos + 4]
    return data[0]


def part_2(data):
    for noun, verb in product(range(100), range(100)):
        if part_1(data.copy(), noun, verb) == 19690720:
            return 100 * noun + verb


def main():
    data = load_input(__file__)
    print("Part 1:", part_1(read_input(data)))
    print("Part 2:", part_2(read_input(data)))


if __name__ == "__main__":
    main()
