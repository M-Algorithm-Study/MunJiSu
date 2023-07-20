# 시간복잡도: O(T * log(min(a, b)))

import sys
input = sys.stdin.readline

T = int(input())

for i in range(T):
    a, b = map(int, input().split())
    c, d = a, b

    while a % b != 0:
        a, b = b, a % b

    print(c * d // b)