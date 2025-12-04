from typing import List

class Solution:
    def how_many_rolls(self, lines: List[str]):
        grid = []
        for line in lines:
            grid.append(line)

        n_rows = len(grid)
        n_cols = len(grid[0])

        moves = [[-1, 0], [-1, -1], [0, -1], [1, -1], [1, 0], [1, 1], [0, 1], [-1, 1]]

        total_rolls = 0
        for row_i in range(n_rows):
            for col_i in range(n_cols):
                if grid[row_i][col_i] != '@':
                    continue
                n_count = 0
                for (dx, dy) in moves:
                    n_r = row_i + dy
                    n_c = col_i + dx
                    if n_cols > n_c >= 0 and n_rows > n_r >= 0 and grid[n_r][n_c] == '@':
                        n_count += 1
                total_rolls += 1 if n_count < 4 else 0
                
        return total_rolls

    def how_many_rolls_removed(self, lines: List[str]):
        grid = []
        for line in lines:
            grid.append([c for c in line])

        n_rows = len(grid)
        n_cols = len(grid[0])

        moves = [[-1, 0], [-1, -1], [0, -1], [1, -1], [1, 0], [1, 1], [0, 1], [-1, 1]]

        def removed_rolls(grid):
            rolls_to_remove = []
            for row_i in range(n_rows):
                for col_i in range(n_cols):
                    if grid[row_i][col_i] != '@':
                        continue
                    n_count = 0
                    for (dx, dy) in moves:
                        n_r = row_i + dy
                        n_c = col_i + dx
                        if n_cols > n_c >= 0 and n_rows > n_r >= 0 and grid[n_r][n_c] == '@':
                            n_count += 1
                    if n_count < 4:
                        rolls_to_remove.append((col_i, row_i))
            
            for col_i, row_i in rolls_to_remove:
                grid[row_i][col_i] = '.'

            return len(rolls_to_remove)
        
        total_removed = 0

        while True:
            removed = removed_rolls(grid=grid)
            print(f'{removed=}')
            if not removed:
                break
            total_removed += removed
        
        return total_removed

if __name__ == '__main__':
    sol = Solution()

    filename = ''

    with open(filename) as file:
        lines = [line.rstrip() for line in file]
        print(sol.how_many_rolls_removed(lines))
