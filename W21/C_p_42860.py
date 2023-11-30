# 시간복잡도: O(N)

def solution(name):
    answer = 0

    # 최소 좌우이동 횟수
    m_move = len(name) - 1

    # 인덱스, 알파벳
    for i, alpha in enumerate(name):
        # 다음 알파벳까지의 최소 이동 횟수
        up = ord(alpha) - ord("A")

        # 이전 알파벳까지의 최소 이동 횟수
        down = ord("Z") - ord(alpha) + 1

        # 다음 혹은 이전 알파벳까지의 최소 이동 횟수 중 최솟값을 찾아 이동 횟수 갱신
        answer += min(up, down)

        # 인덱스 다음으로 넘김
        next = i + 1

        # 진행한 알파벳 다음 알파벳부터 연속된 A 배열 찾기
        while next < len(name) and name[next] == "A":
            next += 1

        # 기존 최소 이동 횟수, 연속 A 배열 왼쪽부터 시작, 오른쪽부터 시작 비교해서 갱신
        m_move = min(m_move, 2 * i + len(name) - next, i + 2 * (len(name) - next))
        
    answer += m_move
    return answer

"""
최소횟수 : 연속된 A의 배열을 찾고 해당 배열의 왼쪽 혹은 오른쪽부터 변경

2 * i : 왼쪽부터 시작하려면 연속된 A 배열 이전의 인덱스 값을 다시 돌아가야하므로 인덱스를 2배 해준 다음 더해줘야 함

오른쪽부터 시작 한 방식도 같은 이유로 2배 해줌
"""
