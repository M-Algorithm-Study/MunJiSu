# 시간복잡도: O(√X)

import sys
input = sys.stdin.readline
X = int(input())
line = 1
while X > line:
    X -= line
    line += 1
print('/'.join([str(line+1-X), str(X)][::2*(line%2)-1]))

"""
그림 그려가며 규칙 찾기
"""