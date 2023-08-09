# 시간복잡도: O(m * N^2)

from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
board = []
m = 0
for i in range(N):
    board.append(list(map(int, input().split())))
    m = max(m, max(board[-1])) # 미리 최대값을 찾아서 그만큼만 반복

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def bfs(x, y, m):
    q = deque()
    q.append((x, y))
    visited[x][y] = 1

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            
            if 0 <= nx < N and 0 <= ny < N and board[nx][ny] > m and visited[nx][ny] == 0:
                q.append((nx, ny))
                visited[nx][ny] = 1

res = 0
for i in range(m):
    cnt = 0
    visited = [[0]*N for _ in range(N)]
    for j in range(N):
        for k in range(N):
            if board[j][k] > i and visited[j][k] == 0:
                bfs(j, k, i)
                cnt += 1
    res = max(res, cnt)

print(res)

"""
연결된 영역 개수 찾기 문제
"""