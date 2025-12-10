from typing import List
from collections import defaultdict
from itertools import product
from typing import Optional
from math import ceil, floor, prod, sqrt, atan2, degrees
from operator import add, sub
import heapq

class Solution:
    def area(self, p1, p2):
        return (abs(p1[0] - p2[0]) + 1) * (abs(p1[1] - p2[1]) + 1)

    def largest_area(self, lines: List[str]):
        points = []
        for line in lines:
            (x, y) = map(int, line.split(','))
            points.append((x,y))

        n_points = len(points)

        l_area = 0

        for p1_i in range(n_points):
            for p2_i in range(p1_i + 1, n_points):
                a = self.area(points[p1_i], points[p2_i])
                if a > l_area:
                    l_area = a
        return l_area

    def largest_area_rg(self, lines: List[str]):
        points = []
        for line in lines:
            (x, y) = map(int, line.split(','))
            points.append((x,y))

        xs = sorted({x for x, _ in points})
        ys = sorted({y for _, y in points})

        grid = [[0] * (len(xs) * 2 - 1) for _ in range(len(ys) * 2 - 1)]

        for (pt1, pt2) in zip(points, points[1:] + points[:1]):
            c_x1, c_x2 = sorted([xs.index(pt1[0]) * 2, xs.index(pt2[0]) * 2])
            c_y1, c_y2 = sorted([ys.index(pt1[1]) * 2, ys.index(pt2[1]) * 2])
            
            for x in range(c_x1, c_x2 + 1):
                for y in range(c_y1, c_y2 + 1):
                    grid[y][x] = 1

        q = [(-1, -1)]

        seen = set([(-1, -1)])

        while q:
            (x, y) = q.pop(0)

            for x_next, y_next in [(x + 1, y), (x - 1, y), (x, y - 1), (x, y + 1)]:
                if x_next < -1 or x_next > len(grid[0]) or y_next < -1 or y_next > len(grid):
                    continue
                if x_next >= 0 and y_next >= 0 and x_next < len(grid[0]) and y_next < len(grid) and grid[y_next][x_next] == 1:
                    continue
                if (x_next, y_next) in seen:
                    continue
                seen.add((x_next, y_next))
                q.append((x_next, y_next))

        for y in range(len(grid)):
            for x in range(len(grid[0])):
                if (x,y) not in seen:
                    grid[y][x] = 1

        def construct_psa(fn):
            psa = [[0] * (len(xs) * 2 - 1) for _ in range(len(ys) * 2 - 1)]
            for y in range(len(psa)):
                for x in range(len(psa[0])):
                    left = psa[y][x - 1] if x > 0 else 0
                    top = psa[y - 1][x] if y > 0 else 0
                    top_left = psa[y - 1][x - 1] if x > 0 and y > 0 else 0
                    psa[y][x] = left + top - top_left + fn(x, y)
            return psa
        
        c_psa = construct_psa(lambda x, y: grid[y][x])

        def validate(psa, pt1, pt2):
            c_x1, c_x2 = sorted([xs.index(pt1[0]) * 2, xs.index(pt2[0]) * 2])
            c_y1, c_y2 = sorted([ys.index(pt1[1]) * 2, ys.index(pt2[1]) * 2])
            left = psa[c_y2][c_x1 - 1] if c_x1 > 0 else 0
            top = psa[c_y1 - 1][c_x2] if c_y1 > 0 else 0
            top_left = psa[c_y1 - 1][c_x1 - 1] if c_y1 > 0 and c_x1 > 0 else 0
            are = psa[c_y2][c_x2] - left - top + top_left
            a = (c_x2 - c_x1 + 1) * (c_y2 - c_y1 + 1)
            return True if are == a else False

        rects = [((x1, y1), (x2, y2)) for i, (x1, y1) in enumerate(points) for x2, y2 in points[:i]]

        valid_rects = [(re[0], re[1]) for re in rects if validate(c_psa, re[0], re[1])]

        a = 0
        for (p1, p2) in valid_rects:
            v = self.area(p1, p2)
            a = max(a, v)

        return a


if __name__ == '__main__':
    sol = Solution()

    filename = ''

    with open(filename) as file:
        lines = [line.replace("\n", "") for line in file]
        print(sol.largest_area_rg(lines))
