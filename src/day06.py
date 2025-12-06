"""
AdventOfCode 2025 Day 6
https://adventofcode.com/2025/day/6
"""
import time
from pathlib import Path

example = """""", -1, -1


def solve_part1(puzzle_input) -> int:
    return 0


def solve_part2(puzzle_input) -> int:
    return 0


def main() -> None:
    if solve_part1(example[0]) != example[1]:
        print("Part 1 failed")
        exit()

    puzzle_input = Path(__file__).with_suffix(".txt").read_text()

    start = time.perf_counter()
    answer = solve_part1(puzzle_input)
    end = time.perf_counter()
    print(f"Part 1 solution: {answer}, runtime = {end - start:.3f} s")

    if solve_part1(example[0]) != example[2]:
        print("Part 2 failed")
        exit()

    start = time.perf_counter()
    answer = solve_part2(puzzle_input)
    end = time.perf_counter()
    print(f"Part 2 solution: {answer}, runtime = {end - start:.3f} s")


if __name__ == "__main__":
    main()
