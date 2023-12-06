from pathlib import Path
from pprint import *
from math import *


def part1(filename):
    with Path(__file__).with_name(filename).open("r") as f:
        lines = f.read().splitlines()
    lines = [list(map(int, i.split()[1:])) for i in lines]
    lines = list(zip(lines[0], lines[1]))
    ans = 1
    for i in lines[:]:
        c = 0
        n1 = 0
        n2 = i[0]
        while n2 > 0:
            n1 += 1
            n2 = i[0] - n1
            if n1 * n2 > i[1]:
                c += 1
        ans *= c
    return ans


def part2(filename):
    with Path(__file__).with_name(filename).open("r") as f:
        lines = f.read().splitlines()
    lines = [list(map(str, i.split()[1:])) for i in lines]
    lines = [int(''.join(i)) for i in lines]
    i = lines
    print(lines)
    ans = 1
    c = 0
    n1 = 0
    n2 = i[0]
    while n2 > 0:
        n1 += 1
        n2 = i[0] - n1
        if n1 * n2 > i[1]:
            c += 1
    ans *= c
    return ans



if __name__ == "__main__":
    print(part1("input.txt"))
    print(part2("input.txt"))
