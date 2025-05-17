def process_input(input_str):
    return [list(map(int, p.split(" "))) for p in input_str.split("\n")]


def extrapolate_value(values):
    deltas = [values]
    is_not_0 = True
    while is_not_0:
        delta = [b - a for a, b in zip(deltas[-1], deltas[-1][1:])]
        deltas.append(delta)
        is_not_0 = any(delta)
    deltas[-1].append(0)
    for i in range(len(deltas) - 2, -1, -1):
        deltas[i].append(deltas[i + 1][-1] + deltas[i][-1])
    return deltas[0][-1]


def part_1(input_data):
    return sum([extrapolate_value(values) for values in process_input(input_data)])


def extrapolate_backward_value(values):
    deltas = [values]
    is_not_0 = True
    while is_not_0:
        delta = [b - a for a, b in zip(deltas[-1], deltas[-1][1:])]
        deltas.append(delta)
        is_not_0 = any(delta)
    deltas[-1].append(0)
    for i in range(len(deltas) - 2, -1, -1):
        deltas[i] = [deltas[i][0] - deltas[i + 1][0]] + deltas[i]
    return deltas[0][0]


def part_2(input_data):
    return sum(
        [extrapolate_backward_value(values) for values in process_input(input_data)]
    )


if __name__ == "__main__":
    from aoc.initialize_day import load_input

    data = load_input(__file__)
    print("Part 1:", part_1(data))
    print("Part 2:", part_2(data))
