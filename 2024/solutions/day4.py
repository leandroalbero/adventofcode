import re

import numpy as np

from tools.problem import Problem


class Day4(Problem):
    def __init__(self, load_example: bool = False):
        super().__init__(2024, 4, "Ceres Search", load_example)
        self.register_implementation(1, "Original", self.part1_original)
        self.register_implementation(1, "Kernel", self.part1_kernel)
        self.register_implementation(2, "Original", self.part2_original)

    def part1_original(self) -> int:
        if not self.data:
            raise ValueError("Empty grid provided")

        rows = len(self.data)
        cols = len(self.data[0])
        pattern = re.compile(r"(?=(XMAS|SAMX))")
        matches = 0

        for row in range(rows):
            matches += len(pattern.findall(self.data[row]))

        for col in range(cols):
            vertical_str = "".join(self.data[row][col] for row in range(rows))
            matches += len(pattern.findall(vertical_str))

        def get_diagonal(start_row: int, start_col: int, dr: int, dc: int) -> str:
            chars = []
            r, c = start_row, start_col
            while 0 <= r < rows and 0 <= c < cols:
                chars.append(self.data[r][c])
                r += dr
                c += dc
            return "".join(chars)

        for row in range(rows):
            diagonal = get_diagonal(row, 0, 1, 1)
            if len(diagonal) >= 4:
                matches += len(pattern.findall(diagonal))

        for col in range(1, cols):
            diagonal = get_diagonal(0, col, 1, 1)
            if len(diagonal) >= 4:
                matches += len(pattern.findall(diagonal))

        for row in range(rows - 1, -1, -1):
            diagonal = get_diagonal(row, 0, -1, 1)
            if len(diagonal) >= 4:
                matches += len(pattern.findall(diagonal))

        for col in range(1, cols):
            diagonal = get_diagonal(rows - 1, col, -1, 1)
            if len(diagonal) >= 4:
                matches += len(pattern.findall(diagonal))

        return matches

    def part1_kernel(self) -> int:
        if not self.data:
            raise ValueError("Empty grid provided")

        grid = np.array([list(row) for row in self.data])
        rows, cols = grid.shape

        kernels = {
            'horizontal': np.array([[1, 1, 1, 1]]),
            'vertical': np.array([[1], [1], [1], [1]]),
            'diagonal': np.eye(4, dtype=int),
            'anti_diagonal': np.fliplr(np.eye(4, dtype=int))
        }

        def check_pattern(window: np.ndarray) -> int:
            if window.shape != (4,):
                return 0
            s = ''.join(window)
            return int('XMAS' in s or 'SAMX' in s)

        def apply_kernel(kernel: np.ndarray) -> int:
            count = 0
            for i in range(rows - kernel.shape[0] + 1):
                for j in range(cols - kernel.shape[1] + 1):
                    window = grid[i:i + kernel.shape[0], j:j + kernel.shape[1]]
                    extracted = window[kernel.astype(bool)]
                    count += check_pattern(extracted)
            return count

        return sum(apply_kernel(kernel) for kernel in kernels.values())

    def part2_original(self) -> int:
        kernels = [
            [
                ['M', None, 'S'],
                [None, 'A', None],
                ['M', None, 'S']
            ],
            [
                ['S', None, 'M'],
                [None, 'A', None],
                ['S', None, 'M']
            ],
            [
                ['M', None, 'M'],
                [None, 'A', None],
                ['S', None, 'S']
            ],
            [
                ['S', None, 'S'],
                [None, 'A', None],
                ['M', None, 'M']
            ]
        ]

        if not self.data:
            raise ValueError("Empty grid provided")

        kernel_size = 3
        if len(self.data) < kernel_size or len(self.data[0]) < kernel_size:
            raise ValueError("Grid smaller than kernel pattern")

        matches = 0
        rows = len(self.data)
        cols = len(self.data[0])

        for row in range(rows - kernel_size + 1):
            for col in range(cols - kernel_size + 1):
                for kernel in kernels:
                    match = True
                    for kr in range(kernel_size):
                        for kc in range(kernel_size):
                            grid_char = self.data[row + kr][col + kc]
                            kernel_char = kernel[kr][kc]
                            if kernel_char is not None and grid_char != kernel_char:
                                match = False
                                break
                        if not match:
                            break
                    if match:
                        matches += 1

        return matches


if __name__ == "__main__":
    day4 = Day4(load_example=False)
    day4.check_solutions()
