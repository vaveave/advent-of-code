def clean_data(input_data):
    cleaned_data = ""
    ind = 0
    while ind < len(input_data):
        if input_data[ind] == "!":
            ind += 2
            continue
        cleaned_data += input_data[ind]
        ind += 1
    return cleaned_data


def part_1_and_2(cleaned_data):
    score = 0
    open_groups = 0
    ind = 0
    while ind < len(cleaned_data):
        if cleaned_data[ind] == "<":
            ind += cleaned_data[ind:].find(">") + 1
            continue
        if cleaned_data[ind] == "{":
            open_groups += 1
        elif cleaned_data[ind] == "}":
            score += open_groups
            open_groups -= 1
        ind += 1
    return score, None


if __name__ == "__main__":
    from aoc.initialize_day import load_input

    data = load_input(__file__)
    part_1, part_2 = part_1_and_2(clean_data(data))
    print("Part 1:", part_1)
    print("Part 2:", part_2)