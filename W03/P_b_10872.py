# 시간복잡도: O(N)

import sys
input = sys.stdin.readline

def factorial_recursive(n):
    # n이 1 이하인 경우 1을 반환
    if n <= 1:
        return 1
    # n! = n * (n-1)!를 그대로 코드로 작성하기
    return n * factorial_recursive(n-1)

n = int(input())
print(factorial_recursive(n))