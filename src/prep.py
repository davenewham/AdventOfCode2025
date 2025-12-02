"""
Prepare for a new day of AoC.
(1) Create a dayNN.py file for the code.
(2) Create a dayNN.txt file for the puzzle input text.
"""
import argparse
from pathlib import Path
from string import Template

template = Template('''"""
AdventOfCode 2025 Day $day
"""
from pathlib import Path

example = """
"""


def solve() -> int:
    ...


def main() -> None:
    puzzle_input = Path(__file__).with_suffix(".txt").read_text()
    print(puzzle_input)


if __name__ == "__main__":
    main()
''')


def main() -> None:
    parser = argparse.ArgumentParser(description="Prepare for a new day of AoC (1...12).")
    parser.add_argument("day", metavar="DAY", type=int, choices=range(1, 13))
    args = parser.parse_args()
    prog = Path(f"day{args.day:02d}.py")
    prog.write_text(template.substitute(day=args.day))
    prog.with_suffix(".txt").write_text("Puzzle input...")


if __name__ == "__main__":
    main()
