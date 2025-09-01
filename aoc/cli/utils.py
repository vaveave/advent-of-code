import os
import requests
from pathlib import Path

from aoc.cli.template import TEMPLATE


def _get_session_token():
    """Retrieve the session token from the environment variable."""
    return os.getenv("ADVENT_OF_CODE_SESSION_ID")


def _download_input(year, day, folder):
    """
    Download the input file for a specific day and save it to the given folder.

    Args:
        year (int): The year of the Advent of Code challenge.
        day (int): The day of the Advent of Code challenge.
        folder (Path): The folder path where the input file will be saved.
    """
    url = f"https://adventofcode.com/{year}/day/{day}/input"
    session_token = _get_session_token()
    if not session_token:
        raise ValueError(
            "No session token found. Set ADVENT_OF_CODE_SESSION_ID in your environment."
        )

    cookies = {"session": session_token}
    headers = {"User-Agent": "AdventOfCodeInputDownloader/1.0 (example@example.com)"}

    response = requests.get(url, cookies=cookies, headers=headers)
    input_path = folder / "input.txt"
    if response.status_code == 200:
        input_path.write_text(response.text.strip())
        print(f"✅ Input downloaded: {input_path.relative_to(Path.cwd())}")
    elif response.status_code == 404:
        print(f"⚠️  Input for year {year}, day {day} is not available yet on Advent of Code.")
        print("You can start coding, but input.txt will be empty until the puzzle is released.")
        input_path.write_text("")
    else:
        print(f"❌ Failed to download input. Status code: {response.status_code}")
        raise RuntimeError(
            f"Failed to download input. Status code: {response.status_code}"
        )


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
            print(
                f"Input file doesn't exist yet. Downloading for year {year}, day {day}..."
            )
            _download_input(year, day, folder)
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
    year_folder = Path(__file__).parent.parent / "solutions" / str(year)
    created_year = False
    if not year_folder.exists():
        year_folder.mkdir(parents=True, exist_ok=True)
        init_file = year_folder / "__init__.py"
        if not init_file.exists():
            init_file.touch()  # Create the __init__.py file
        created_year = True

    # Create the day folder
    folder = year_folder / str(day).zfill(2)
    created_day = False
    if not folder.exists():
        folder.mkdir(parents=True, exist_ok=True)
        created_day = True

    # Write TEMPLATE to the day's script file
    script_path = folder / "__main__.py"
    created_script = False
    if not script_path.exists():
        with open(script_path, "w") as script_file:
            script_file.write(TEMPLATE)
        created_script = True

    # Download the input file
    load_input(script_path)

    if created_year:
        print(f"Year folder: {year_folder.relative_to(Path.cwd())}")
    if created_day:
        print(f"Day folder: {folder.relative_to(Path.cwd())}")
    if created_script:
        print(f"Script template: {script_path.relative_to(Path.cwd())}")
    print("✅  Initialization complete!")
