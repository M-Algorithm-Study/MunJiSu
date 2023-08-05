# 시간복잡도: O(N^M * M)

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
li = []

def solve(start):
    if len(li) == M:
        print(' '.join(map(str, li)))
        return
    for i in range(start, N+1):
        if i not in li:
            li.append(i)
            solve(i+1)
            li.pop()
solve(1)