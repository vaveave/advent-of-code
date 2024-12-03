import hashlib
from pathlib import Path


def mine_adventcoin(secret_key, n_zeros):
    number = 1
    while True:
        to_be_hashed = f"{secret_key}{number}".encode('utf-8')
        hash_hex = hashlib.md5(to_be_hashed).hexdigest()
        if hash_hex[:n_zeros] == '0'*n_zeros:
            return number
        number += 1


def part_1(input_data):
    return str(mine_adventcoin(input_data, 5))


def part_2(input_data):
    return str(mine_adventcoin(input_data, 6))


if __name__ == "__main__":
    
    from aoc.initialize_day import load_input

    folder = Path(__file__).parent
    try:
        year = int(folder.parts[-2])
        day = int(folder.parts[-1])
    except ValueError:
        print("Failed to determine year and day from folder structure.")
        raise SystemExit(1)

    data = load_input(year, day)

    print("Part 1:", part_1(data))
    print("Part 2:", part_2(data))
