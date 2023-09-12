# 시간복잡도: O(N)

import sys
sys.stdin = open("input_1859.txt", "r")

T = int(input())
for t in range(1, T + 1):
    N = int(input())
    nums = list(map(int, input().split()))
    res = 0
    price = 0
    for num in nums[::-1]:
        if num >= price:
            price = num
        else:
            res += price - num

    print("#{} {}".format(t, res))