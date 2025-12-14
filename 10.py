from typing import List, Set
from collections import defaultdict
from itertools import product
from typing import Optional
from math import ceil, floor, prod, sqrt
from operator import add, sub
import heapq
import z3

class Solution:
    def fewest_button_presses(self, lines: List[str]):
        machines = []
        for line in lines:
            items = line.split(' ')

            lights = items[0]
            buttons = items[1:-1]
            joltage = items[-1]
            machine = [[l for l in lights[1:-1]], [list(map(int, button[1:-1].split(','))) for button in buttons]]
            machines.append(machine)
        
        def find_press(machine, max_presses, lights, presses_count, buttons):
            if lights == machine[0]:
                return presses_count
            if presses_count >= max_presses:
                return 0
            for button_i in buttons:
                button = machine[1][button_i]
                for light_i in button:
                    lights[light_i] = '#' if lights[light_i] == '.' else '.'
                r = find_press(machine, max_presses, lights, presses_count + 1, buttons[:button_i]+buttons[button_i+1:])
                if r:
                    return r
                for light_i in button:
                    lights[light_i] = '#' if lights[light_i] == '.' else '.'
            return 0

        total = 0
        for i, machine in enumerate(machines):
            res = 0
            for v in range(1, len(machine[1]) + 5):
                n_lights = len(machine[0])
                lights = ['.'] * n_lights
                buttons = [i for i in range(len(machine[1]))]
                res = find_press(machine, v, lights, 0, buttons)
                if res:
                    break
            if res:
                total += res
            print(f"{i=} {res=} {len(machines)} {total=}")

        return total
      
    def joltage_fewest_button_presses(self, lines: List[str]):
        machines = []
        for line in lines:
            items = line.split(' ')

            buttons = items[1:-1]
            joltage = items[-1]
            machine = [list(map(int, joltage[1:-1].split(','))), [set(map(int, button[1:-1].split(','))) for button in buttons]]
            machines.append(machine)

        total = 0
        for i, machine in enumerate(machines):
            o = z3.Optimize()
            vars = z3.Ints(f'n{i}' for i in range(len(machine[1])))
            for var in vars:
                o.add(var >= 0)
            for i, jolt in enumerate(machine[0]):
                equation = 0
                for b, button in enumerate(machine[1]):
                    if i in button:
                        equation += vars[b]
                o.add(equation == jolt)
            o.minimize(sum(vars))
            o.check()
            total += o.model().eval(sum(vars)).as_long()

        return total

if __name__ == '__main__':
    sol = Solution()

    filename = ''

    with open(filename) as file:
        lines = [line.replace("\n", "") for line in file]
        print(sol.joltage_fewest_button_presses(lines))
