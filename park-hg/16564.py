import sys
sys.stdin = open('input.txt')

N, K = map(int, sys.stdin.readline().split())

X = [int(sys.stdin.readline()) for _ in range(N)]

def func(t):
    total = 0
    for x in X:
        total += max(t-x, 0)
    return total

left, right = -1, 10**9+1
while left < right:
    mid = (left+right) // 2
    if func(mid) <= K:
        left = mid+1
    else:
        right = mid

print(left-1)