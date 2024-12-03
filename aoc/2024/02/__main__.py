import numpy as np
from pathlib import Path


def read_input(input_data):
    return [np.fromstring(row, sep=" ", dtype=int) for row in input_data.splitlines()]


def is_report_safe(report):
    report_diff = np.diff(report)
    is_safely_increasing = np.all((report_diff >= 1) & (report_diff <= 3))
    is_safely_decreasing = np.all((report_diff >= -3) & (report_diff <= -1))
    return is_safely_increasing or is_safely_decreasing


def part_1(reports):
    return sum([is_report_safe(report) for report in reports])


def is_report_dampened_safe(report):
    for i in range(len(report)):
        if is_report_safe(np.delete(report, i)):
            return True
    return False


def part_2(reports):
    return sum([is_report_dampened_safe(report) for report in reports])


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

    print("Part 1:", part_1(read_input(data)))
    print("Part 2:", part_2(read_input(data)))