# 시간복잡도: O(2^N) 또는 O(3^N)

import sys

input = sys.stdin.readline
dp = {1: 0, 2: 1}


# 딕셔너리에 필요한 계산의 값만 추가 => N이 커지면 시간복잡도 증가
# 값을 찾는 연산 부분에서 리스트보다 딕셔너리가 속도면에서 빠름
def solve(x):
    if x in dp:
        return dp[x]
    # x를 2 또는 3으로 나눈 나머지를 연산하는 데 필요한 연산 횟수 (한 번 나누었으므로 1회 추가)
    # 나머지를 더 해 주는 것은 2 또는 3으로 나눠떨어지지 않을 때는 1을 빼며 진행해야 하므로 나머지만큼 더해줌
    res = 1 + min(solve(x // 3) + x % 3, solve(x // 2) + x % 2)
    dp[x] = res
    return res

print(solve(int(input())))


# 시간복잡도: O(N)

import sys

input = sys.stdin.readline
N = int(input())
dp = [0] * (N + 1)

# 1은 1을 빼는 방법만 사용 가능하기 때문에 dp[1] = 0 이다.
for i in range(2, N + 1):
    # 1을 빼는 연산 => 1회
    dp[i] = dp[i - 1] + 1
    # 나누었으므로 1회 추가
    if i % 3 == 0:
        dp[i] = min(dp[i], dp[i // 3] + 1)
    if i % 2 == 0:
        dp[i] = min(dp[i], dp[i // 2] + 1)
        
print(dp[N])

"""
1. X가 3으로 나누어 떨어지면, 3으로 나눈다.
2. X가 2로 나누어 떨어지면, 2로 나눈다.
3. 1을 뺀다.

세가지 연산을 모두 비교해야 하기 때문에 미리 1을 뺴는 연산을 해준 뒤 시작

dp의 값은 횟수
"""
