import pandas as pd
from pathlib import Path


def part_1(input_data):
    input_data = [list(row) for row in input_data.splitlines()]
    message = pd.DataFrame(input_data).mode()
    return "".join(message.values.tolist()[0])


def part_2(input_data):
    input_data = [list(row) for row in input_data.splitlines()]
    df_message = pd.DataFrame(input_data)
    message = []
    for col in df_message:
        message.append(df_message[col].value_counts().index[-1])
    return "".join(message)


if __name__ == "__main__":
    with (Path(__file__).parent / "input.txt").open("r") as f:
        data = f.read()

    print("Part 1:", part_1(data))
    print("Part 2:", part_2(data))
