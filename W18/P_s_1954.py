# 시간복잡도: O(T * N^2)

import sys

sys.stdin = open("input_1954.txt", "r")

def d(x, y):
    if 0 <= x < N and 0 <= y < N:
        return True
    else:
        return False


T = int(input())
for t in range(1, T + 1):
    N = int(input())
    li = [[0] * N for _ in range(N)]
    # 우, 하, 좌, 상
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]

    # 첫 시작점 (0, 0)으로 만들어주기 위해
    nx, ny = 0, -1
    di = 0  # 우: 0, 하: 1, 좌: 2, 하: 3

    i = 1
    while i <= N**2:
        nx, ny = nx + dx[di], ny + dy[di]

        while d(nx, ny) and li[nx][ny] == 0:
            li[nx][ny] = i
            nx, ny = nx + dx[di], ny + dy[di]
            i += 1
        # 범위를 벗어났으므로 진행된 방향 반대로 한 칸 이동(이동하기 전으로 다시 돌아감)
        nx, ny = nx - dx[di], ny - dy[di]

        # 다음 방향으로 넘어가는데, 우-하-좌-상 4가지 방향으로 반복해서 순환되므로 % 사용
        di = (di + 1) % 4

    print(f"#{t}")
    for k in li:
        print(*k)