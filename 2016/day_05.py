import hashlib
from pathlib import Path
import time


def part1(input_data):
    print("Running part 1...")
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


def part2(input_data):
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
    # Get the input file path and read the input data
    input_file = Path(__file__).parent / f"day_05_input.txt"
    with open(input_file) as f:
        data = f.read().strip()

    # Timing part 1
    start_time = time.time()
    result_part1 = part1(data)
    end_time = time.time()
    print(f"Part 1: {result_part1} (Time taken: {end_time - start_time:.2f} seconds)")

    # Timing part 2
    start_time = time.time()
    result_part2 = part2(data)
    end_time = time.time()
    print(f"Part 2: {result_part2} (Time taken: {end_time - start_time:.2f} seconds)")
