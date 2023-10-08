# 시간복잡도: O(N log N)

import sys

input = sys.stdin.readline

N = int(input())
time = []

for i in range(N):
    start, end = map(int, input().split())
    time.append((start, end))

time.sort(key=lambda x: x[0])
time.sort(key=lambda x: x[1])

last, cnt = 0, 0

for start, end in time:
    if start >= last:
        cnt += 1
        last = end
print(cnt)