from enum import Enum


def process_input(input_str):
    return list(map(lambda str_: [str_.split(" ")[0], int(str_.split(" ")[1])], input_str.split("\n")))


class CamelCardsHandType(Enum):
    HighCard = 1
    OnePair = 2
    TwoPairs = 3
    ThreeOfAKind = 4
    FullHouse = 5
    FourOfAKind = 6
    FiveOfAKind = 7


class Hand:
    def __init__(self, cards: str, bid: int, use_jokers: bool = False):
        self.cards = cards
        self.bid = bid
        self.use_jokers = use_jokers

    def __repr__(self):
        return f"Hand(cards='{self.cards}', bid={str(self.bid)})"

    @classmethod
    def from_string(cls, str_: str, use_jokers: bool = False):
        splitted_str = str_.split(" ")
        return cls(splitted_str[0], int(splitted_str[1]), use_jokers=use_jokers)

    @property
    def cards_order(self):
        return "AKQT98765432J" if self.use_jokers else "AKQJT98765432"

    @property
    def hand_type(self) -> CamelCardsHandType:
        to_be_checked = self.cards
        if self.use_jokers:
            if self.cards == "J"*5:
                return CamelCardsHandType.FiveOfAKind
            if "J" in self.cards:
                char_counts = {char: self.cards.count(char) for char in set(self.cards.replace("J", ""))}
                most_common_char = max(char_counts, key=char_counts.get)
                to_be_checked = self.cards.replace("J", most_common_char)
        char_count = {}
        for char in to_be_checked:
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1
        unique_counts = list(char_count.values())
        if 5 in unique_counts:
            return CamelCardsHandType.FiveOfAKind
        elif 4 in unique_counts:
            return CamelCardsHandType.FourOfAKind
        elif 3 in unique_counts and 2 in unique_counts:
            return CamelCardsHandType.FullHouse
        elif 3 in unique_counts:
            return CamelCardsHandType.ThreeOfAKind
        elif 2 in unique_counts and len(unique_counts) == 3:
            return CamelCardsHandType.TwoPairs
        elif 2 in unique_counts:
            return CamelCardsHandType.OnePair
        else:
            return CamelCardsHandType.HighCard

    def __gt__(self, other):
        for i in range(len(self.cards)):
            ind_1 = self.cards_order.find(self.cards[i])
            ind_2 = self.cards_order.find(other.cards[i])
            if ind_1 < ind_2:
                return True
            elif ind_1 > ind_2:
                return False
        # If all characters are equal, return False (cards are considered equal)
        return False


def sort_hands(hands):
    sorted_hands = []
    for type_ in CamelCardsHandType:
        hands_substr = [hand for hand in hands if hand.hand_type == type_]
        sorted_hands += sorted(hands_substr)
    return sorted_hands


def part_1(input_data):
    hands = [Hand.from_string(str_) for str_ in input_data.splitlines()]
    sorted_hands = sort_hands(hands)
    return str(sum([(i+1) * hand.bid for i, hand in enumerate(sorted_hands)]))


def part_2(input_data):
    hands = [Hand.from_string(str_, use_jokers=True) for str_ in input_data.splitlines()]
    sorted_hands = sort_hands(hands)
    return str(sum([(i+1) * hand.bid for i, hand in enumerate(sorted_hands)]))


if __name__ == "__main__":

    from aoc.initialize_day import load_input
    data = load_input(__file__)
    print("Part 1:", part_1(data))
    print("Part 2:", part_2(data))
