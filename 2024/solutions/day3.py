import re
from typing import Generator

from tools.problem import Problem


class Day3(Problem):
    def __init__(self, load_example: bool = False):
        super().__init__(2024, 3, "Mull It Over", load_example)

        self.register_implementation(1, "Regex with list comp", self.part1_regex_listcomp)
        self.register_implementation(1, "Regex with map", self.part1_regex_map)

        self.register_implementation(2, "Regex state machine", self.part2_regex_state)
        self.register_implementation(2, "Iterator based", self.part2_iterator)

    def part1_regex_listcomp(self) -> int:
        operations = re.findall(r"mul\(\d+,\d+\)", "".join(self.data))
        return sum(int(x) * int(y) for op in operations for x, y in [op[4:-1].split(",")])

    def part1_regex_map(self) -> int:
        operations = re.findall(r"mul\((\d+),(\d+)\)", "".join(self.data))
        return sum(int(x) * int(y) for x, y in operations)

    def part2_regex_state(self) -> int:
        instructions = re.findall(
            r"mul\(\d{1,3},\d{1,3}\)|do\(\)|don't\(\)",
            "".join(self.data)
        )
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

    def part2_iterator(self) -> int:
        def instruction_parser(data: str) -> Generator:
            pattern = re.compile(r"mul\(\d{1,3},\d{1,3}\)|do\(\)|don't\(\)")
            mul_enabled = True

            for match in pattern.finditer(data):
                instr = match.group()
                if instr == "do()":
                    mul_enabled = True
                elif instr == "don't()":
                    mul_enabled = False
                elif mul_enabled and instr.startswith("mul"):
                    x, y = map(int, instr[4:-1].split(","))
                    yield x * y

        return sum(instruction_parser("".join(self.data)))


if __name__ == "__main__":
    day3 = Day3(load_example=False)
    day3.check_solutions()
