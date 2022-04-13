import sys, heapq
sys.stdin = open('input.txt')
input = sys.stdin.readline

m, n, l = map(int, input().split())
mx = list(map(int, input().split()))
ani = []
check_list = [0] * n
for _ in range(n):
    x, y = map(int, input().split())
    if not y > l:
        ani.append([x, y])
        
for i in range(0, m):
    for j in range(0, len(ani)):
        leng = abs(mx[i] - ani[j][0]) + ani[j][1]
        
        if leng <= l:
            check_list[j] = 1

print(check_list.count(1))