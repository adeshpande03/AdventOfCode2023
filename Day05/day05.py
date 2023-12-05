from pathlib import Path
from pprint import *
from math import *


def part1(filename):
    with Path(__file__).with_name(filename).open("r") as f:
        lines = f.read().splitlines()
    seeds = list(map(int, lines[0].split(": ")[1].split(" ")))
    lines = lines[2:]
    temp = []
    maps = []
    for i in lines:
        if i == "":
            maps.append([list(map(int, i)) for i in temp])
            temp = []
        elif i[0].isdigit():
            temp.append(i.split(" "))
    maps.append([list(map(int, i)) for i in temp])
    m = inf
    for seed in seeds[:]:
        for ma in maps:
            for part in ma:
                if seed < part[1] + part[2] and seed >= part[1]:
                    seed = seed - part[1] + part[0]
                    break
        m = min(m, seed)
    return m


def part2(filename):
    with Path(__file__).with_name(filename).open("r") as f:
        lines = f.read()
    maps = lines.split('\n\n')
    seeds = list(map(int, maps[0].split()[1:]))
    p = list(zip(seeds[::2], seeds[1::2]))
    for m in maps[1:]:
        maps2 = [list(map(int, l.split()))
                        for l in m.splitlines()[1:]]
        nr = []
        for start, r_len in p:
            while r_len != 0:
                mila = False
                best = r_len
                for e, st, length in maps2:
                    if st <= start < st+length:
                        off = start - st
                        rl = min(length - off, r_len)
                        nr.append((e+off, rl))
                        start += rl
                        r_len -= rl
                        mila = True
                        break
                    else:
                        if start < st:
                            best = min(st - start, best)
                if not mila:
                    h = min(best, r_len)
                    nr.append((start, h))
                    start += h
                    r_len -= h
        p = nr
    return min(start for start, length in p)
    


if __name__ == "__main__":
    print(part1("input.txt"))
    print(part2("input.txt"))
