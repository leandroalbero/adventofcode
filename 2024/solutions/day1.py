from typing import cast

from tools.problem import Problem


class Day1(Problem):
    def __init__(self, load_example: bool = False):
        super().__init__(2024, 1, "Day 1", load_example)

    def load_into_columns(self) -> tuple[list[int], list[int]]:
        numbers: list[list[int]] = []
        for line in self.data:
            nums = [int(x) for x in line.split()]
            numbers.append(nums)

        columns: tuple[tuple[int, ...], tuple[int, ...]] = cast(
            tuple[tuple[int, ...], tuple[int, ...]],
            tuple(zip(*numbers, strict=False)),
        )
        col1: list[int] = sorted(columns[0])
        col2: list[int] = sorted(columns[1])

        return col1, col2

    def run(self) -> int:
        col1, col2 = self.load_into_columns()

        total = sum(abs(a - b) for a, b in zip(col1, col2, strict=False))
        return total

    def run_part2(self) -> int:
        col1, col2 = self.load_into_columns()

        similarity_array: list[int] = []

        for num in col1:
            coincidences = 0
            for num2 in col2:
                if num == num2:
                    coincidences += 1
            similarity_array.append(num * coincidences)

        total = sum(similarity_array)
        return total


if __name__ == "__main__":
    day1 = Day1(load_example=False)
    day1.check_solutions()
