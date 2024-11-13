import os
import requests


def get_session_token():
    return os.getenv("ADVENT_OF_CODE_SESSION_ID")


def download_input(year, day):
    url = f"https://adventofcode.com/{year}/day/{day}/input"
    session_token = get_session_token()
    if not session_token:
        raise ValueError("No session token found. Please set ADVENT_OF_CODE_SESSION_ID in your environment.")

    cookies = {"session": session_token}
    headers = {"User-Agent": "AdventOfCodeInputDownloader/1.0 (***REMOVED***)"}

    print(f"Retrieving input from: {url}")

    response = requests.get(url, cookies=cookies, headers=headers)

    if response.status_code == 200:
        # Ensure the inputs directory exists
        input_path = f"{year}/day_{day:02}_input.txt"
        os.makedirs(os.path.dirname(input_path), exist_ok=True)

        with open(input_path, "w") as f:
            f.write(response.text)
        print(f"Input for day {day}, {year} downloaded successfully to {input_path}.")
    else:
        print(f"Failed to download input for day {day}. Status code: {response.status_code}. "
              f"Check your session token or day number.")


def initialize_day(year, day):
    # Ensure year directory exist
    year_dir = f"{year}"
    os.makedirs(year_dir, exist_ok=True)

    # Path to the new day file
    day_file = f"{year_dir}/day_{day:02}.py"

    # Check if the day script already exists
    if not os.path.exists(day_file):
        # Read the day template
        with open("aoc/day_template.py") as template_file:
            template_content = template_file.read()

        # Replace placeholders with actual year and day information
        script_content = (
            template_content.
            replace("{{year}}", str(year)).
            replace("{{day}}", f"{day:02}").
            replace("{{day}}", f"{day:02}")
        )

        # Write the modified content to the new day script
        with open(day_file, "w") as day_script:
            day_script.write(script_content)

        print(f"Created {day_file} using day template.")
    else:
        print(f"{day_file} already exists.")

    # Download input for the specified day and year
    download_input(year=year, day=day)
