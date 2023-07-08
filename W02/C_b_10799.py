# 시간복잡도: O(len(a))

import sys
input = sys.stdin.readline

a = list(input().strip())
li = []
cnt = 0

for i in range(len(a)):
    if a[i] == '(': li.append(a[i])
    else:
        if a[i-1] == '(': li.pop(); cnt += len(li)
        else: li.pop(); cnt += 1

print(cnt)

"""
- for i in a: 로 반복문을 돌리려고 했으나 앞 순서의 괄호가 어떤 것인지 알기 위해서 range(len(a))로 변경
- 굳이 리스트로 하지 않고 문자열로 해도 될 것 같음
"""