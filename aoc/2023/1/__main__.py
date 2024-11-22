from pathlib import Path


# Define a dictionary mapping string literals to digits
literals_to_digits = {
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9',
}


def rm_non_digits(str_):
    digits = "0123456789"
    return "".join([char for char in str_ if char in digits])


def first_last(str_):
    return str_[0] + str_[-1]


def calib_from_string(str_):
    return first_last(rm_non_digits(str_))


def first_str_digit(str_):
    for i in range(len(str_)):
        for digit in list(literals_to_digits)+list(literals_to_digits.values()):
            if str_[i:].startswith(digit):
                return literals_to_digits.get(digit, digit)
    raise ValueError(f"Input {str_} does not contain any digits")


def last_str_digit(str_):
    for i in range(len(str_), 0, -1):
        for digit in list(literals_to_digits)+list(literals_to_digits.values()):
            if str_[:i].endswith(digit):
                return literals_to_digits.get(digit, digit)
    raise ValueError(f"Input {str_} does not contain any digits")


def calib_from_string_with_replacement(str_):
    return first_str_digit(str_) + last_str_digit(str_)


def part_1(input_data):
    calibration_values = [
        int(calib_from_string(line_)) for line_ in input_data.splitlines()
    ]
    return str(sum(calibration_values))


def part_2(input_data):
    calibration_values = [
        int(calib_from_string_with_replacement(line_)) for line_ in input_data.splitlines()
    ]
    return str(sum(calibration_values))


if __name__ == "__main__":
    with (Path(__file__).parent / "input.txt").open("r") as f:
        data = f.read()

    print("Part 1:", part_1(data))
    print("Part 2:", part_2(data))
