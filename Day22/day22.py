from pathlib import Path
from pprint import *
from collections import *
import math
from copy import deepcopy
from functools import cache
import numpy as np


def part1(filename):
    with Path(__file__).with_name(filename).open("r") as f:
        lines = f.read().splitlines()
    brick = []
    for line in lines:
        a, b = line.split("~")
        a = list(map(int, a.split(",")))
        b = list(map(int, b.split(",")))
        brick.append((a, b))
    n = len(brick)
    brick.sort(key=lambda x: x[0][2])
    highest = defaultdict(lambda: (0, -1))
    bad = set()
    graph = [[] for i in range(n)]
    for idx, b in enumerate(brick):
        mxh = -1
        support_set = set()
        for x in range(b[0][0], b[1][0] + 1):
            for y in range(b[0][1], b[1][1] + 1):
                if highest[x, y][0] + 1 > mxh:
                    mxh = highest[x, y][0] + 1
                    support_set = {highest[x, y][1]}
                elif highest[x, y][0] + 1 == mxh:
                    support_set.add(highest[x, y][1])
        for x in support_set:
            if x != -1:
                graph[x].append(idx)
        if len(support_set) == 1:
            bad.add(support_set.pop())
        fall = b[0][2] - mxh
        if fall > 0:
            b[0][2] -= fall
            b[1][2] -= fall

        for x in range(b[0][0], b[1][0] + 1):
            for y in range(b[0][1], b[1][1] + 1):
                highest[x, y] = (b[1][2], idx)

    return len(brick) - len(bad) + 1


def part2(filename):
    with Path(__file__).with_name(filename).open("r") as f:
        lines = f.read().splitlines()
    brick = []
    for line in lines:
        a, b = line.split("~")
        a = list(map(int, a.split(",")))
        b = list(map(int, b.split(",")))
        brick.append((a, b))
    n = len(brick)
    brick.sort(key=lambda x: x[0][2])
    highest = defaultdict(lambda: (0, -1))
    graph = [[] for i in range(n)]
    for idx, b in enumerate(brick):
        mxh = -1
        support_set = set()
        for x in range(b[0][0], b[1][0] + 1):
            for y in range(b[0][1], b[1][1] + 1):
                if highest[x, y][0] + 1 > mxh:
                    mxh = highest[x, y][0] + 1
                    support_set = {highest[x, y][1]}
                elif highest[x, y][0] + 1 == mxh:
                    support_set.add(highest[x, y][1])
        for x in support_set:
            if x != -1:
                graph[x].append(idx)
        fall = b[0][2] - mxh
        if fall > 0:
            b[0][2] -= fall
            b[1][2] -= fall
        for x in range(b[0][0], b[1][0] + 1):
            for y in range(b[0][1], b[1][1] + 1):
                highest[x, y] = (b[1][2], idx)

    def count(idx, graph):
        indeg = [0 for _ in range(n)]
        for j in range(n):
            for i in graph[j]:
                indeg[i] += 1
        q = [idx]
        count = -1
        while len(q) > 0:
            count += 1
            x = q.pop()
            for i in graph[x]:
                indeg[i] -= 1
                if indeg[i] == 0:
                    q.append(i)
        return count

    return sum(count(x, graph) for x in range(n))


if __name__ == "__main__":
    print(part1("input.txt"))
    print(part2("input.txt"))
