from pathlib import Path


def part1(filename):
    ans = 0
    p = Path(__file__).with_name(filename)
    with p.open("r") as f:
        lines = f.readlines()
    for line in lines:
        for letter in line:
            if letter.isdigit():
                ans += int(letter) * 10
                break
        for letter in line[::-1]:
            if letter.isdigit():
                ans += int(letter)
                break
    return ans


def part2(filename):
    digit_dict = {
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9",
    }
    p = Path(__file__).with_name(filename)
    ans = 0
    with p.open() as f:
        lines = f.readlines()
    for idx, word in enumerate(lines):
        for key in digit_dict:
            numTimes = word.count(key)
            for _ in range(numTimes):
                lines[idx] = lines[idx].replace(
                    key, f"{key[:-1]}{digit_dict[key]}{key[-1:]}"
                )
    for line in lines:
        for letter in line:
            if letter.isdigit():
                ans += int(letter) * 10
                break
        for letter in line[::-1]:
            if letter.isdigit():
                ans += int(letter)
                break
    return ans


if __name__ == "__main__":
    print(part1("input.txt"))
    print(part2("input.txt"))
