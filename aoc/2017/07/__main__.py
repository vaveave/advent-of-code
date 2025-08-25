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

def calc_tree_depth(node, depth, tree):
    """
    Recursively calculates total tree depth from node.
    """
    return depth + sum(calc_tree_depth(child, depth + 1, tree) for child in tree[node]["children"])

def find_root(tree):
    """
    Returns the node with the longest total tree depth.
    """
    for node in tree:
        tree[node]["tree_depth"] = calc_tree_depth(node, 1, tree)
    return max(tree.items(), key=lambda item: item[1]["tree_depth"])[0]

def calc_total_weight(node, tree):
    """
    Recursively calculates the total weight of a node including its children.
    """
    total = tree[node]["weight"]
    for child in tree[node]["children"]:
        total += calc_total_weight(child, tree)
    return total

def find_imbalance(tree, root):
    """
    Identifies imbalance in child weights and returns adjusted weight for correction.
    """
    child_weights = {child: calc_total_weight(child, tree) for child in tree[root]["children"]}
    weight_difference = max(child_weights.values()) - min(child_weights.values())
    if weight_difference == 0:
        return None
    unbalanced_child = max(child_weights, key=child_weights.get)
    correction = find_imbalance(tree, unbalanced_child)
    if not correction:
        return tree[unbalanced_child]["weight"] - weight_difference
    else:
        return correction

if __name__ == "__main__":
    from aoc.initialize_day import load_input

    input_text = load_input(__file__)
    parsed_tree = read_input(input_text)
    root = find_root(parsed_tree)
    print("Part 1:", root)
    print("Part 2:", find_imbalance(parsed_tree, root))