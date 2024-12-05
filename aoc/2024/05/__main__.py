
def read_input(input_data):
    rules, updates = [line.splitlines() for line in input_data.split("\n\n")]
    rules = [tuple(map(int, line.split("|"))) for line in rules]
    updates = [list(map(int, line.split(","))) for line in updates]
    return {"rules": rules, "updates": updates}


def is_update_valid(update, rules):
    if len(update) == 1:
        return True
    for page in update[1:]:
        if not (update[0], page) in rules:
            return False
    return is_update_valid(update[1:], rules)


def part_1(input_data):
    sum_central_pages = 0
    for update in input_data["updates"]:
        if is_update_valid(update, input_data["rules"]):
            sum_central_pages += update[len(update) // 2]
    return sum_central_pages


def part_2(input_data):
    rules = input_data["rules"]
    sum_central_pages = 0

    class Page:
        def __init__(self, x: int):
            self.value = x

        def __gt__(self, other):
            if (self.value, other.value) in rules:
                return True
            return False

    for update in input_data["updates"]:
        if not is_update_valid(update, input_data["rules"]):
            update_new = [Page(i) for i in update]
            update_new.sort()
            sum_central_pages += update_new[len(update) // 2].value
    return sum_central_pages


if __name__ == "__main__":

    from aoc.initialize_day import load_input
    data = load_input(__file__)
    print("Part 1:", part_1(read_input(data)))
    print("Part 2:", part_2(read_input(data)))
