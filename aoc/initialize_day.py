import sys
from utils import initialize_day


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python initialize_day.py <year> <day>")
        sys.exit(1)

    year = int(sys.argv[1])
    day = int(sys.argv[2])
    initialize_day(year, day)
