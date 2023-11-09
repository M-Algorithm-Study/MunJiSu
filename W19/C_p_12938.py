# 시간복잡도: O(N)

def solution(n, s):
    # 집합의 원소의 개수 n과 모든 원소들의 합 s
    # 원소 개수가 합보다 크면 집합은 존재할 수 없다
    if n > s:
        return [-1]
    
    a, b = divmod(s, n)
    answer = [a] * n
    
    for i in range(b):
        answer[i] += 1
        
    return sorted(answer)

"""
합이 같은 두 수 들을 곱한 값은 해당 두 수의 차가 적어야 큼
=> 원소의 합 S를 원소의 개수로 나눠서 집합의 원소들이 최대한 적은 차를 가지도록 함

divmod(a, b) = (a // b, a % b)
"""