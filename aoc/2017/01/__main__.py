
def read_input(input_data):
    return input_data


def part_1(input_data):
    counter = 0
    input_data += input_data[0]
    for i in range(len(input_data)-1):
        if input_data[i] == input_data[i+1]:
            counter += int(input_data[i])
    return counter


def part_2(input_data):
    counter = 0
    length = len(input_data)
    for i in range(length):
        if input_data[i] == input_data[(length//2 + i) % length]:
            counter += int(input_data[i])
    return counter


if __name__ == "__main__":

    from aoc.initialize_day import load_input
    data = load_input(__file__)
    print("Part 1:", part_1(read_input(data)))
    print("Part 2:", part_2(read_input(data)))
