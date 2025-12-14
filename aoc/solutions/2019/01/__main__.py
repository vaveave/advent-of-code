from aoc.cli.utils import load_input


def read_input(data: str) -> list[str]:
    return data.splitlines()


def fuel_required(mass: int) -> int:
    return mass // 3 - 2


def part_1(data: list[str]) -> int:
    return sum(fuel_required(int(mass)) for mass in data)


def part_2(data: list[str]) -> int:
    total_fuel: int = 0
    for mass in data:
        m = int(mass)
        additional_fuel = fuel_required(m)
        while additional_fuel > 0:
            total_fuel += additional_fuel
            additional_fuel = fuel_required(additional_fuel)
    return total_fuel


def main() -> None:
    data = load_input(__file__)
    lines = read_input(data)
    print("Part 1:", part_1(lines))
    print("Part 2:", part_2(lines))


if __name__ == "__main__":
    main()
