def read_input(input_data):
    return input_data


def calculate_sum(input_data, offset):
    length = len(input_data)
    return sum(
        int(input_data[i])
        for i in range(length)
        if input_data[i] == input_data[(i + offset) % length]
    )


if __name__ == "__main__":
    from aoc.initialize_day import load_input

    data = load_input(__file__)
    print("Part 1:", calculate_sum(data, 1))  # Offset of 1 for part 1
    print(
        "Part 2:", calculate_sum(data, len(data) // 2)
    )  # Offset of length//2 for part 2
