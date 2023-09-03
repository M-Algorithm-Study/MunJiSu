# 시간복잡도: O(T * 10000)

import sys
sys.stdin = open("input_1216.txt", "r")

def is_pal_idx(arr, leng):
    for lst in arr:
        for i in range(100-leng+1):
            for j in range(leng//2):
                if lst[i+j] != lst[i+leng-1-j]:
                    break
            else:
                return True
    return False


T = 10
for _ in range(1, T+1):
    t = int(input())
    maxNum = 0

    arr1 = [input().strip() for _ in range(100)]
    arr2 = [''.join(x) for x in zip(*arr1)]

    for leng in range(100, 1, -1):
        if is_pal_idx(arr1, leng) or is_pal_idx(arr2, leng):
            break

    print("#{} {}".format(t, leng))