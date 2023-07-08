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
투포인터를 활용해야함
"""

"""
https://blogeon.tistory.com/entry/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-LV2-%ED%8C%8C%EC%9D%B4%EC%8D%AC-Python-%EC%97%B0%EC%86%8D%EB%90%9C-%EB%B6%80%EB%B6%84-%EC%88%98%EC%97%B4%EC%9D%98-%ED%95%A9


"""