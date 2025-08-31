
# Advent of Code Solutions

Welcome to my small **[Advent of Code](https://adventofcode.com/)** corner! 🎄🎮 This repository contains my solutions to the Advent of Code challenges, with one Python script for each day of the challenge. The input data for each day is automatically downloaded using a session token, so all you need to do is run the scripts!

## Setup Instructions

### 1. Set Up Your Session Token

To download the input data, you'll need to authenticate by setting the `ADVENT_OF_CODE_SESSION_ID` environment variable.

#### For Windows:
```cmd
setx ADVENT_OF_CODE_SESSION_ID "your_session_token_here"
```

#### For macOS/Linux:
```bash
export ADVENT_OF_CODE_SESSION_ID="your_session_token_here"
```

### 2. Set Up the Environment

This project uses `pyproject.toml` for managing dependencies and environment setup. To get started, make sure you have **[Poetry](https://python-poetry.org/)** installed, as it helps manage Python packages and virtual environments.

If you don’t have Poetry installed, you can install it by running:

#### For macOS/Linux/Windows:
```bash
curl -sSL https://install.python-poetry.org | python3 -
```

Once Poetry is installed, you can create and activate the virtual environment with the following command:

```bash
poetry install
```

This will install all the necessary dependencies defined in `pyproject.toml` and create a virtual environment for you.

To activate the virtual environment, run:

```bash
poetry shell
```

### 3. Run the Solution for Any Day


You can use a single command to run any day's solution:

```bash
py -m aoc <year> <day>
```

For example, to run Day 1 of 2023:

```bash
py -m aoc 2023 1
```

### 4. (Optional) Day Initialization
To create the folder structure and script template for a specific day automatically, use the `-init` flag:

```bash
py -m aoc <year> <day> -init
```

For example, to initialize Day 1 of 2023:

```bash
py -m aoc 2023 1 -init
```

#### What If the Input File Is Missing?
If the input file for the day is missing when running the script, it will attempt to download it automatically using your session token.

### 5. Happy Coding!

That’s it! Now you can enjoy solving the puzzles. 🎉 If you want to try a different year or day, just run the corresponding script with `py`.

---

## License

MIT License. See LICENSE for details.
