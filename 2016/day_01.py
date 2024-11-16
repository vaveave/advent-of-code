# Advent of Code: Year 2016, Day 01
# Usage: python 2016/day_01.py

from pathlib import Path
import numpy as np

rotate_right = np.array([[0, 1], [-1, 0]])
rotate_left = np.array([[0, -1], [1, 0]])
mapping = {"R": (1, rotate_right), "L": (-1, rotate_left)}


def part1(input_data):
    instructions = input_data.split(", ")
    position = np.array([0, 0])
    direction = np.array([1, 0])

    for instruction in instructions:
        sign, rotation = mapping[instruction[0]]
        position += sign * direction * int(instruction[1:])
        direction = rotation.dot(direction)

    return str(int(np.linalg.norm(position, 1)))


def part2(input_data):
    instructions = input_data.split(", ")
    position = np.array([0, 0])
    direction = np.array([1, 0])
    positions = [position.copy()]

    for instruction in instructions:
        sign, rotation = mapping[instruction[0]]

        for i in range(1, int(instruction[1:])+1):
            position += sign * direction
            if any(np.array_equal(position, step) for step in positions):
                return abs(position[0]) + abs(position[1])
            else:
                positions.append(position.copy())
        direction = rotation.dot(direction)

    return "no position found!"


if __name__ == "__main__":
    # Get the input file path and read the input data
    input_file = Path(__file__).parent / f"day_01_input.txt"
    with open(input_file) as f:
        data = f.read().strip()

    print("Part 1:", part1(data))
    print("Part 2:", part2(data))
