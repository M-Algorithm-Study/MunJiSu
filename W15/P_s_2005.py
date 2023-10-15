# 시간복잡도: O(T * N^2)

import sys

sys.stdin = open("input_2005.txt", "r")

T = int(input())
for t in range(1, T + 1):
    res = 0
    N = int(input())
    pas = [0] * N
    for i in range(N):
        pas[i] = [1] * (i + 1)
    for j in range(2, N):
        for k in range(1, len(pas[j])):
            if k < len(pas[j]) - 1:
                pas[j][k] = pas[j - 1][k - 1] + pas[j - 1][k]
    print(f"#{t}")
    for i in range(N):
        print(*pas[i])
