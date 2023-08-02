# 시간복잡도: O(N^2)

def dfs(idx, visited, computers):
    visited[idx] = True
    # 연결된 컴퓨터들을 모두 방문처리
    for nei in range(len(computers)): 
        if not visited[nei] and computers[idx][nei]: 
            dfs(nei, visited, computers)

def solution(n, computers):
    cnt = 0   
    visited = [False] * n   

    # 모든 컴퓨터를 하나씩 방문
    for idx in range(n):
        if not visited[idx] :
            dfs(idx, visited, computers)
            # dfs 함수 종료는 하나의 네트워크가 완성
            cnt += 1 

    return cnt

"""
깊이 우선 탐색: 한 노드에서 시작하여 인접한 노드를 탐색하면서 최대한 깊숙히 들어가며, 더 이상 진행할 수 없을 때 되돌아가서 다른 경로를 탐색 => DFS 사용

computers[i][i] 는 무조건 1이다.
computers[1][2] = 1 이면 1번 컴퓨터와 2번 컴퓨터가 연결되어있다.
"""