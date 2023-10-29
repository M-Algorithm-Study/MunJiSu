# 시간복잡도: O(N log N)

import sys
from heapq import heappop, heappush

input = sys.stdin.readline

heap = []
n = int(input())

for _ in range(n):
    nums = map(int, input().split())
    for num in nums:
        # heap의 크기를 n개로 유지
        if len(heap) < n:
            heappush(heap, num)
        else:
            if heap[0] < num:
                heappop(heap)
                heappush(heap, num)
print(heap[0])
