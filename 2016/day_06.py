import pandas as pd
from pathlib import Path


def part1(input_data):
    input_data = [list(row) for row in input_data.splitlines()]
    message = pd.DataFrame(input_data).mode()
    return "".join(message.values.tolist()[0])


def part2(input_data):
    input_data = [list(row) for row in input_data.splitlines()]
    df_message = pd.DataFrame(input_data)
    message = []
    for col in df_message:
        message.append(df_message[col].value_counts().index[-1])
    return "".join(message)


if __name__ == "__main__":
    # Get the input file path and read the input data
    input_file = Path(__file__).parent / f"day_06_input.txt"
    with open(input_file) as f:
        data = f.read().strip()

    print("Part 1:", part1(data))
    print("Part 2:", part2(data))
