# 시간복잡도: O(N)

import sys

sys.stdin = open("input_1984.txt", "r")

T = int(input())
for t in range(1, T + 1):
    nums = list(map(int, input().split()))
    M = max(nums)
    m = min(nums)
    res = round((sum(nums) - (M + m)) / 8)
    print("#{} {}".format(t, res))
