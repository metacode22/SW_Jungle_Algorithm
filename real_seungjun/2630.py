import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

n = int(input())
board = [(list(map(int, input().split()))) for _ in range(n)]

one = 0
zero = 0

def recur(x, y, n):                 # (x, y)부터 (x+n, y+n)까지 0인지 1인지 확인한다.
    global one, zero
    
    if n == 0:
        return
        
    tot = 0
    for i in range(x, x + n):       # 현재 recur의 좌표에서 각 원소가 계속 0인지 1인지 확인하겠다.
        for j in range(y, y + n):
            tot += board[i][j]
            
    if tot == 0:                    # 다 합친 것이 0이라면, 모든 원소가 0이라는 뜻.
        zero += 1
        return
    elif tot == n**2:               # 다 합친 것이 1이라면, n*n 만큼의 원소가 모두 1이었다는 뜻.
        one += 1
        return
    
    recur(x, y, n//2)               # 위에서 모두 1이었거나 0이었거나를 걸러냈다.
    recur(x, y + n//2, n//2)        # 따라서 모두 0 혹은 1이 아니었다면 4분할을 해야 하므로 재귀에 들어간다.
    recur(x + n//2, y, n//2)
    recur(x + n//2, y + n//2, n//2)
    
recur(0, 0, n)                      # 0, 0부터 분할정복을 실시하겠다.
print(zero)
print(one)
