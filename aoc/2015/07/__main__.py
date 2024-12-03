from pathlib import Path


N_BIT = 16

bitwise_op = ["AND", "OR", "LSHIFT", "RSHIFT"]

size = 2**N_BIT-1


def parse_input_wires(str_: str) -> list:
    check_bitwise_op = [b in str_ for b in bitwise_op]
    if any(check_bitwise_op):
        operation = [bitwise_op[c] for c in range(len(bitwise_op)) if check_bitwise_op[c]][0]
        return [str_.split(" "+operation+" "), operation, None]
    elif "NOT " in str_:
        return [[str_.replace("NOT ", "")], "NOT", None]
    else:
        return [[str_], "", None]


def calc_gate(input_list, solutions):
    if input_list[0][0].isnumeric():
        a = input_list[0][0]
    else:
        a = solutions[input_list[0][0]]
    if len(input_list[0]) > 1:
        if input_list[0][1].isnumeric():
            b = input_list[0][1]
        else:
            b = solutions[input_list[0][1]]

    match input_list[1]:
        case "AND":
            return int(a) & int(b)
        case "OR":
            return int(a) | int(b)
        case "LSHIFT":
            return int(a) << int(b)
        case "RSHIFT":
            return int(a) >> int(b)
        case "NOT":
            return ~int(a) & size
        case _:
            return int(a)


def part_1(input_data):
    circuit = {
        row.split(" -> ")[1]: parse_input_wires(row.split(" -> ")[0])
        for row in input_data.splitlines()
    }
    solutions = {}
    while len(solutions) < len(circuit):
        for wire, operation in circuit.items():
            if all(input_.isnumeric() for input_ in operation[0]) | all(input_ in solutions for input_ in operation[0] if not input_.isnumeric()):
                sol = calc_gate(operation, solutions)
                solutions[wire] = sol
    return solutions["a"]


def part_2(input_data):
    circuit = {
        row.split(" -> ")[1]: parse_input_wires(row.split(" -> ")[0])
        for row in input_data.splitlines()
    }
    solutions = {}
    while len(solutions) < len(circuit):
        for wire, operation in circuit.items():
            if wire == "b":
                solutions[wire] = 3176
            elif all(input_.isnumeric() for input_ in operation[0]) | all(input_ in solutions for input_ in operation[0] if not input_.isnumeric()):
                sol = calc_gate(operation, solutions)
                solutions[wire] = sol
    return solutions["a"]


if __name__ == "__main__":
    
    from aoc.initialize_day import load_input

    folder = Path(__file__).parent
    try:
        year = int(folder.parts[-2])
        day = int(folder.parts[-1])
    except ValueError:
        print("Failed to determine year and day from folder structure.")
        raise SystemExit(1)

    data = load_input(year, day)

    print("Part 1:", part_1(data))
    print("Part 2:", part_2(data))
