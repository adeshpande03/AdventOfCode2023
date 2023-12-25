from pathlib import Path
from pprint import *
from collections import *
import math
from copy import deepcopy
from functools import cache
import numpy as np
from sympy import symbols, Eq, solve
import itertools
from networkx import Graph, connected_components, minimum_edge_cut
from typing import List


def part1(filename):
    with Path(__file__).with_name(filename).open("r") as f:
        lines = f.read().splitlines()
    graph = Graph()
    ans = 1
    lines = [[i.split(": ")[0], i.split(": ")[1].split()] for i in lines]
    for node, connections in lines:
        graph.add_node(node)
        for connection in connections:
            graph.add_node(connection)
            graph.add_edge(
                *((node, connection) if node > connection else (connection, node))
            )
    cut = minimum_edge_cut(graph)
    graph.remove_edges_from(cut)
    components = connected_components(graph)
    for component in components:
        ans *= len(component)
    return ans


if __name__ == "__main__":
    print(part1("input.txt"))
    # Part 2 was impossible with my skillset so the solution has been omitted.
