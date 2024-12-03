import re
from pathlib import Path


color_max_cnt = {
        "green": 13,
        "blue": 14,
        "red": 12
    }


def process_game(game_string):
    game_splitted = re.split(r'[;:,]\s*', game_string)
    game_id = int(game_splitted[0].split(" ")[1])
    game_results = game_splitted[1:]
    return game_id, game_results


def is_game_valid(game_results):
    colour_count = {
        "green": 0,
        "blue": 0,
        "red": 0
    }
    for result in game_results:
        splitted_result = result.split(" ")
        color = splitted_result[1]
        color_cnt = int(splitted_result[0])
        if color_cnt > color_max_cnt[color]:
            return False
        else:
            colour_count[color] = max(colour_count[color], color_cnt)
    return True


def part_1(input_data):
    i = 0
    for game_string in input_data.splitlines():
        id_, game_results = process_game(game_string)
        if is_game_valid(game_results):
            i += id_
    return str(i)


def cubes_needed_by_game(game_results):
    game_colors = {
        "green": 0,
        "blue": 0,
        "red": 0
    }
    for result in game_results:
        splitted_result = result.split(" ")
        color = splitted_result[1]
        color_cnt = int(splitted_result[0])
        if color_cnt > game_colors[color]:
            game_colors[color] = color_cnt
    return game_colors


def power_minimum_set(game_string):
    game_results = process_game(game_string)[1]
    cubes_needed = cubes_needed_by_game(game_results)
    return cubes_needed['red'] * cubes_needed['blue'] * cubes_needed['green']


def part_2(input_data):
    result = 0
    for game_string in input_data.splitlines():
        result += power_minimum_set(game_string)
    return result


if __name__ == "__main__":
    
    from aoc.initialize_day import load_input

    folder = Path(__file__).parent
    try:
        year = int(folder.parts[-2])
        day = int(folder.parts[-1])
    except ValueError:
        print("Failed to determine year and day from folder structure.")
        raise SystemExit(1)

    data = load_input(year, day)

    print("Part 1:", part_1(data))
    print("Part 2:", part_2(data))
