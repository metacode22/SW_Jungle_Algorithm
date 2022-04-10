import sys
sys.stdin = open('input.txt')

N, M = map(int, sys.stdin.readline().split())
trees = list(map(int, sys.stdin.readline().split()))
def func(x):
    y = 0
    for tree in trees:
        y += max((tree-x), 0)
    
    return y

left, right = 0, 2*10**9+1

while left < right:
    
    mid = (left + right) // 2
    print(left, right, mid, func(mid), M)
    if func(mid) > M:
        left = mid+1
    elif func(mid) == M:
        left = mid
        break
    else:
        right = mid

print(left)