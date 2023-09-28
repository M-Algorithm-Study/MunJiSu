# 시간복잡도: O(log n)

import sys

input = sys.stdin.readline

n, k = map(int, input().split())
# start: 가위질 최소값, end: 가위질 최대값
start, end = 0, n // 2 + 1


# 가위질해서 만들 수 있는 색종이 총 개수를 구하는 함수
def paper(x):
    return (x + 1) * (n - x + 1)


while start != end:
    mid = (start + end) // 2
    res = paper(mid)
    if res == k:
        print("YES")
        exit(0)
    # 가위질 횟수가 k보다 크면 횟수를 줄여야 함 => end를 mid값으로 갱신
    if res > k:
        end = mid
    # 가위질 횟수가 k보다 작으면 횟수를 늘려야 함 => start를 mid + 1 값으로 갱신
    else:
        start = mid + 1

print("NO")

"""
1번 => 2장 (한방향 n번)
2번 => 3~4장 (최소: 한방향으로 n번, 최대: 가로 n/2, 세로 n/2)
3번 => 4~6장 (최소: 한방향 n번, 최대: 가로, 세로 1, 2번)
4번 => 5~9장 (최소: 한방향 n번, 최대: 가로 n/2, 세로 n/2)
5번 => 6~12장 (최소: 한방향 n번, 최대: 가로, 세로 2, 3번)
6번 => 7~16장 (최소: 한방향 n번, 최대: 가로 n/2, 세로 n/2)

색종이 총 개수 = 가로+1 * 세로+1
n = 가로 + 세로

따라서 색종이 총 개수 cnt = (가로+1) * (n-가로 +1)
"""
