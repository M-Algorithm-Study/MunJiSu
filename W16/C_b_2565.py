# 시간복잡도: O(N^2)

import sys

input = sys.stdin.readline

n = int(input())
cable = sorted([list(map(int, input().split())) for _ in range(n)])

# 증가하지 않더라도 해당 순서만 포함된 수열이 있기 때문에 전체 초기값 1
dp = [1] * n
for i in range(n):
    for j in range(i):
        if cable[i][1] > cable[j][1]:
            dp[i] = max(dp[i], dp[j] + 1)

print(n - max(dp))

"""
A 전깃줄 순으로 정렬해서 다음 번호의 B 전깃줄이 이전 번호의 B 전깃줄 숫자보다 작으면 교차
A 기준 정렬 => B 전깃줄 최대 증가 수열 찾기
"""
