from pathlib import Path
from pprint import *
from math import *


def part1(filename):
    with Path(__file__).with_name(filename).open("r") as f:
        lines = f.read().splitlines()
    t = len(lines[0])
    d = {
        "S": [],
        "-": [-1, 1],
        ".": [],
        "|": [t, -1 * t],
        "7": [-1, t],
        "J": [-1, -1 * t],
        "F": [1, t],
        "L": [1, -1 * t],
    }
    grid = "".join(lines)
    sIndex = grid.find("S")

    p = {sIndex}
    grid = [d[g] for g in grid]

    for i, o in enumerate(grid):
        if sIndex in (i + q for q in o):
            d["S"].append(i - sIndex)

    dist = 0
    new = None
    while True:
        new2 = new
        new = set()
        for r in new2 or p:
            for o in grid[r]:
                if r + o not in p:
                    new.add(r + o)
        if new:
            p |= new
            dist += 1
        else:
            break
    return dist


def part2(filename):
    with Path(__file__).with_name(filename).open("r") as f:
        lines = f.read().splitlines()
    t = len(lines[0])
    d = {
        "S": [],
        "-": [-1, 1],
        ".": [],
        "|": [t, -1 * t],
        "7": [-1, t],
        "J": [-1, -1 * t],
        "F": [1, t],
        "L": [1, -1 * t],
    }
    grid = "".join(lines)
    sIndex = grid.find("S")

    p = {sIndex}
    grid = [d[g] for g in grid]

    for i, o in enumerate(grid):
        if sIndex in (i + q for q in o):
            d["S"].append(i - sIndex)

    dist = 0
    new = None
    while True:
        new2 = new
        new = set()
        for r in new2 or p:
            for o in grid[r]:
                if r + o not in p:
                    new.add(r + o)
        if new:
            p |= new
            dist += 1
        else:
            break

    tiles = 0
    for i in range(len(grid)):
        if i in p:
            continue
        oR, oL = True, True
        k = i
        while k > 0:
            if k in p and 1 in grid[k]:
                oR = not oR
            if k in p and -1 in grid[k]:
                oL = not oL
            k -= t
        if not (oR or oL):
            tiles += 1
    return tiles


if __name__ == "__main__":
    print(part1("input.txt"))
    print(part2("input.txt"))
