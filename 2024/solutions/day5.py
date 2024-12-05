from abc import ABC, abstractmethod
from collections import defaultdict, deque
from dataclasses import dataclass, field
from typing import Dict, List, Set

from tools.problem import Problem


@dataclass
class Rule:
    prev: str
    next: str

    @classmethod
    def from_string(cls, rule_str: str) -> 'Rule':
        prev, next_page = rule_str.split('|')
        return cls(prev, next_page)


class Graph:
    def __init__(self) -> None:
        self.edges: Dict[str, List[str]] = defaultdict(list)
        self.in_degree: Dict[str, int] = defaultdict(int)
        self.vertices: Set[str] = set()

    def add_edge(self, source: str, target: str) -> None:
        self.edges[source].append(target)
        self.in_degree[target] += 1
        self.vertices.add(source)
        self.vertices.add(target)

    def get_topology(self) -> List[str]:
        result = []
        visited = set()
        queue = deque([v for v in self.vertices if self.in_degree[v] == 0])

        while queue:
            current = queue.popleft()
            if current not in visited:
                result.append(current)
                visited.add(current)

                for neighbor in self.edges[current]:
                    self.in_degree[neighbor] -= 1
                    if self.in_degree[neighbor] == 0:
                        queue.append(neighbor)

        return result if len(result) == len(self.vertices) else []


@dataclass
class RuleSet:
    rules: Dict[str, List[str]] = field(default_factory=lambda: defaultdict(list))

    def add_rule(self, rule: Rule) -> None:
        self.rules[rule.prev].append(rule.next)

    def get_next_pages(self, page: str) -> List[str]:
        return self.rules[page]

    def is_valid_transition(self, current: str, next_page: str) -> bool:
        return current in self.rules and next_page in self.rules[current]

    @classmethod
    def from_rules(cls, rules: List[Rule]) -> 'RuleSet':
        ruleset = cls()
        for rule in rules:
            ruleset.add_rule(rule)
        return ruleset


class Sequence(ABC):
    @abstractmethod
    def is_valid(self, ruleset: RuleSet) -> bool:
        pass

    @abstractmethod
    def get_middle_value(self) -> int:
        pass


class PageSequence(Sequence):
    def __init__(self, sequence: str):
        self._pages = sequence.split(',')
        self._valid = False

    @property
    def pages(self) -> List[str]:
        return self._pages

    @pages.setter
    def pages(self, new_pages: List[str]) -> None:
        self._pages = new_pages

    def is_valid(self, ruleset: RuleSet) -> bool:
        return all(
            ruleset.is_valid_transition(self.pages[i], self.pages[i + 1])
            for i in range(len(self.pages) - 1)
        )

    def get_valid_ordering(self, ruleset: RuleSet) -> None:
        graph = Graph()
        pages_set = set(self.pages)

        for page in self.pages:
            if page in ruleset.rules:
                for next_page in ruleset.get_next_pages(page):
                    if next_page in pages_set:
                        graph.add_edge(page, next_page)

        new_ordering = graph.get_topology()
        if new_ordering:
            self.pages = new_ordering
            self._valid = True

    def get_middle_value(self) -> int:
        return int(self.pages[len(self.pages) // 2])


class Day5(Problem):
    def __init__(self, load_example: bool = False):
        super().__init__(2024, 5, "Print Queue", load_example)
        self._ruleset: RuleSet = self._create_ruleset()
        self._sequences: List[PageSequence] = self._create_sequences()

        self.register_implementation(1, "Original", self.part1_original)
        self.register_implementation(2, "Original", self.part2_original)

    def _create_ruleset(self) -> RuleSet:
        rules = [Rule.from_string(line) for line in self.data if line and '|' in line]
        return RuleSet.from_rules(rules)

    def _create_sequences(self) -> List[PageSequence]:
        return [PageSequence(line) for line in self.data if line and ',' in line]

    def part1_original(self) -> int:
        return sum(
            seq.get_middle_value()
            for seq in self._sequences
            if seq.is_valid(self._ruleset)
        )

    def part2_original(self) -> int:
        invalid_sequences = [
            seq for seq in self._sequences
            if not seq.is_valid(self._ruleset)
        ]

        for seq in invalid_sequences:
            seq.get_valid_ordering(self._ruleset)

        return sum(seq.get_middle_value() for seq in invalid_sequences)


if __name__ == "__main__":
    problem = Day5(load_example=False)
    problem.check_solutions()
