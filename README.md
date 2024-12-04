# Advent of code 🎄🧑‍💻
This repository contains my solutions for the Advent of Code challenges.

Supports multiple implementations and checks the performance of each one.

## How to use
Just run `make check-problems` to check all problems for the current year.
```md
--------------------
Checking all problems for year 2024

Checking Day 1...
Initializing <<Historian Hysteria>> (Year 2024, Day 1)
✓ Loaded data from 2024/data/day1
✓ Loaded solutions from 2024/solutions.csv

=================================================================================
Running solutions for Day 1: <<Historian Hysteria>> at 2024-12-04 02:02:03
=================================================================================

Part 1 - Initial: ✓ PASS 1938424
  ⧗ avg: 657.233µs [±301.814µs] (min: 503.458µs, max: 1.196ms, runs: 5)

Part 1 - Using sets: ✓ PASS 1938424
  ⧗ avg: 525.992µs [±119.950µs] (min: 446.958µs, max: 733.792µs, runs: 5)

Part 1 - Using zip_longest: ✓ PASS 1938424
  ⧗ avg: 487.492µs [±3.403µs] (min: 485.125µs, max: 493.500µs, runs: 5)

Part 2 - Initial: ✓ PASS 22014209
  ⧗ avg: 8.484ms [±189.362µs] (min: 8.201ms, max: 8.671ms, runs: 5)

Part 2 - Using Counter: ✓ PASS 22014209
  ⧗ avg: 569.909µs [±32.130µs] (min: 541.000µs, max: 625.000µs, runs: 5)

=================================================================================


Checking Day 2...
... skipping next days
```

Or if you prefer to run one day you can just:
```shell
python 2024/solutions/day1.py
```
And you will get the output of the solution for the different implementations:
```md
Initializing <<Mull It Over>> (Year 2024, Day 3)
✓ Loaded data from 2024/data/day3
✓ Loaded solutions from 2024/solutions.csv

=================================================================================
Running solutions for Day 3: <<Mull It Over>> at 2024-12-04 02:01:20
=================================================================================

Part 1 - Regex with list comp: ✓ PASS 174103751
  ⧗ avg: 260.817µs [±24.020µs] (min: 243.083µs, max: 303.125µs, runs: 5)

Part 1 - Regex with map: ✓ PASS 174103751
  ⧗ avg: 246.258µs [±45.358µs] (min: 215.375µs, max: 323.667µs, runs: 5)

Part 2 - Regex state machine: ✓ PASS 100411201
  ⧗ avg: 309.658µs [±40.437µs] (min: 281.209µs, max: 380.333µs, runs: 5)

Part 2 - Iterator based: ✓ PASS 100411201
  ⧗ avg: 322.167µs [±5.766µs] (min: 312.834µs, max: 328.333µs, runs: 5)

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
