# 시간복잡도: O(N^2)

import sys

input = sys.stdin.readline

N = int(input())
seq = list(map(int, input().split()))

# 수열 길이를 저장할 dp리스트
dp = [0] * N

for i in range(N):
    for j in range(i):
        # 현재 인덱스와 이전의 인덱스들을 비교하여 더 큰값인지
        # dp리스트의 현재 인덱스가 이전의 인덱스들과 비교하여 더 작은 값인지
        if seq[i] > seq[j] and dp[i] < dp[j]:
            dp[i] = dp[j]
    # 이전 값들이 더 크더라도 현재 인덱스 하나의 수열이 생성됨
    dp[i] += 1
print(max(dp))
