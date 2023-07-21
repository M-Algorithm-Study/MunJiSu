# 시간복잡도: O(N + M)

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
S = set([input().strip() for _ in range(N)])
cnt = 0
for _ in range(M):
    s = input().strip()
    if s in S: cnt += 1
print(cnt)