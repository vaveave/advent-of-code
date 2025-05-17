from itertools import permutations


def process_input(input_data):
    rows = input_data.splitlines()
    arches = dict()
    nodes = set()
    for row in rows:
        split_1 = row.split(" = ")
        split_2 = split_1[0].split(" to ")
        arches[tuple(split_2)] = int(split_1[1])
        nodes = nodes.union(set(split_2))
    return arches, nodes


def part_1(input_data):
    arches, nodes = process_input(input_data)
    n_nodes = len(nodes)
    paths = {path: None for path in permutations(nodes, n_nodes)}
    for path in paths.keys():
        path_len = 0
        for i in range(n_nodes - 1):
            try:
                path_len += arches[path[i : i + 2]]
            except KeyError:
                path_len += arches[path[i : i + 2][::-1]]
        paths[path] = path_len
    return str(paths[min(paths, key=paths.get)])


def part_2(input_data):
    arches, nodes = process_input(input_data)
    n_nodes = len(nodes)
    paths = {path: None for path in permutations(nodes, n_nodes)}
    for path in paths.keys():
        path_len = 0
        for i in range(n_nodes - 1):
            try:
                path_len += arches[path[i : i + 2]]
            except KeyError:
                path_len += arches[path[i : i + 2][::-1]]
        paths[path] = path_len
    return str(paths[max(paths, key=paths.get)])


if __name__ == "__main__":
    from aoc.initialize_day import load_input

    data = load_input(__file__)
    print("Part 1:", part_1(data))
    print("Part 2:", part_2(data))
