# 시간복잡도: O(N logN)

import sys
from heapq import heappop, heappush

input = sys.stdin.readline

n = int(input())
heap = []
for i in range(n):
    x = int(input())
    if x:
        heappush(heap, (-x, x))
    else:
        if len(heap) >= 1:
            print(heappop(heap)[1])
        else:
            print(0)
