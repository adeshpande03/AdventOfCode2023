from pathlib import Path
from pprint import *
from math import *
import time


def part1(filename):
    with Path(__file__).with_name(filename).open("r") as f:
        lines = f.read().splitlines()
    lines = [(int(i.split()[:2][1]), i.split()[:2][0])[::-1] for i in lines]
    dirs = {"R": (0, 1), "D": (1, 0), "L": (0, -1), "U": (-1, 0)}
    borders = []
    cX = cY = 0
    for line in lines:
        d, l = line
        dy, dx = dirs[d]
        borders.append((cY + dy * l, cX + dx * l + 1))
        cY, cX = cY + dy * l, cX + dx * l
    t = sum([i[1] for i in lines]) / 2 + 1
    for i, j in enumerate(borders[:-1]):
        t += (j[0] + borders[i + 1][0]) * (j[1] - borders[i + 1][1]) / 2
    return int(t)


def part2(filename):
    with Path(__file__).with_name(filename).open("r") as f:
        lines = f.read().splitlines()
    danceFloor = {"1": "D", "2": "L", "3": "U", "0": "R"}
    lines = [
        (int(i.split()[-1][2:-1][:5], 16), danceFloor[i.split()[-1][2:-1][5:]])[::-1]
        for i in lines
    ]
    dirs = {"R": (0, 1), "D": (1, 0), "L": (0, -1), "U": (-1, 0)}
    borders = []
    cX = cY = 0
    for line in lines:
        d, l = line
        dy, dx = dirs[d]
        borders.append((cY + dy * l, cX + dx * l + 1))
        cY, cX = cY + dy * l, cX + dx * l
    t = sum([i[1] for i in lines]) / 2 + 1
    for i, j in enumerate(borders[:-1]):
        t += (j[0] + borders[i + 1][0]) * (j[1] - borders[i + 1][1]) / 2
    return int(t)


if __name__ == "__main__":
    s = time.perf_counter()
    print(part1("input.txt"))
    print(part2("input.txt"))
