from pathlib import Path
from pprint import *
import collections
import math
from copy import deepcopy
from functools import cache
import numpy as np


def part1(filename):
    with Path(__file__).with_name(filename).open("r") as f:
        lines = f.read().splitlines()
    lines = [list(i) for i in lines]
    for i, j in enumerate(lines):
        for k, l in enumerate(j):
            if l == "S":
                sr, sc = i, k
    q = [[(sr, sc)]]
    for _ in range(64):
        gplots = q.pop(0)
        temp = set()
        for i in gplots:
            crow, ccol = i
            for trow in range(crow - 1, crow + 2):
                for tcol in range(ccol - 1, ccol + 2):
                    if (
                        0 <= trow < len(lines)
                        and 0 <= tcol < len(lines[0])
                        and (trow, tcol) != (crow, ccol)
                        and (abs(ccol - tcol) + abs(crow - trow) != 2)
                    ):
                        if lines[trow][tcol] != "#":
                            temp.add((trow, tcol))
        q.append(temp)
    return len(temp)


def part2(filename):
    with Path(__file__).with_name(filename).open("r") as f:
        lines = f.read().splitlines()
    lines = [list(i) for i in lines]
    og = deepcopy(lines)
    r = 99
    og = og * r
    og = [line * r for line in og]
    cs = []
    for i in range(len(og)):
        for j in range(len(og[i])):
            if og[i][j] == "S":
                cs.append((i, j))
    cc = cs[len(cs) // 2]
    for i in range(len(og)):
        for j in range(len(og[i])):
            if og[i][j] == "S" and cc != (i, j):
                og[i][j] = "."
    def repeat(n):
        q = [[(cc)]]
        for _ in range(n):
            gplots = q.pop(0)
            temp = set()
            for i in gplots:
                crow, ccol = i
                for trow in range(crow - 1, crow + 2):
                    for tcol in range(ccol - 1, ccol + 2):
                        if (
                            0 <= trow < len(og)
                            and 0 <= tcol < len(og[0])
                            and (trow, tcol) != (crow, ccol)
                            and (abs(ccol - tcol) + abs(crow - trow) != 2)
                        ):
                            if og[trow][tcol] != "#":
                                temp.add((trow, tcol))
            q.append(temp)
        return len(temp)

    d = {}
    for x in range(3):
        d[x] = repeat(65 + len(lines) * x)
    c = d[0]
    o = d[1] - c
    b = d[2] - c
    a = np.array([[4, 2], [1, 1]])
    cabana = np.array([[b], [o]])
    s = np.linalg.solve(a, cabana).tolist()
    s = [int(i[0]) for i in s]

    def q(x):
        return s[0] * x**2 + s[1] * x + c

    return q((26501365 - 65) // 131)


if __name__ == "__main__":
    print(part1("input.txt"))
    print(part2("input.txt"))
