# 시간복잡도: O(N^N * N)

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
li = []

def solve(start):
    if len(li) == M:
        print(' '.join(map(str, li)))
        return
    for i in range(start, N+1):
        li.append(i)
        solve(i)
        li.pop()
solve(1)