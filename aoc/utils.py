import os
import requests


def get_session_token():
    """
    Retrieve the Advent of Code session token from the environment variables.

    Returns:
        str: The session token for authenticating requests.
    """
    return os.getenv("ADVENT_OF_CODE_SESSION_ID")


def download_input(year, day):
    """
    Download the input data for a specific day and year from Advent of Code.

    Args:
        year (int): The year of the Advent of Code challenge.
        day (int): The day of the challenge.

    Raises:
        ValueError: If no session token is found in the environment.
    """
    url = f"https://adventofcode.com/{year}/day/{day}/input"
    session_token = get_session_token()
    if not session_token:
        raise ValueError("No session token found. Please set ADVENT_OF_CODE_SESSION_ID in your environment.")

    cookies = {"session": session_token}
    headers = {"User-Agent": "AdventOfCodeInputDownloader/1.0"}

    response = requests.get(url, cookies=cookies, headers=headers)

    if response.status_code == 200:
        input_path = f"{year}/day_{day:02}_input.txt"
        os.makedirs(os.path.dirname(input_path), exist_ok=True)
        with open(input_path, "w") as f:
            f.write(response.text)
        print(f"Input for day {day}, {year} downloaded successfully.")
    else:
        print(f"Failed to download input for day {day}. Status code: {response.status_code}.")


def initialize_day(year, day):
    """
    Initialize a new day script and download the input for a specific year and day.

    Args:
        year (int): The year of the Advent of Code challenge.
        day (int): The day of the challenge.
    """
    year_dir = f"{year}"
    os.makedirs(year_dir, exist_ok=True)

    day_file = f"{year_dir}/day_{day:02}.py"

    if not os.path.exists(day_file):
        with open("aoc/day_template.py") as template_file:
            template_content = template_file.read()

        script_content = template_content.replace("{{year}}", str(year)).replace("{{day}}", f"{day:02}")

        with open(day_file, "w") as day_script:
            day_script.write(script_content)

        print(f"Created {day_file} using day template.")
    else:
        print(f"{day_file} already exists.")

    download_input(year=year, day=day)
