
from tools.problem import Problem


def check_report(report: list) -> int:
    if len(report) <= 1:
        return -1

    increasing = report[-1] >= report[0]

    if increasing:
        for i in range(1, len(report)):
            diff = report[i] - report[i - 1]
            if diff <= 0 or diff > 3:
                return i
    else:
        for i in range(1, len(report)):
            diff = report[i] - report[i - 1]
            if diff >= 0 or abs(diff) > 3:
                return i
    return -1


class Day2(Problem):
    def __init__(self, load_example: bool = False):
        super().__init__(2024, 2, "Day 2", load_example)

    def run(self) -> int:
        numbers = []
        safe_reports = 0
        for line in self.data:
            nums = [int(x) for x in line.split()]
            numbers.append(nums)
        for report in numbers:
            try:
                if report[0] > report[-1]:  # decreasing
                    for i in range(1, len(report)):
                        assert report[i] < report[i - 1]
                        assert abs(report[i] - report[i - 1]) < 4
                else:
                    for i in range(1, len(report)):
                        assert report[i] > report[i - 1]
                        assert report[i] - report[i - 1] < 4
                safe_reports += 1
            except AssertionError:
                continue

        return safe_reports

    def run_part2(self) -> int:
        numbers = []
        safe_reports = 0
        for line in self.data:
            nums = [int(x) for x in line.strip().split()]
            numbers.append(nums)

        for report in numbers:
            is_safe = False
            result = check_report(report)

            if result == -1:
                is_safe = True
            else:
                for i in range(len(report)):
                    dampened = report[:i] + report[i + 1:]
                    if check_report(dampened) == -1:
                        is_safe = True
                        break

            if is_safe:
                safe_reports += 1

        return safe_reports


if __name__ == "__main__":
    day2 = Day2(load_example=False)
    day2.check_solutions()
