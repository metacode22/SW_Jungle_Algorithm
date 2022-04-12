import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

n, b = map(int, input().split())
mat = []

for _ in range(n):
    mat.append(list(map(int, input().split())))
    
def multi(mat_m1, mat_m2):
    res = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                res[i][j] += mat_m1[i][k] * mat_m2[k][j]
            res[i][j] %= 1000
    return res

def recur(mat_r, b):
    if b == 1:
        for i in range(n):
            for j in range(n):
                mat_r[i][j] %= 1000
        return mat_r
    else:
        tmp = recur(mat_r, b//2)
        if b % 2 == 0:
            return multi(tmp, tmp)
        else:
            return multi(mat_r, multi(tmp, tmp))

res = recur(mat, b)

for i in range(n):
    print(*res[i])