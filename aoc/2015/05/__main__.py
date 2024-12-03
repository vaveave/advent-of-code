from pathlib import Path


def contains_3_vowels(str_: str):
    vowels = ['a', 'e', 'i', 'o', 'u']
    vowels_counter = 0
    for char_ in str_:
        if char_ in vowels:
            vowels_counter += 1
        if vowels_counter >= 3:
            return True
    return False


def contains_duplicates(str_: str):
    for i in range(str_.__len__()-1):
        if str_[i].isalpha() and str_[i] == str_[i+1]:
            return True
    return False


def contains_naughty_strings(str_: str):
    naughty_strings = ['ab', 'cd', 'pq', 'xy']
    for naughty_string in naughty_strings:
        if naughty_string in str_:
            return True
    return False


def is_nice_pt1(str_: str):
    if contains_3_vowels(str_) and contains_duplicates(str_) and not contains_naughty_strings(str_):
        return True
    return False


def has_pair_twice(str_: str):
    for i in range(len(str_)):
        if str_[i:i+2] in str_[i+2:]:
            return True
    return False


def has_repeating_letter(str_: str):
    for i in range(len(str_)-2):
        if str_[i] == str_[i+2]:
            return True
    return False


def is_nice_pt2(str_: str):
    if has_pair_twice(str_) and has_repeating_letter(str_):
        return True
    return False


def part_1(input_data):
    return str(sum([is_nice_pt1(str_) for str_ in input_data.splitlines()]))


def part_2(input_data):
    return str(sum([is_nice_pt2(str_) for str_ in input_data.splitlines()]))


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
