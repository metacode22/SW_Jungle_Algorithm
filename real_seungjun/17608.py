import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

n = int(input())
a = list()
for _ in range(n):
    num = int(input())
    a.append(num)
stack = []

# stack을 사용하여 중복을 없애는 동시에 크기 순으로 정렬하면 된다.
for i in a:
    while stack and stack[-1] <= i:     # stack에 원소가 존재하면서, i보다 작은 원소들을 계속 지운다.
        stack.pop()
    stack.append(i)     # stack 길이가 0이거나, while문에서 i보다 작은 걸 지우다가 i보다 큰 걸 만났으면 stack에 append    
    
print(len(stack))