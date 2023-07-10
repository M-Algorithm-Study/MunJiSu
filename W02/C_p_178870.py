# 시간복잡도: O(N)

def solution(sequence, k):
    answer = []
    n = len(sequence)
    start, end = 0, 0
    for i in range(n):
        while start < k and end < n:
            start += sequence[end]
            end += 1
        if start == k:
            answer.append((i, end-1))
        start -= sequence[i]
        
    return sorted(answer, key=lambda x: x[1]-x[0])[0]

"""
투 포인터 알고리즘을 활용해야함
"""