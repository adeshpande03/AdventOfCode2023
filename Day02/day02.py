from pathlib import Path
from pprint import *


def getColorDict(s):
    d = dict()
    s = s.split(", ")
    for i in s:
        i = i.split(" ")
        num = int(i[0])
        color = i[1]
        d[color] = num
    return d


def part1(filename):
    p = Path(__file__).with_name(filename)
    with p.open("r") as f:
        lines = f.read().splitlines()
    subt = 0
    maxNumDict = {"blue": 14, "green": 13, "red": 12}
    lines = [i.split(': ')[1:][0].split("; ") for i in lines]
    for i in range(len(lines)):
        for j in range(len(lines[i])):
            lines[i][j] = getColorDict(lines[i][j])
    for idx, game in enumerate(lines):
        for roll in game:
            if (
                roll.get("blue", -1) > maxNumDict["blue"]
                or roll.get("red", -1) > maxNumDict["red"]
                or roll.get("green", -1) > maxNumDict["green"]
            ):
                subt += idx + 1
                break
    return 50 * 101 - subt


def part2(filename):
    p = Path(__file__).with_name(filename)
    with p.open("r") as f:
        lines = f.read().splitlines()
    lines = [i.split(': ')[1:][0].split("; ") for i in lines]
    for i in range(len(lines)):
        for j in range(len(lines[i])):
            lines[i][j] = getColorDict(lines[i][j])
    ans = 0
    for game in lines:
        b, g, r = 0, 0, 0
        for roll in game:
            b = max(b, roll.get("blue", 0))
            g = max(g, roll.get("green", 0))
            r = max(r, roll.get("red", 0))
        ans += b * g * r

    return ans


if __name__ == "__main__":
    print(part1("input.txt"))
    print(part2("input.txt"))
