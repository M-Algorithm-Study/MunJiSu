# 시간복잡도: O(N * M)

import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())
campus = [list(input().rstrip()) for _ in range(N)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 도연이 위치를 먼저 찾아서 초기 위치 변수에 할당
for i in range(N):
    for j in range(M):
        if campus[i][j] == "I":
            s_x, s_y = i, j


# 만날 수 있는 사람 수 계산할 수 있는 bfs 함수
def bfs(x, y):
    visited = [[0] * M for _ in range(N)]
    q = deque()
    q.append((x, y))
    visited[x][y] = 1
    cnt = 0

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            # 범위 확인
            if 0 <= nx < N and 0 <= ny < M:
                # 벽이 아니고 방문하지 않은 곳이면 방문
                if campus[nx][ny] != "X" and not visited[nx][ny]:
                    q.append((nx, ny))
                    visited[nx][ny] = 1

                    # 사람이면 += 1
                    if campus[nx][ny] == "P":
                        cnt += 1

    return cnt


res = bfs(s_x, s_y)

if res == 0:
    print("TT")
else:
    print(res)
