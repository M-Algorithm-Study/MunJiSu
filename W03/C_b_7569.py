# 시간복잡도: O(H * N * M)

import sys
from collections import deque
input = sys.stdin.readline

M, N, H = map(int, input().split())
tomato = [[list(map(int, input().split())) for _ in range(N)] for _ in range(H)]
q = deque([])
for z in range(H):
    for y in range(N):
        for x in range(M):
            if(tomato[z][y][x] == 1):
                q.append([z,y,x])
dx = [1,-1,0,0,0,0]
dy = [0,0,1,-1,0,0]
dz = [0,0,0,0,1,-1]
def in_range(z,y,x):
    return 0 <= z < H and 0 <= y < N and 0 <= x < M
cnt = 0
while q:
    new_q = deque([])
    while(q):
        z, y, x = q.pop()
        for i in range(6):
            nz, ny, nx = z+dz[i], y+dy[i], x+dx[i]
            if in_range(nz,ny,nx) and tomato[nz][ny][nx] == 0:
                new_q.append([nz,ny,nx])
                tomato[nz][ny][nx] = 1
    cnt += 1
    q = new_q
for z in range(H):
    for y in range(N):
        for x in range(M):
            if(tomato[z][y][x] == 0):
                print(-1)
                exit(0)
print(cnt-1)