# 시간복잡도: O(K * M * N)

from collections import deque
import sys
input = sys.stdin.readline

M, N, K = map(int, input().split())
board = [[0]*N for _ in range(M)]
for _ in range(K):
    x1, y1, x2, y2 = map(int, input().split())
    for i in range(y1, y2):
        for j in range(x1, x2):
            board[i][j] = 1

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
result = []

def bfs(x, y):
    q = deque()
    q.append((x, y))
    board[x][y] = 1
    size = 1
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < M and 0 <= ny < N and board[nx][ny] == 0:
                board[nx][ny] = 1
                q.append((nx, ny))
                size += 1
    return size

for i in range(M):
    for j in range(N):
        if board[i][j] == 0:
            result.append(bfs(i, j))

print(len(result))
print(*sorted(result))