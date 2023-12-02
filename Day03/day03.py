from pathlib import Path
from pprint import *


def part1(filename):
    p = Path(__file__).with_name(filename)
    with p.open("r") as f:
        lines = f.read().splitlines()


def part2(filename):
    p = Path(__file__).with_name(filename)
    with p.open("r") as f:
        lines = f.read().splitlines()
    return 0


if __name__ == "__main__":
    print(part1("input.txt"))
    print(part2("input.txt"))
