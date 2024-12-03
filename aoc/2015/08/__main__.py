from contextlib import redirect_stdout
from io import StringIO
from pathlib import Path

# Create a StringIO object to capture the output
output_buffer = StringIO()


def compute_extra_chars_num(input_list):
    tot_chars = 0
    tot_memory = 0
    for str_ in input_list:
        tot_chars += len(str_)
        with redirect_stdout(output_buffer):
            exec(f"p={str_}")
        captured_output = output_buffer.getvalue()
        result_value = locals()["p"]
        tot_memory += len(result_value)
    return str(tot_chars-tot_memory)


def part_1(input_data):
    return compute_extra_chars_num(input_data.splitlines())


def repl_special_chars(str_):
    return (str_.replace('\\', '\\\\')).replace(r'"', r'\"')


def input_list_with_replacements(input_data):
    return ["\""+repl_special_chars(str_)+"\"" for str_ in input_data.splitlines()]


def part_2(input_data):
    return compute_extra_chars_num(input_list_with_replacements(input_data))


if __name__ == "__main__":
    
    from aoc.initialize_day import load_input

    folder = Path(__file__).parent
    try:
        year = int(folder.parts[-2])
        day = int(folder.parts[-1])
    except ValueError:
        print("Failed to determine year and day from folder structure.")
        raise SystemExit(1)

    data = load_input(year, day)

    print("Part 1:", part_1(data))
    print("Part 2:", part_2(data))
