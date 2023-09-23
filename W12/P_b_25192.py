# 시간복잡도: O(N * |l|)

import sys

input = sys.stdin.readline


l = set()
r = 0
for i in range(int(input())):
    n = input().rstrip()
    if n == "ENTER":
        l = set()
    elif n not in l:
        r += 1
        l.add(n)
print(r)
