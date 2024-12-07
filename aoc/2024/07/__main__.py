import re
from itertools import product

pattern = re.compile(r'\d+')


def read_input(input_data):
    return [list(map(int, re.findall(r'\d+', line))) for line in input_data.splitlines()]


def generate_bool_combinations(operators, max_length):
    combinations = []
    for i in range(1, max_length):
        combinations.append(list(product(range(operators), repeat=i)))
    return combinations


def is_equation_true(equation, combination):
    result = equation[0]
    parameters = equation[1:]
    for operations in combination:
        temp_result = parameters[0]
        for i, operation in enumerate(operations):
            if operation:
                temp_result += parameters[i+1]
            else:
                temp_result *= parameters[i+1]
        if temp_result == result:
            return True
    return False


def part_1(input_data):
    max_length = max(len(line) for line in input_data) - 1
    combinations = generate_bool_combinations(operators=2, max_length=max_length)
    cnt = 0
    for equation in input_data:
        if is_equation_true(equation, combinations[len(equation)-3]):
            cnt += equation[0]
    return cnt


def is_equation_wit_concat_true(equation, combination):
    result = equation[0]
    parameters = equation[1:]
    for operations in combination:
        temp_result = parameters[0]
        for i, operation in enumerate(operations):
            if operation == 0:
                temp_result += parameters[i+1]
            elif operation == 1:
                temp_result *= parameters[i+1]
            else:
                temp_result = int(str(temp_result)+str(parameters[i+1]))
        if temp_result == result:
            return True
    return False


def part_2(input_data):
    max_length = max(len(line) for line in input_data) - 1
    combinations = generate_bool_combinations(operators=3, max_length=max_length)
    cnt = 0
    for equation in input_data:
        if is_equation_wit_concat_true(equation, combinations[len(equation)-3]):
            cnt += equation[0]
    return cnt


test_data = """190: 10 19
3267: 81 40 27
83: 17 5
156: 15 6
7290: 6 8 6 15
161011: 16 10 13
192: 17 8 14
21037: 9 7 18 13
292: 11 6 16 20"""

if __name__ == "__main__":

    from aoc.initialize_day import load_input
    data = load_input(__file__)
    print("Part 1:", part_1(read_input(data)))
    print("Part 2:", part_2(read_input(data)))
