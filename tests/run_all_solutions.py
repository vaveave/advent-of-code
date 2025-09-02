import subprocess
from pathlib import Path


def run_all_solutions():
    """
    Discover and run all `aoc.<year>.<day>` modules as standalone scripts.
    """
    base_path = Path(__file__).parent.parent / "aoc" / "solutions"
    for year_path in base_path.iterdir():
        if year_path.is_dir() and year_path.name.isdigit():
            year = year_path.name
            for day_path in year_path.iterdir():
                if day_path.is_dir() and day_path.name.isdigit():
                    day = day_path.name.zfill(2)
                    module_name = f"aoc.solutions.{year}.{day}"
                    print(f"\n--- Running: {module_name} ---")
                    try:
                        # Use subprocess to run the module
                        subprocess.run(["py", "-m", module_name], check=True)
                    except subprocess.CalledProcessError as e:
                        print(f"Error running {module_name}: {e}")


if __name__ == "__main__":
    run_all_solutions()
