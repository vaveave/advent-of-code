import re

from aoc.cli.utils import load_input


def read_input(data):
    return data

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

def part_1(data):
    return len(decompress_string(data))

def part_2(data):
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
                    length += repeat * recursive_decompress(subsegment)
                    i += segment_length
        return length
    return recursive_decompress(data)

def main():
    data = load_input(__file__)
    print("Part 1:", part_1(read_input(data)))
    print("Part 2:", part_2(read_input(data)))

if __name__ == "__main__":
    main()
