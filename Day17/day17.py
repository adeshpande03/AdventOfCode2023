from pathlib import Path
from pprint import *
from math import *
import sys
from heapq import heappop, heappush


def part1(filename):
    with Path(__file__).with_name(filename).open("r") as f:
        lines = f.read().splitlines()
    lines = [list(map(int, list(i))) for i in lines]
    ll = lines
    DIRS = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    def inr(pos, arr):
        return pos[0] in range(len(arr)) and pos[1] in range(len(arr[0]))

    def run(mindist, maxdist):
        q = [(0, 0, 0, -1)]
        seen = set()
        costs = {}
        while q:
            cost, x, y, dd = heappop(q)
            if x == len(ll) - 1 and y == len(ll[0]) - 1:
                return cost
            if (x, y, dd) in seen:
                continue
            seen.add((x, y, dd))
            for direction in range(4):
                costincrease = 0
                if direction == dd or (direction + 2) % 4 == dd:
                    continue
                for distance in range(1, maxdist + 1):
                    xx = x + DIRS[direction][0] * distance
                    yy = y + DIRS[direction][1] * distance
                    if inr((xx, yy), ll):
                        costincrease += ll[xx][yy]
                        if distance < mindist:
                            continue
                        nc = cost + costincrease
                        if costs.get((xx, yy, direction), 1e100) <= nc:
                            continue
                        costs[(xx, yy, direction)] = nc
                        heappush(q, (nc, xx, yy, direction))

    return run(1, 3)


def part2(filename):
    with Path(__file__).with_name(filename).open("r") as f:
        lines = f.read().splitlines()
    lines = [list(map(int, list(i))) for i in lines]
    ll = lines
    DIRS = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    def inr(pos, arr):
        return pos[0] in range(len(arr)) and pos[1] in range(len(arr[0]))

    def run(mindist, maxdist):
        q = [(0, 0, 0, -1)]
        seen = set()
        costs = {}
        while q:
            cost, x, y, dd = heappop(q)
            if x == len(ll) - 1 and y == len(ll[0]) - 1:
                return cost
            if (x, y, dd) in seen:
                continue
            seen.add((x, y, dd))
            for direction in range(4):
                costincrease = 0
                if direction == dd or (direction + 2) % 4 == dd:
                    continue
                for distance in range(1, maxdist + 1):
                    xx = x + DIRS[direction][0] * distance
                    yy = y + DIRS[direction][1] * distance
                    if inr((xx, yy), ll):
                        costincrease += ll[xx][yy]
                        if distance < mindist:
                            continue
                        nc = cost + costincrease
                        if costs.get((xx, yy, direction), 1e100) <= nc:
                            continue
                        costs[(xx, yy, direction)] = nc
                        heappush(q, (nc, xx, yy, direction))

    return run(4, 10)


if __name__ == "__main__":
    print(part1("input.txt"))
    print(part2("input.txt"))
