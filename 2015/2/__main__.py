from pathlib import Path


def part_1(input_data):
    input_per_row = input_data.split('\n')
    surf = 0
    for i, row in enumerate(input_per_row):
        size = [int(s) for s in row.split('x')]
        surf_1 = size[0]*size[1]
        surf_2 = size[1]*size[2]
        surf_3 = size[0]*size[2]
        surf += 2*surf_1 + 2*surf_2 + 2*surf_3 + min((surf_1, surf_2, surf_3))
    return str(surf)


def part_2(input_data):
    input_per_row = input_data.split('\n')
    ribbon = 0
    for i, row in enumerate(input_per_row):
        size = [int(s) for s in row.split('x')]
        size.sort()
        min_perimeter = 2 * size[0] + 2 * size[1]
        vol = size[0] * size[1] * size[2]
        ribbon += min_perimeter + vol
    return str(ribbon)


if __name__ == "__main__":
    with (Path(__file__).parent / "input.txt").open("r") as f:
        data = f.read()

    print("Part 1:", part_1(data))
    print("Part 2:", part_2(data))
