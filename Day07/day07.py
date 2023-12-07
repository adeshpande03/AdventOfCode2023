from pathlib import Path
from pprint import *
from math import *


def part1(filename):
    with Path(__file__).with_name(filename).open("r") as f:
        lines = f.read().splitlines()
    lines = [[i.split()[0], int(i.split()[1])] for i in lines]

    def t(r):
        r[0] = r[0].replace("T", "B")
        r[0] = r[0].replace("J", "C")
        r[0] = r[0].replace("Q", "D")
        r[0] = r[0].replace("K", "E")
        r[0] = r[0].replace("A", "F")
        return r

    five = []
    four = []
    full = []
    thre = []
    twop = []
    onep = []
    high = []
    for i in lines[:]:
        if (len(set(i[0]))) == 1:
            five.append(i)
        elif len(set(i[0])) == 2 and i[0].count(i[0][0]) in [1, 4]:
            four.append(i)
        elif len(set(i[0])) == 2:
            full.append(i)
        elif (
            (len(set(i[0]))) == 3
            and i[0].count(i[0][0]) == 3
            or i[0].count(i[0][1]) == 3
            or i[0].count(i[0][2]) == 3
        ):
            thre.append(i)
        elif len(set(i[0])) == 3:
            twop.append(i)
        elif len(set(i[0])) == 4:
            onep.append(i)
        else:
            high.append(i)
    ans = 0
    five.sort(reverse = True, key=t)
    four.sort(reverse = True, key=t)
    full.sort(reverse = True, key=t)
    thre.sort(reverse = True, key=t)
    high.sort(reverse = True, key=t)
    twop.sort(reverse = True, key=t)
    onep.sort(reverse = True, key=t)
    high.sort(reverse = True, key=t)
    lines = five + four + full + thre + twop + onep + high
    for i, j in enumerate(lines):
        ans += (len(lines) - (i)) * j[1]
    return ans


def part2(filename):
    with Path(__file__).with_name(filename).open("r") as f:
        lines = f.read().splitlines()
    lines = [[i.split()[0], int(i.split()[1])] for i in lines]
    m = "AKQT98765432J"[::-1]

    def t(r):
        if r == "JJJJJ":
            return "JJJJJ", "FFFFF"
        s = r
        h = set(s)
        g = r
        g = "".join([j for j in s if j != "J"])
        ltr = max(h, key=g.count)
        s = s.replace("J", ltr)
        return r, s

    def l(r):
        s = r[0][0]
        s = [m.index(x) for x in s]
        return s

    five = []
    four = []
    full = []
    thre = []
    twop = []
    onep = []
    high = []
    lines = [[t(s[0]), s[1]] for s in lines]
    ans = 0
    for i in lines[:]:
        if (len(set(i[0][1]))) == 1:
            five.append(i)
        elif len(set(i[0][1])) == 2 and i[0][1].count(i[0][1][0]) in [1, 4]:
            four.append(i)
        elif len(set(i[0][1])) == 2:
            full.append(i)
        elif (
            (len(set(i[0][1]))) == 3
            and i[0][1].count(i[0][1][0]) == 3
            or i[0][1].count(i[0][1][1]) == 3
            or i[0][1].count(i[0][1][2]) == 3
        ):
            thre.append(i)
        elif len(set(i[0][1])) == 3:
            twop.append(i)
        elif len(set(i[0][1])) == 4:
            onep.append(i)
        else:
            high.append(i)

    five.sort(reverse = True, key=l)
    four.sort(reverse = True, key=l)
    full.sort(reverse = True, key=l)
    thre.sort(reverse = True, key=l)
    high.sort(reverse = True, key=l)
    twop.sort(reverse = True, key=l)
    onep.sort(reverse = True, key=l)
    high.sort(reverse = True, key=l)
    lines = five + four + full + thre + twop + onep + high

    for i, j in enumerate(lines):
        ans += (len(lines) - (i)) * j[1]
    return ans


if __name__ == "__main__":
    print(part1("input.txt"))
    print(part2("input.txt"))
