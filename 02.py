from typing import List

class Solution:
    def add_invalid_ids(self, lines: List[str]):
        line = lines[0]

        arr = []
        for inter in line.split(','):
            (a, b) = map(int, inter.split('-'))

            for v in range(a, b + 1, 1):
                v_s = str(v)
                v_l = len(v_s)
                if v_l & 1:
                    continue
                v_h = v_l // 2

                if v_s[:v_h] == v_s[v_h:]:
                    a += v
                    arr.append(v)
                    print(f'{v=}')

        r = sum(arr)
        return r

    def add_invalid_ids_new_rules(self, lines: List[str]):
        line = lines[0]

        arr = []
        for inter in line.split(','):
            (a, b) = map(int, inter.split('-'))

            for v in range(a, b + 1, 1):
                v_s = str(v)
                v_l = len(v_s)
 
                for part_denominator in range(2, v_l + 1, 1):
                    if v_l % part_denominator:
                        continue
                    v_h = v_l // part_denominator
                    num_parts = v_l // v_h
                    found_invalid_id = True
                    for part_i in range(1, num_parts):
                        if v_s[:v_h] != v_s[v_h * part_i:v_h * part_i+v_h]:
                            found_invalid_id = False
                            break
                    if found_invalid_id:
                        arr.append(v)
                        break

        r = sum(arr)
        return r

if __name__ == '__main__':
    sol = Solution()

    filename = ''

    with open(filename) as file:
        lines = [line.rstrip() for line in file]
        print(sol.add_invalid_ids_new_rules(lines))
