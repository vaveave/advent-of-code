
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

### 2. Run the Solution for Any Day


After setting your virtual environment, you can use a single command to run any day's solution:

```bash
py -m aoc run <year> <day>
```

For example, to run Day 1 of 2023:

```bash
py -m aoc run 2023 1
```

### 3. (Optional) Day Initialization
To create the folder structure and script template for a specific day automatically, use the `init` command instead:

```bash
py -m aoc init <year> <day>
```

For example, to initialize Day 1 of 2023:

```bash
py -m aoc init 2023 1
```

#### What If the Input File Is Missing?
If the input file for the day is missing when running the script, it will attempt to download it automatically using your session token.

### 4. Happy Coding!

That’s it! Now you can enjoy solving the puzzles. 🎉 If you want to try a different year or day, just run the corresponding script with `py`.

---

## License

MIT License. See LICENSE for details.
