import numpy as np
from pathlib import Path


rotate_right = np.array([[0, 1], [-1, 0]])
rotate_left = np.array([[0, -1], [1, 0]])
mapping = {"R": (1, rotate_right), "L": (-1, rotate_left)}


def part_1(input_data):
    instructions = input_data.split(", ")
    position = np.array([0, 0])
    direction = np.array([1, 0])

    for instruction in instructions:
        sign, rotation = mapping[instruction[0]]
        position += sign * direction * int(instruction[1:])
        direction = rotation.dot(direction)

    return str(int(np.linalg.norm(position, 1)))


def part_2(input_data):
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
    with (Path(__file__).parent / "input.txt").open("r") as f:
        data = f.read()

    print("Part 1:", part_1(data))
    print("Part 2:", part_2(data))
