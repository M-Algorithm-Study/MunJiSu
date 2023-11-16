# 시간복잡도: O(N logN)

def solution(citations):
    # 내림차순 정렬
    citations.sort(reverse=True)
    for i, j in enumerate(citations):
        # h편 이상 인용된 눈문이 h편 이상
        if i >= j:
            return i
    # 하나의 값만 존재할 때는 1
    return len(citations)

"""
논문 n편 중, h번 이상 인용된 논문이 h편 이상이고 나머지 논문이 h번 이하 인용되었다면 h의 최댓값

큰 숫자 부터 정렬
인덱스  값
0   6
1   5
2   3
3   1
4   0
"""