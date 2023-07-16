# 시간복잡도: O(N!)

import sys
input = sys.stdin.readline
N = int(input())

cnt = 0
visited = [0] * N

def is_queen(n):
    for i in range(n):
        if visited[n] == visited[i] or abs(visited[n] - visited[i]) == abs(n - i):
            return False
    
    return True

def n_queens(n):
    global cnt
    if n == N:
        cnt += 1

    else:
        for i in range(N):
            visited[n] = i
            if is_queen(n):
                n_queens(n+1)

n_queens(0)
print(cnt)

"""
시간초과 해결 : y축차이 = x축 차이일 때 같은 대각선에 있다
"""

# 시간초과
import sys
input = sys.stdin.readline

def is_queen(visited, row, col, N):
    # 같은 열
    for i in range(row):
        if visited[i][col] == 1:
            return False
    
    # 왼쪽 위 대각선
    i, j = row, col
    while i >= 0 and j >= 0:
        if visited[i][j] == 1:
            return False
        i -= 1
        j -= 1
    
    # 오른쪽 위 대각선
    i, j = row, col
    while i >= 0 and j < N:
        if visited[i][j] == 1:
            return False
        i -= 1
        j += 1
        
    return True

def solve(visited, row, N):
    if row == N:
        return 1
    
    cnt = 0
    for col in range(N):
        if is_queen(visited, row, col, N):
            visited[row][col] = 1
            cnt += solve(visited, row+1, N)
            visited[row][col] = 0
    return cnt

def n_queen(N):
    visited = [[0] * N for _ in range(N)]
    return solve(visited, 0, N)

N = int(input())
print(n_queen(N))


"""
체스에서 퀸은 가로, 세로, 대각선 원하는 만큼 이동 가능하다.
=> 무조건 한 줄에 하나만 놓기 가능
"""