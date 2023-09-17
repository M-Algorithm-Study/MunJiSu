# 시간복잡도: O(N * M) (M은 각 숫자를 문자열로 변환한 후에 문자열의 길이)

import sys

sys.stdin = open("input_1926.txt", "r")

N = int(input())
clap = ["3", "6", "9"]

for i in range(1, N + 1):
    cnt = 0
    for j in str(i):
        if j in clap:
            cnt += 1
    if cnt > 0:
        i = "-" * cnt
    print(i, end=" ")
