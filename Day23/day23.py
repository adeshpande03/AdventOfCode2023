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

    def print_justified(list_of_lists):
        col_widths = [
            max(len(str(item)) for item in col) for col in zip(*list_of_lists)
        ]

        for row in list_of_lists:
            print(
                " ".join(str(item).ljust(width) for item, width in zip(row, col_widths))
            )

    lines = [list(i) for i in lines]
    seen = {}
    q = [(0, 1, 0)]
    m = 0
    while q:
        i = q.pop()
        r, c, l = i
        m = max(m, l)
        if seen.get((r, c), 0) > l:
            continue
        else:
            seen[(r, c)] = l
        lines[r][c] = f"{l}"
        neighbors = []
        d = [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]
        for pair in d:
            pr, pc = pair
            if pc < 0 or pc >= len(lines[0]) or pr < 0 or pr >= len(lines):
                continue
            else:
                neighbors.append(pair)
        for pair in neighbors:
            pr, pc = pair
            if lines[pr][pc] == ".":
                if seen.get((pr, pc), 0) < l + 1:
                    q.append((pr, pc, l + 1))
            elif lines[pr][pc] == ">":
                if pc - c == 1:
                    if seen.get((pr, pc + 1), 0) < l + 2:
                        q.append((pr, pc + 1, l + 2))
            elif lines[pr][pc] == "<":
                if pc - c == -1:
                    if seen.get((pr, pc - 1), 0) < l + 2:
                        q.append((pr, pc - 1, l + 2))
            elif lines[pr][pc] == "^":
                if pr - r == -1:
                    if seen.get((pr + 1, pc), 0) < l + 2:
                        q.append((pr - 1, pc, l + 2))
            elif lines[pr][pc] == "v":
                if pr - r == 1:
                    if seen.get((pr - 1, pc), 0) < l + 2:
                        q.append((pr + 1, pc, l + 2))
            elif lines[pr][pc].isdigit() and abs(int(lines[pr][pc]) - l) > 1:
                if seen.get((pr, pc), 0) < l + 1:
                    q.append((pr, pc, l + 1))

    return m


def part2(filename):
    with Path(__file__).with_name(filename).open("r") as f:
        lines = f.read().splitlines()
    edges = {} 
    for r, row in enumerate(lines):
        for c, v in enumerate(row):
            if v in ".>v":
                for dr, dc in [(-1, 0), (0, -1), (0, 1), (1, 0)]:
                    ar, ac = r + dr, c + dc
                    if not (0 <= ar < len(lines) and 0 <= ac < len(row)):
                        continue
                    if lines[ar][ac] in ".>v":
                        edges.setdefault((r, c), set()).add((ar, ac, 1))
                        edges.setdefault((ar, ac), set()).add((r, c, 1))

    while True:
        for n, e in edges.items():
            if len(e) == 2:
                a, b = e
                edges[a[:2]].remove(n + (a[2],))
                edges[b[:2]].remove(n + (b[2],))
                edges[a[:2]].add((b[0], b[1], a[2] + b[2]))
                edges[b[:2]].add((a[0], a[1], a[2] + b[2]))
                del edges[n]
                break
        else:
            break

    n, m = len(lines), len(lines[0])

    q = [(0, 1, 0)]
    visited = set()
    best = 0
    while q:
        r, c, d = q.pop()
        if d == -1:
            visited.remove((r, c))
            continue
        if (r, c) == (n - 1, m - 2):
            best = max(best, d)
            continue
        if (r, c) in visited:
            continue
        visited.add((r, c))
        q.append((r, c, -1))
        for ar, ac, l in edges[(r, c)]:
            q.append((ar, ac, d + l))
    return (best)
        



if __name__ == "__main__":
    print(part1("input.txt"))
    print(part2("input.txt"))
