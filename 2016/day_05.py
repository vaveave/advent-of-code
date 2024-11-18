import hashlib
from pathlib import Path


def part1(input_data):
    print("Running part 1...")
    index = 0
    password = ""
    while (len(password) <= 7):
        door_id_plus_index = input_data + str(index)
        md5_hash = hashlib.md5(door_id_plus_index.encode()).hexdigest()
        if md5_hash[:5] == "00000":
            password += md5_hash[5]
        index += 1
        if index % 1e5 == 0:
            print(f"Total iterations: {str(index)}")
    return password


def part2(input_data):
    index = 0
    password = ["_"]*8
    len_password = 0
    while (len_password <= 7):
        door_id_plus_index = input_data + str(index)
        md5_hash = hashlib.md5(door_id_plus_index.encode()).hexdigest()
        if md5_hash[:5] == "00000":
            print(f"New possible hash: {md5_hash}")
            ind = md5_hash[5]
            possible_char = md5_hash[6]
            if ind.isdigit():
                if  int(ind) <= 7 and password[int(ind)] == "_":
                    password[int(ind)] = possible_char
                    len_password += 1
                    print(f"Hash is valid! Updated password: {''.join(password)}")
                else:
                    print("Hash is not valid.")
            else:
                print("Hash not valid.")
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

    print("Part 1:", part1(data))
    print("Part 2:", part2(data))
