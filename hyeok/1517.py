# 못품

import sys


def read(): return sys.stdin.readline().rstrip()


swap_count = 0


def merge_sort(start, end):
    global swap_count

    if start < end:
        mid = (start + end) // 2
        merge_sort(start, mid)
        merge_sort(mid + 1, end)

        a, b = start, mid + 1
        temp = []

        while a <= mid and b <= end:
            if A[a] <= A[b]:
                temp.append(A[a])
                a += 1
            else:
                temp.append(A[b])
                b += 1
                swap_count += (mid - a + 1)

        if a <= mid:
            temp = temp + A[a:mid + 1]
        if b <= end:
            temp = temp + A[b:end + 1]

        for i in range(len(temp)):
            A[start + i] = temp[i]


N = int(read())
A = list(map(int, read().split()))
merge_sort(0, N - 1)
print(swap_count)

# ~~~ 사랑시 ~ 고백구 ~행볶똥~~
# tmp = 0
# sum = 0
# for i in range(lenA-1):
#     if A[i] > A[i+1]:
#         tmp += 1
#         sum += tmp
#     else:
#         tmp = 0

# print(sum)
