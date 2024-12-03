import os
import requests
from pathlib import Path


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


def load_input(year, day):
    """
    Ensure the input file exists; if not, download it.

    Args:
        year (int): The year of the Advent of Code challenge.
        day (int): The day of the Advent of Code challenge.
    """
    folder = Path(__file__).parent.parent / str(year) / str(day).zfill(2)
    input_file = folder / "input.txt"

    if not input_file.exists():
        print(f"Input file not found. Attempting to download for year {year}, day {day}...")
        try:
            download_input(year, day, folder)
        except Exception as e:
            print(f"Error downloading input: {e}")
            raise  # Re-raise the exception to stop further execution

    return input_file.read_text()
