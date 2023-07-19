# 시간복잡도: O(N)

import sys
input = sys.stdin.readline

n = int(input())
step = [int(input()) for _ in range(n)]

def solve(step):
    if n == 1: return step[0]
    if n == 2: return step[0] + step[1]

    dp = [0] * n
    dp[0], dp[1] = step[0], step[0] + step[1]
    dp[2] = max(step[0] + step[2], step[1] + step[2])

    for i in range(3, n):
        dp[i] = max(step[i] + step[i-1] + dp[i-3], step[i] + dp[i-2])
    
    return dp[-1]

print(solve(step))