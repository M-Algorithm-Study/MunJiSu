# 시간복잡도: O(N * M)

from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int, input().split()) # N: 세로, M: 가로
board = [list(map(int, input().split())) for _ in range(N)]
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
time = 0
def bfs(x, y):
    q = deque()
    q.append((x, y))
    visited[x][y] = 1

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < N and 0 <= ny < M:
                # 다음이 공기
                if visited[nx][ny] == 0 and board[nx][ny] == 0:
                    q.append((nx, ny))
                    visited[nx][ny] = 1
                # 다음이 치즈
                elif board[nx][ny] == 1:
                    visited[nx][ny] = visited[nx][ny] + 1

while 1:
    visited = [[0]*M for _ in range(N)]
    bfs(0, 0)
    # 한 번 진행 후 한 시간 추가
    time += 1
    for i in range(N):
        for j in range(M):
            # 두 방향 이상 공기 => 값을 0으로
            if visited[i][j] >= 2: board[i][j] = 0
    air = 0
    for i in range(N):
        for j in range(M):
            if board[i][j] == 0: air += 1
    # 종료조건: 공기수 = 배열 크기
    if air == (N*M): break
    
print(time)

"""
모눈종이의 맨 가장자리에는 치즈가 놓이지 않는 것으로 가정.
4방향 중 2방향이 실내온도 공기 접촉이면 한 시간만에 녹아 없어진다.
치즈 내부에 있는 공간은 외부 공기와 접촉하지 않는다.
치즈 => 1
"""