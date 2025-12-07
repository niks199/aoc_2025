from typing import List
from collections import defaultdict
from itertools import product
from typing import Optional
from math import ceil, floor
from operator import add, sub

class Solution:
    def how_many_available_ingredient(self, lines: List[str]):
        id_ranges = []
        available_ids = []
        read_ranges = True
        for line in lines:
            if not line:
                read_ranges = False
                continue

            if read_ranges:
                id_ranges.append(list(map(int, line.split('-'))))
            else:
                available_ids.append(int(line))

        id_ranges.sort()

        fresh_ids = []
        for available_id in available_ids:
            for (a, b) in id_ranges:
                if available_id < a or available_id > b:
                    continue
                if available_id >= a and available_id <= b:
                    fresh_ids.append(available_id)
                    break


        return len(fresh_ids)
    
    def how_many_in_ranges(self, lines: List[str]):
        id_ranges = []
        available_ids = []
        read_ranges = True
        for line in lines:
            if not line:
                read_ranges = False
                continue

            if read_ranges:
                id_ranges.append(list(map(int, line.split('-'))))
            else:
                available_ids.append(int(line))

        id_ranges.sort()

        fresh_ids = []

        for (a, b) in id_ranges:
            if not fresh_ids:
                fresh_ids.append([a, b])
            else:
                if a <= fresh_ids[-1][1]:
                    max_b = max(b, fresh_ids[-1][1])
                    fresh_ids[-1][1] = max_b
                else:
                    fresh_ids.append([a, b])

        t = 0
        for (a, b) in fresh_ids:
            t += b - a + 1

        return t

if __name__ == '__main__':
    sol = Solution()

    filename = ''

    with open(filename) as file:
        lines = [line.rstrip() for line in file]
        print(sol.how_many_in_ranges(lines))
