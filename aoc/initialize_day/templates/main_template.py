from pathlib import Path
from solution import part_1, part_2

if __name__ == "__main__":
    input_path = Path(__file__).parent / "input.txt"
    with input_path.open("r") as f:
        data = f.read().strip()

    print("Part 1:", part_1(data))
    print("Part 2:", part_2(data))
