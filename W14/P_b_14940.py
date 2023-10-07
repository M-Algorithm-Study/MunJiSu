# 시간복잡도: O(nm)

import sys
from collections import deque

input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

n, m = map(int, input().split())
board = []
visited = [[0] * m for _ in range(n)]
res = [[-1] * m for _ in range(n)]
q = deque()
for i in range(n):
    row = list(map(int, input().split()))
    for j in range(m):
        if row[j] == 2:
            q.append((i, j))
            visited[i][j] = 1
            res[i][j] = 0
        if row[j] == 0:
            res[i][j] = 0
    board.append(row)

while q:
    x, y = q.popleft()

    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]

        if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and board[nx][ny] == 1:
            q.append((nx, ny))
            visited[nx][ny] = 1
            res[nx][ny] = res[x][y] + 1

for i in res:
    print(*i)
