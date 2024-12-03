import re

from tools.problem import Problem


class Day3(Problem):
    def __init__(self, load_example: bool = False):
        super().__init__(2024, 3, "Day 3", load_example)

    def run(self) -> int:
        operations = re.findall(r"mul\(\d+,\d+\)", "".join(self.data))
        return sum(int(x) * int(y) for op in operations for x, y in [op[4:-1].split(",")])

    def run_part2(self) -> int:
        instructions = re.findall(r"mul\(\d{1,3},\d{1,3}\)|do\(\)|don't\(\)", "".join(self.data))
        mul_enabled = True
        results = []

        for instr in instructions:
            if instr == "do()":
                mul_enabled = True
            elif instr == "don't()":
                mul_enabled = False
            elif mul_enabled and instr.startswith("mul"):
                x, y = map(int, instr[4:-1].split(","))
                results.append(x * y)
        return sum(results)


if __name__ == "__main__":
    day3 = Day3(load_example=False)
    day3.check_solutions()
