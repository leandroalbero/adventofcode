import abc
import csv
import time
import tracemalloc
from dataclasses import dataclass
from datetime import datetime
from statistics import mean, stdev
from typing import Callable, Dict, List, Optional, Tuple

from colorama import Fore, Style, init

init()  # Initialize colorama


@dataclass
class TimingStats:
    mean: float
    std_dev: float
    min_time: float
    max_time: float
    runs: int


@dataclass
class MemoryStats:
    peak_memory: int
    current_memory: int
    memory_blocks: int


@dataclass
class Implementation:
    name: str
    func: Callable[[], int]
    enabled: bool = True
    timing_stats: Optional[TimingStats] = None
    memory_stats: Optional[MemoryStats] = None


@dataclass
class RunResult:
    name: str
    result: int
    timing_stats: TimingStats
    memory_stats: MemoryStats
    passed: bool


class Problem(abc.ABC):
    def __init__(self, year: int, day: int, name: str, load_example: bool = False) -> None:
        self.year: int = year
        self.day: int = day
        self.name: str = name
        self.data: List[str] = []
        self.solutions: Dict[str, int] = {}
        self.implementations: Dict[int, Dict[str, Implementation]] = {1: {}, 2: {}}

        print(f"{Fore.CYAN}Initializing <<{self.name}>> (Year {self.year}, Day {self.day}){Style.RESET_ALL}")
        self._load_data(load_example)
        self._load_solutions(load_example)

    def register_implementation(self, part: int, name: str, func: Callable[[], int], enabled: bool = True) -> None:
        if part not in (1, 2):
            raise ValueError("Part must be 1 or 2")
        self.implementations[part][name] = Implementation(name, func, enabled)

    def _load_data(self, load_example: bool) -> None:
        file_path = f'{self.year}/data/day{self.day}{"-intro" if load_example else ""}'
        try:
            with open(file_path) as file:
                self.data = [line.rstrip() for line in file]
            print(f"{Fore.GREEN}✓ Loaded data from {file_path}{Style.RESET_ALL}")
        except FileNotFoundError:
            print(f"{Fore.RED}✗ Error: File {file_path} not found.{Style.RESET_ALL}")
            self.data = []
        except Exception as e:
            print(f"{Fore.RED}✗ Error loading data: {e}{Style.RESET_ALL}")
            self.data = []

    def _load_solutions(self, load_example: bool) -> None:
        file_path = f'{self.year}/solutions.csv'
        try:
            with open(file_path, mode='r') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    if int(row["day"]) == self.day:
                        self.solutions = {
                            'part_1': int(row['part_1_sample']) if load_example else int(row['part_1_solution']),
                            'part_2': int(row['part_2_sample']) if load_example else int(row['part_2_solution']),
                        }
                        print(f"{Fore.GREEN}✓ Loaded solutions from {file_path}{Style.RESET_ALL}")
                        break
        except FileNotFoundError:
            print(f"{Fore.RED}✗ Error: File {file_path} not found.{Style.RESET_ALL}")
        except Exception as e:
            print(f"{Fore.RED}✗ Error loading solutions: {e}{Style.RESET_ALL}")

    def _measure_memory(self, func: Callable[[], int]) -> Tuple[int, MemoryStats]:
        tracemalloc.start()
        result = func()
        snapshot = tracemalloc.take_snapshot()
        stats = snapshot.statistics('lineno')
        current, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()

        return result, MemoryStats(
            peak_memory=peak,
            current_memory=current,
            memory_blocks=len(stats)
        )

    def _format_memory(self, bytes: int) -> str:
        if bytes >= 1_000_000_000:
            return f"{bytes / 1_000_000_000:.2f} GB"
        elif bytes >= 1_000_000:
            return f"{bytes / 1_000_000:.2f} MB"
        elif bytes >= 1_000:
            return f"{bytes / 1_000:.2f} KB"
        else:
            return f"{bytes} B"

    def _measure_performance(self, func: Callable[[], int], runs: int = 5) -> TimingStats:
        timings = []
        for _ in range(runs):
            start_time = time.perf_counter_ns()
            func()
            elapsed = time.perf_counter_ns()
            timings.append((elapsed - start_time) / 1e6)  # Convert to milliseconds

        return TimingStats(
            mean=mean(timings),
            std_dev=stdev(timings) if len(timings) > 1 else 0,
            min_time=min(timings),
            max_time=max(timings),
            runs=runs
        )

    def _format_time(self, ms: float) -> str:
        if ms >= 1000:
            return f"{ms / 1000:.3f}s"
        elif ms >= 1:
            return f"{ms:.3f}ms"
        elif ms >= 0.001:
            return f"{ms * 1000:.3f}µs"
        else:
            return f"{ms * 1000000:.3f}ns"

    def _get_performance_indicators(self, results: List[RunResult]) -> Dict[str, List[str]]:
        indicators: Dict[str, List[str]] = {}
        if not results:
            return {}

        indicators = {result.name: [] for result in results}

        # Find fastest implementation
        fastest = min(results, key=lambda x: x.timing_stats.mean)
        indicators[fastest.name].append(f"{Fore.YELLOW}⚡ FASTEST{Style.RESET_ALL}")

        # Find most memory efficient implementation
        most_efficient = min(results, key=lambda x: x.memory_stats.peak_memory)
        indicators[most_efficient.name].append(f"{Fore.BLUE}💎 MEMORY{Style.RESET_ALL}")

        return indicators

    def _run_implementation(self, part: int, name: str, impl: Implementation, solution: Optional[int] = None) -> \
    Optional[RunResult]:
        if not impl.enabled:
            print(f"{Fore.YELLOW}Part {part} - {name}: SKIPPED{Style.RESET_ALL}")
            return None

        try:
            # Measure memory first in isolation
            result, memory_stats = self._measure_memory(impl.func)
            # Then measure timing
            timing_stats = self._measure_performance(impl.func)

            passed = solution is None or result == solution
            return RunResult(name, result, timing_stats, memory_stats, passed)

        except Exception as e:
            print(f"{Fore.RED}Part {part} - {name}: ✗ Error occurred: {e}{Style.RESET_ALL}\n")
            return None

    def _print_results(self, part: int, results: List[RunResult], indicators: Dict[str, List[str]],
                       solution: Optional[int] = None) -> None:
        for run in results:
            timing_info = (
                f"avg: {self._format_time(run.timing_stats.mean)} "
                f"[±{self._format_time(run.timing_stats.std_dev)}] "
                f"(min: {self._format_time(run.timing_stats.min_time)}, "
                f"max: {self._format_time(run.timing_stats.max_time)}, "
                f"runs: {run.timing_stats.runs})"
            )

            memory_info = (
                f"peak: {self._format_memory(run.memory_stats.peak_memory)} "
                f"final: {self._format_memory(run.memory_stats.current_memory)} "
                f"blocks: {run.memory_stats.memory_blocks}"
            )

            status = f"{Fore.GREEN}✓ PASS{Style.RESET_ALL}" if run.passed else f"{Fore.RED}✗ FAIL{Style.RESET_ALL}"
            perf_indicators = ' '.join(indicators.get(run.name, []))

            result_str = f"Part {part} - {run.name}: {status} {run.result} {perf_indicators}"

            if not run.passed and solution is not None:
                result_str += f" {Fore.RED}(expected: {solution}){Style.RESET_ALL}"

            print(result_str)
            print(f"{Fore.CYAN}  ⧗ {timing_info}{Style.RESET_ALL}")
            print(f"{Fore.MAGENTA}  📊 {memory_info}{Style.RESET_ALL}\n")

    def check_solutions(self, implementation_name: Optional[str] = None) -> None:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"\n{Fore.CYAN}={'=' * 80}{Style.RESET_ALL}")
        print(f"{Fore.CYAN}Running solutions for Day {self.day}: <<{self.name}>> at {timestamp}{Style.RESET_ALL}")
        print(f"{Fore.CYAN}={'=' * 80}{Style.RESET_ALL}\n")

        if not self.solutions and implementation_name is not None:
            print(f"{Fore.YELLOW}No solutions available, running without verification.{Style.RESET_ALL}\n")

        for part in (1, 2):
            solution = self.solutions.get(f'part_{part}') if self.solutions else None
            implementations = self.implementations[part]

            if not implementations:
                print(f"{Fore.YELLOW}No implementations registered for part {part}{Style.RESET_ALL}\n")
                continue

            if implementation_name is not None:
                if implementation_name in implementations:
                    result = self._run_implementation(part, implementation_name,
                                                      implementations[implementation_name], solution)
                    if result:
                        self._print_results(part, [result], self._get_performance_indicators([result]), solution)
                else:
                    print(
                        f"{Fore.RED}Implementation '{implementation_name}' not found for part {part}{Style.RESET_ALL}\n")
            else:
                results = []
                for name, impl in implementations.items():
                    result = self._run_implementation(part, name, impl, solution)
                    if result:
                        results.append(result)

                indicators = self._get_performance_indicators(results)
                self._print_results(part, results, indicators, solution)

        print(f"{Fore.CYAN}={'=' * 80}{Style.RESET_ALL}\n")
