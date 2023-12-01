from pathlib import Path


def part1(filename):
    ans = 0
    p = Path(__file__).with_name(filename)
    with p.open("r") as f:
        lines = f.readlines()
    return 0


def part2(filename):
    p = Path(__file__).with_name(filename)
    with p.open("r") as f:
        lines = f.readlines()
    return 0


if __name__ == "__main__":
    print(part1("input.txt"))
    print(part2("input.txt"))
