# 시간복잡도: O(N)

import sys
input = sys.stdin.readline

N, S = map(int, input().split())
nums = list(map(int, input().split()))

start, end = 0, 0
cur_sum = nums[0]
max_sum = 100001

while 1:
    if cur_sum < S:
        end += 1
        if end == N: break
        cur_sum += nums[end]
    else:
        cur_sum -= nums[start]
        max_sum = min(max_sum, end-start+1)
        start += 1

print(max_sum if max_sum != 100001 else 0)

"""
투 포인터 알고리즘 이용
수열의 각 원소는 10000 이하의 자연수이므로 수열의 최대값은 100000 이다.
"""