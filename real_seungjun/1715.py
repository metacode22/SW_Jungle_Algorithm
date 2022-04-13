import sys
import heapq
sys.stdin = open('input.txt')
input = sys.stdin.readline

n = int(input())
min_h = []  # 최소끼리 더해가는 것이 유리하기 때문에 min heap 사용

for _ in range(n):
    heapq.heappush(min_h, int(input()))

res = 0
while True:
    if len(min_h) >= 2:
        tmp1 = heapq.heappop(min_h)     # 최소의 수들을 더해가는 과정 반복  
        tmp2 = heapq.heappop(min_h)
        res += (tmp1 + tmp2)
        heapq.heappush(min_h, (tmp1 + tmp2))    # 만약 더해진 카드 묶음, 즉 tmp1 + tmp2가 더 이상 최소의 수가 아니라면 min_h에 들어갈 때 우선순위가 밀려난다.
        
    # min_h 안에 들어있는 원소 수가 1개 이하라면, 즉 마지막에 원소 1개가 남는다면 그 카드를 다른 카드와 묶을 필요가 없으므로 비교하는 의미가 사라진다.
    # 또한 애초에 1개 이하로 들어와있다면 비교할 대상이 없으므로 바로 break하고 res = 0을 그대로 남겨둔다.
    else:
        break
    
print(res)

# import sys, heapq
# sys.stdin = open('input.txt')
# input = sys.stdin.readline

# n = int(input())
# a = []
# for _ in range(n):
#     card = int(input())
#     heapq.heappush(a, card)

# res = 0
# while True:
#     if len(a) == 1:
#         break
#     tmp1 = heapq.heappop(a)
#     tmp2 = heapq.heappop(a)
#     tmp = tmp1 + tmp2
#     res += tmp
#     heapq.heappush(a, tmp)
    
# print(res)
    

