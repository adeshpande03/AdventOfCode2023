from pathlib import Path
from pprint import *
from math import *
from functools import cache
from collections import OrderedDict


def part1(filename):
    with Path(__file__).with_name(filename).open("r") as f:
        lines = f.read()
    lines = lines.split(",")

    def sha(s):
        v = 0
        for i in s:
            v += ord(i)
            v = (v * 17) % 256
        return v

    return sum(list(map(sha, [i.strip() for i in lines])))


def part2(filename):
    with Path(__file__).with_name(filename).open("r") as f:
        lines = f.read()
    lines = [i.strip() for i in lines.split(",")]
    ans = [OrderedDict() for _ in range(256)]

    def sha(s):
        v = 0
        for i in s:
            v += ord(i)
            v = (v * 17) % 256
        return v

    for i in lines:
        i = i.split("=")
        if len(i) == 1:
            key = i[0][:-1]
            enc = sha(key)
            if key in ans[enc]:
                del ans[enc][key]

        else:
            key, focal = i
            enc = sha(key)
            ans[enc][key] = focal

    total = 0
    for i, j in enumerate(ans):
        for c, d in enumerate(j):
            total += (i + 1) * (c + 1) * int(j[d])
    return total


if __name__ == "__main__":
    print(part1("input.txt"))
    print(part2("input.txt"))
