import re


def read_input(input_data):
    """
    Parses input into a dictionary of {name: {"weight": int, "children": [str]}}.
    """
    pattern = re.compile(r"(\w+) \((\d+)\)(?: -> (.+))?")
    tree = {}
    for line in input_data.splitlines():
        name, weight, children = pattern.match(line).groups()
        tree[name] = {
            "weight": int(weight),
            "children": children.split(", ") if children else []
        }
    return tree


def calc_branch_length(node, depth, tree):
    """
    Recursively calculates total branch length from node.
    """
    return depth + sum(calc_branch_length(child, depth + 1, tree) for child in tree[node]["children"])


def part_1(tree):
    """
    Returns the node with the longest total branch length.
    """
    for node in tree:
        tree[node]["branch_length"] = calc_branch_length(node, 1, tree)
    return max(tree.items(), key=lambda item: item[1]["branch_length"])[0]


def calc_total_weight(node, tree):
    """
    Recursively calculates the total weight of a node including its children.
    """
    total = tree[node]["weight"]
    for child in tree[node]["children"]:
        total += calc_total_weight(child, tree)
    return total


def part_2(tree, root):
    """
    Identifies imbalance in child weights and returns adjusted weight for correction.
    """
    weights = {
        child: calc_total_weight(child, tree)
        for child in tree[root]["children"]
    }
    print(weights)
    weights_error = max(weights.values()) - min(weights.values())
    if weights_error == 0:
        return None
    next_step = max(weights, key=weights.get)
    next_weights = part_2(tree, next_step)
    if not next_weights:
        return tree[next_step]["weight"] - weights_error
    else:
        return next_weights


if __name__ == "__main__":
    from aoc.initialize_day import load_input

    input_text = load_input(__file__)
    parsed_tree = read_input(input_text)
    root = part_1(parsed_tree)
    print("Part 1:", root)
    print("Part 2:", part_2(read_input(input_text), root))
