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


def get_substring(input_line, is_end=False):
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
    new_line_part = ""
    replaced = False

    for char in input_line:
        new_line_part = new_line_part + char if not is_end else char + new_line_part

        for k, v in digit_dict.items():
            if k in new_line_part:
                new_line_part = new_line_part.replace(k, v)
                replaced = True
                break
        if replaced:
            break
    return new_line_part


def part2(filename):
    p = Path(__file__).with_name(filename)
    with p.open("r") as f:
        lines = f.readlines()
        total = 0
        for line in lines:
            new_line_start = get_substring(line, False)
            new_line_end = get_substring(line[::-1], True)
            new_line = new_line_start + new_line_end
            digits = "".join([char for char in new_line if char.isdigit()])
            total += int(digits[0] + digits[-1])
        return total


if __name__ == "__main__":
    print(part1("input.txt"))
    print(part2("input.txt"))
