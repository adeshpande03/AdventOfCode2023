from pathlib import Path
from pprint import *


def part1(filename):
    with Path(__file__).with_name(filename).open("r") as f:
        lines = f.read().splitlines()
    ans = 0
    lines = [
        [word.split(" ") for word in line]
        for line in [i.split(": ")[1].split(" | ") for i in lines]
    ]
    for game in lines:
        c = 0
        for i in game[0]:
            if i.isdigit() and i in game[1]:
                c += 1
        ans += int(2 ** (c - 1))
    return ans


def part2(filename):
    with Path(__file__).with_name(filename).open("r") as f:
        lines = f.read().splitlines()
    lines = [
        [word.split(" ") for word in line]
        for line in [i.split(": ")[1].split(" | ") for i in lines]
    ]
    dp = [1] * len(lines)
    for game in range(len(lines)):
        c = 0
        for i in lines[game][0]:
            c += 1 if i.isdigit() and i in lines[game][1] else 0
        for i in range(1, c + 1):
            dp[game + i] += dp[game]
    return sum(dp)


if __name__ == "__main__":
    print(part1("input.txt"))
    print(part2("input.txt"))
