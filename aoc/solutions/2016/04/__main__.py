import re
from collections import Counter, OrderedDict

from aoc.cli.utils import load_input


def read_input(data):
    return data

def part_1(data):
    rooms_list = data.splitlines()
    pattern = r"([a-z\-]+)-(\d+)\[([a-z]+)\]"
    real_rooms_counter = 0
    for room in rooms_list:
        matched_pattern = re.match(pattern, room)
        decoded_room = [
            matched_pattern.group(1).replace("-", ""),
            int(matched_pattern.group(2)),
            matched_pattern.group(3),
        ]
        char_count = Counter(decoded_room[0])
        sorted_string = "".join(
            sorted(decoded_room[0], key=lambda x: (-char_count[x], x))
        )
        if "".join(list(OrderedDict.fromkeys(sorted_string)))[:5] == decoded_room[2]:
            real_rooms_counter += decoded_room[1]
    return str(real_rooms_counter)

def decrypt_room_name(room_name, key):
    decrypted_name = ""
    for ch in room_name:
        if ch != "-":
            decrypted_name += chr((ord(ch) - 97 + key) % 26 + 97)
        else:
            decrypted_name += "-"
    return decrypted_name

def part_2(data):
    rooms_list = data.splitlines()
    pattern = r"([a-z\-]+)-(\d+)\[([a-z]+)\]"
    output = []
    for room in rooms_list:
        matched_pattern = re.match(pattern, room)
        name = matched_pattern.group(1)
        key = int(matched_pattern.group(2))
        decrypted = decrypt_room_name(name, key)
        if "northpole" in decrypted:
            output.append((decrypted, key))
    return output[0][1] if output else None

def main():
    data = load_input(__file__)
    print("Part 1:", part_1(read_input(data)))
    print("Part 2:", part_2(read_input(data)))

if __name__ == "__main__":
    main()
