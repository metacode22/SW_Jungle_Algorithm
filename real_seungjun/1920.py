import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
a.sort()    # 이분 탐색 문제는 우리가 찾으려는 값이 포함된 자료가 정렬되어 있어야 한다는 것이 전제 조건이다.

m = int(input())
b = list(map(int, input().split()))

# 리스트 a의 원소들이 규칙 있게 되어있는지 우린 알 수 없다.
# 따라서 절대적인 범위를 정할 수 없기 때문에 index를 범위로 잡는다.
# lt와 rt는 즉 index를 범위로 할 것이다.
for i in b:
    lt = 0
    rt = n - 1
    while lt <= rt:
        mid = (lt + rt)//2
        if a[mid] == i:
            print(1)
            break
        elif a[mid] < i:    # 찾아야 하는 것이 a[mid]보다 오른쪽에 있을 것으로 추정
            lt = mid + 1
        else:               # 찾아야 하는 것이 a[mid]보다 왼쪽에 있을 것으로 추정
            rt = mid - 1
    else:
        print(0)