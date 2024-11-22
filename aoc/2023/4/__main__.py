import re
from pathlib import Path


def process_card(card_str):
    card_str_no_multi_spaces = re.sub(r'\s+', ' ', card_str)
    separators = [":", "|"]
    pattern = "|".join(map(re.escape, separators))
    card_to_list = [re.sub(r'\s+', ' ', part).strip().split(" ") for part in re.split(pattern, card_str_no_multi_spaces)]
    return {"_id": card_to_list[0][1], "winners": card_to_list[1], "card_numbers": card_to_list[2], "card_count": 1}


def find_card_winners(card_dict):
    return [number for number in card_dict["card_numbers"] if number in card_dict["winners"]]


def evaluate_card_points(card_dict):
    winners_number = len(find_card_winners(card_dict))
    if winners_number == 0:
        return 0
    else:
        return 2**(winners_number-1)


def count_all_points(input_str):
    input_rows = input_str.split("\n")
    processed_cards = [process_card(card_str) for card_str in input_rows]
    return sum([evaluate_card_points(processed_card) for processed_card in processed_cards])


def part_1(input_data):
    return count_all_points(input_data)


def count_all_scratchcards(input_str):
    cards = [process_card(row) for row in input_str.split("\n")]
    for i, card in enumerate(cards):
        card_winners = len(find_card_winners(card))
        for j in range(i+1, min(i+card_winners+1, len(cards))):
            cards[j]["card_count"] += card["card_count"]
    return sum([card["card_count"] for card in cards])


def part_2(input_data):
    return count_all_scratchcards(input_data)


if __name__ == "__main__":
    with (Path(__file__).parent / "input.txt").open("r") as f:
        data = f.read()

    print("Part 1:", part_1(data))
    print("Part 2:", part_2(data))
