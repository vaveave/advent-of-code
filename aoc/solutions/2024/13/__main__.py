import re
import numpy as np

from aoc.cli.utils import load_input


match = re.compile(r"\d+")


def read_input(input_data):
    lines = [
        np.array(list(map(int, re.findall(r"\d+", line))))
        for line in input_data.split("\n\n")
    ]
    return [(line[:4].reshape(2, 2).T, line[4:].reshape(2, 1)) for line in lines]


def solve_puzzle(input_data, solution_filter, adjust_prize=0, round_precision=2):
    solutions = []
    for coefficients, prize_position in input_data:
        prize_position += adjust_prize
        if np.linalg.det(coefficients) != 0:
            sol_a, sol_b = np.round(
                np.linalg.solve(coefficients, prize_position), round_precision
            )
            sol_a, sol_b = sol_a[0], sol_b[0]
            if solution_filter(sol_a, sol_b):
                solutions.append(int(3 * sol_a + sol_b))
    return sum(solutions)


def part_1(input_data):
    return solve_puzzle(
        input_data,
        solution_filter=lambda sol_a, sol_b: (
            0 < sol_a <= 100
            and sol_a.is_integer()
            and 0 < sol_b <= 100
            and sol_b.is_integer()
        ),
    )


def part_2(input_data):
    return solve_puzzle(
        input_data,
        adjust_prize=10_000_000_000_000,
        solution_filter=lambda sol_a, sol_b: (
            sol_a > 0 and sol_a.is_integer() and sol_b > 0 and sol_b.is_integer()
        ),
    )


def main():
    data = load_input(__file__)
    print("Part 1:", part_1(read_input(data)))
    print("Part 2:", part_2(read_input(data)))


if __name__ == "__main__":
    main()
