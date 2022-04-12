import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

n, m = map(int, input().split())
h = list(map(int, input().split()))
h.sort()

def check(len):     # len으로 나무들(h)을 잘랐을 때 가지고 갈 수 있는 길이(tot)
    tot = 0
    
    for i in range(n):
        if h[i] > len:
            tot += h[i] - len
    
    return tot
    
lt = 1
rt = h[-1]
res = 0
while lt <= rt:
    mid = (lt + rt)//2
    
    if check(mid) >= m:     # 이분 탐색에서 mid는, 예상할 수 있는 범위 내에서(lt ~ rt) 찾는 것이기 떄문에 처음 mid가 당연히 우리가 찾는 길이는 아닐 것이다.
        lt = mid + 1        # 이 문제에서는 처음 mid = 10으로 할 경우 tot = 22가 반환되는데 이는 충분하다. 이 때 mid는 우리가 찾으려는 최적의 mid 값이 아니다. 우리는 m = 7만큼만 가져가면 되기 때문이다.
        res = mid           # 따라서 mid를 올려서(올리기 때문에 최댓값이다) 7 혹은 7과 가까운 길이만큼만 가져갈 수 있도록 최적화해야 한다.(결정알고리즘)
    else:                   # mid를 올려야 하므로 lt를 mid 옆으로 옮긴다.
        rt = mid - 1
        
print(res)