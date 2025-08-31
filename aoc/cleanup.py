"""
Utility script to clean up cache folders in the Advent of Code project.
"""

from pathlib import Path
import shutil

CACHE_DIRS = [".idea", ".mypy_cache", "__pycache__"]

def cleanup_cache_folders(root_dir: Path):
    """
    Recursively remove cache folders from the given root directory.
    """
    root_dir = Path(root_dir)
    for subdir in root_dir.rglob("*"):
        if subdir.is_dir() and subdir.name in CACHE_DIRS:
            try:
                shutil.rmtree(subdir)
                print(f"Removed: {subdir}")
            except Exception as e:
                print(f"Error removing {subdir}: {e}")

if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1:
        root = Path(sys.argv[1])
    else:
        root = Path.cwd()
    if not root.exists():
        print(f"Root directory {root} does not exist.")
    else:
        cleanup_cache_folders(root)
