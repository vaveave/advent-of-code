def read_input(input_data):
    return [line.split() for line in input_data.splitlines()]


def part_1_2(input_data):
    # Values
    max_reached = 0
    registers = {instr[0] for instr in input_data}
    [exec(register + "=0") for register in registers]
    for instr in input_data:
        # Example line: ['d', 'dec', '683', 'if', 'qn', '==', '0']
        condition = "".join(instr[4:])
        if eval(condition):
            if instr[1] == "inc":
                exec(instr[0] + "=" + instr[0] + "+" + instr[2])
            else:  # instr[1] == "dec":
                exec(instr[0] + "=" + instr[0] + "-" + instr[2])
        max_reached_instr = f"max({','.join([instr[0] for instr in input_data])})"
        max_reached = eval(f"max(max_reached, {max_reached_instr})")
    return eval(max_reached_instr), max_reached


if __name__ == "__main__":
    from aoc.initialize_day import load_input

    data = load_input(__file__)
    last_max, max_reached = part_1_2(read_input(data))
    print("Part 1:", last_max)
    print("Part 2:", max_reached)
