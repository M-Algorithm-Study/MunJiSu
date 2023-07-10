# 시간복잡도: O(N + M)

import sys
input = sys.stdin.readline

N = int(input())
n_li = sorted(list(map(int, input().split())))
M = int(input())
m_li = list(map(int, input().split()))

cards = {}
for i in range(len(n_li)):
    cards[n_li[i]] = 0

for j in range(M):
    if m_li[j] not in cards: print(0, end=' ')
    else: print(1, end=' ')