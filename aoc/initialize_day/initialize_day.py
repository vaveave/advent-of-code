from pathlib import Path

BASE_DIR = "./aoc"
TEMPLATES_DIR = "initialize_day/templates"


def initialize_day(year, day):
    year = str(year)
    day = str(day).zfill(2)

    day_path = Path(BASE_DIR) / year / day
    if day_path.exists():
        print(f"Day {day} of {year} already exists. Aborting.")
        return

    # Create the directory
    day_path.mkdir(parents=True)

    # Copy templates
    with open(
            Path(BASE_DIR) / Path(TEMPLATES_DIR) / "main_template.py", "r"
    ) as src:
        with open(day_path / "__main__.py", "w") as dest:
            dest.write(src.read())

    with open(
            Path(BASE_DIR) / Path(TEMPLATES_DIR) / "solution_template.py", "r"
    ) as src:
        with open(day_path / "solution.py", "w") as dest:
            dest.write(src.read())

    # Create an empty input file
    (day_path / "input.txt").touch()

    print(f"Initialized {year}/{day} successfully!")

