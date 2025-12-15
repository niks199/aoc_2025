from typing import List, Set
from collections import defaultdict
from itertools import product
from typing import Optional
from math import ceil, floor, prod, sqrt
from operator import add, sub
import heapq
import z3

class Solution:
    def how_many_paths(self, lines: List[str]):
        adj_list = defaultdict(lambda: [])

        for line in lines:
            items = line.split(':')

            source = items[0]
            outputs = [w for w in items[1].split(' ') if w]

            adj_list[source] = outputs
        
        c = 0

        def dfs(node):
            nonlocal c
            if node == 'out':
                c += 1
                return
            for s in adj_list[node]:
                dfs(s)

        dfs("you")

        return c
    
    def how_many_paths_dac_fft(self, lines: List[str]):
        adj_list = defaultdict(lambda: [])

        for line in lines:
            items = line.split(':')

            source = items[0]
            outputs = [w for w in items[1].split(' ') if w]

            adj_list[source] = outputs
        
        def dfs(node, dst, memo):
            if node == dst:
                return 1
            
            if memo[node] != -1:
                return memo[node]
            
            c = 0
            
            for s in adj_list[node]:
                c += dfs(s, dst, memo)
            
            memo[node] = c

            return c

        srv_to_dac = dfs("svr", "dac", defaultdict(lambda: -1))
        dac_to_fft = dfs("dac", "fft", defaultdict(lambda: -1))
        fft_to_out = dfs("fft", "out", defaultdict(lambda: -1))

        v1 = srv_to_dac * dac_to_fft * fft_to_out

        srv_to_fft = dfs("svr", "fft", defaultdict(lambda: -1))
        fft_to_dac = dfs("fft", "dac", defaultdict(lambda: -1))
        dac_to_out = dfs("dac", "out", defaultdict(lambda: -1))

        v2 = srv_to_fft * fft_to_dac * dac_to_out

        return v1 + v2

if __name__ == '__main__':
    sol = Solution()

    filename = ''

    with open(filename) as file:
        lines = [line.replace("\n", "") for line in file]
        print(sol.how_many_paths_dac_fft(lines))
