import re


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
        if is_abba(net[i - 4:i]):
            return True
    return False


def split_ip_components(ip):
    ip_components = re.split(r"[\[\]]+", ip)
    return ip_components[0::2], ip_components[1::2]


def support_tls(ip):
    supernets, hypernets = split_ip_components(ip)
    if (
        not any(map(contain_abbas, hypernets))
        and any(map(contain_abbas, supernets))
    ):
        return True
    return False


def support_ssl(ip):
    supernets, hypernets = split_ip_components(ip)
    for supernet in supernets:
        for i in range(3, len(supernet) + 1):
            segment = supernet[i - 3:i]
            if is_aba(segment):
                if any(is_bab(segment, hypernet) for hypernet in hypernets):
                    return True
    return False


def part_1(input_data):
    input_data = input_data.splitlines()
    return sum(1 for ip in input_data if support_tls(ip))


def part_2(input_data):
    input_data = input_data.splitlines()
    return sum(1 for ip in input_data if support_ssl(ip))


if __name__ == "__main__":

    from aoc.initialize_day import load_input
    data = load_input(__file__)
    print("Part 1:", part_1(data))
    print("Part 2:", part_2(data))
