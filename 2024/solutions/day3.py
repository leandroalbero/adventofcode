import re

from tools.problem import Problem


class Day3(Problem):
    def __init__(self, load_example: bool = False):
        super().__init__(2024, 3, "Day 3", load_example)

    def run(self) -> int:
        def extract_operation(line: str) -> str | None:
            start_point = line.find("mul(")
            if start_point != -1:
                for char in line[start_point + 4:]:
                    if char not in ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0", ",", ")"]:
                        return extract_operation(line[start_point + 4:])
                    if char == ")":
                        end_point = line[start_point:].find(")") + start_point
                        return line[start_point:end_point + 1]
            return None

        total_sum = 0
        for line in self.data:
            memory = []
            while True:
                operation = extract_operation(line)
                if operation:
                    memory.append(operation)
                    line = line.replace(operation, "")
                else:
                    break
            sum = 0
            for operation in memory:
                operation = operation.replace("mul(", "")
                operation = operation.replace(")", "")
                first_operand, second_operand = operation.split(",")
                sum += int(first_operand) * int(second_operand)

            total_sum += sum
        return total_sum

    def run_part2(self) -> int:
        joined = "".join(self.data)
        pattern = r"mul\(\d{1,3},\d{1,3}\)|do\(\)|don't\(\)"
        instructions = re.findall(pattern, joined)
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
