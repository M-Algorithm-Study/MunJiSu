import sys
sys.stdin = open("input.txt", "r")

T = int(input())

for t in range(1, T+1) :
    N = int(input())

    res = 1
    for i in range(2, N+1) :
        if i % 2 == 0 :
            res -= i
        else :
            res += i

    print("#{} {}".format(t, res))