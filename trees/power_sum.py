'''
    https://www.hackerrank.com/challenges/the-power-sum/forum

    I think this is the optimal solution. Very tricky recursion.
    The solution comes from a decision tree and traversing it in order,
    terminating the exploration of a branch when the target value is hit,
    or exceeded. The exploration is then done in the optimal way.

    Sample input:
    800
    2
    > 561
'''

import math
import itertools

target_val = int(input())
exponent = int(input())

num_bases = 0
for i in range(1, math.floor(math.pow(target_val, 1 / exponent)) + 1):
    num_bases = i

power_list = [i ** exponent for i in range(1, num_bases + 1)]


def sum_nums(power_list, curr_sum, curr_count):
    for i, x in enumerate(power_list):
        if curr_sum + x > target_val:
            return curr_count
        if curr_sum + x == target_val:
            return curr_count + 1
        if len(power_list) > 1:
            curr_count = sum_nums(power_list[i + 1:], curr_sum + x, curr_count)
    return curr_count


count = sum_nums(power_list, 0, 0)
print(count)
