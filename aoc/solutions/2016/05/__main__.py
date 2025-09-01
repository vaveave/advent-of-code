import hashlib

from aoc.cli.utils import load_input


def read_input(data):
    return data


def part_1(data):
    index = 0
    password = ""
    while len(password) <= 7:
        door_id_plus_index = data + str(index)
        md5_hash = hashlib.md5(door_id_plus_index.encode()).hexdigest()
        if md5_hash[:5] == "00000":
            password += md5_hash[5]
        index += 1
    return password


def part_2(data):
    index = 0
    password = ["_"] * 8
    len_password = 0
    while len_password <= 7:
        door_id_plus_index = data + str(index)
        md5_hash = hashlib.md5(door_id_plus_index.encode()).hexdigest()
        if md5_hash[:5] == "00000":
            pos = md5_hash[5]
            possible_char = md5_hash[6]
            if pos.isdigit():
                pos = int(pos)
                if pos <= 7 and password[pos] == "_":
                    password[pos] = possible_char
                    len_password += 1
        index += 1
    return "".join(password)


def main():
    data = load_input(__file__)
    print("Part 1:", part_1(read_input(data)))
    print("Part 2:", part_2(read_input(data)))


if __name__ == "__main__":
    main()
