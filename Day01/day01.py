from pathlib import Path


def part1(filename):
    p = Path(__file__).with_name(filename)
    with p.open("r") as f:
        lines = f.readlines()
    return sum(
        [
            int(w[0] + w[-1])
            for w in ["".join([d for d in i if d.isdigit()]) for i in lines]
        ]
    )


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
    with p.open() as f:
        lines = f.readlines()
    for idx, word in enumerate(lines):
        for key in digit_dict:
            lines[idx] = lines[idx].replace(
                key, f"{key[:-1]}{digit_dict[key]}{key[-1:]}"
            )
    return sum(
        [
            int(w[0] + w[-1])
            for w in ["".join([d for d in i if d.isdigit()]) for i in lines]
        ]
    )


if __name__ == "__main__":
    print(part1("input.txt"))
    print(part2("input.txt"))
