# 시간복잡도: O(N^M * M)

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
li = []

def solve():
    if len(li) == M:
        print(' '.join(map(str, li)))
        return
    for i in range(1, N+1):
        li.append(i)
        solve()
        li.pop()
solve()