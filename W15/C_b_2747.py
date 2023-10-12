# 시간복잡도: O(N)

import sys

input = sys.stdin.readline

dp = [0] * 46

dp[1], dp[2] = 1, 1


def fibo(x):
    # 이미 계산한 적 있는 문제라면 그대로 반환
    if dp[x] != 0:
        return dp[x]
    # 아직 계산하지 않은 문제라면 점화식에 따라서 피보나치 결과 반환
    dp[x] = fibo(x - 1) + fibo(x - 2)
    return dp[x]


print(fibo(int(input())))
