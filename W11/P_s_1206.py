# 시간복잡도: O(N)

import sys

sys.stdin = open("input_1206.txt", "r")

for t in range(1, 11):
    N = int(input())
    heights = list(map(int, input().split()))
    res = 0

    for i in range(2, N - 2):
        maxHeight = max(heights[i - 1], heights[i - 2], heights[i + 1], heights[i + 2])
        if heights[i] > maxHeight:
            res += heights[i] - maxHeight

    print("#{} {}".format(t, res))
