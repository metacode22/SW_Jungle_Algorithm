import sys
sys.stdin = open('input.txt')
N, B = map(int, sys.stdin.readline().split())
A = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

def matmul(M1, M2):
    new_matrix = [[0]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            for k in range(N):
                new_matrix[i][j] += M1[i][k]*M2[k][j]
                new_matrix[i][j] %= 1000
    return new_matrix


def rec(M, n):
    for i in range(N):
        M[i] = [m%1000 for m in M[i]]
    if n == 1:
        return M
    half = rec(M, n//2)
    if n%2 == 0:
        return matmul(half, half)
    if n%2 == 1:
        return matmul(M, matmul(half, half))

C = rec(A, B)
for c in C:
    print(*c)