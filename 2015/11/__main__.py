import string
from pathlib import Path


alphabet = string.ascii_lowercase


def next_char(char):
    return chr((ord(char) - ord('a') + 1) % 26 + ord('a'))


def validation_rule_1(psw):
    for i in range(len(psw)-2):
        if psw[i:i+3] in alphabet:
            return True
    return False


def validation_rule_2(psw):
    return not any([chr_ in psw for chr_ in 'iol'])


def validation_rule_3(psw):
    cnt = 0
    for i in range(len(psw)-1):
        if psw[i] == psw[i+1]:
            cnt += 1
        if cnt == 2:
            return True
    return False


def validate_psw(psw):
    return validation_rule_1(psw) & validation_rule_2(psw) & validation_rule_3(psw)


def test_validate_psw():
    assert not validate_psw("hijklmmn")
    assert not validate_psw("abbceffg")
    assert not validate_psw("abbcegjk")


def increment_psw(psw):
    for i in range(len(psw)-1, 0, -1):
        char = psw[i]
        if char != 'z':
            psw[i] = next_char(char)
            psw[i+1:-1] = "a" * (len(psw) - i)
    raise Exception(f"Impossible to increment password")


def part_1(input_data):
    return increment_psw(input_data)


def part_2(input_data):
    pass


if __name__ == "__main__":
    with (Path(__file__).parent / "input.txt").open("r") as f:
        data = f.read()

    print("Part 1:", part_1(data))
    print("Part 2:", part_2(data))
