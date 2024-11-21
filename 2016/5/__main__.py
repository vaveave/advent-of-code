import hashlib
from pathlib import Path


def part_1(input_data):
    index = 0
    password = ""
    while len(password) <= 7:
        door_id_plus_index = input_data + str(index)
        md5_hash = hashlib.md5(door_id_plus_index.encode()).hexdigest()
        if md5_hash[:5] == "00000":
            password += md5_hash[5]
            print(f"Character {md5_hash[5]} added! Updated password: {password}")
        index += 1
    return password


def part_2(input_data):
    index = 0
    password = ["_"] * 8
    len_password = 0
    while len_password <= 7:
        door_id_plus_index = input_data + str(index)
        md5_hash = hashlib.md5(door_id_plus_index.encode()).hexdigest()
        if md5_hash[:5] == "00000":
            print(f"New possible hash: {md5_hash}")
            pos = md5_hash[5]
            possible_char = md5_hash[6]
            if pos.isdigit():
                pos = int(pos)
                if pos <= 7 and password[pos] == "_":
                    password[pos] = possible_char
                    len_password += 1
                    print(f"Hash is valid! Updated password: {''.join(password)}")
                else:
                    print("Hash is not valid.")
            else:
                print("Hash not valid.")
        index += 1
    return "".join(password)


if __name__ == "__main__":
    with (Path(__file__).parent / "input.txt").open("r") as f:
        data = f.read()

    print("Part 1:", part_1(data))
    print("Part 2:", part_2(data))
