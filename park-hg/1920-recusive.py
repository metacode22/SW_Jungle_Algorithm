import sys
sys.stdin = open('input.txt')

N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))
A.sort()
M = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split()))

def rec(left, right, num):
    if left < right:
        mid = (left + right) // 2
        if A[mid] < num:
            return rec(mid+1, right, num)
        elif A[mid] > num:
            return rec(left, mid, num)
        else:
            return 1
    return 0

for num in nums:
    print(rec(0, len(A), num))