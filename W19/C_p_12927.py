# 시간복잡도: O(NlogN)

from heapq import heapify, heappop, heappush

def solution(n, works):
    # 남은 작업량이 없으므로 피로도는 0
    if sum(works) <= n:
        return 0
    
    answer = 0
    # 가장 큰 값을 먼저 사용하기 위해 최대 힙 사용
    works = [-w for w in works]
    heapify(works)
    
    while n > 0:
        max_num = heappop(works)
        heappush(works, max_num+1)
        n -= 1

    for w in works:
        answer += w ** 2
    return answer

"""
n 시간만큼 n 만큼의 일만 가능.
제곱의 합을 최소화해야하므로 남은 작업량 값들을 하향평준화.
"""