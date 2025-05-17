def map_instruction(move):
    match move:
        case "^":
            return 0, 1
        case "v":
            return 0, -1
        case ">":
            return 1, 0
        case "<":
            return -1, 0
        case _:
            print(f"Move {move} not recognised")


def follow_path(starting_position, instructions):
    path = [starting_position]
    for i, move in enumerate(instructions):
        instr = map_instruction(move)
        path.append((path[i][0] + instr[0], path[i][1] + instr[1]))
    return path


def part_1(input_data):
    santa_path = follow_path((0, 0), input_data)
    return str(set(santa_path).__len__())


def part_2(input_data):
    santa_path = follow_path((0, 0), input_data[::2])
    robo_santa_path = follow_path((0, 0), input_data[1::2])
    return str(set(santa_path).union(set(robo_santa_path)).__len__())


if __name__ == "__main__":
    from aoc.initialize_day import load_input

    data = load_input(__file__)
    print("Part 1:", part_1(data))
    print("Part 2:", part_2(data))
