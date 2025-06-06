import re


def read_input(input_data):
    # Regex to parse inputs as 'name (weight) -> [children]' into a dictionary
    # {'name': {'weight': int, 'children': [list of children names]}}
    pattern = re.compile(r'(\w+) \((\d+)\)(?: -> (.+))?')
    data = {}
    for line in input_data.splitlines():
        match = pattern.match(line)
        if match:
            name, weight, children = match.groups()
            data[name] = {
                'weight': int(weight),
                'children': children.split(', ') if children else []
            }
    return data


def calc_branch_length(node, depth, nodes_map):
    """
    Recursively calculates the total branch length starting from the given node.
    Each level of depth adds 1 to the branch length.
    """
    total_length = depth
    for child in nodes_map[node]['children']:
        total_length += calc_branch_length(child, depth + 1, nodes_map)
    return total_length
    

def part_1(nodes_map):
    """
    For each node, calculates its branch length and finds the node with the longest branch.
    Returns the name of the node with the maximum branch length.
    """
    for node in nodes_map:
        nodes_map[node]['branch_length'] = calc_branch_length(node, 1, nodes_map)
    # Find the node with the maximum branch length
    max_length_node = max(nodes_map.items(), key=lambda item: item[1]['branch_length'])
    return max_length_node[0]


def part_2(input_data):
    # Implement part 2 solution
    pass


if __name__ == "__main__":
    from aoc.initialize_day import load_input

    data = load_input(__file__)
    print("Part 1:", part_1(read_input(data)))
    print("Part 2:", part_2(read_input(data)))
