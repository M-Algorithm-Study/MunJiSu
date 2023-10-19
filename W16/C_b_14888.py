# 시간복잡도: O(4^N)

import sys

input = sys.stdin.readline

N = int(input())
nums = list(map(int, input().split()))
plus, minus, multi, div = map(int, input().split())
ops = ["+", "-", "*", "/"]

# 최댓값으로 만들 수 있는 최솟값, 최솟값으로 만들 수 있는 최댓값
max_num, min_num = -1e9, 1e9


# 모든 경우의 수 탐색하기 위해서 dfs 마무리 된 후 연산자 개수 다시 채워줌
def dfs(idx, cur):
    global plus, minus, multi, div, max_num, min_num
    if idx == N:
        max_num = max(max_num, cur)
        min_num = min(min_num, cur)
    else:
        if plus > 0:
            plus -= 1
            dfs(idx + 1, cur + nums[idx])
            plus += 1
        if minus > 0:
            minus -= 1
            dfs(idx + 1, cur - nums[idx])
            minus += 1
        if multi > 0:
            multi -= 1
            dfs(idx + 1, cur * nums[idx])
            multi += 1
        if div > 0:
            div -= 1
            dfs(idx + 1, int(cur / nums[idx]))
            div += 1

# idx가 1 => 맨 처음 숫자는 초기값으로 설정함
dfs(1, nums[0])

print(max_num, min_num, sep="\n")

"""
연산자를 어떻게 끼워넣어도 항상 -10억보다 크거나 같고, 10억보다 작거나 같은 결과가 나오는 입력만 주어진다.
=> 최댓값, 최솟값 설정
"""
