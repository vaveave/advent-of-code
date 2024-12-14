from pathlib import Path
import shutil

# Define cache directories to remove
CACHE_DIRS = [".idea", ".mypy_cache", "__pycache__"]


def remove_cache_folders(root_dir: Path):
    """
    Remove cache folders in the specified directory and its subdirectories.
    """
    # Ensure root_dir is a Path object
    root_dir = Path(root_dir)

    # Iterate over all subdirectories of `root_dir`
    for subdir in root_dir.rglob("*"):
        if subdir.is_dir() and subdir.name in CACHE_DIRS:
            try:
                shutil.rmtree(subdir)
                print(f"Removed: {subdir}")
            except Exception as e:
                print(f"Error removing {subdir}: {e}")


if __name__ == "__main__":
    # Use the current working directory as root directory
    root_dir_ = Path.cwd()

    if not root_dir_.exists():
        print(f"Root directory {root_dir_} does not exist.")
    else:
        remove_cache_folders(root_dir_)
