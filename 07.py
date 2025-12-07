from typing import List
from collections import defaultdict
from itertools import product
from typing import Optional
from math import ceil, floor, prod
from operator import add, sub

class Solution:
    def how_many_split(self, lines: List[str]):
        grid = []
        for line in lines:
            line_c = [c for c in line]
            grid.append(line_c)
        x_s = grid[0].index('S')

        n_rows = len(grid)
        n_cols = len(grid[0])

        upper_beams = set([x_s])
        current_beams = set()

        split_count = 0

        for row_i in range(1, n_rows):
            for col_i in range(n_cols):
                if grid[row_i][col_i] == '.':
                    if col_i in upper_beams:
                        grid[row_i][col_i] = '|'
                        current_beams.add(col_i)
                else:
                    if col_i in upper_beams:
                        split_count += 1
                        if col_i > 0:
                            current_beams.add(col_i - 1)
                        if col_i < n_cols - 1:
                            current_beams.add(col_i + 1)
            upper_beams = current_beams
            current_beams = set()

        return split_count

    def how_many_timelines_backtrack(self, lines: List[str]):
        grid = []
        for line in lines:
            line_c = [c for c in line]
            grid.append(line_c)

        x_s = grid[0].index('S')

        n_rows = len(grid)
        n_cols = len(grid[0])

        def dfs(row_i: int, col_i: int):
            if row_i == n_rows - 1:
                return 1
            r = 0
            if grid[row_i + 1][col_i] == '.':
                grid[row_i + 1][col_i] = '|'
                r += dfs(row_i + 1, col_i)
                grid[row_i + 1][col_i] = '.'
            elif grid[row_i + 1][col_i] == '^':
                if col_i > 0:
                    grid[row_i + 1][col_i - 1] = '|'
                    r += dfs(row_i + 1, col_i - 1)
                    grid[row_i + 1][col_i - 1] = '.'
                if col_i < n_cols - 1:
                    grid[row_i + 1][col_i + 1] = '|'
                    r += dfs(row_i + 1, col_i + 1)
                    grid[row_i + 1][col_i + 1] = '.'
            return r
        
        d = dfs(0, x_s)

        return d

    def how_many_timelines(self, lines: List[str]):
        grid = []
        for line in lines:
            line_c = [c for c in line]
            grid.append(line_c)

        x_s = grid[0].index('S')

        n_rows = len(grid)
        n_cols = len(grid[0])

        def dfs(row_i: int, col_i: int):
            if row_i == n_rows - 1:
                return 1
            r = 0
            if grid[row_i + 1][col_i] == '.':
                grid[row_i + 1][col_i] = '|'
                r += dfs(row_i + 1, col_i)
            elif grid[row_i + 1][col_i] == '^':
                if col_i > 0:
                    grid[row_i + 1][col_i - 1] = '|'
                    r += dfs(row_i + 1, col_i - 1)
                if col_i < n_cols - 1:
                    grid[row_i + 1][col_i + 1] = '|'
                    r += dfs(row_i + 1, col_i + 1)
            return r
        
        d = dfs(0, x_s)

        summation = [[0] * n_cols for _ in range(n_rows)]

        for row_i in range(n_rows - 1, -1, -1):
            pass
            for col_i in range(n_cols):
                if grid[row_i][col_i] == '|':
                    if row_i == n_rows - 1:
                        summation[row_i][col_i] = 1
                    else:
                        if grid[row_i + 1][col_i] in ['|', '^']:
                            summation[row_i][col_i] = summation[row_i + 1][col_i]
            for col_i in range(n_cols):
                if grid[row_i][col_i] == '^':
                    summation[row_i][col_i] = summation[row_i][col_i - 1] + summation[row_i][col_i + 1]
        
        return summation[1][x_s]

if __name__ == '__main__':
    sol = Solution()

    filename = ''

    with open(filename) as file:
        lines = [line.replace("\n", "") for line in file]
        print(sol.how_many_timelines(lines))
