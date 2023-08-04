# 시간복잡도: O(N^M)

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
n_li = sorted(list(map(int, input().split())))
li = []

def solve():
    if len(li) == M:
        print(' '.join(map(str, li)))
        return
    for i in range(N):
        if n_li[i] not in li:
            li.append(n_li[i])
            solve()
            li.pop()
solve()