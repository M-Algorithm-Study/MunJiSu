# 시간복잡도: O(N)

import sys
input = sys.stdin.readline

N = int(input())
cnt, m_cnt = 0, 0

for _ in range(N):
    p = input().rstrip()
    k, m = map(int, input().split())
    pokemon = 0
    while k <= m:
        m -= k
        m += 2
        pokemon += 1
    cnt += pokemon
    
    if pokemon > m_cnt: m_cnt = pokemon; m_pokemon = p

print(cnt, m_pokemon, sep='\n')