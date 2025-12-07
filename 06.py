from typing import List
from collections import defaultdict
from itertools import product
from typing import Optional
from math import ceil, floor, prod
from operator import add, sub

class Solution:
    def grand_total(self, lines: List[str]):
        n_lines = len(lines)

        nums = []
        for line_i in range(n_lines - 1):
            nn = [w.strip() for w in lines[line_i].split(' ') if w]
            nums.append(list(map(int, nn)))
        
        opers = [c for c in lines[-1] if c != ' ']

        total = 0
        for i in range(len(nums[0])):
            uu = []
            for row_i in range(len(nums)):
                uu.append(nums[row_i][i])
            t = 0
            if opers[i] == '*':
                t = prod(uu)
            else:
                t= sum(uu)
            total += t

        return total

    def grand_total_2(self, lines: List[str]):
        n_lines = len(lines)

        line_spaces = []

        for line_i in range(n_lines - 1):
            line = lines[line_i]
            spaces = set()
            for c_i in range(len(line)):
                if line[c_i] == ' ':
                    spaces.add(c_i)
            line_spaces.append(spaces)

        u = list(set.intersection(*line_spaces))
        u.sort()

        line_parts = []
        for line_i in range(n_lines - 1):
            line = lines[line_i]
            parts = []
            for u_i in range(1, len(u)):
                part = line[u[u_i - 1] + 1:u[u_i]]
                parts.append(part)
            part = line[u[-1] + 1:]
            if part:
                parts.append(part)
            line_parts.append(parts)

        n_rows = len(line_parts)
        n_cols = len(line_parts[0])

        operands = []

        for col_i in range(n_cols):
            part_rows = []
            for k in range(n_rows):
                part_rows.append(line_parts[k][col_i])

            part_l = len(part_rows[0])

            operand = []
            for part_col_i in range(part_l):
                numb = 0
                for row_i in range(n_rows):
                    part_row = part_rows[row_i]
                    c = part_row[part_l - part_col_i - 1]
                    if c == ' ':
                        continue
                    numb *= 10
                    numb += int(c)
                operand.append(numb)
            operands.append(operand)
        
        opers = [c for c in lines[-1] if c != ' ']

        total = 0
        for i in range(len(line_parts[0])):
            t = 0
            if opers[i] == '*':
                t = prod(operands[i])
            else:
                t= sum(operands[i])
            total += t

        return total


if __name__ == '__main__':
    sol = Solution()

    filename = ''

    with open(filename) as file:
        lines = [line.replace("\n", "") for line in file]
        print(sol.grand_total_2(lines))
