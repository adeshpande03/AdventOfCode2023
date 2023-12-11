from pathlib import Path
from pprint import *
from math import *


def part1(filename):
    with Path(__file__).with_name(filename).open("r") as f:
        lines = f.read().splitlines()
    blankRows = []
    blankCols = []
    for i in range(len(lines)):
        if lines[i].count("#") > 0:
            continue
        else:
            blankRows.append(i)
    temp = list(zip(*(lines)))
    for i in range(len(temp)):
        if temp[i].count("#") > 0:
            continue
        else:
            blankCols.append(i)
    locs = []
    for i in range(len(lines)):
        for j in range(len(lines[i])):
            if lines[i][j] == "#":
                locs.append((i, j))
    ans = 0
    def getDists(loc1, loc2):
        basicXDist = abs(loc1[0] - loc2[0])
        basicYDist = abs(loc1[1] - loc2[1])
        moreX, moreY = 0, 0
        for i in blankRows:
            if loc1[0] < i < loc2[0] or loc2[0] < i < loc1[0]:
                moreX += 1 
        for i in blankCols:
            if loc1[1] < i < loc2[1] or loc2[1] < i < loc1[1]:
                moreY += 1
        return basicXDist + basicYDist + moreX + moreY

    for i in range(len(locs)):
        for j in range(i, len(locs)):
            ans += getDists(locs[i], locs[j])
    return ans


def part2(filename):
    with Path(__file__).with_name(filename).open("r") as f:
        lines = f.read().splitlines()
    blankRows = []
    blankCols = []
    for i in range(len(lines)):
        if lines[i].count("#") > 0:
            continue
        else:
            blankRows.append(i)
    temp = list(zip(*(lines)))
    for i in range(len(temp)):
        if temp[i].count("#") > 0:
            continue
        else:
            blankCols.append(i)
    locs = []
    for i in range(len(lines)):
        for j in range(len(lines[i])):
            if lines[i][j] == "#":
                locs.append((i, j))
    ans = 0
    def getDists(loc1, loc2):
        basicXDist = abs(loc1[0] - loc2[0])
        basicYDist = abs(loc1[1] - loc2[1])
        moreX, moreY = 0, 0
        for i in blankRows:
            if loc1[0] < i < loc2[0] or loc2[0] < i < loc1[0]:
                moreX += 10**6 - 1
        for i in blankCols:
            if loc1[1] < i < loc2[1] or loc2[1] < i < loc1[1]:
                moreY += 10**6 - 1
        return basicXDist + basicYDist + moreX + moreY

    for i in range(len(locs)):
        for j in range(i, len(locs)):
            ans += getDists(locs[i], locs[j])
    return ans


if __name__ == "__main__":
    print(part1("input.txt"))
    print(part2("input.txt"))
