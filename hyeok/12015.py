import sys

sys.stdin = open("input_py.txt")

input = sys.stdin.readline

A = int(input())

arr = [int(x) for x in input().split()]

# print(arr)
stack = [0]


def find(target):
    left = 0
    right = len(stack) - 1
    while left <= right:
        mid = (left + right) // 2
        if stack[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return left


for a in arr:
    if stack[-1] < a:
        stack.append(a)
    else:
        stack[find(a)] = a

print(len(stack)-1)

print(f"stack : {stack}")
