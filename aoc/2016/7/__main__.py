import re
from pathlib import Path


def is_abba(string):
    if (string[0] == string[3]) and (string[1] == string[2]) and (string[0] != string[2]):
        return True
    return False


def contain_abbas(string):
    for i in range(4, len(string)+1):
        if is_abba(string[i-4:i]):
            return True
    return False

def split_ip_components(ip):
    ip_components = re.split(r"[\[\]]+", ip)
    return (ip_components[0::2], ip_components[1::2])


def support_tls(ip):
    supernet_sequences, hypernet_sequences = split_ip_components(ip)
    if not any(map(contain_abbas, hypernet_sequences)) and any(map(contain_abbas, supernet_sequences)):
        return True
    return False

def support_ssl(ip):
    pass

def part_1(input_data):
    input_data = input_data.splitlines()
    return sum(1 for ip in input_data if support_tls(ip))


def part_2(input_data):
    input_data = input_data.splitlines()
    return sum(1 for ip in input_data if support_ssl(ip))


if __name__ == "__main__":
    with (Path(__file__).parent / "input.txt").open("r") as f:
        data = f.read()

    print("Part 1:", part_1(data))
    print("Part 2:", part_2(data))
