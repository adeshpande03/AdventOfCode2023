from pathlib import Path
from pprint import *
import collections
import math


def part1(filename):
    with Path(__file__).with_name(filename).open("r") as f:
        lines = f.read().splitlines()
        m = {}

        for line in lines:
            a, b = line.split(" -> ")
            b = b.split(", ")

            if a == "broadcaster":
                t = None
            else:
                t = a[0]
                a = a[1:]

            assert a not in m
            m[a] = (t, b)

        data = m

        num_low = 0
        num_high = 0
        memory = {}

        input_map = collections.defaultdict(list)

        for node, (_, dests) in data.items():
            for d in dests:
                input_map[d].append(node)

        for node, (t, _) in data.items():
            if t is None:
                continue
            if t == "%":
                memory[node] = False
            if t == "&":
                memory[node] = {d: False for d in input_map[node]}

        for _ in range(1000):
            todo = [(None, "broadcaster", False)]

            while todo:
                new_todo = []

                for src, node, is_high_pulse in todo:
                    if is_high_pulse:
                        num_high += 1
                    else:
                        num_low += 1

                    info = data.get(node)
                    if info is None:
                        continue

                    t, dests = info
                    if t == "%":
                        if is_high_pulse:
                            continue
                        state = memory[node]
                        memory[node] = not state
                        for d in dests:
                            new_todo.append((node, d, not state))
                        continue
                    if t == "&":
                        state = memory[node]
                        state[src] = is_high_pulse

                        if sum(state.values()) == len(state):
                            # All are high, send a low pulse
                            to_send = False
                        else:
                            to_send = True

                        for d in dests:
                            new_todo.append((node, d, to_send))
                        continue
                    if t is None:
                        for d in dests:
                            new_todo.append((node, d, is_high_pulse))
                        continue
                    assert False

                todo = new_todo

        answer = num_low * num_high
        return answer

def part2(filename):
    with Path(__file__).with_name(filename).open("r") as f:
        lines = f.read().splitlines()
        m = {}

        for line in lines:
            a, b = line.split(" -> ")
            b = b.split(", ")

            if a == "broadcaster":
                t = None
            else:
                t = a[0]
                a = a[1:]

            assert a not in m
            m[a] = (t, b)

        data = m

        num_low = 0
        num_high = 0
        memory = {}

        input_map = collections.defaultdict(list)

        for node, (_, dests) in data.items():
            for d in dests:
                input_map[d].append(node)

        for node, (t, _) in data.items():
            if t is None:
                continue
            if t == "%":
                memory[node] = False
            if t == "&":
                memory[node] = {d: False for d in input_map[node]}

        assert len(input_map["rx"]) == 1

        single = input_map["rx"][0]

        assert data[single][0] == "&"

        sources = input_map[single]

        assert all(data[s][0] == "&" for s in sources)

        low_counts = {}

        cycle = 0

        while len(low_counts) < len(sources):
            cycle += 1
            todo = [(None, "broadcaster", False)]

            while todo:
                new_todo = []

                for src, node, is_high_pulse in todo:
                    if node in sources:
                        if not is_high_pulse:
                            if node not in low_counts:
                                low_counts[node] = cycle
                    if node == "rx" and not is_high_pulse:
                        rx_count += 1

                    if is_high_pulse:
                        num_high += 1
                    else:
                        num_low += 1

                    info = data.get(node)
                    if info is None:
                        continue

                    t, dests = info
                    if t == "%":
                        if is_high_pulse:
                            continue
                        state = memory[node]
                        memory[node] = not state
                        for d in dests:
                            new_todo.append((node, d, not state))
                        continue
                    if t == "&":
                        state = memory[node]
                        state[src] = is_high_pulse

                        if sum(state.values()) == len(state):
                            # All are high, send a low pulse
                            to_send = False
                        else:
                            to_send = True

                        for d in dests:
                            new_todo.append((node, d, to_send))
                        continue
                    if t is None:
                        for d in dests:
                            new_todo.append((node, d, is_high_pulse))
                        continue
                    assert False

                todo = new_todo

        answer = math.lcm(*low_counts.values())
        return answer

if __name__ == "__main__":
    print(part1("input.txt"))
    print(part2("input.txt"))
