import numpy as np
import pandas as pd
from io import StringIO
from pathlib import Path


# Define the shape of the matrix
grid_shape = (1000, 1000)


def data_processing(input_: str):
    input_ = input_.replace(" through ", ")\t(")
    input_ = input_.replace("turn on ", "1\t(")
    input_ = input_.replace("toggle ", "2\t(")
    input_ = input_.replace("turn off ", "3\t(")
    input_ = input_.replace("\n", ")\n")
    df = pd.read_csv(StringIO(input_+")"), sep="\t", header=None, names=["action", "corner_1", "corner_2"])
    df['corner_1'] = df['corner_1'].apply(lambda x: tuple(map(int, x.strip('()').split(','))))
    df['corner_2'] = df['corner_2'].apply(lambda x: tuple(map(int, x.strip('()').split(','))))
    print(df.dtypes)
    return df


def part_1(input_data):
    grid_light = np.zeros((grid_shape[0], grid_shape[1]), dtype=int)
    for instruction in input_data.splitlines():
        instruction_words = instruction.split(" ")
        x1, y1 = map(int, instruction_words[-3].split(","))
        x2, y2 = map(int, instruction_words[-1].split(","))
        if instruction.startswith("turn on"):
            grid_light[x1:x2+1, y1:y2+1] = 1
        elif instruction.startswith("toggle"):
            grid_light[x1:x2+1, y1:y2+1] = 1 - grid_light[x1:x2+1, y1:y2+1]
        elif instruction.startswith("turn off"):
            grid_light[x1:x2 + 1, y1:y2 + 1] = 0
        else:
            print(f"Instruction {instruction} non recognized")
    return np.sum(grid_light)


def part_2(input_data):
    grid_light = np.zeros((grid_shape[0], grid_shape[1]), dtype=int)
    for instruction in input_data.splitlines():
        instruction_words = instruction.split(" ")
        x1, y1 = map(int, instruction_words[-3].split(","))
        x2, y2 = map(int, instruction_words[-1].split(","))
        if instruction.startswith("turn on"):
            grid_light[x1:x2+1, y1:y2+1] = 1+grid_light[x1:x2+1, y1:y2+1]
        elif instruction.startswith("toggle"):
            grid_light[x1:x2+1, y1:y2+1] = 2+grid_light[x1:x2+1, y1:y2+1]
        elif instruction.startswith("turn off"):
            grid_light[x1:x2+1, y1:y2+1] = np.maximum(grid_light[x1:x2+1, y1:y2+1]-1, 0)
        else:
            print(f"Instruction {instruction} non recognized")
    return np.sum(grid_light)


if __name__ == "__main__":
    with (Path(__file__).parent / "input.txt").open("r") as f:
        data = f.read()

    print("Part 1:", part_1(data))
    print("Part 2:", part_2(data))
