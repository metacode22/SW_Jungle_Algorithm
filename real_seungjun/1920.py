import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
a.sort()

m = int(input())
b = list(map(int, input().split()))

def check(x):
    lt = 0
    rt = n - 1
    print(rt)

    while lt <= rt:
        mid = (lt + rt) // 2

        if a[mid] == x:
            return 1

        elif a[mid] > x:
            rt = mid - 1

        else:
            lt = mid + 1

    return 0

for i in b:
    print(check(i))