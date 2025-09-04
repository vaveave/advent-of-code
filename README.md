# Advent of Code solutions

Welcome to my small **[Advent of Code](https://adventofcode.com/)** corner! 🎄🎮 This repository contains my solutions to the Advent of Code challenges, with one Python script for each day of the challenge. The input data for each day is automatically downloaded using a session token, so all you need to do is run the scripts!

## Setup instructions

### 1. Set up your session token

To download the input data, you'll need to authenticate by setting the `ADVENT_OF_CODE_SESSION_ID` environment variable.

#### For Windows:
```cmd
setx ADVENT_OF_CODE_SESSION_ID "your_session_token_here"
```

#### For macOS/Linux:
```bash
export ADVENT_OF_CODE_SESSION_ID="your_session_token_here"
```

### 2. Install and use uv for dependency management

This project uses [`uv`](https://docs.astral.sh/uv/getting-started/installation/) for dependency management and running solutions.  
Follow the [uv installation guide](https://docs.astral.sh/uv/getting-started/installation/) to install `uv` on your system.

You do **not** need to manually configure a Python environment—`uv` handles everything for you!

### 3. Run the solution for any day

From the project root (where `pyproject.toml` is located), simply run:

```bash
uv run aoc run <year> <day>
```

For example, to run Day 1 of 2023:

```bash
uv run aoc run 2023 1
```

### 4. (Optional) Day initialization

To create the folder structure and script template for a specific day automatically, use the `init` command:

```bash
uv run aoc init <year> <day>
```

For example, to initialize Day 1 of 2023:

```bash
uv run aoc init 2023 1
```

#### What if the input file is missing?
If the input file for the day is missing when running the script, it will attempt to download it automatically using your session token.

### 5. Happy coding!

That’s it! Now you can enjoy solving the puzzles. 🎉

---

## License

MIT License. See LICENSE for details.
