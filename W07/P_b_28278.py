# 시간복잡도: O(N)

import sys
input = sys.stdin.readline

stack = []

N = int(input())
for i in range(N):
    command = input().split()
    a = command[0]
    if a == '1': stack.append(command[1])
    elif a == '2':
        if stack: print(stack.pop())
        else: print(-1)
    elif a == '3': print(len(stack))
    elif a == '4':
        if not stack: print(1)
        else: print(0)
    else:
        if stack: print(stack[-1])
        else: print(-1)