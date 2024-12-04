from tools.problem import Problem


class Day4(Problem):
    def __init__(self, load_example: bool = False):
        super().__init__(2024, 4, "Day 4", load_example)
        self.register_implementation(1, "Original", self.part1_original)
        self.register_implementation(2, "Original", self.part2_original)

    def parse_input(self) -> list[list[str]]:
        return [line.strip().split() for line in self.data]

    def part1_original(self) -> int:
        return -1

    def part2_original(self) -> int:
        return -1


if __name__ == "__main__":
    day4 = Day4(load_example=True)
    day4.check_solutions("Original")
