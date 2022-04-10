import sys
sys.stdin = open('input.txt')
N = int(sys.stdin.readline())
grid = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

white, blue = 0, 0
def rec(x, y, n):
    global white, blue
    
    if n == 0:
        return
        
    total_sum = 0
    for i in range(x, x+n):
        for j in range(y, y+n):
            total_sum += grid[i][j]
    if total_sum == 0:
        white += 1
        return
    if total_sum == n**2:
        blue += 1
        return

    mid = n//2
    rec(x, y, mid)
    rec(x, y+mid, mid)
    rec(x+mid, y, mid)
    rec(x+mid, y+mid, mid)

rec(0, 0, N)
print(white)
print(blue)