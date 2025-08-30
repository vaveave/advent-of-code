def read_input(input_data):
    return [line.split() for line in input_data.splitlines()]


def part_1_and_2(instructions):
    registers = {}
    max_reached = float('-inf')

    # Map of condition operators to actual Python lambdas
    ops = {
        "==": lambda x, y: x == y,
        "!=": lambda x, y: x != y,
        "<" : lambda x, y: x < y,
        "<=": lambda x, y: x <= y,
        ">" : lambda x, y: x > y,
        ">=": lambda x, y: x >= y
    }

    for reg, action, value, _, cond_reg, cond_op, cond_value in instructions:
        value = int(value)
        cond_value = int(cond_value)

        # Initialize registers if not seen yet
        registers.setdefault(reg, 0)
        registers.setdefault(cond_reg, 0)

        # Check condition
        if ops[cond_op](registers[cond_reg], cond_value):
            registers[reg] += value if action == "inc" else -value

        # Track max value ever held in any register
        max_reached = max(max_reached, max(registers.values()))

    return max(registers.values()), max_reached


if __name__ == "__main__":
    from aoc.initialize_day import load_input

    data = load_input(__file__)
    part_1, part_2 = part_1_and_2(read_input(data))
    print("Part 1:", part_1)
    print("Part 2:", part_2)
