import os
import requests
import argparse


def get_session_token():
    """Retrieve the session token from the environment variable."""
    return os.getenv("ADVENT_OF_CODE_SESSION_ID")


def download_input(year, day, folder):
    """
    Download the input file for a specific day and save it to the given folder.

    Args:
        year (int): The year of the Advent of Code challenge.
        day (int): The day of the Advent of Code challenge.
        folder (str): The folder path where the input file will be saved.
    """
    url = f"https://adventofcode.com/{year}/day/{day}/input"
    session_token = get_session_token()
    if not session_token:
        raise ValueError("No session token found. Set ADVENT_OF_CODE_SESSION_ID in your environment.")

    cookies = {"session": session_token}
    headers = {"User-Agent": "AdventOfCodeInputDownloader/1.0 (example@example.com)"}

    response = requests.get(url, cookies=cookies, headers=headers)
    if response.status_code == 200:
        input_path = os.path.join(folder, "input.txt")
        with open(input_path, "w") as f:
            f.write(response.text.strip())
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
    folder_name = f"aoc/{year}/{day}"
    os.makedirs(folder_name, exist_ok=True)

    # Create the script file
    script_path = os.path.join(folder_name, "__main__.py")
    if not os.path.exists(script_path):
        with open("aoc/day_template.py") as template_file:
            template_content = template_file.read()
        script_content = template_content.replace("{{year}}", str(year)).replace("{{day}}", f"{day:02}")
        with open(script_path, "w") as script_file:
            script_file.write(script_content)
        print(f"Script created at {script_path}")
    else:
        print(f"Script already exists at {script_path}")

    # Download the input file
    download_input(year, day, folder_name)


if __name__ == "__main__":
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
