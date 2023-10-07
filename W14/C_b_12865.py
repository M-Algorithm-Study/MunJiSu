# 시간복잡도: O(N * K)

import sys

input = sys.stdin.readline

# 물품 수, 무게
N, K = map(int, input().split())
dp = [[0] * (K + 1) for _ in range(N + 1)]

# 물건 0개의 값은 모두 0 => range 1부터
for i in range(1, N + 1):
    # 물건 무게, 물건 가치 (한 물건)
    W, V = map(int, input().split())
    for j in range(1, K + 1):
        # 감당할 수 있는 무게 - 물건의 무게 의 값은 무조건 0 이상이어야 하므로 음수인 값은 전부 dp 이전값을 받아옴
        if j - W < 0:
            dp[i][j] = dp[i - 1][j]
        # 감당할 수 있는 무게 - 물건의 무게 의 값이 0이상인 경우 이전값과 현재 물건 배낭에 넣고 남은 무게에 대한 값을 비교해서 큰 값 선택
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - W] + V)

print(dp[N][K])

"""
물품 수와 무게를 기준으로 이차원 리스트를 만들어 가치의 합을 값으로 저장

N, K = 4, 7
W   V       N\K 0 1 2 3 4 5  6  7
            0   0 0 0 0 0 0  0  0
6   13      1   0 0 0 0 0 0  13 13
4   8       2   0 0 0 0 8 8  13 13
3   6       3   0 0 0 6 8 8  13 14
5   12      4   0 0 0 6 8 12 13 14
"""
