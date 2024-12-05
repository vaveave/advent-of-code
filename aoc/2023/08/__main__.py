from math import lcm


decode_instr = {"L": 0, "R": 1}


def process_input(input_str):
    instructions, nodes_str = input_str.split("\n\n")
    nodes_map = {
        node.split(" = ")[0]:
            eval(node.split(" = ")[1].replace('(', '[\'').replace(')', '\']').replace(', ', '\',\''))
        for node in nodes_str.split("\n")
    }
    return instructions, nodes_map


def follow_the_path_mr_camel(input_str):
    instructions, nodes_map = process_input(input_str)
    i = 0
    node = "AAA"
    len_instr = len(instructions)
    while node != "ZZZ":
        instruction = decode_instr[instructions[i % len_instr]]
        node = nodes_map[node][instruction]
        i += 1
    return i


def follow_the_ghosts_path_mr_camel(input_str):
    instructions, nodes_map = process_input(input_str)
    nodes = [node for node in nodes_map.keys() if node.endswith('A')]

    def follow_the_ghosts_path(node):
        i = 0
        len_instr = len(instructions)
        while not node.endswith("Z"):
            instruction = decode_instr[instructions[i % len_instr]]
            node = nodes_map[node][instruction]
            i += 1
        return i

    path_lengths = [follow_the_ghosts_path(node) for node in nodes]
    return lcm(*path_lengths)


def part_1(input_data):
    return follow_the_path_mr_camel(input_data)


def part_2(input_data):
    return follow_the_ghosts_path_mr_camel(input_data)


if __name__ == "__main__":

    from aoc.initialize_day import load_input
    data = load_input(__file__)
    print("Part 1:", part_1(data))
    print("Part 2:", part_2(data))
