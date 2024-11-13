
# Advent of Code Solutions

This repository contains solutions to the Advent of Code challenges for each year and day. Each day has a separate Python script that implements the solution for that day. The input for each day is downloaded automatically using a session token, and the solutions for **Part 1** and **Part 2** of each challenge are implemented in the respective scripts.

## How to Run the Code

To run the solutions for a given day, follow the instructions below:

### 1. Set Up the Environment Variable

Before running the scripts, you need to set the `ADVENT_OF_CODE_SESSION_ID` environment variable. This token is required to download the input for each day.

#### For Windows:

1. Open Command Prompt and run:

   ```cmd
   setx ADVENT_OF_CODE_SESSION_ID "your_session_token_here"
   ```

   Alternatively, for the current session, you can use:

   ```cmd
   set ADVENT_OF_CODE_SESSION_ID="your_session_token_here"
   ```

#### For macOS/Linux:

1. Open a terminal and run:

   ```bash
   export ADVENT_OF_CODE_SESSION_ID="your_session_token_here"
   ```

2. To persist the environment variable across sessions, you can add it to your `~/.bashrc`, `~/.zshrc`, or other shell configuration files:

   ```bash
   echo 'export ADVENT_OF_CODE_SESSION_ID="your_session_token_here"' >> ~/.bashrc
   source ~/.bashrc
   ```

Replace `your_session_token_here` with your actual Advent of Code session token. You can find this token in your browser's cookies when logged in to the Advent of Code website.

### 2. Initialize a Day Script (Optional)

To generate the script for a particular day, run the following command in your terminal:

```bash
python aoc/initialize_day.py <year> <day>
```

Replace `<year>` and `<day>` with the year and day of the challenge you want to solve. This will create a new Python script for that day in the appropriate `days` folder, download the input data, and create any necessary directories.

Example:

```bash
python aoc/initialize_day.py 2023 01
```

This will create `2023/days/day_01.py` for Day 1 of 2023, with the input data downloaded into `2023/inputs/day_01.txt`.

### 3. Run the Solution

To run the solution for a specific day, use:

```bash
python 2023/days/day_01.py
```

This will execute the solution for Day 1 of 2023.

### 4. Running from PyCharm

In PyCharm, simply open the desired day’s script (`2023/days/day_01.py`) and click the "Run" or "Debug" button to run the solution directly from the IDE. PyCharm will automatically handle the working directory, and the script will read input from the appropriate file in the `inputs` directory.

### 5. Customize for Different Years/Days

You can use the `initialize_day.py` script to initialize scripts for any other year or day. For example:

```bash
python aoc/initialize_day.py 2022 05
```

This will create a script for Day 5 of 2022.

## Directory Structure

```
advent-of-code/
│
├── 2023/
│   ├── day_01.py            # Solution for day 1 of 2023
│   └── day_01_input.txt     # Input data for day 1 of 2023
│
├── aoc/
│   ├── day_template.py      # Template for day solutions
│   ├── initialize_day.py    # Script to initialize day solutions
│   ├── utils.py             # Utility functions for downloading input and initializing day scripts
└── README.md                # This README file
```

## License

This repository is provided under the MIT License. See the LICENSE file for details.

