# 시간복잡도: O(N)

from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def solution(rectangle, characterX, characterY, itemX, itemY):
    answer = 0

    board = [[-1] * 102 for i in range(102)]
    
    for r in rectangle:
    	# 모든 좌표값을 2배 해줌
        x1, y1, x2, y2 = map(lambda x: x*2, r)
        for i in range(x1, x2+1):
            for j in range(y1, y2+1):
                # 직사각형 내부이면 0으로 바꿈
                if x1 < i < x2 and y1 < j < y2:
                    board[i][j] = 0
                # 직사각형의 테두리일 때 1로 바꿈
                elif board[i][j] != 0:
                    board[i][j] = 1
                    
    q = deque()
    q.append([characterX * 2, characterY * 2])
    # 아직 방문하지 않은 곳은 1로 채움
    visited = [[1] * 102 for i in range(102)]
    # 시작 지점은 0으로 초기화(거리가 0)
    visited[characterX * 2][characterY * 2] = 0
    
    while q:
        x, y = q.popleft()
        # 현재 좌표가 아이템 좌표라면 현재의 최단거리//2 를 answer로 함
        if x == itemX * 2 and y == itemY * 2:
            answer = visited[x][y] // 2
            break
        # 아니라면 상하좌우 탐색
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            
            # 현재 좌표가 테두리이고 아직 방문하지 않은 곳이라면 q에 추가 후 visited를 최단거리로 갱신
            if board[nx][ny] == 1 and visited[nx][ny] == 1:
                q.append([nx, ny])
                visited[nx][ny] = visited[x][y] + 1
    
    return answer

"""
[좌측 하단 x, 좌측 하단 y, 우측 상단 x, 우측 상단 y]
초기 캐릭터의 위치 characterX, characterY
아이템의 위치 itemX, itemY

테두리를 그리기 위해 직사각형을 테두리를 포함하여 모두 1로 채운 후 내면만 0으로 바꿈

101*101 크기는 틀림 => 좌표를 2배 해주었으므로

좌표를 2배 해주는 경우는 블로그 참고
"""
# 시간초과 풀이
"""
from collections import deque


# 좌표의 직사각형 내 존재 유무 판별 함수
def inside(x, y, rectangle):
    for rect in rectangle:
        x1, y1, x2, y2 = rect
        if x1 <= x <= x2 and y1 <= y <= y2:
            return True
    return False


def solution(rectangle, characterX, characterY, itemX, itemY):
    # 현재x, 현재y, 이동거리
    q = deque([(characterX, characterY, 0)])
    # 탐색 시간복잡도 줄이기 위해 set 사용
    visited = set([(characterX, characterY)])

    while q:
        x, y, distance = q.popleft()

        if x == itemX and y == itemY:
            return distance

        # 상하좌우로 이동가능한 좌표
        cd = [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]

        for cd_x, cd_y in cd:
            # 테두리로 이동해야 하므로 직사각형 내에 존재하면 안됨
            if not inside(cd_x, cd_y, rectangle) and (cd_x, cd_y) not in visited:
                q.append((cd_x, cd_y, distance + 1))
                visited.add((cd_x, cd_y))

    return -1
"""
