# 시간복잡도: O(N)

import sys
from collections import deque

input = sys.stdin.readline

N = int(input())
d = deque()
for i in range(N):
    order = list(map(int, input().split()))
    o1 = order[0]
    if len(order) > 1:
        o2 = order[1]

    if o1 == 1:
        d.appendleft(o2)
    elif o1 == 2:
        d.append(o2)
    elif o1 == 3:
        print(d.popleft() if d else -1)
    elif o1 == 4:
        print(d.pop() if d else -1)
    elif o1 == 5:
        print(len(d))
    elif o1 == 6:
        print(0 if d else 1)
    elif o1 == 7:
        print(d[0] if d else -1)
    else:
        print(d[-1] if d else -1)
