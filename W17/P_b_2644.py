# 시간복잡도: O(N + M)

import sys

input = sys.stdin.readline

n = int(input())
a, b = map(int, input().split())
m = int(input())

graph = [[] for _ in range(n + 1)]
visited = [0] * (n + 1)
res = [0] * (n + 1)

for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)


def dfs(v):
    visited[v] = 1
    for i in graph[v]:
        if not visited[i]:
            res[i] = res[v] + 1
            dfs(i)


dfs(a)

print(res[b] if res[b] > 0 else -1)
