from pathlib import Path
from pprint import *
from math import *
from functools import cache


def part1(filename):
    with Path(__file__).with_name(filename).open("r") as f:
        lines = f.read().splitlines()
    lines = list(zip(*reversed(lines)))
    lines = ["".join(i).split("#") for i in lines]
    for i in range(len(lines)):
        for j in range(len(lines[i])):
            lines[i][j] = sorted(lines[i][j])

    new = []
    for i in lines:
        temp = []
        for j in i:
            if not j:
                temp.append("#")
                continue
            else:
                temp += j
                temp += ["#"]
        new.append(temp[:-1])
    lines = new
    ans = 0
    for i in range(len(lines)):
        for j in range(len(lines[i])):
            if lines[i][j] == "O":
                ans += j + 1
    return ans


def part2(filename):
    with Path(__file__).with_name(filename).open("r") as f:
        lines = f.read().splitlines()

    @cache
    def cycle(lines):
        for _ in range(4):
            lines = list(zip(*reversed(lines)))
            lines = ["".join(i).split("#") for i in lines]
            for i in range(len(lines)):
                for j in range(len(lines[i])):
                    lines[i][j] = sorted(lines[i][j])

            new = []
            for i in lines:
                temp = []
                for j in i:
                    if not j:
                        temp.append("#")
                        continue
                    else:
                        temp += j
                        temp += ["#"]
                new.append(tuple(temp[:-1]))
            lines = new
        return tuple(lines)

    for _ in range(1000):
        lines = cycle(tuple(lines))
        
    
    lines = list(zip(*reversed(lines)))
    ans = 0
    for i in range(len(lines)):
        for j in range(len(lines[i])):
            if lines[i][j] == "O":
                ans += j + 1

    return ans


if __name__ == "__main__":
    print(part1("input.txt"))
    print(part2("input.txt"))
