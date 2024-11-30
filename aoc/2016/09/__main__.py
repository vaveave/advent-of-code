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


def iterate_decompression(string, length=0, repeat=1):
    index = string.find("(")
    if index == -1:
        return "", repeat * (length+len(string))
    elif index != 0:
        length += index
        string = string[index:]
    match = re.match(r"\((\d+)x(\d+)\)", string)
    x, y = match.groups()
    sub_ind = len(x)+len(y)+3    # add 3 spaces for "(", ")" and "," characters
    iterate_decompression(
        string[sub_ind:sub_ind+int(x)],
        length=length,
        repeat=repeat*int(y)
    )



def part_2(input_data):
    return(iterate_decompression(input_data)[1])


test_data_1 = {
    "ADVENT": "ADVENT",
    "A(1x5)BC": "ABBBBBC",
    "(3x3)XYZ": "XYZXYZXYZ",
    "A(2x2)BCD(2x2)EFG": "ABCBCDEFEFG",
    "(6x1)(1x3)A": "(1x3)A",
    "X(8x2)(3x3)ABCY": "X(3x3)ABC(3x3)ABCY"
}

test_data_2 = {
    "X(8x2)(3x3)ABCY": len("XABCABCABCABCABCABCY"),
    "(27x12)(20x12)(13x14)(7x10)(1x12)A": 241920,
    "(25x3)(3x3)ABC(2x3)XY(5x2)PQRSTX(18x9)(3x2)TWO(5x7)SEVEN": 445
}


def test_decompress_string():
    for key, value in test_data_1.items():
        assert decompress_string(key) == value


def test_iterate_decompression():
    for key, value in test_data_2.items():
        assert iterate_decompression(key)[1] == value


if __name__ == "__main__":
    with (Path(__file__).parent / "input.txt").open("r") as f:
        data = f.read()

    test_decompress_string()
    # test_iterate_decompression()

    print("Part 1:", part_1(data))
    print("Part 2:", part_2("X(8x2)(3x3)ABCY"))
