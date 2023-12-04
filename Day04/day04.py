from pathlib import Path
from pprint import *


def part1(filename):
    with Path(__file__).with_name(filename).open("r") as f:
        lines = f.read().splitlines()
    ans = 0
    lines = [i.split(": ")[1].split(" | ") for i in lines]
    for i in range(len(lines)):
        for j in range(len(lines[i])):
            lines[i][j] = lines[i][j].split(" ")

    for game in lines:
        c = 0
        for i in game[0]:
            if i.isdigit() and i in game[1]:
                c += 1
        ans += 2 ** (c - 1) if c > 0 else 0
    return ans


def part2(filename):
    with Path(__file__).with_name(filename).open("r") as f:
        lines = f.read().splitlines()
    lines = [i.split(": ")[1].split(" | ") for i in lines]
    for i in range(len(lines)):
        for j in range(len(lines[i])):
            lines[i][j] = lines[i][j].split(" ")
    dp = [1] * len(lines)
    for game in range(len(lines)):
        c = 0
        for i in lines[game][0]:
            if i.isdigit() and i in lines[game][1]:
                c += 1
        for i in range(1, c + 1):
            dp[game + i] += 1 * dp[game]
    # I have no idea how I figured this out but it works.
    return sum(dp)


if __name__ == "__main__":
    print(part1("input.txt"))
    print(part2("input.txt"))
