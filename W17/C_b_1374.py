# 시간복잡도: O(N log N)

import sys
from heapq import heappop, heappush

input = sys.stdin.readline

N = int(input())
lectures = []
for _ in range(N):
    num, s, e = map(int, input().split())
    # 강의 번호는 필요없으므로 시작시간과 끝나는 시간만 사용
    lectures.append((s, e))

# 강의 시작 시간, 강의 종료 시간 => 시작 시간 기준 정렬
lectures.sort(key=lambda x: x[0])

heap = []
for s, e in lectures:
    # 가장 일찍 종료되는 시간보다 현재 시작 시간이 늦으면 가장 작은 값(이전 수업 종료 값) pop
    if heap and s >= heap[0]:
        heappop(heap)
    # 힙에 끝나는 시간 추가 (다음 시작시간과 비교하기 위해)
    heappush(heap, e)

# heap에 남는 원소들은 강의실을 재사용할 수 없는 강의시간만 남으므로 힙 리스트의 개수를 세면 됨
print(len(heap))

"""
dfs 시도 => 시간초과
파이썬 heapq 라이브러리 => 기본적으로 최소힙으로 구현
"""
