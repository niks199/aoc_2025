from typing import List

class Solution:
    def total_joltage(self, lines: List[str]):
        banks = []
        for line in lines:
            bank = []
            for c in line:
                bank.append(int(c))
            banks.append(bank)
        arr = []

        for bank in banks:
            bank_l = len(bank)
            left_digit_i = 0
            jolt = []
            for jolt_digit_i in range(12):
                max_dig_i = left_digit_i
                for bank_dig_i in range(left_digit_i, bank_l - (12 - jolt_digit_i - 1)):
                    if bank[max_dig_i] < bank[bank_dig_i]:
                        max_dig_i = bank_dig_i
                left_digit_i = max_dig_i + 1
                jolt.append(bank[max_dig_i])
            arr.append(jolt)

        ans = []
        for a in arr:
            v = 0
            for d_i in range(12):
                v += a[d_i] * (10 ** (12 - d_i - 1))
            ans.append(v)

        return sum(ans)

if __name__ == '__main__':
    sol = Solution()

    filename = ''

    with open(filename) as file:
        lines = [line.rstrip() for line in file]
        print(sol.total_joltage(lines))
