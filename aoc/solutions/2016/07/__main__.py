import re

from aoc.cli.utils import load_input


def read_input(data):
    return data


def is_abba(segment):
    if (
        (segment[0] == segment[3])
        and (segment[1] == segment[2])
        and (segment[0] != segment[2])
    ):
        return True
    return False


def is_aba(segment):
    if (segment[0] == segment[2]) and (segment[0] != segment[1]):
        return True
    return False


def is_bab(aba, hypernet):
    a, b = aba[0], aba[1]
    bab = f"{b}{a}{b}"
    return bab in hypernet


def contain_abbas(net):
    for i in range(4, len(net) + 1):
        if is_abba(net[i - 4 : i]):
            return True
    return False


def split_ip_components(ip):
    ip_components = re.split(r"[\[\]]+", ip)
    return ip_components[0::2], ip_components[1::2]


def support_tls(ip):
    supernets, hypernets = split_ip_components(ip)
    if not any(map(contain_abbas, hypernets)) and any(map(contain_abbas, supernets)):
        return True
    return False


def part_1(data):
    return sum(support_tls(ip) for ip in data.splitlines())


def support_ssl(ip):
    supernets, hypernets = split_ip_components(ip)
    abas = [net[i:i+3] for net in supernets for i in range(len(net)-2) if is_aba(net[i:i+3])]
    for aba in abas:
        for hypernet in hypernets:
            if is_bab(aba, hypernet):
                return True
    return False


def part_2(data):
    return sum(support_ssl(ip) for ip in data.splitlines())


def main():
    data = load_input(__file__)
    print("Part 1:", part_1(read_input(data)))
    print("Part 2:", part_2(read_input(data)))


if __name__ == "__main__":
    main()
