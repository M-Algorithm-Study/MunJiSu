# 시간복잡도: O(N)

import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
q = deque()
for i in range(N):
    command = input().split()
    a = command[0]

    if a == 'push': q.append(command[1])
    elif a == 'pop': 
        if not q: print(-1)
        else: print(q.popleft())
    elif a == 'size': print(len(q))
    elif a == 'empty':
        if not q: print(1)
        else: print(0)
    elif a == 'front':
        if not q: print(-1)
        else: print(q[0])
    else:
        if not q: print(-1)
        else: print(q[-1])