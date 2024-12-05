import re
import math


def process_input(input_str):
    pre_proc = [re.sub(' +', ' ', str_) for str_ in input_str.split("\n")]
    time_values = list(map(int, pre_proc[0].replace("Time: ", "").split(" ")))
    distance_values = list(map(int, pre_proc[1].replace("Distance: ", "").split(" ")))
    return [(time_values[i], distance_values[i]) for i in range(len(distance_values))]


def solve_race(time, distance):
    """
    Returns integer solutions x (holding button time) of inequalities:
        - 0 < x < time
        - (time - x) * x > distance, ie
          (time-math.sqrt(time**2-4*distance))/2 < x < (time+math.sqrt(time**2-4*distance))/2
    """
    discriminant = time ** 2 - 4 * distance

    if discriminant >= 0:
        sqrt_discriminant = math.sqrt(discriminant)
        lower_bound = (time - sqrt_discriminant) / 2
        upper_bound = (time + sqrt_discriminant) / 2

        return set(range(math.ceil(lower_bound), math.floor(upper_bound)+1)).intersection(set(range(1, time)))
    else:
        raise TypeError(f"No solutions found for time {str(time)} and total distance {str(distance)}")


def part_1(input_data):
    p = process_input(input_data)
    combinations = 1
    for (time, distance) in p:
        combinations *= len(solve_race(time, distance))
    return str(combinations)


def process_input_2(input_str):
    return tuple(map(int, [re.sub(r'Time:|Distance:|\s', '', str_) for str_ in input_str.split("\n")]))


def count_race_solutions(time, distance):
    """
    Returns number of integer solutions x (holding button time) of inequalities:
        - 0 < x < time
        - (time - x) * x > distance, ie
          (time-math.sqrt(time**2-4*distance))/2 < x < (time+math.sqrt(time**2-4*distance))/2
    """
    discriminant = time ** 2 - 4 * distance

    if discriminant >= 0:
        sqrt_discriminant = math.sqrt(discriminant)
        lower_bound = (time - sqrt_discriminant) / 2
        upper_bound = (time + sqrt_discriminant) / 2

        return min(math.floor(upper_bound)+1, time) - max(math.ceil(lower_bound), 1)
    else:
        raise TypeError(f"No solutions found for time {str(time)} and total distance {str(distance)}")


def part_2(input_data):
    p = process_input_2(input_data)
    return str(count_race_solutions(p[0], p[1]))


if __name__ == "__main__":

    from aoc.initialize_day import load_input
    data = load_input(__file__)
    print("Part 1:", part_1(data))
    print("Part 2:", part_2(data))
