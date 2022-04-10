import sys
sys.stdin = open('input.txt')

N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))
A.sort()
M = int(sys.stdin.readline())
queries = list(map(int, sys.stdin.readline().split()))

def check(num):
    left, right = 0, len(A)
    while left < right:
        mid = (left + right) // 2
        if A[mid] < num:
            left = mid + 1
        elif A[mid] > num:
            right = mid
        else:
            return 1
    return 0

for q in queries:
    print(check(q))