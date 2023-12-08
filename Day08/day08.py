from pathlib import Path
from pprint import *
from math import *
from collections import OrderedDict
from functools import cache
def part1(filename):
    with Path(__file__).with_name(filename).open("r") as f:
        lines = f.read().splitlines()
    inst = lines[0]
    lines = lines[2:]
    lines = [i.split(' = ') for i in lines]
    d = {}
    for i in lines:
        d[i[0]] = tuple(i[1][1:-1].split(', '))
    lines  = d
    ans = 0
    cur = 'AAA'
    m = {'R':-1, 'L': 0}
    for i in inst*1000:
        if cur == 'ZZZ':
            break
        else:
            cur = d[cur][m.get(i)]
            
        ans += 1
    return ans


def part2(filename):
    with Path(__file__).with_name(filename).open("r") as f:
        lines = f.read().splitlines()
    inst = lines[0]
    lines = lines[2:]
    lines = [i.split(' = ') for i in lines]
    d = {}
    for i in lines:
        d[i[0]] = tuple(i[1][1:-1].split(', '))
    lines  = d
    curList = []
    for i in d:
        if i[-1] == "A":
            curList.append(i)
    m = {'R':-1, 'L': 0}
    lcmList = [] * len(curList)
    for c in curList:
        ans = 0
        for i in inst*1000:
            if c[-1] == 'Z':
                break
            else:
                c = d[c][m.get(i)]
            ans += 1
        lcmList.append(ans)
    return lcm(*lcmList)


if __name__ == "__main__":
    print(part1("input.txt"))
    print(part2("input.txt"))
