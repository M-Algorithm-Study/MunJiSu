# 시간복잡도: O(V + E) V: 노드수, E: 간선수

import sys
from collections import deque

input = sys.stdin.readline

# 수빈, 동생
N, K = map(int, input().split())

graph = [-1] * 100001
graph[N] = 0
q = deque([N])

while q:
    x = q.popleft()
    if x == K:
        print(graph[x])
        break
    # 순간이동이 걷기보다 우선순위가 높으므로 걷기보다 앞에 위치시킴
    for i in (2 * x, x - 1, x + 1):
        # 범위 내 인지 확인 + 이동하지 않았는지 판단
        if 0 <= i < 100001 and graph[i] == -1:
            # 순간이동
            if i == 2 * x:
                graph[i] = graph[x]
                q.appendleft(i)
            # 걷기
            else:
                graph[i] = graph[x] + 1
                q.append(i)