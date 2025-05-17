import re
import itertools


def read_input(input_data):
    pattern = re.compile(
        r"^([\w\-]+) would (gain|lose) (\d+) happiness units by sitting next to ([\w\-]+)\."
    )
    out = {}
    for line in input_data.splitlines():
        match = pattern.findall(line)[0]
        out.update(
            {(match[0], match[3]): int(match[2]) * (1 if match[1] == "gain" else -1)}
        )
    return out


class AttendeesCombination:
    def __init__(self, names: tuple, scores):
        self.names = names
        self.scores = scores
        self.len = len(names)
        self.normalized_names = min(names[k:] + names[:k] for k in range(len(names)))

    def __eq__(self, other):
        return self.normalized_names == other.normalized_names

    def __hash__(self):
        return hash(self.normalized_names)

    def compute_score(self):
        pairs = [
            (self.names[k], self.names[(k + 1) % self.len]) for k in range(self.len)
        ] + [(self.names[(k + 1) % self.len], self.names[k]) for k in range(self.len)]
        return sum(self.scores[pair] for pair in pairs)


def part_1(input_data, neutral_guest=False):
    attendees = {k[0] for k in input_data.keys()}
    if neutral_guest:
        input_data.update({("Guest", a): 0 for a in attendees})
        input_data.update({(a, "Guest"): 0 for a in attendees})
        attendees.add("Guest")
    combinations = {
        AttendeesCombination(k, input_data)
        for k in list(itertools.permutations(attendees))
    }
    return max([combo.compute_score() for combo in combinations])


def part_2(input_data):
    return part_1(input_data, neutral_guest=True)


if __name__ == "__main__":
    from aoc.initialize_day import load_input

    data = load_input(__file__)
    print("Part 1:", part_1(read_input(data)))
    print("Part 2:", part_2(read_input(data)))
