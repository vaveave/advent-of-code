import os
import requests
import argparse
import shutil
from pathlib import Path


PATH_AOC = Path("./aoc")
PATH_TEMPLATE = PATH_AOC / Path("initialize_day") / Path("templates")


def get_session_token():
    """Retrieve the session token from the environment variable."""
    return os.getenv("ADVENT_OF_CODE_SESSION_ID")


def download_input(year, day, folder):
    """
    Download the input file for a specific day and save it to the given folder.

    Args:
        year (int): The year of the Advent of Code challenge.
        day (int): The day of the Advent of Code challenge.
        folder (Path): The folder path where the input file will be saved.
    """
    url = f"https://adventofcode.com/{year}/day/{day}/input"
    session_token = get_session_token()
    if not session_token:
        raise ValueError("No session token found. Set ADVENT_OF_CODE_SESSION_ID in your environment.")

    cookies = {"session": session_token}
    headers = {"User-Agent": "AdventOfCodeInputDownloader/1.0 (example@example.com)"}

    response = requests.get(url, cookies=cookies, headers=headers)
    if response.status_code == 200:
        input_path = folder / "input.txt"
        input_path.write_text(response.text.strip())
        print(f"Input downloaded to {input_path}")
    else:
        raise RuntimeError(f"Failed to download input. Status code: {response.status_code}")


def initialize_day(year, day):
    """
    Initialize the folder, script, and input file for a specific day.

    Args:
        year (int): The year of the Advent of Code challenge.
        day (int): The day of the Advent of Code challenge.
    """
    # Create the day folder
    folder = PATH_AOC / str(year) / str(day).zfill(2)
    folder.mkdir(parents=True, exist_ok=True)

    # Copy the templates for the scripts
    main_template_path = PATH_TEMPLATE / "main_template.py"
    solution_template_path = PATH_TEMPLATE / "solution_template.py"

    # Create the __main__.py script
    script_path = folder / "__main__.py"
    if not script_path.exists():
        shutil.copy(main_template_path, script_path)
        print(f"Script created at {script_path}")
    else:
        print(f"Script already exists at {script_path}")

    # Create the solution.py file
    solution_path = folder / "solution.py"
    if not solution_path.exists():
        shutil.copy(solution_template_path, solution_path)
        print(f"Solution file created at {solution_path}")
    else:
        print(f"Solution file already exists at {solution_path}")

    # Download the input file
    download_input(year, day, folder)


def main():
    """Parse command-line arguments and initialize the day."""
    parser = argparse.ArgumentParser(description="Initialize Advent of Code day folder, script, and input.")
    parser.add_argument("year", type=int, help="The year of the Advent of Code challenge.")
    parser.add_argument("day", type=int, help="The day of the Advent of Code challenge (1-25).")

    args = parser.parse_args()

    if not (1 <= args.day <= 25):
        parser.error("Day must be between 1 and 25.")

    try:
        initialize_day(args.year, args.day)
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
