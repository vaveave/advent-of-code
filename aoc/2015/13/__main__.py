import re
import itertools


def read_input(input_data):
    first_name_pattern = re.compile(r"^([\w\-]+)")
    last_name_pattern = re.compile(r"\b(\w+).$")
    score_pattern = re.compile(r"\d+")
    return {
        (first_name_pattern.findall(x)[0], last_name_pattern.findall(x)[0]):
            int(score_pattern.findall(x)[0]) * (-1 if "lose" in x else 1) for x in input_data.splitlines()
    }


class AttendeeCombination:
    def __init__(self, names: tuple, scores):
        self.names = names
        self.scores = scores
        self.len = len(names)
        self.normalized_names = min(
            names[k:] + names[:k] for k in range(len(names))
        )

    def __eq__(self, other):
        if isinstance(other, AttendeeCombination):
            return self.normalized_names == other.normalized_names
        return False

    def __hash__(self):
        return hash(self.normalized_names)

    def compute_score(self):
        pairs = (
            [(self.names[k], self.names[k+1]) for k in range(self.len-1)]
            + [(self.names[k+1], self.names[k]) for k in range(self.len-1)]
            + [(self.names[self.len-1], self.names[0])]
            + [(self.names[0], self.names[self.len-1])]
        )
        scores = [self.scores[pair] for pair in pairs]
        return sum(scores)


def part_1(input_data, neutral_guest=False):
    attendees = list(set().union(*[{k[0]} for k in input_data.keys()]))
    if neutral_guest:
        for attendee in attendees:
            input_data[("Guest", attendee)] = 0
            input_data[(attendee, "Guest")] = 0
        attendees.append("Guest")
    permute_attendees = [AttendeeCombination(k, input_data) for k in list(itertools.permutations(attendees))]
    permute_attendees_set = set(permute_attendees)
    return max([attendee_list.compute_score() for attendee_list in permute_attendees_set])


def part_2(input_data):
    return part_1(input_data, neutral_guest=True)


if __name__ == "__main__":

    from aoc.initialize_day import load_input
    data = load_input(__file__)
    print("Part 1:", part_1(read_input(data)))
    print("Part 2:", part_2(read_input(data)))
