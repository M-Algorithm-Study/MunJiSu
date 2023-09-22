# 시간복잡도: O(N)

import sys

input = sys.stdin.readline

N = int(input())
M = int(input())
if M != 0:
    btn = list(input().strip())
else:
    btn = []
# 채널 N으로 이동하기 위해 필요한 숫자
need = abs(100 - N)


# 채널의 각 숫자를 확인하여 고장난 버튼 필요한지 찾는 함수
def find_channel(channel):
    ch = list(str(channel))
    for i in ch:
        if i in btn:
            return False
    return True


# 0부터 100만까지 모든 채널에 대해 검사 (일반적인 모든 채널은 999999 까지임)
# 그리고 수빈이가 이동하려고 하는 채널 N (0 ≤ N ≤ 500,000)이 주어지면 위의 채널 숫자로 가서 -를 해도 되기 때문에 2배 적용
for channel in range(1000001):
    if find_channel(channel):
        # 현재 채널에서 N까지의 거리 + 숫자 버튼을 누르는 횟수
        # => 리모컨으로 이동할 수 있는 가장 가까운 숫자로 가서 +, - 버튼 누를 수 있기 떄문
        need = min(need, abs(N - channel) + len(str(channel)))

print(need)
