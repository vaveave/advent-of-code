import re


def decompress_string(string):
    decompressed = []
    i = 0
    while i < len(string):
        if string[i] != "(":
            decompressed.append(string[i])
            i += 1
        else:
            match = re.match(r"\((\d+)x(\d+)\)", string[i:])
            if match:
                length, repeat = map(int, match.groups())
                marker_length = match.end()
                i += marker_length
                decompressed.append(string[i : i + length] * repeat)
                i += length
    return "".join(decompressed)


def part_1(input_data):
    return len(decompress_string(input_data))


def part_2(input_data):
    def recursive_decompress(string):
        length = 0
        i = 0
        while i < len(string):
            if string[i] != "(":
                length += 1
                i += 1
            else:
                match = re.match(r"\((\d+)x(\d+)\)", string[i:])
                if match:
                    marker_length = match.end()
                    segment_length, repeat = map(int, match.groups())
                    i += marker_length
                    subsegment = string[i : i + segment_length]
                    length += recursive_decompress(subsegment) * repeat
                    i += segment_length
        return length

    return recursive_decompress(input_data)


# Test cases
test_data_1 = {
    "ADVENT": "ADVENT",
    "A(1x5)BC": "ABBBBBC",
    "(3x3)XYZ": "XYZXYZXYZ",
    "A(2x2)BCD(2x2)EFG": "ABCBCDEFEFG",
    "(6x1)(1x3)A": "(1x3)A",
    "X(8x2)(3x3)ABCY": "X(3x3)ABC(3x3)ABCY",
}

test_data_2 = {
    "X(8x2)(3x3)ABCY": len("XABCABCABCABCABCABCY"),
    "(27x12)(20x12)(13x14)(7x10)(1x12)A": 241920,
    "(25x3)(3x3)ABC(2x3)XY(5x2)PQRSTX(18x9)(3x2)TWO(5x7)SEVEN": 445,
}


def test_decompress_string():
    for key, expected in test_data_1.items():
        assert decompress_string(key) == expected


def test_recursive_decompression():
    for key, expected in test_data_2.items():
        assert part_2(key) == expected


if __name__ == "__main__":
    from aoc.initialize_day import load_input

    data = load_input(__file__)

    test_decompress_string()
    test_recursive_decompression()

    print("Part 1:", part_1(data))
    print("Part 2:", part_2(data))
