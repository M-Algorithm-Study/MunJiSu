# 시간복잡도: O(N)

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
a_li = list(map(int, input().split()))

cnt, cur_sum, end = 0, 0, 0

for start in range(N):
    while cur_sum < M and end < N:
        cur_sum += a_li[end]
        end += 1
    if cur_sum == M:
        cnt += 1
    cur_sum -= a_li[start]

print(cnt)