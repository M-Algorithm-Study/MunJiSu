# 시간복잡도: O(M * logM)

import sys

input = sys.stdin.readline

# 컴퓨터 수
N = int(input())
# 연결할 수 있는 선의 수
M = int(input())

parent = [i for i in range(N + 1)]


# 특정 원소가 속한 집합을 찾는 함수
def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]


# 두 원소가 속한 집합을 합치는 함수
def union(a, b):
    a, b = find(a), find(b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


# 모든 간선을 담을 리스트
edges = []

# 최종 비용
res = 0

for _ in range(M):
    # a, b : 컴퓨터 번호, c : 두 컴퓨터 연결하는 비용
    a, b, cost = map(int, input().split())
    edges.append((cost, a, b))

# 간선을 비용순으로 정렬
edges.sort()

# 간선을 하나씩 확인하며 사이클이 발생하지 않는 경우에만 집합에 포함
for edge in edges:
    cost, a, b = edge
    if find(a) != find(b):
        union(a, b)
        res += cost

print(res)

"""
크루스칼 알고리즘 사용
"""