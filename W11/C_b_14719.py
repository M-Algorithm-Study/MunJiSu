# 시간복잡도: O(W^2)

import sys

input = sys.stdin.readline

H, W = map(int, input().split())
height = list(map(int, input().split()))

cnt = 0
for i in range(1, W - 1):
    left = max(height[:i])
    right = max(height[i + 1 :])
    low = min(left, right)
    if height[i] < low:
        cnt += low - height[i]
print(cnt)