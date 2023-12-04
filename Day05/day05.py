from pathlib import Path
from pprint import *


def part1(filename):
    with Path(__file__).with_name(filename).open("r") as f:
        lines = f.read().splitlines()
        

def part2(filename):
    with Path(__file__).with_name(filename).open("r") as f:
        lines = f.read().splitlines()
        

if __name__ == "__main__":
    print(part1("input.txt"))
    print(part2("input.txt"))
