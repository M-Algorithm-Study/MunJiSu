# 시간복잡도: O(N)

import sys

sys.stdin = open("input_15941.txt", "r")

T = int(input())
for t in range(1, T + 1):
    N = int(input())
    res = N**2
    print("#{} {}".format(t, res))
