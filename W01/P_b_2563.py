# 시간복잡도: O(N)

import sys
input = sys.stdin.readline
arr = [[0]*100 for _ in range(100)]
P = int(input())
for _ in range(P):
    x, y = list(map(int, input().split()))
    for i in range(x, x+10):
        for j in range(y, y+10):
            arr[i][j] = 1
result = 0
for i in arr:
    result += i.count(1)
print(result)