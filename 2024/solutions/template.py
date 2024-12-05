from tools.problem import Problem


class Day1(Problem):
    def __init__(self, load_example: bool = False):
        super().__init__(2024, 1, "Day 1", load_example)
        self.register_implementation(1, "Original", self.part1_original)


    def part1_original(self) -> int:
        return 0

    def part2_original(self) -> int:
        return 0


if __name__ == "__main__":
    day1 = Day1(load_example=False)
    day1.check_solutions()
