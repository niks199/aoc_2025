from typing import List
from operator import add, sub

class Solution:
    #part2
    def what_is_password(self, lines: List[str]):
        a = 0
        
        r = 50

        for line in lines:
            dir = line[0]
            num = int(line[1:])

            for i in range(num):
                oper = add if dir == 'L' else sub
                r = oper(r, 1) % 100
                if r == 0:
                    a += 1

        print(f'{a=}')

        return a     

if __name__ == '__main__':
    sol = Solution()

    filename = ''

    with open(filename) as file:
        lines = [line.rstrip() for line in file]
        print(sol.what_is_password(lines))
