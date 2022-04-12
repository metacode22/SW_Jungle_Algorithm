import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

n, c = map(int, input().split())
a = [int(input()) for _ in range(n)]
a.sort()

def count(x):
    end_point = a[0]
    cnt = 1
    
    for i in a:
        if i - end_point >= x:
            end_point = i
            cnt += 1
            
    return cnt
    
lt = 1      # 같은 좌표를 가지는 일은 없으므로 항상 최소 1이상의 거리는 차이가 나게 되어있다.
rt = a[-1] - a[0]
res = 0
while lt <= rt:
    mid = (lt + rt)//2
    if count(mid) >= c:
        res = mid
        lt = mid + 1
    else:
        rt = mid - 1
        
print(res)
        
