import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

n, k = map(int, input().split())
a = [int(input()) for _ in range(n)]
a.sort()

def level(x):
    tot = 0
    for i in a:
        if i < x:
            tot += (x - i)
            
    return tot

lt = a[0]
rt = a[-1] + k
res = 0
while lt <= rt:
    mid = (lt + rt)//2
    
    if level(mid) <= k:     # k보다 작다면 충분히 최소 레벨을 올려볼 가치가 있다는 것.
        res = mid
        lt = mid + 1
    else:
        rt = mid - 1        # k보다 크다면 쓸 수 있는 레벨(k)보다 더 썼다는 뜻이니 줄여야 한다.

print(res)