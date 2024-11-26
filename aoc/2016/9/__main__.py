import re
from pathlib import Path


def decompress_string(string):
    decompressed_string = []
    index = 0
    while index < len(string):
        if string[index] != "(":
            decompressed_string.append(string[index])
            index += 1
        else:
            if match := re.match(r"\((\d+)x(\d+)\)", string[index:]):
                x, y = match.groups()
                index += len(x)+len(y)+3    # add 3 spaces for "(", ")" and "," characters
                decompressed_string.append(string[index:index+int(x)]*int(y))
                index += int(x)
    return "".join(decompressed_string)


def part_1(input_data):
    return len(decompress_string(input_data))


def part_2(input_data):
    pass


test_data_1 = {
    "ADVENT": "ADVENT",
    "A(1x5)BC": "ABBBBBC",
    "(3x3)XYZ": "XYZXYZXYZ",
    "A(2x2)BCD(2x2)EFG": "ABCBCDEFEFG",
    "(6x1)(1x3)A": "(1x3)A",
    "X(8x2)(3x3)ABCY": "X(3x3)ABC(3x3)ABCY"
}


def test_decompress_string():
    for key, value in test_data_1.items():
        assert decompress_string(key) == value


if __name__ == "__main__":
    with (Path(__file__).parent / "input.txt").open("r") as f:
        data = f.read()

    test_decompress_string()

    print("Part 1:", part_1(data))
    print("Part 2:", part_2(data))
