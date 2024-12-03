from tools.problem import Problem


def is_valid_sequence(sequence: list) -> bool:
    if len(sequence) <= 1:
        return True

    increasing = sequence[-1] > sequence[0]
    for i in range(1, len(sequence)):
        diff = sequence[i] - sequence[i - 1]
        if increasing:
            if diff <= 0 or diff > 3:
                return False
        else:
            if diff >= 0 or abs(diff) > 3:
                return False
    return True


class Day2(Problem):
    def __init__(self, load_example: bool = False):
        super().__init__(2024, 2, "Day 2", load_example)

    def parse_input(self) -> list[list[int]]:
        return [[int(x) for x in line.strip().split()] for line in self.data]

    def run(self) -> int:
        return sum(1 for sequence in self.parse_input() if is_valid_sequence(sequence))

    def run_part2(self) -> int:
        safe_count = 0
        for sequence in self.parse_input():
            if is_valid_sequence(sequence):
                safe_count += 1
                continue

            for i in range(len(sequence)):
                dampened = sequence[:i] + sequence[i + 1:]
                if is_valid_sequence(dampened):
                    safe_count += 1
                    break

        return safe_count


if __name__ == "__main__":
    day2 = Day2(load_example=False)
    day2.check_solutions()
