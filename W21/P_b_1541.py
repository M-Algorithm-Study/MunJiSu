# 시간복잡도: O(N)

import sys

input = sys.stdin.readline

arr = input().split("-")
s = 0
for i in arr[0].split("+"):
    s += int(i)
for i in arr[1:]:
    for j in i.split("+"):
        s -= int(j)
print(s)

"""
+, - 만 존재하기 때문에 - 기준으로 괄호 배치하면 됨
"""
