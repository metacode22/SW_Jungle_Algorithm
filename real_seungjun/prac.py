import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

a, b, c = map(int, input().split())

def recur(x, y):
    global c
    
    if y == 1:
        return x % c
    else:
        tmp = recur(x, y//2)
        
    if y % 2 == 0:
        return (tmp * tmp) % c
    elif y % 2 == 1:
        return (tmp * tmp * x) %c 
        
print(recur(a, b))