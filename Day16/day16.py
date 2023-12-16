from pathlib import Path
from pprint import *
from math import *
import copy


def part1(filename):
    with Path(__file__).with_name(filename).open("r") as f:
        lines = f.read().splitlines()
    lines = [list(i) for i in lines]
    beams = [(0, -1, (0, 1))]
    seen = set()
    mirs = set()
    tot = 0
    while beams:
        i = beams.pop()
        curX = i[1]
        curY = i[0]
        dX = i[2][1]
        dY = i[2][0]
        if (curY, curX, (dY, dX)) not in seen:
            seen.add((curY, curX, (dY, dX)))
        else:
            continue
        if (
            0 <= curX < len(lines[0])
            and 0 <= curY < len(lines)
            and lines[curY][curX] == "."
        ):
            lines[curY][curX] = "#"

        newX = curX + dX
        newY = curY + dY
        if newX in [-1, len(lines[0])]:
            continue
        if newY in [-1, len(lines)]:
            continue
        if lines[newY][newX] == "|":
            if (newX, newY) not in mirs:
                tot += 1
                mirs.add((newX, newY))
            if dX in [1, -1]:
                if (newY, newX, (1, 0)) not in beams:
                    beams.append((newY, newX, (1, 0)))
                if (newY, newX, (-1, 0)) not in beams:
                    beams.append((newY, newX, (-1, 0)))
                continue
        if lines[newY][newX] == "-":
            if (newX, newY) not in mirs:
                tot += 1
                mirs.add((newX, newY))
            if dY in [1, -1]:
                if (newY, newX, (0, 1)) not in beams:
                    beams.append((newY, newX, (0, 1)))
                if (newY, newX, (0, -1)) not in beams:
                    beams.append((newY, newX, (0, -1)))
                continue
        elif lines[newY][newX] == "\\":
            if (newX, newY) not in mirs:
                tot += 1
                mirs.add((newX, newY))
            if dX in [1, -1]:
                dY = dX
                dX = 0
            elif dY in [1, -1]:
                dX = dY
                dY = 0
        elif lines[newY][newX] == "/":
            if (newX, newY) not in mirs:
                tot += 1
                mirs.add((newX, newY))
            if dX in [1, -1]:
                dY = -1 * dX
                dX = 0
            elif dY in [1, -1]:
                dX = -1 * dY
                dY = 0
        curX = newX
        curY = newY
        if (curY, curX, (dY, dX)) not in beams:
            beams.append((curY, curX, (dY, dX)))

    return sum([sum([1 for i in j if i == "#"]) for j in lines] + [tot])


def part2(filename):
    with Path(__file__).with_name(filename).open("r") as f:
        lines = f.read().splitlines()
    lines = [list(i) for i in lines]

    def getHashtags(lines, y, x, dy, dx):
        lines = copy.deepcopy(lines)
        beams = [(y, x, (dy, dx))]
        seen = set()
        mirs = set()
        tot = 0
        while beams:
            i = beams.pop()
            curX = i[1]
            curY = i[0]
            dX = i[2][1]
            dY = i[2][0]
            if (curY, curX, (dY, dX)) not in seen:
                seen.add((curY, curX, (dY, dX)))
            else:
                continue

            if (
                0 <= curX < len(lines[0])
                and 0 <= curY < len(lines)
                and lines[curY][curX] == "."
            ):
                lines[curY][curX] = "#"

            newX = curX + dX
            newY = curY + dY
            if newX in [-1, len(lines[0])]:
                continue
            if newY in [-1, len(lines)]:
                continue
            if lines[newY][newX] == "|":
                if (newX, newY) not in mirs:
                    tot += 1
                    mirs.add((newX, newY))
                if dX in [1, -1]:
                    if (newY, newX, (1, 0)) not in beams:
                        beams.append((newY, newX, (1, 0)))
                    if (newY, newX, (-1, 0)) not in beams:
                        beams.append((newY, newX, (-1, 0)))
                    continue
            if lines[newY][newX] == "-":
                if (newX, newY) not in mirs:
                    tot += 1
                    mirs.add((newX, newY))
                if dY in [1, -1]:
                    if (newY, newX, (0, 1)) not in beams:
                        beams.append((newY, newX, (0, 1)))
                    if (newY, newX, (0, -1)) not in beams:
                        beams.append((newY, newX, (0, -1)))
                    continue
            elif lines[newY][newX] == "\\":
                if (newX, newY) not in mirs:
                    tot += 1
                    mirs.add((newX, newY))
                if dX in [1, -1]:
                    dY = dX
                    dX = 0
                elif dY in [1, -1]:
                    dX = dY
                    dY = 0
            elif lines[newY][newX] == "/":
                if (newX, newY) not in mirs:
                    tot += 1
                    mirs.add((newX, newY))
                if dX in [1, -1]:
                    dY = -1 * dX
                    dX = 0
                elif dY in [1, -1]:
                    dX = -1 * dY
                    dY = 0
            curX = newX
            curY = newY
            if (curY, curX, (dY, dX)) not in beams:
                beams.append((curY, curX, (dY, dX)))

        return sum([sum([1 for i in j if i == "#"]) for j in lines] + [tot])

    ans = 0

    for i in range(len(lines)):
        ans = max(ans, getHashtags(lines, i, -1, 0, 1))
        ans = max(ans, getHashtags(lines, i, len(lines[0]), 0, -1))
    for j in range(len(lines[0])):
        ans = max(ans, getHashtags(lines, -1, j, 1, 0))
        ans = max(ans, getHashtags(lines, len(lines), j, -1, 0))

    return ans


if __name__ == "__main__":
    print(part1("input.txt"))
    print(part2("input.txt"))
