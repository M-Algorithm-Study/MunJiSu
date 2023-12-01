# 시간복잡도: O(N)

def solution(N, number):
    # 중복 허용하지 않고 탐색이 빠른 set 사용
    n_set = [set() for _ in range(9)]

    # N을 i번씩 사용하는 숫자들을 정수형으로 바꿔 각 set에 추가해줌
    for i in range(1, 9):
        n_set[i].add(int(str(N) * i))

    # 규칙 참고
    for i in range(1, 9):
        for j in range(1, i):
            for x in n_set[j]:
                for y in n_set[i - j]:
                    n_set[i].add(x + y)
                    n_set[i].add(x - y)
                    n_set[i].add(x * y)
                    # 분모가 0인 경우는 값이 무한대로 나누기가 불가능
                    # 나머지 무시하므로 몫만
                    if y != 0:
                        n_set[i].add(x // y)
        if number in n_set[i]:
            return i
    return -1


solution(5, 12)

"""
N을 i번 사용하는 경우

- N이 i번 반복되는 수
- (N을 1번) 사칙연산 (N을 i-1번)
- (N을 2번) 사칙연산 (N을 i-2번)
- (N을 3번) 사칙연산 (N을 i-3번)
...
- (N을 i-1번) 사칙연산 (N을 1번)
"""
