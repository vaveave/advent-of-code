import string

from aoc.cli.utils import load_input


alphabet = string.ascii_lowercase


def next_char(char):
    return alphabet[(alphabet.find(char) + 1) % 26]


def validation_rule_1(psw):
    for i in range(len(psw) - 2):
        if psw[i : i + 3] in alphabet:
            return True
    return False


def validation_rule_2(psw):
    return not any([chr_ in psw for chr_ in "iol"])


def validation_rule_3(psw):
    counter, char = 0, ""
    for i in range(len(psw) - 1):
        if (psw[i] == psw[i + 1]) & (psw[i] != char):
            counter += 1
            char = psw[i]
        if counter == 2:
            return True
    return False


def validate_psw(psw):
    return validation_rule_1(psw) & validation_rule_2(psw) & validation_rule_3(psw)


def test_validate_psw():
    assert not validate_psw("hijklmmn")
    assert not validate_psw("abbceffg")
    assert not validate_psw("abbcegjk")


def increment_psw(password):
    for i in range(len(password) - 1, 0, -1):
        char = password[i]
        if char != "z":
            return password[0:i] + next_char(char) + ("a" * (len(password) - i - 1))
    raise Exception("Impossible to increment password")


def part_1(password):
    # Brute force approach to find next valid password
    valid_password = False
    while not valid_password:
        password = increment_psw(password)
        valid_password = validate_psw(password)
    return password


def main():
    data = load_input(__file__)
    test_validate_psw()
    next_santa_password = part_1(data)
    print("Part 1:", next_santa_password)
    print("Part 2:", part_1(next_santa_password))


if __name__ == "__main__":
    main()
