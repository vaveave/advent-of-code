import re

from aoc.cli.utils import load_input


def read_input(input_data):
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
    return depth + sum(calc_tree_depth(child, depth + 1, tree) for child in tree[node]["children"])


def find_root(tree):
    for node in tree:
        tree[node]["tree_depth"] = calc_tree_depth(node, 1, tree)
    return max(tree.items(), key=lambda item: item[1]["tree_depth"])[0]


def calc_total_weight(node, tree):
    total = tree[node]["weight"]
    for child in tree[node]["children"]:
        total += calc_total_weight(child, tree)
    return total


def find_imbalance(tree, root):
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


def part_1(data):
    tree = read_input(data)
    return find_root(tree)


def part_2(data):
    tree = read_input(data)
    root = find_root(tree)
    return find_imbalance(tree, root)


def main():
    data = load_input(__file__)
    print("Part 1:", part_1(data))
    print("Part 2:", part_2(data))


if __name__ == "__main__":
    main()
