from typing import List
from collections import defaultdict
from itertools import product
from typing import Optional
from math import ceil, floor, prod, sqrt
from operator import add, sub
import heapq

class Solution:
    def distance(self, p1, p2):
        return sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2 + (p1[2] - p2[2]) ** 2)

    def find(self, parents, p_i):
        if parents[p_i] == p_i:
            return p_i
        parents[p_i] = self.find(parents, parents[p_i])
        return parents[p_i]

    def union(self, parents, sizes, p1_i, p2_i):
        p_p1_i = self.find(parents, p1_i)
        p_p2_i = self.find(parents, p2_i)

        if p_p1_i != p_p2_i:
            parents[p_p2_i] = parents[p_p1_i]
            sizes[p_p1_i] += sizes[p_p2_i]
            return True
        return False

    def three_largest_circuits(self, lines: List[str]):
        points = []
        for line in lines:
            (x, y, z) = map(int, line.split(','))
            points.append((x,y,z))

        n_points = len(points)

        parents = [0] * n_points
        sizes = [1] * n_points

        for i in range(n_points):
            parents[i] = i

        dists_pq = []
        for p1_i in range(n_points):
            for p2_i in range(p1_i + 1, n_points):
                heapq.heappush(dists_pq, (self.distance(points[p1_i], points[p2_i]), p1_i, p2_i))
        
        pair_count = 0

        while dists_pq and pair_count < 1000:
            (dist, p1_i, p2_i) = heapq.heappop(dists_pq)
            self.union(parents, sizes, p1_i, p2_i)
            pair_count += 1

        cuircuit_sizes = [0] * n_points
        for p_i, p_p_i in enumerate(parents):
            r_p_i = self.find(parents, p_i)
            cuircuit_sizes[r_p_i] += 1

        cuircuit_sizes.sort(reverse=True)

        v = cuircuit_sizes[0] * cuircuit_sizes[1] * cuircuit_sizes[2]
        return v
            
    def last_to_boxes_multiply(self, lines: List[str]):
        points = []
        for line in lines:
            (x, y, z) = map(int, line.split(','))
            points.append((x,y,z))

        n_points = len(points)

        parents = [0] * n_points
        sizes = [1] * n_points

        for i in range(n_points):
            parents[i] = i

        dists_pq = []
        for p1_i in range(n_points):
            for p2_i in range(p1_i + 1, n_points):
                heapq.heappush(dists_pq, (self.distance(points[p1_i], points[p2_i]), p1_i, p2_i))

        l_p1_i = 0
        l_p2_i = 0

        while dists_pq:
            (dist, p1_i, p2_i) = heapq.heappop(dists_pq)
            if self.union(parents, sizes, p1_i, p2_i):
                l_p1_i = p1_i
                l_p2_i = p2_i

        return points[l_p1_i][0] * points[l_p2_i][0]

if __name__ == '__main__':
    sol = Solution()

    filename = ''

    with open(filename) as file:
        lines = [line.replace("\n", "") for line in file]
        print(sol.last_to_boxes_multiply(lines))
