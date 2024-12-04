from collections import Counter
from itertools import zip_longest
from typing import cast

from tools.problem import Problem


class Day1(Problem):
    def __init__(self, load_example: bool = False):
        super().__init__(2024, 1, "Historian Hysteria", load_example)
        self.register_implementation(1, "Initial", self.part1_initial)
        self.register_implementation(2, "Initial", self.part2_initial)
        self.register_implementation(1, "Using sets", self.part1_sets)
        self.register_implementation(2, "Using Counter", self.part2_counter)
        self.register_implementation(
            1,
            "Using zip_longest",
            self.part1_zip_longest
        )

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

    def part1_initial(self) -> int:
        col1, col2 = self.load_into_columns()
        total = sum(abs(a - b) for a, b in zip(col1, col2, strict=False))
        return total

    def part1_sets(self) -> int:
        col1, col2 = self.load_into_columns()
        total = 0
        for i in range(len(col1)):
            total += abs(col1[i] - col2[i])
        return total

    def part1_zip_longest(self) -> int:
        col1, col2 = self.load_into_columns()
        total = 0
        for a, b in zip_longest(col1, col2):
            if a is None and b is not None:
                total += abs(b)
            elif b is None and a is not None:
                total += abs(a)
            else:
                assert a is not None and b is not None
                total += abs(a - b)
        return total

    def part2_initial(self) -> int:
        col1, col2 = self.load_into_columns()
        similarity_array: list[int] = []

        for num in col1:
            coincidences = 0
            for num2 in col2:
                if num == num2:
                    coincidences += 1
            similarity_array.append(num * coincidences)

        return sum(similarity_array)

    def part2_counter(self) -> int:
        col1, col2 = self.load_into_columns()
        counter2 = Counter(col2)
        return sum(num * counter2[num] for num in col1)


if __name__ == "__main__":
    day1 = Day1(load_example=False)
    day1.check_solutions()
