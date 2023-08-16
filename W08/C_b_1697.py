# 시간복잡도: O(1)

from collections import deque
import sys
input = sys.stdin.readline

N, K = map(int, input().split()) # N: 수빈, K: 동생

visited = [0] * 100001

def bfs():
    q = deque()
    q.append(N)

    while q:
        x = q.popleft()
        if x == K: print(visited[x]); break

        for i in (x-1, x+1, 2*x):
            if 0 <= i <= 100000 and visited[i] == 0:
                visited[i] = visited[x] + 1
                q.append(i)

bfs()

"""
걷는다 => 1초 후에 X-1 또는 X+1로 이동
순간이동 => 1초 후에 2*X의 위치로 이동
최대 크기 100,000
"""