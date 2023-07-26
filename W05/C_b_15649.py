# 시간복잡도: O(N^M)

import sys
input = sys.stdin.readline
N, M = map(int, input().split())
li = [] # M개의 수열을 저장하기 위한 리스트
def solve():
    if len(li) == M: # M개가 되면 출력하고 함수 끝
        print(' '.join(map(str, li)))
        return
    for i in range(1, N+1): # 1~N
        if i not in li: # 리스트와 중복 확인
            li.append(i) 
            solve()
            li.pop() # 4 2 입력이라면 1 - 1,2 - 1 - 1,3 - 1 - 1,4
solve()

# 시간복잡도: O(N! / (N-M)!)

from itertools import permutations
N,M = map(int, input().split(' '))
print('\n'.join(list(map(' '.join, permutations(map(str, range(1, N+1)), M)))))

"""
permutations 함수는 가능한 모든 순열을 생성
"""