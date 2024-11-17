import hashlib
from pathlib import Path


def part1(input_data):
    max_iter = 1e10
    index = 0
    password = ""
    while (len(password) <= 7) and (index <= max_iter):
        door_id_plus_index = input_data + str(index)
        md5_hash = hashlib.md5(door_id_plus_index.encode()).hexdigest()
        if md5_hash[:5] == "00000":
            password += md5_hash[5]
        index += 1
    if len(password) <= 7:
        return f"password not found after {str(index)} iterations!"
    else:
        return password


def part2(input_data):
    max_iter = 1e10
    index = 0
    password = [""]*8
    len_password = 0
    while (len_password <= 7) and (index <= max_iter):
        door_id_plus_index = input_data + str(index)
        md5_hash = hashlib.md5(door_id_plus_index.encode()).hexdigest()
        if md5_hash[:5] == "00000":
            ind = md5_hash[5]
            possible_char = md5_hash[6]
            if ind in "01234567" and password[int(ind)] == "":
                password[int(ind)] = possible_char
                len_password += 1
            print(md5_hash)
            print(password)
            print(len_password)
        index += 1
    if len(password) <= 7:
        return f"password not found after {str(index)} iterations!"
    else:
        return "".join(password)


if __name__ == "__main__":
    # Get the input file path and read the input data
    input_file = Path(__file__).parent / f"day_05_input.txt"
    with open(input_file) as f:
        data = f.read().strip()

    # print("Part 1:", part1(data))
    print("Part 2:", part2(data))
