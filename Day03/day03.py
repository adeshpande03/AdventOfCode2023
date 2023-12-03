from pathlib import Path
from pprint import *


def part1(filename):
    with Path(__file__).with_name(filename).open("r") as f:
        lines = f.read().splitlines()
    ans = 0
    lines = [list(i) for i in lines]
    num = ""
    replacearr = []
    for i in range(len(lines)):
        for j in range(len(lines[i])):
            if lines[i][j].isdigit():
                replacearr.append((i, j))
                num += lines[i][j]
            else:
                for idx in replacearr:
                    lines[idx[0]][idx[1]] = num
                num = ""
                replacearr = []
    ans = []
    for i in range(1, len(lines) - 1):
        for j in range(1, len(lines[i]) - 1):
            if not lines[i][j].isalnum() and not lines[i][j] == ".":
                for k in range(i - 1, i + 2):
                    for l in range(j - 1, j + 2):
                        if (
                            lines[k][l].isdigit()
                            and [int(lines[k][l]), k, i, j] not in ans
                        ):
                            ans.append([int(lines[k][l]), k, i, j])

    return sum([i[0] for i in ans])


def part2(filename):
    with Path(__file__).with_name(filename).open("r") as f:
        lines = f.read().splitlines()
    ans = 0
    lines = [list(i) for i in lines]
    num = ""
    replacearr = []
    for i in range(len(lines)):
        for j in range(len(lines[i])):
            if lines[i][j].isdigit():
                replacearr.append((i, j))
                num += lines[i][j]
            else:
                for idx in replacearr:
                    lines[idx[0]][idx[1]] = num
                num = ""
                replacearr = []
    ans = 0
    temp = set()
    for i in range(1, len(lines) - 1):
        for j in range(1, len(lines[i]) - 1):
            if not lines[i][j].isalnum() and not lines[i][j] == ".":
                for k in range(i - 1, i + 2):
                    for l in range(j - 1, j + 2):
                        if lines[k][l].isdigit():
                            temp.add(lines[k][l])
                if len(temp) == 2:
                    temp = list(temp)
                    ans += (int(temp[0]) * int(temp[1]))
                temp = set()
    return ans


if __name__ == "__main__":
    print(part1("input.txt"))
    print(part2("input.txt"))
