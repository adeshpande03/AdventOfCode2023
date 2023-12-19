from pathlib import Path
from pprint import *
import sys
import re
from copy import deepcopy
from math import gcd
from collections import defaultdict, Counter, deque
import heapq


def part1(filename):
    with Path(__file__).with_name(filename).open("r") as f:
        lines = f.read()
    flows, nums = lines.split("\n\n")
    flows = [i.strip() for i in flows.split()]
    nums = [i.strip() for i in nums.split()]
    nums = [i[1:-1] for i in nums]
    numsList = []
    for line in nums:
        numsDict = {}
        line = line.split(",")
        for i in line:
            i = i.split("=")
            numsDict[i[0]] = int(i[1])
        numsList.append(numsDict)
    # pprint(nums)
    # pprint(numsList)
    flowList = {}
    for flow in flows:
        flow = flow[:-1]
        name, rule = flow.split("{")
        rule = rule.split(",")
        flowList[name] = rule
    # pprint(flowList)
    A = []
    R = []
    for nums in numsList[::1]:
        cur = "in"
        while True:
            x = nums.get("x")
            m = nums.get("m")
            a = nums.get("a")
            s = nums.get("s")
            if cur == "A":
                A.append(nums)
                break
            elif cur == "R":
                break
            rules = flowList[cur]
            il = []
            for rule in rules:
                if ":" in rule:
                    rule = rule.split(":")
                    il.append(eval(rule[0]))
            il.append(rules[-1])
            if not any(il[:-1]):
                cond = il[-1]
                if cond == "A":
                    A.append(nums)
                    break
                elif cond == "R":
                    R.append(nums)
                    break
                else:
                    cur = cond
            for i, j in enumerate(il):
                if j == True:
                    cur = rules[i].split(":")[1]
                    break

    ans = 0
    for i in A:
        for num in i:
            ans += i[num]

    return ans


def part2(filename):
    with Path(__file__).with_name(filename).open("r") as f:
        D = f.read().strip()
    L = D.split("\n")
    G = [[c for c in row] for row in L]
    R = len(G)
    C = len(G[0])
    rules, parts = D.split("\n\n")
    R = {}
    for rule in rules.split("\n"):
        name, rest = rule.split("{")
        R[name] = rest[:-1]

    def accepted(part):
        state = "in"
        while True:
            rule = R[state]
            for cmd in rule.split(","):
                applies = True
                res = cmd
                if ":" in cmd:
                    cond, res = cmd.split(":")
                    var = cond[0]
                    op = cond[1]
                    n = int(cond[2:])
                    if op == ">":
                        applies = part[var] > n
                    else:
                        applies = part[var] < n
                if applies:
                    if res == "A":
                        return True
                    if res == "R":
                        return False
                    state = res
                    break

    def new_range(op, n, lo, hi):
        if op == ">":
            lo = max(lo, n + 1)
        elif op == "<":
            hi = min(hi, n - 1)
        elif op == ">=":
            lo = max(lo, n)
        elif op == "<=":
            hi = min(hi, n)
        else:
            assert False
        return (lo, hi)

    def new_ranges(var, op, n, xl, xh, ml, mh, al, ah, sl, sh):
        if var == "x":
            xl, xh = new_range(op, n, xl, xh)
        elif var == "m":
            ml, mh = new_range(op, n, ml, mh)
        elif var == "a":
            al, ah = new_range(op, n, al, ah)
        elif var == "s":
            sl, sh = new_range(op, n, sl, sh)
        return (xl, xh, ml, mh, al, ah, sl, sh)

    ans = 0
    ans = 0
    Q = deque([("in", 1, 4000, 1, 4000, 1, 4000, 1, 4000)])
    while Q:
        state, xl, xh, ml, mh, al, ah, sl, sh = Q.pop()
        if xl > xh or ml > mh or al > ah or sl > sh:
            continue
        if state == "A":
            score = (xh - xl + 1) * (mh - ml + 1) * (ah - al + 1) * (sh - sl + 1)
            ans += score
            continue
        elif state == "R":
            continue
        else:
            rule = R[state]
            for cmd in rule.split(","):
                applies = True
                res = cmd
                if ":" in cmd:
                    cond, res = cmd.split(":")
                    var = cond[0]
                    op = cond[1]
                    n = int(cond[2:])
                    Q.append(
                        (res, *new_ranges(var, op, n, xl, xh, ml, mh, al, ah, sl, sh))
                    )
                    xl, xh, ml, mh, al, ah, sl, sh = new_ranges(
                        var,
                        "<=" if op == ">" else ">=",
                        n,
                        xl,
                        xh,
                        ml,
                        mh,
                        al,
                        ah,
                        sl,
                        sh,
                    )
                else:
                    Q.append((res, xl, xh, ml, mh, al, ah, sl, sh))
                    break
    return ans

if __name__ == "__main__":
    print(part1("input.txt"))
    print(part2("input.txt"))
