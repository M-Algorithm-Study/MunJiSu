# 시간복잡도: O(2^N)

import sys
input = sys.stdin.readline

N = int(input())
print(2**N -1)
def hanoi(N, start, end, block):
    if N == 1: print(start, end); return
    else:
        hanoi(N-1, start, block, end); print(start, end)
        hanoi(N-1, block, end, start)

hanoi(N, 1, 3, 2)


"""
이해하기 어려워 하노이탑 알고리즘 관련 강의 찾아봄
그림 그려가며 풀면 규칙 찾기, 이해 쉬움
"""