import abc
import csv
from typing import Dict, List


class Problem(abc.ABC):
    def __init__(self, year: int, day: int, name: str, load_example: bool = False) -> None:
        self.year: int = year
        self.day: int = day
        self.name: str = name
        self.data: List[str] = []
        self.solutions: Dict[str, int] = {}

        self._load_data(load_example)
        self._load_solutions(load_example)

    @abc.abstractmethod
    def run(self) -> int:
        raise NotImplementedError

    @abc.abstractmethod
    def run_part2(self) -> int:
        raise NotImplementedError

    def _load_data(self, load_example: bool) -> None:
        file_path = f'{self.year}/data/day{self.day}{"-intro" if load_example else ""}'
        try:
            with open(file_path) as file:
                self.data = file.readlines()
        except FileNotFoundError:
            print(f"Error: File {file_path} not found.")
            self.data = []
        except Exception as e:
            print(f"An error occurred while loading data: {e}")
            self.data = []

    def _load_solutions(self, load_example: bool) -> None:
        file_path = f'{self.year}/solutions.csv'
        try:
            with open(file_path, mode='r') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    if int(row["day"]) == self.day:
                        self.solutions = {
                            'part_1': int(row['part_1_sample']) if load_example else int(row['part_1_solution']),
                            'part_2': int(row['part_2_sample']) if load_example else int(row['part_2_solution']),
                        }
                        break
        except FileNotFoundError:
            print(f"Error: File {file_path} not found.")
        except Exception as e:
            print(f"An error occurred while loading solutions: {e}")

    def check_solutions(self) -> None:
        if not self.solutions:
            print("No solutions available, running without verification.")

        for part in (1, 2):
            run_func = self.run if part == 1 else self.run_part2
            try:
                actual = run_func()
                if not self.solutions:
                    print(f"Part {part}: {actual}")
                    continue

                expected = self.solutions[f'part_{part}']
                passed = actual == expected
                result = f"Part {part}: {'✅' if passed else '❌'} {actual}"
                if not passed:
                    result += f" (expected: {expected})"
                print(result)
            except Exception as e:
                print(f"Part {part}: ❌ Error occurred: {e}")
