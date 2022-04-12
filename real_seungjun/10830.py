import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

n, b = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]

def mul(m1, m2):
    m3 = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                m3[i][j] += m1[i][k] * m2[k][j]      
            m3[i][j] %= 1000
            
    return m3

def recur(mat, x):
    if x == 1:
        for i in range(n):
            for j in range(n):
                mat[i][j] %= 1000
        return mat
        
    else:
        tmp = recur(mat, x//2)
        
        if x % 2 == 0:
            return mul(tmp, tmp)
        else:
            return mul(mul(tmp, tmp), mat)

res = recur(a, b)
for i in res:
    print(*i)