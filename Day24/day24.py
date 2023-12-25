from pathlib import Path
from pprint import *
from collections import *
import math
from copy import deepcopy
from functools import cache
import numpy as np
from sympy import symbols, Eq, solve
import itertools
from z3 import Ints, Solver, Int

def part1(filename):
    with Path(__file__).with_name(filename).open("r") as f:
        lines = f.read().splitlines()
    lines2 = deepcopy(lines)
    lines = [[d.split(", ") for d in i.split(" @ ")] for i in lines]
    lines = [[list(map(int, d)) for d in i] for i in lines]
    test_area = (7, 27) if len(lines2) < 9 else (200000000000000, 400000000000000)
    c = 0
    for h1, h2 in itertools.combinations(lines, 2):
        (px1, py1, pz1), (vx1, vy1, vz1) = h1
        (px2, py2, pz2), (vx2, vy2, vz2) = h2
        slope_1 = vy1 / vx1
        inter_1 = py1 - slope_1 * px1
        slope_2 = vy2 / vx2
        inter_2 = py2 - slope_2 * px2
        if slope_1 == slope_2:
            continue
        ix = (inter_2 - inter_1) / (slope_1 - slope_2)
        iy = slope_1 * ix + inter_1
        t1 = (ix - px1) / vx1
        t2 = (ix - px2) / vx2
        if t1 < 0 or t2 < 0:
            continue
        if test_area[0] <= ix <= test_area[1] and test_area[0] <= iy <= test_area[1]:
            c += 1
    return c


def part2(filename):
    with Path(__file__).with_name(filename).open("r") as f:
        lines = f.read().splitlines()
    lines2 = deepcopy(lines)
    lines = [[d.split(", ") for d in i.split(" @ ")] for i in lines]
    lines = [[list(map(int, d)) for d in i] for i in lines]
    pxr, pyr, pzr, vxr, vyr, vzr = Ints("pxr pyr pzr vxr vyr vzr")
    s = Solver()
    for k, h in enumerate(lines[:3]):
        tK = Int(f"t{k}")
        s.add(tK > 0)
        (pxh, pyh, pzh), (vxh, vyh, vzh) = h
        s.add(pxr + tK * vxr == pxh + tK * vxh)
        s.add(pyr + tK * vyr == pyh + tK * vyh)
        s.add(pzr + tK * vzr == pzh + tK * vzh)
    s.check()
    pxr = s.model()[pxr].as_long()
    pyr = s.model()[pyr].as_long()
    pzr = s.model()[pzr].as_long()
    return pxr + pyr + pzr


if __name__ == "__main__":
    print(part1("input.txt"))
    print(part2("input.txt"))
