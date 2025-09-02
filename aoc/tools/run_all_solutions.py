import importlib
from pathlib import Path

# To run: "py -m aoc.tools.run_all_solutions" from the project root directory


def run_all_solutions():
    """
    Discover and run all `aoc.solutions.<year>.<day>` modules as standalone scripts.
    """
    base_path = Path().resolve() / "aoc" / "solutions"
    
    # Find all __main__.py files two levels deep (year/day)
    main_files = base_path.rglob("__main__.py")
    
    for main_file in main_files:
        # Ensure it's under a numeric year/day structure
        try:
            day_path = main_file.parent
            year_path = day_path.parent
            year, day = year_path.name, day_path.name
            if not (year.isdigit() and day.isdigit()):
                continue
        except IndexError:
            continue

        module_name = f"aoc.solutions.{year}.{int(day):02d}.__main__"
        print(f"\n--- Running day {day}, year {year} ---")
        try:
            module = importlib.import_module(module_name)
            module.main()
        except ModuleNotFoundError:
            print(f"❌ Module not found: {module_name}. Day {day}, year {year} skipped.")


if __name__ == "__main__":
    run_all_solutions()
