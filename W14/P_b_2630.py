# 시간복잡도:

import sys

input = sys.stdin.readline

N = int(input())
paper = [list(map(int, input().split())) for _ in range(N)]

white, blue = 0, 0


def solve(x, y, N):
    global white, blue
    color = paper[x][y]
    for i in range(x, x + N):
        for j in range(y, y + N):
            if color != paper[i][j]:
                solve(x, y, N // 2)
                solve(x + N // 2, y, N // 2)
                solve(x, y + N // 2, N // 2)
                solve(x + N // 2, y + N // 2, N // 2)
                return
    if color == 0:
        white += 1
    else:
        blue += 1


solve(0, 0, N)
print(white, blue, sep="\n")
