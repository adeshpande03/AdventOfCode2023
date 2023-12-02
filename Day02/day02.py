from pathlib import Path
from pprint import *


def part1(filename):
    p = Path(__file__).with_name(filename)
    with p.open("r") as f:
        lines = f.readlines()

    def getColorDict(s):
        d = dict()
        s = s.split(", ")
        for i in s:
            i = i.split(" ")
            num = int(i[0])
            color = i[1]
            d[color] = num
        return d

    subt = 0
    maxNumDict = {"blue": 14, "green": 13, "red": 12}
    lines = [i.strip() for i in lines]
    for i in range(len(lines)):
        lines[i] = lines[i].split(": ")[1:]
    lines = [i[0].split("; ") for i in lines]
    for i in range(len(lines)):
        for j in range(len(lines[i])):
            lines[i][j] = getColorDict(lines[i][j])
    lines.insert(0, [dict()])
    for idx, game in enumerate(lines):
        if idx == 0:
            continue
        for roll in game:
            if (
                roll.get("blue", -1) > maxNumDict["blue"]
                or roll.get("red", -1) > maxNumDict["red"]
                or roll.get("green", -1) > maxNumDict["green"]
            ):
                subt += idx
                break
    return 50 * 101 - subt


def part2(filename):
    p = Path(__file__).with_name(filename)
    with p.open("r") as f:
        lines = f.readlines()
    return 0


if __name__ == "__main__":
    print(part1("input.txt"))
    print(part2("input.txt"))
