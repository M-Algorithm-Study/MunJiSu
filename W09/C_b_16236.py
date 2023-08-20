# 시간복잡도: O(N^4)

from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

# 아기상어의 좌표, 사이즈 초기값 (아기 상어의 초기 사이즈는 2)
s_x, s_y, s_size = 0, 0, 2

# 상어의 위치 좌표를 미리 찾아주고 값을 0으로 바꿔줌
for i in range(N):
    for j in range(N):
        if board[i][j] == 9:
            s_x, s_y = i, j
            board[i][j] = 0

def bfs(x, y, size):
    distance = [[0]*N for _ in range(N)]
    visited = [[0]*N for _ in range(N)]
    # 거리가 가까운 물고기가 많다면, 가장 위에 있는 물고기, 그러한 물고기가 여러마리라면, 가장 왼쪽에 있는 물고기를 먹는다. => 정렬 필요
    li = []
    q = deque()
    q.append((x, y))
    visited[x][y] = 1

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < N and 0 <= ny < N:
                # 사이즈가 같고, 방문하지 않았으면 이동 가능한 좌표
                if board[nx][ny] <= size and visited[nx][ny] == 0:
                    q.append((nx, ny))
                    visited[nx][ny] = 1
                    distance[nx][ny] = distance[x][y] + 1

                    # 물고기가 있으며 먹을 수 있는 크기 (같은 크기는 포함 X)
                    if board[nx][ny] != 0 and board[nx][ny] < size:
                        li.append((nx, ny, distance[nx][ny]))
    # distance, x, y 순 오름차순
    return sorted(li, key=lambda x: (x[2], x[0], x[1]))

cnt = 0
res = 0
while True:
    shark = bfs(s_x, s_y, s_size)
    # 먹을 수 있는 물고기가 없다면 종료
    if len(shark) == 0: break
    s_x, s_y, dis = shark[0]
    cnt += 1
    # 자신의 크기와 같은 수의 물고기를 먹을 때 마다 크기가 1 증가
    if cnt == s_size: s_size += 1; cnt = 0

    board[s_x][s_y] = 0
    res += dis

print(res)


"""
N×N 크기의 공간에 물고기 M마리와 아기 상어 1마리
한 칸에는 물고기가 최대 1마리 존재
가장 처음에 아기 상어의 크기는 2이고, 아기 상어는 1초에 상하좌우로 인접한 한 칸씩 이동
크기가 같은 물고기는 먹을 수 없지만, 그 물고기가 있는 칸은 지나갈 수 있다.
아기 상어의 이동은 1초, 물고기를 먹는데 걸리는 시간은 없다

더 이상 먹을 수 있는 물고기가 공간에 없다면 아기 상어는 엄마 상어에게 도움을 요청한다.
먹을 수 있는 물고기가 1마리라면, 그 물고기를 먹으러 간다.
먹을 수 있는 물고기가 1마리보다 많다면, 거리가 가장 가까운 물고기를 먹으러 간다. => bfs 사용 (bfs는 항상 최단 경로의 결과)
거리는 아기 상어가 있는 칸에서 물고기가 있는 칸으로 이동할 때, 지나야하는 칸의 개수의 최솟값이다.
거리가 가까운 물고기가 많다면, 가장 위에 있는 물고기, 그러한 물고기가 여러마리라면, 가장 왼쪽에 있는 물고기를 먹는다.

물고기를 먹으면, 그 칸은 빈 칸이 된다.
아기 상어는 자신의 크기와 같은 수의 물고기를 먹을 때 마다 크기가 1 증가

0, 1, 2, 3, 4, 5, 6, 9
0: 빈 칸
1, 2, 3, 4, 5, 6: 칸에 있는 물고기의 크기
9: 아기 상어의 위치

아기 상어가 엄마 상어에게 도움을 요청하지 않고 물고기를 잡아먹을 수 있는 시간을 출력
"""