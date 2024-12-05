

def look_and_say(str_):
    out = ""
    i, j = 0, 0
    while i < len(str_):
        char = str_[i]
        char_cnt = 1
        if i+char_cnt == len(str_):
            return out+str(char_cnt)+char
        while char == str_[i+char_cnt]:
            char_cnt += 1
            if i+char_cnt == len(str_):
                return out+str(char_cnt)+char
        i += char_cnt
        out += str(char_cnt) + char


def part_1(input_data):
    out = input_data
    for i in range(40):
        out = look_and_say(out)
    return len(out)


def part_2(input_data):
    out = input_data
    for i in range(50):
        out = look_and_say(out)
    return len(out)


if __name__ == "__main__":

    from aoc.initialize_day import load_input
    data = load_input(__file__)
    print("Part 1:", part_1(data))
    print("Part 2:", part_2(data))
