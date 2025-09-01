import re
import numpy as np

from aoc.cli.utils import load_input


def read_input(input_data):
    pattern = re.compile(r"\d+")
    stats = np.array(
        [
            tuple(map(np.int32, pattern.findall(line)))
            for line in input_data.splitlines()
        ]
    )
    return [stats[:, 0], stats[:, 1], stats[:, 2]]


def reindeer_race(reindeer_stats, total_time):
    speeds, fly_durations, rest_durations = reindeer_stats
    full_cycles = np.int32(np.floor(total_time / (fly_durations + rest_durations)))
    remaining_time = total_time - full_cycles * (fly_durations + rest_durations)
    total_fly_time = full_cycles * fly_durations + np.minimum(
        remaining_time, fly_durations
    )
    return total_fly_time * speeds


def part_1(reindeer_stats, total_time):
    return np.max(reindeer_race(reindeer_stats, total_time))


def part_2(reindeer_stats, total_time):
    speeds, fly_durations, rest_durations = reindeer_stats
    time_intervals = np.arange(1, total_time + 1).reshape(-1, 1)
    distances = reindeer_race(reindeer_stats, np.tile(time_intervals, speeds.shape[0]))
    max_distances = np.max(distances, axis=1, keepdims=True)
    return np.max(np.sum(distances == max_distances, axis=0))


def main():
    data = load_input(__file__)
    print("Part 1:", part_1(read_input(data), 2503))
    print("Part 2:", part_2(read_input(data), 2503))


if __name__ == "__main__":
    main()
