# 시간복잡도: O(N * M)

import sys
from collections import deque

input = sys.stdin.readline

dx, dy = [0, 0, -1, 1], [-1, 1, 0, 0]

N, M = map(int, input().split())

board = [list(map(int, input().strip())) for _ in range(N)]


def bfs(x, y):
    q = deque()
    q.append((x, y))

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if 0 <= nx < N and 0 <= ny < M and board[nx][ny] == 1:
                board[nx][ny] = board[x][y] + 1
                q.append((nx, ny))
    return board[N - 1][M - 1]


print(bfs(0, 0))
