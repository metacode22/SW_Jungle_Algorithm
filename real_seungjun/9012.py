import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

n = int(input())

def check(x):
    stack = []
    for i in x:
        if i == '(':
            stack.append('(')
        elif i == ')' and len(stack) == 0:
            return 'NO'
            
        elif i == ')':
            stack.pop()
        
    if len(stack) == 0:
        return 'YES'
    else:
        return 'NO'

for _ in range(n):
    bracket = list(input().rstrip())
    
    print(check(bracket))