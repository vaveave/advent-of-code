
# Advent of Code Solutions

This repository contains solutions to the Advent of Code challenges for each year and day. Each day has a Python script implementing the solution. The input for each day is downloaded automatically using a session token.

## Setup Instructions

### 1. Set Up the Environment Variable

Set the `ADVENT_OF_CODE_SESSION_ID` environment variable to authenticate and download the input data.

#### For Windows:
```cmd
setx ADVENT_OF_CODE_SESSION_ID "your_session_token_here"
```

#### For macOS/Linux:
```bash
export ADVENT_OF_CODE_SESSION_ID="your_session_token_here"
```

### 2. Initialize a Day Script (Optional)

Run the following command to create a new day script for a specific year and day, and download the input data:

```bash
python aoc/initialize_day.py <year> <day>
```

Example:
```bash
python aoc/initialize_day.py 2023 01
```

This creates the script `2023/day_01.py` and downloads the input file `2023/day_01_input.txt`.

### 3. Run the Solution

To run the solution for a specific day, use:

```bash
python 2023/day_01.py
```

This will execute the solution for Day 1 of 2023.

### 4. Running from PyCharm

In PyCharm, open the desired day's script (`2023/day_01.py`) and click the "Run" or "Debug" button to run the solution directly from the IDE.

## Directory Structure

```
advent-of-code/
│
├── 2023/
│   ├── day_01.py             # Solution for day 1 of 2023
│   └── day_01_input.txt      # Input data for day 1 of 2023
│
├── aoc/
│   ├── day_template.py       # Template for day solutions
│   ├── initialize_day.py     # Script to initialize day solutions
│   ├── utils.py              # Utility functions for downloading input and initializing day scripts
└── README.md                 # This README file
```

## License

MIT License. See LICENSE for details.
