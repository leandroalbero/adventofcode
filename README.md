# Advent of code
This repository contains my solutions for the Advent of Code challenges.

Supports multiple implementations and checks the performance of each one.

## How to use
Just run `make check-problems` to check all problems for the current year.
```shell
Checking all problems for year 2024

Checking Day 1...
Initializing Day 1 (Year 2024, Day 1)
✓ Loaded data from 2024/data/day1
✓ Loaded solutions from 2024/solutions.csv

=================================================================================
Running solutions for Day 1: Day 1 at 2024-12-04 00:44:12
=================================================================================

Part 1 - Initial: ✓ PASS 1938424
  ⧗ avg: 614.575µs [±264.039µs] (min: 471.458µs, max: 1.085ms, runs: 5)

Part 1 - Using sets: ✓ PASS 1938424
  ⧗ avg: 467.425µs [±3.972µs] (min: 462.500µs, max: 471.166µs, runs: 5)

Part 1 - Using zip_longest: ✓ PASS 1938424
  ⧗ avg: 471.800µs [±3.690µs] (min: 469.084µs, max: 478.208µs, runs: 5)

Part 2 - Initial: ✓ PASS 22014209
  ⧗ avg: 8.594ms [±114.229µs] (min: 8.436ms, max: 8.737ms, runs: 5)

Part 2 - Using Counter: ✓ PASS 22014209
  ⧗ avg: 584.850µs [±32.469µs] (min: 546.458µs, max: 623.167µs, runs: 5)

=================================================================================


Checking Day 2...
Initializing Day 2 (Year 2024, Day 2)

... ommited rest of days
```

Or if you prefer to run one day you can just:
```shell
python 2024/solutions/day1.py
```
And you will get the output of the solution for the different implementations:
```shell
Initializing Day 1 (Year 2024, Day 1)
✓ Loaded data from 2024/data/day1
✓ Loaded solutions from 2024/solutions.csv

=================================================================================
Running solutions for Day 1: Day 1 at 2024-12-04 01:56:41
=================================================================================

Part 1 - Initial: ✓ PASS 1938424
  ⧗ avg: 594.242µs [±222.712µs] (min: 486.292µs, max: 992.458µs, runs: 5)

Part 1 - Using sets: ✓ PASS 1938424
  ⧗ avg: 445.525µs [±13.815µs] (min: 428.791µs, max: 460.167µs, runs: 5)

Part 1 - Using zip_longest: ✓ PASS 1938424
  ⧗ avg: 478.783µs [±20.271µs] (min: 461.875µs, max: 512.708µs, runs: 5)

Part 2 - Initial: ✓ PASS 22014209
  ⧗ avg: 8.366ms [±157.065µs] (min: 8.243ms, max: 8.543ms, runs: 5)

Part 2 - Using Counter: ✓ PASS 22014209
  ⧗ avg: 583.467µs [±36.802µs] (min: 527.000µs, max: 630.333µs, runs: 5)

=================================================================================
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
## Contributing
Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

## License
This project is licensed under the MIT License - see the license file for details.
