import sys
import heapq
sys.stdin = open('input.txt')
input = sys.stdin.readline

n = int(input())
max_h, min_h = [], []

# 갯수는 왼쪽 max_h가 1개 더, 혹은 min_h랑 같게 유지하면서 max_h의 최대가 min_h의 최소보다 높아지면 둘의 루트를 바꿔준다.
# | 1 2 3 4 || 5 6 7 |
for _ in range(n):
    x = int(input())
    if len(max_h) == len(min_h):        # 왼쪽은 max, 오른쪽은 min으로 유지시키고 번갈아 넣어준다.    
        heapq.heappush(max_h, -x)       # 왼쪽에서 중간 값이 나오기 때문에 왼쪽의 갯수가 더 크게 한다.
    else:
        heapq.heappush(min_h, x)
        
# 위에서, 수를 비교해가며 번갈아 넣어주는 것이 아니기 때문에 왼쪽의 max 값이 오른쪽 min 값보다 커질 수 있다.        
# 만약 그렇게 된다면 둘의 루트를 바꿔주면 된다.
    if len(max_h) >= 1 and len(min_h) >= 1 and -max_h[0] > min_h[0]:
        max_val = heapq.heappop(max_h)
        min_val = heapq.heappop(min_h)
        
        heapq.heappush(max_h, -min_val)
        heapq.heappush(min_h, -max_val)
        
    print(-max_h[0])
