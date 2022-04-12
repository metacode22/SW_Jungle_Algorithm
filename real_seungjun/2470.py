import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
a.sort()

lt = 0
rt = n - 1
min = float('inf')
while lt < rt:      # 서로 다른 두 용액을 혼합시키는 것이기 때문에 lt와 rt가 같은 곳을 가르킬 수 없다.
    tot = a[lt] + a[rt]
    
    if abs(tot) < min:
        res_lt = lt
        res_rt = rt
        min = abs(tot)
        if abs(tot) == 0:
            break
    elif tot < 0:       # 포인터로 계속해서 0에 가까운 수들을 찾는 과정이다.
        lt += 1
    elif tot > 0:
        rt -= 1
        
print(a[res_lt], a[res_rt])