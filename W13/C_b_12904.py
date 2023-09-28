# 시간복잡도: O(N*M)

"""
S에서 T로 변환하는 풀이로 시간초과 => T에서 S로 변환
"""
import sys

input = sys.stdin.readline

S = input().strip()
T = input().strip()

# S와 T의 길이가 같아질 때까지 반복함
while len(S) != len(T):
    # 마지막 글자가 A라면 문자열 마지막의 A를 뺀다.
    if T[-1] == "A":
        T = T[:-1]
    # 마지막 글자가 B라면 B를 제거하고 문자열을 뒤집는다.
    else:
        T = T[:-1][::-1]
if S == T:
    print(1)
else:
    print(0)

"""
문자열의 뒤에 A를 추가한다. => 문자열 뒤의 A를 뺀다.
문자열을 뒤집고 뒤에 B를 추가한다. => B를 제거하고 문자열을 뒤집는다.
"""

# 시간초과 풀이
import sys

input = sys.stdin.readline

S = input().strip()
T = input().strip()


def solve(S, T):
    # S에서 T로 변환하기 때문에 S의 길이가 T보다 길어지면 False 반환
    if len(S) > len(T):
        return False
    # S와 T가 같아지면 True 반환
    if S == T:
        return True
    # 변환하는 방법 1, 2번을 각각 시도해서 True가 존재하면 True 반환
    if solve(S + "A", T) or solve(S[::-1] + "B", T):
        return True
    # 모든 값이 False이면 False 반환
    return False


if solve(S, T):
    print(1)
else:
    print(0)
