import os
import requests
import shutil
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


def load_input(path: str | Path):
    """
    Ensure the input file exists; if not, download it.

    Args:
        path (str | Path): Path of the daily script where to save the file.
    """
    folder = Path(path).parent
    input_file = folder / "input.txt"

    if not input_file.exists():
        try:
            year = int(folder.parts[-2])
            day = int(folder.parts[-1])
            print(f"Input file not found. Attempting to download for year {year}, day {day}...")
            download_input(year, day, folder)
        except Exception as e:
            print(f"Error downloading input: {e}")
            raise  # Re-raise the exception to stop further execution

    return input_file.read_text()


def initialize_day(year, day):
    """
    Initialize the folder, script, input file, and __init__.py for a specific day.

    Args:
        year (int): The year of the Advent of Code challenge.
        day (int): The day of the Advent of Code challenge.
    """
    # Create the year folder if it doesn't exist, and the __init__.py file
    year_folder = Path(__file__).parent.parent / str(year)
    if not year_folder.exists():
        year_folder.mkdir(parents=True, exist_ok=True)
        init_file = year_folder / "__init__.py"
        if not init_file.exists():
            init_file.touch()  # Create the __init__.py file
            print(f"Created {init_file}")

    # Create the day folder
    folder = year_folder / str(day).zfill(2)
    folder.mkdir(parents=True, exist_ok=True)

    # Copy the template script to the day folder and rename it
    template_path = Path(__file__).parent.parent / "initialize_day" / "day_template.py"
    script_path = folder / "__main__.py"
    if not script_path.exists():
        shutil.copy(template_path, script_path)
        print(f"Script created at {script_path}")
    else:
        print(f"Script already exists at {script_path}")

    # Download the input file
    load_input(script_path)
