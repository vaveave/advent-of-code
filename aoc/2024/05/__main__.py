def read_input(input_data):
    rules, updates = [line.splitlines() for line in input_data.split("\n\n")]
    rules = [tuple(map(int, line.split("|"))) for line in rules]
    updates = [list(map(int, line.split(","))) for line in updates]
    return {"rules": rules, "updates": updates}


def is_update_valid(update, rules):
    if len(update) == 1:
        return True
    for page in update[1:]:
        if (update[0], page) not in rules:
            return False
    return is_update_valid(update[1:], rules)


def part_1(input_data):
    sum_central_pages = 0
    valid_updates, invalid_updates = [], []
    for update in input_data["updates"]:
        if is_update_valid(update, input_data["rules"]):
            valid_updates.append(update)
            sum_central_pages += update[len(update) // 2]
        else:
            invalid_updates.append(update)
    return sum_central_pages, valid_updates, invalid_updates


def part_2(rules, invalid_updates):
    class Page:
        def __init__(self, x: int):
            self.value = x

        def __gt__(self, other):
            if (self.value, other.value) in rules:
                return True
            return False

    sum_central_pages = 0
    for update in invalid_updates:
        update_new = [Page(i) for i in update]
        update_new.sort()
        sum_central_pages += update_new[len(update) // 2].value
    return sum_central_pages


if __name__ == "__main__":
    from aoc.initialize_day import load_input

    data = read_input(load_input(__file__))
    result, _, invalid_upd = part_1(data)
    print("Part 1:", result)
    print("Part 2:", part_2(data["rules"], invalid_upd))
