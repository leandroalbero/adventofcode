# Advent of code
This repository contains my solutions for the Advent of Code challenges.

## How to use
Just run `make check-problems` to check all problems for the current year.
```shell
Checking Day 1...
Part 1: ✅ 1938424
Part 2: ✅ 22014209

Checking Day 2...
Part 1: ✅ 299
Part 2: ✅ 364

Checking Day 3...
Part 1: ✅ 174103751
Part 2: ✅ 100411201
... 
```

Linting code is easy, just run `make lint` to check all the code. It runs `ruff` and `mypy`
```shell
make lint
```

## Structure
The repository is structured as follows:
```
.
├── 2024                # One folder per year of AoC
│   ├── data            # Input data for each problem
│   │   ├── day1
│   │   ├── day1-intro
│   ├── docs            # Description of each of the problems
│   │   ├── day1.md
│   ├── solutions       # Solutions for each problem
│   │   ├── day1.py
│   │   └── template.py
│   └── solutions.csv   # CSV file with all the values of the solutions
├── Makefile
├── README.md
├── pyproject.toml
├── requirements.txt
├── setup.cfg
└── tools
    ├── helpers.py
    └── problem.py
```