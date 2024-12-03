from tools.problem import Problem


class Day1(Problem):
    def __init__(self, load_example: bool = False):
        super().__init__(2024, 1, "Day 1", load_example)

    def run(self) -> int:
        return 0

    def run_part2(self) -> int:
        return 0


if __name__ == "__main__":
    day1 = Day1(load_example=False)
    day1.check_solutions()
