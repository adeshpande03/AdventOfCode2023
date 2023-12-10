from pathlib import Path
from pprint import *
from math import *

def part1(filename):
    with Path(__file__).with_name(filename).open("r") as f:
        lines = f.read().splitlines()
    lines = [list(map(int, i.split(' ')) )for i in lines]
    def getNextNumber(diffList):
        ans = 0
        while set(diffList) != {0}:
            ans += (diffList[-1])
            diffList = [diffList[i] - diffList[i - 1] for i in range(1, len(diffList))]
        return ans
    return sum([getNextNumber(l) for l in lines])



def part2(filename):
    with Path(__file__).with_name(filename).open("r") as f:
        lines = f.read().splitlines()
    lines = [list(map(int, i.split(' ')) )for i in lines]
    def getNextNumber(diffList):
        ans = 0
        while set(diffList) != {0}:
            ans += diffList[-1]
            diffList = [diffList[i] - diffList[i - 1] for i in range(1, len(diffList))]
        return ans
    return sum([getNextNumber(l[::-1]) for l in lines])



if __name__ == "__main__":
    print(part1("input.txt"))
    print(part2("input.txt"))
