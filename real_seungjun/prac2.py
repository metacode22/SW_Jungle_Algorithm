import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

n = int(input())
mat = [list(map(int, list(str(input().rstrip())))) for _ in range(n)]
res = []

def recur(x, y, N):
    tot = 0
    for i in range(x, x + N):
        for j in range(y, y + N):
            tot += mat[i][j]
    
    if tot == N**2:
        res.append('1')
        return
    elif tot == 0:
        res.append('0')
        return
    else:
        res.append('(')
        recur(x, y, N//2)
        recur(x, y + N//2, N//2)
        recur(x + N//2, y, N//2)
        recur(x + N//2, y + N//2, N//2)
        res.append(')')
        
recur(0, 0, n)
print(''.join(res))