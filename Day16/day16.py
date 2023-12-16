from pathlib import Path
from pprint import *
from math import *
from functools import cache
import numpy as np


def part1(filename):
    with Path(__file__).with_name(filename).open("r") as f:
        lines = f.read().splitlines()
    lines = [list(i) for i in lines]
    beams = [(0, -1, (0, 1))]

    def show(lines):
        return "\n".join(["".join(i) for i in lines])

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
        if 0 <= curX < len(lines[0]) and 0 <= curY < len(lines):
            if lines[curY][curX] == ".":
                lines[curY][curX] = "#"
        else:
            newX = curX + dX
            newY = curY + dY
            curX = newX
            curY = newY
            if (curY, curX, (dY, dX)) not in beams:
                beams.append((curY, curX, (dY, dX)))
            continue

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

    for i in enumerate(lines):
        for j in enumerate(i[1]):
            if j[1] == "#":
                tot += 1
    if lines[0][0] == ".":
        return tot - 1
    pprint(lines)
    return tot


def part2(filename):
    with Path(__file__).with_name(filename).open("r") as f:
        lines = f.read().splitlines()
    directions = {"right": (0, 1), "up": (-1, 0), "down": (1, 0), "left": (0, -1)}

    def find_energized(direction, position):
        q = []
        visited = np.zeros((len(lines), len(lines[0])))
        ds = {}
        q.append((direction, position))
        while len(q):
            direction, position = q.pop()
            i, j = tuple([sum(x) for x in zip(direction, position)])
            if (i not in range(len(lines))) or (j not in range(len(lines))):
                continue
            char = lines[i][j]
            visited[i][j] = 1
            if (i, j) in ds:
                if direction in ds[(i, j)]:
                    continue
                ds[(i, j)].append(direction)
            else:
                ds[(i, j)] = [direction]
            if char == "/":
                if direction == directions["up"]:
                    q.append((directions["right"], (i, j)))
                elif direction == directions["down"]:
                    q.append((directions["left"], (i, j)))
                elif direction == directions["left"]:
                    q.append((directions["down"], (i, j)))
                elif direction == directions["right"]:
                    q.append((directions["up"], (i, j)))
            elif char == "\\":
                if direction == directions["up"]:
                    q.append((directions["left"], (i, j)))
                elif direction == directions["down"]:
                    q.append((directions["right"], (i, j)))
                elif direction == directions["left"]:
                    q.append((directions["up"], (i, j)))
                elif direction == directions["right"]:
                    q.append((directions["down"], (i, j)))
            elif char == "-":
                if direction == directions["up"] or direction == directions["down"]:
                    q.append((directions["left"], (i, j)))
                    q.append((directions["right"], (i, j)))
                else:
                    q.append((direction, (i, j)))
            elif char == "|":
                if direction == directions["left"] or direction == directions["right"]:
                    q.append((directions["up"], (i, j)))
                    q.append((directions["down"], (i, j)))
                else:
                    q.append((direction, (i, j)))
            else:
                q.append((direction, (i, j)))
        return np.sum(visited)

    m = 0
    for i in range(len(lines)):
        m = max(m, find_energized(directions["right"], (i, -1)))
        m = max(m, find_energized(directions["left"], (i, len(lines[0]))))
    for j in range(len(lines[0])):
        m = max(m, find_energized(directions["down"], (-1, j)))
        m = max(m, find_energized(directions["up"], (len(lines), j)))
    print(m)
    return 0


if __name__ == "__main__":
    print(part1("sample.txt"))
    print(part2("input.txt"))
