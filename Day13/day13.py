from pathlib import Path
from pprint import *
from math import *


def part1(filename):
    with Path(__file__).with_name(filename).open("r") as f:
        lines = f.read().split("\n\n")
    ps = list(map(str.splitlines, lines))

    def f(p, s):
        for i in range(1, len(p)):
            if (
                sum(
                    c1 != c2
                    for r1, r2 in zip(p[i - 1 :: -1], p[i:])
                    for c1, c2 in zip(r1, r2)
                )
                == s
            ):
                return i
        else:
            return 0

    ans = sum(100 * f(p, 0) + f([*zip(*p)], 0) for p in ps)
    return ans


def part2(filename):
    with Path(__file__).with_name(filename).open("r") as f:
        lines = f.read().split("\n\n")
    ps = list(map(str.splitlines, lines))

    def f(p, s):
        for i in range(1, len(p)):
            if (
                sum(
                    c1 != c2
                    for r1, r2 in zip(p[i - 1 :: -1], p[i:])
                    for c1, c2 in zip(r1, r2)
                )
                == s
            ):
                return i
        else:
            return 0

    ans = sum(100 * f(p, 1) + f([*zip(*p)], 1) for p in ps)
    return ans


if __name__ == "__main__":
    print(part1("input.txt"))
    print(part2("input.txt"))
