# 시간복잡도: O(2^C)

import sys
input = sys.stdin.readline

L, C = map(int, input().split())
s_li = sorted(list(map(str, input().strip().split())))

vowel = ['a', 'e', 'i', 'o', 'u']

def password(cur, cur_l, idx, v_cnt, c_cnt):
    if cur_l == L and v_cnt > 0 and c_cnt > 1:
        print(cur)
        return
    for i in range(idx, C):
        if s_li[i] in vowel: password(cur+s_li[i], cur_l+1, i+1, v_cnt+1, c_cnt)
        else: password(cur+s_li[i], cur_l+1, i+1, v_cnt, c_cnt+1)

password("", 0, 0, 0, 0)