import os
import sys
import importlib
from pathlib import Path
from typing import Optional


def check_all_problems(year: Optional[int] = 2024) -> None:
    print("--------------------")
    print(f"Checking all problems for year {year}")

    project_root = Path(__file__).resolve().parent.parent
    sys.path.insert(0, str(project_root))

    year_dir = project_root / str(year)
    data_dir = year_dir / "data"

    os.chdir(project_root)

    for day in range(1, 26):
        try:
            data_file = data_dir / f"day{day}"
            if not data_file.exists():
                # print(f"\nData file not found: {data_file}")
                continue

            print(f"\nChecking Day {day}...")

            module_name = f"{year}.solutions.day{day}"
            module = importlib.import_module(module_name)
            problem_class = getattr(module, f"Day{day}")
            problem = problem_class(load_example=False)
            problem.check_solutions()

        except ModuleNotFoundError as e:
            print(f"Module not found for Day {day}: {e}")
            print(f"Current sys.path: {sys.path}")
        except Exception as e:
            print(f"Error processing Day {day}: {e}")


if __name__ == "__main__":
    if len(sys.argv) > 1:
        try:
            year = int(sys.argv[1])
            check_all_problems(year)
        except ValueError:
            print(f"Invalid year format: {sys.argv[1]}")
            sys.exit(1)
    else:
        check_all_problems()
