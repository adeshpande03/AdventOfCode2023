from pathlib import Path
from pprint import *
import collections
import math
from copy import deepcopy
from functools import cache
def part1(filename):
    with Path(__file__).with_name(filename).open("r") as f:
        lines = f.read().splitlines()
    lines = [list(i) for i in lines]
    for i, j in enumerate(lines):
        for k, l in enumerate(j):
            if l == "S":
                sr, sc = i, k
    q = [[(sr, sc)]]
    for _ in range(64):
        gplots = q.pop(0)
        temp = set()
        for i in gplots:
            crow, ccol = i
            for trow in range(crow - 1, crow + 2):
                for tcol in range(ccol - 1, ccol + 2):
                    if (
                        0 <= trow < len(lines)
                        and 0 <= tcol < len(lines[0])
                        and (trow, tcol) != (crow, ccol)
                        and (abs(ccol - tcol) + abs(crow - trow) != 2)
                    ):
                        if lines[trow][tcol] != "#":
                            temp.add((trow, tcol))
        q.append(temp)
    return len(temp)


def part2(filename):
    with Path(__file__).with_name(filename).open("r") as f:
        lines = f.read().splitlines()
    lines = [list(i) for i in lines]
    numRows = len(lines)
    numCols = len(lines[0])
    og = deepcopy(lines)
    og = og * 101
    og = [line * 101 for line in og]
    def show(og):
        return '\n'.join([''.join(i) for i in og])
    cs = []
    for i in range(len(og)):
        for j in range(len(og[i])):
            if og[i][j] == "S":
                cs.append((i, j))
    cc = cs[len(cs)//2]
    for i in range(len(og)):
        for j in range(len(og[i])):
            if og[i][j] == "S" and cc != (i, j):
                og[i][j] = '.'
    for i, j in enumerate(og):
        for k, l in enumerate(j):
            if l == "S":
                sr, sc = i, k
    q = [[(sr, sc)]]
    for _ in range(0):
        gplots = q.pop(0)
        temp = set()
        for i in gplots:
            crow, ccol = i
            for trow in range(crow - 1, crow + 2):
                for tcol in range(ccol - 1, ccol + 2):
                    if (
                        0 <= trow < len(og)
                        and 0 <= tcol < len(og[0])
                        and (trow, tcol) != (crow, ccol)
                        and (abs(ccol - tcol) + abs(crow - trow) != 2)
                    ):
                        if og[trow][tcol] != "#":
                            temp.add((trow, tcol))
        q.append(temp)


    def q(x):
        return 14913*x*x + 15004*x +3778
    return(q((26501365 - 65)/131))

    ## a(65^2) + b(65) + c = 2722
    ## a(196^2) + b(196) + c = 25621
    ## a(327^2) + b(327) + c = 71435


    
    
    # t = []
    # for i in range(16 - numRows //2, 16 + numRows//2):
    #     temp = []
    #     for j in range(16 - numCols //2, 16 + numCols//2):
    #         temp.append(traverseOG(og, i, j))
    #     t.append(temp)
    # pprint(t)
    
    
            
            
    
    # for i, j in enumerate(lines):
    #     for k, l in enumerate(j):
    #         if l == "S":
    #             sr, sc = i, k
    # q = [[(sr, sc)]]
    # def traverseOG(lines, crow, ccol):
    #     for trow in range(crow - 1, crow + 2):
    #             for tcol in range(ccol - 1, ccol + 2):
    #                 if (
    #                     0 <= trow < len(lines)
    #                     and 0 <= tcol < len(lines[0])
    #                     and (trow, tcol) != (crow, ccol)
    #                     and (abs(ccol - tcol) + abs(crow - trow) != 2)
    #                 ):
    #                     if lines[trow][tcol] != "#":
    #                         temp.add((trow, tcol))
    #                         lines[trow][tcol] = _
                            
        
                
                
                
                
                
                
                
        
    # tot = set((sr, sc))
    # for _ in range(64):
    #     gplots = q.pop(0)
    #     temp = set()
    #     for i in gplots:
    #         tot.add(i)
    #         crow, ccol = i
    #         for trow in range(crow - 1, crow + 2):
    #             for tcol in range(ccol - 1, ccol + 2):
    #                 if (
    #                     0 <= trow < len(lines)
    #                     and 0 <= tcol < len(lines[0])
    #                     and (trow, tcol) != (crow, ccol)
    #                     and (abs(ccol - tcol) + abs(crow - trow) != 2)
    #                 ):
    #                     if lines[trow][tcol] != "#":
    #                         temp.add((trow, tcol))
    #     q.append(temp)
    # return len(temp)


if __name__ == "__main__":
    print(part1("input.txt"))
    print(part2("input.txt"))
