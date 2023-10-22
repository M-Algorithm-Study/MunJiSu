# 시간복잡도: O(N^3)

import sys

input = sys.stdin.readline

N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]

for i in range(N):
    for j in range(N):
        for k in range(N):
            if graph[j][i] and graph[i][k]:
                graph[j][k] = 1

for a in graph:
    print(*a)
