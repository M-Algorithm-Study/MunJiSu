# 시간복잡도: O(p * (8-p+1))

import sys
sys.stdin = open("input.txt", "r")

T = 10
for t in range(1, T + 1):
    p = int(input())
    board = [list(input().strip()) for _ in range(8)]

    cnt = 0

    # 가로
    for i in range(0, 8):
        for j in range(0, 8-p+1):
            if board[i][j:j+p] == board[i][j:j+p][::-1]: cnt += 1
    
    # 세로
    for k in range(0, 8):
        for l in range(0, 8-p+1):
            char = ''
            for c in range(l, l+p):
                char += board[c][k]
            if char == char[::-1]: cnt += 1
    print('#{} {}'.format(t, cnt))