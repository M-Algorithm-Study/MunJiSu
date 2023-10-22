# 시간복잡도: O(N)

import sys

input = sys.stdin.readline

T = int(input())

P = [0 for _ in range(101)]
P[1], P[2], P[3] = 1, 1, 1
for i in range(4, 101):
    P[i] = P[i - 3] + P[i - 2]

for _ in range(T):
    print(P[int(input())])