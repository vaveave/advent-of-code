from pathlib import Path


def read_input(input_data):
    return [[int(entry) for entry in row.split(" ")] for row in input_data.splitlines()]


def is_report_safe(report):
    is_asc = report[0] <= report[1]
    for i in range(len(report)-1):
        if is_asc:
            if not (1 <= report[i+1] - report[i] <= 3):
                return False
        elif not (1 <= report[i] - report[i+1] <= 3):
            return False
    return True


def part_1(reports):
    return sum([is_report_safe(report) for report in reports])


def is_report_dampened_safe(report):
    for i in range(len(report)):
        if is_report_safe([report[j] for j in range(len(report)) if j!=i]):
            return True
    return False


def part_2(reports):
    return sum([is_report_dampened_safe(report) for report in reports])


test_data = """7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9"""


if __name__ == "__main__":
    with (Path(__file__).parent / "input.txt").open("r") as f:
        data = f.read()

    print("Part 1:", part_1(read_input(data)))
    print("Part 2:", part_2(read_input(data)))
