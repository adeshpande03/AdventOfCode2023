from pathlib import Path


def part1(filename):
    # this could be one line but its cursed enough as it is
    with Path(__file__).with_name(filename).open("r") as f:
        lines = f.read().splitlines()
    return sum(
        [
            int(w[0] + w[-1])
            for w in ["".join([d for d in i if d.isdigit()]) for i in lines]
        ]
    )


def part2(filename):
    # i could technically make this less lines it's just also cursed
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
    with Path(__file__).with_name(filename).open("r") as f:
        lines = f.read().splitlines()
    lines = [
        lines[idx].replace(key, f"{key[:-1]}{digit_dict[key]}{key[-1:]}")
        for key in digit_dict
        for idx, word in enumerate(lines)
    ]
    return sum(
        [
            int(w[0] + w[-1])
            for w in ["".join([d for d in i if d.isdigit()]) for i in lines]
        ]
    )


if __name__ == "__main__":
    print(part1("input.txt"))
    print(part2("input.txt"))
