# 시간복잡도: O(leng1 * leng2)

import sys

input = sys.stdin.readline

word1 = input().strip()
word2 = input().strip()

leng1, leng2 = len(word1), len(word2)

dp = [[0] * (leng2 + 1) for _ in range(leng1 + 1)]

for i in range(1, leng1 + 1):
    for j in range(1, leng2 + 1):
        if word1[i - 1] == word2[j - 1]:
            dp[i][j] = dp[i - 1][j - 1] + 1
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
print(dp[-1][-1])
