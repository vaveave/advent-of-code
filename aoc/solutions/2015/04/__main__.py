import hashlib

from aoc.cli.utils import load_input


def mine_adventcoin(secret_key, n_zeros):
    number = 1
    while True:
        to_be_hashed = f"{secret_key}{number}".encode("utf-8")
        hash_hex = hashlib.md5(to_be_hashed).hexdigest()
        if hash_hex[:n_zeros] == "0" * n_zeros:
            return number
        number += 1


def part_1(input_data):
    return str(mine_adventcoin(input_data, 5))


def part_2(input_data):
    return str(mine_adventcoin(input_data, 6))


def main():
    data = load_input(__file__)
    print("Part 1:", part_1(data))
    print("Part 2:", part_2(data))


if __name__ == "__main__":
    main()
