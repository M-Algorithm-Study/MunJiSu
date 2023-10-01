# 시간복잡도: O(N + M)

import sys
from collections import deque

input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

M = int(input())
C = list(map(int, input().split()))

d = deque()

for i in range(N):
    if A[i] == 0:
        d.appendleft(B[i])

for j in range(M):
    d.append(C[j])
    print(d.popleft(), end=" ")
