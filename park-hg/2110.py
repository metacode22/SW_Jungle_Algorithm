import sys
sys.stdin = open('input.txt')
N, C = map(int, sys.stdin.readline().split())
X = [int(sys.stdin.readline()) for _ in range(N)]
X.sort()

def func(x):
    cnt = 1
    start = X[0]
    for i in range(1, len(X)):
        if X[i] - start >= x:
            cnt += 1
            start = X[i]

    return cnt

left, right = -1, 10**9+1
while left < right:
    mid = (left+right) // 2
    if func(mid) >= C:
        left = mid+1
    else:
        right = mid

print(left-1)