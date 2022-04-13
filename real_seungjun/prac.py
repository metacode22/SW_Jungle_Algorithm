import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

m, n, l = map(int, input().split())
mx = list(map(int, input().split()))
ani = [list(map(int, input().split())) for _ in range(n)]
mx.sort()

cnt = 0 
for x, y in ani:
    if y > l:
        continue
    
    lt = 0
    rt = m - 1
    min_m = x + y - l
    max_m = x - y + l
    while lt <= rt:
        mid = (lt + rt)//2
        if min_m <= mx[mid] <= max_m:
            cnt += 1
            break    
        elif mx[mid] < min_m:
            lt = mid + 1
        else:
            rt = mid - 1

print(cnt)
        