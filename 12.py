from typing import List, Set
from collections import defaultdict
from itertools import product
from typing import Optional
from math import ceil, floor, prod, sqrt
from operator import add, sub
import heapq
import z3

class Solution:
    def how_many_regions(self, lines: List[str]):
        blocks = []
        for i in range(6):
            block = lines[i * 5 + 1:i * 5 + 4]
            occupied_count = 0
            for b_line in block:
                occupied_count += sum([1 for c in b_line if c == '#'])
            blocks.append({"block": block, "occupied_count": occupied_count})

        regions = []
        for i in range(30, len(lines)):
            items = lines[i].split(':')
            dims = items[0].split('x')
            region = list(map(int, dims))
            allocates = list(map(int, items[1].strip().split(' ')))
            regions.append({"region": region, "allocates": allocates})

        c = 0
        for region in regions:
            (rows, cols) = region["region"]
            region_area = rows * cols

            blocks_area = 0
            for (alloc_i, alloc_count) in enumerate(region["allocates"]):
                blocks_area += blocks[alloc_i]["occupied_count"] * alloc_count
            
            if region_area >= blocks_area:
                c += 1
        return c


if __name__ == '__main__':
    sol = Solution()

    filename = ''

    with open(filename) as file:
        lines = [line.replace("\n", "") for line in file]
        print(sol.how_many_regions(lines))
