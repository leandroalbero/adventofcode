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


def is_valid_sequence_alt(sequence: list) -> bool:
    if len(sequence) <= 1:
        return True

    diffs = [b - a for a, b in zip(sequence, sequence[1:])]
    increasing = diffs[0] > 0

    return all(
        (0 < d <= 3) if increasing else (-3 <= d < 0)
        for d in diffs
    )


class Day2(Problem):
    def __init__(self, load_example: bool = False):
        super().__init__(2024, 2, "Day 2", load_example)

        self.register_implementation(1, "Original", self.part1_original)
        self.register_implementation(1, "List comprehension", self.part1_list_comp)
        self.register_implementation(1, "Using filter", self.part1_filter)

        self.register_implementation(2, "Original", self.part2_original)
        self.register_implementation(2, "Using any", self.part2_using_any)
        self.register_implementation(2, "Slicing", self.part2_slicing)

    def parse_input(self) -> list[list[int]]:
        return [[int(x) for x in line.strip().split()] for line in self.data]

    def part1_original(self) -> int:
        return sum(1 for sequence in self.parse_input() if is_valid_sequence(sequence))

    def part1_list_comp(self) -> int:
        return len([seq for seq in self.parse_input() if is_valid_sequence_alt(seq)])

    def part1_filter(self) -> int:
        return len(list(filter(is_valid_sequence, self.parse_input())))

    def part2_original(self) -> int:
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

    def part2_using_any(self) -> int:
        def check_sequence(seq: list[int]) -> bool:
            if is_valid_sequence(seq):
                return True
            return any(
                is_valid_sequence(seq[:i] + seq[i + 1:])
                for i in range(len(seq))
            )

        return sum(1 for seq in self.parse_input() if check_sequence(seq))

    def part2_slicing(self) -> int:
        safe_count = 0
        for sequence in self.parse_input():
            if is_valid_sequence(sequence):
                safe_count += 1
                continue

            for i in range(len(sequence)):
                dampened = sequence[:]
                del dampened[i]
                if is_valid_sequence(dampened):
                    safe_count += 1
                    break

        return safe_count


if __name__ == "__main__":
    day2 = Day2(load_example=False)

    print("Running all implementations:")
    day2.check_solutions()

    print("\nRunning only 'Using any' implementation for part 2:")
    day2.check_solutions("Using any")

    day2.register_implementation(
        1,
        "Runtime slice validation",
        lambda: sum(
            is_valid_sequence(seq)
            for seq in [[int(x) for x in line.strip().split()]
                        for line in day2.data]
        )
    )

    print("\nRunning all implementations including runtime addition:")
    day2.check_solutions()
