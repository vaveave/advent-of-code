from aoc.cli.utils import load_input


def read_input(input_data):
    return [line.split() for line in input_data.splitlines()]


def part_1_and_2(instructions):
    registers = {}
    max_reached = float('-inf')
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
        registers.setdefault(reg, 0)
        registers.setdefault(cond_reg, 0)
        if ops[cond_op](registers[cond_reg], cond_value):
            registers[reg] += value if action == "inc" else -value
        max_reached = max(max_reached, max(registers.values()))
    return max(registers.values()), max_reached


def part_1(data):
    return part_1_and_2(read_input(data))[0]


def part_2(data):
    return part_1_and_2(read_input(data))[1]


def main():
    data = load_input(__file__)
    print("Part 1:", part_1(data))
    print("Part 2:", part_2(data))


if __name__ == "__main__":
    main()
