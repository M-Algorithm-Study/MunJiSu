# 시간복잡도: O(N logN)

import sys
from heapq import heappop, heappush

numbers = int(input())
heap = []

for _ in range(numbers):
    num = int(sys.stdin.readline())
    if num != 0:
        heappush(heap, num)
    else:
        try:
            print(heappop(heap))
        except:
            print(0)
