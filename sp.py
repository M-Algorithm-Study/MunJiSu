def solution(N, number):
    n_set = [set() for _ in range(9)]
    print(n_set)
    
    for i in range(1, 9):
        n_set[i].add(int(str(N)*i))
    
    for i in range(1, 9):
        for j in range(1, i):
            for x in n_set[j]:
                for y in n_set[i-j]:
                    n_set[i].add(x+y)
                    n_set[i].add(x-y)
                    n_set[i].add(x*y)
                    if y != 0:
                        n_set[i].add(x//y)
        if number in n_set[i]:
            return i
    return -1

solution(5, 12)