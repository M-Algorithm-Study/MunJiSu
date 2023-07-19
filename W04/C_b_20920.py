# 시간복잡도: O(N logN)

import sys
input = sys.stdin.readline
from collections import Counter

N, M = map(int, input().split())
d = Counter([i for _ in range(N) if len(i:= input().strip()) >= M])
# 알파벳 사전 순
res = sorted(list(d.keys()))
# 길이 순
res.sort(key=len, reverse=True)
# 빈도수
res.sort(key=d.get,reverse=True)
print('\n'.join(res))

"""
:= 

- Python 3.8부터 도입된 연산자
- 할당과 반환을 동시에 하는 연산자
- 변수 := 표현식
- 코드량이 줄어들면서 가독성이 높아진다
"""
"""
value 기준으로 정렬할 때, key 값만 얻는 목적이면 key=dict.get 사용
"""