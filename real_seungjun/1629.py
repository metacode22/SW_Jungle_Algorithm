import sys

A, B, C = map(int, sys.stdin.readline().split())

def rec(x, n):
    if n == 1:
        return x%C
    half = rec(x, n//2)
    if n%2 == 0:
        return (half*half)%C
    
    if n%2 == 1:
        return (half*half*x)%C

print(rec(A, B))
