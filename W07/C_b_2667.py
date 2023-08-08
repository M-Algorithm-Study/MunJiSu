# 시간복잡도: O(N^3)

from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
board = [list(map(int, input().rstrip())) for _ in range(N)]

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

res = []

def bfs(board, x, y):
    q = deque()
    q.append((x, y))
    board[x][y] = 0
    cnt = 1

    while q:
        x, y = q.popleft()
        board[x][y] = 0

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            
            if 0 <= nx < N and 0 <= ny < N and board[nx][ny] == 1:
                board[nx][ny] = 0
                q.append((nx, ny))
                cnt += 1
    
    return cnt

for i in range(N):
    for j in range(N):
        if board[i][j] == 1:
            cnt = bfs(board, i, j)
            res.append(cnt)

res.sort()
print(len(res))
for a in res:
    print(a)