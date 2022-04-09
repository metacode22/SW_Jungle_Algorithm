import sys

sys.stdin = open("./input_py.txt", "r")
input = sys.stdin.readline

M, N, L = map(int, input().split())

shooters = [int(x) for x in input().split()]
shooters.sort()

targets = [[int(x) for x in input().split()] for _ in range(N)]


count = 0


def shoot(arr, locations):
    # arr : targets, locations : shooters location,
    global count
    for x, y in targets:
        if y > L:
            continue
        elif y == L:
            if x in locations:
                count += 1
        else:
            distance = L - y
            if binarySearch(x, distance, locations, 0, M-1):
                count += 1
        # 가까운 애들을 찾자 ㄴ ㄴ 이진탐색 !!!!!!!!!
        # for location in locations:
        #     if x - distance <= location <= x + distance:
        #         count += 1
        #         break
    return


def binarySearch(x, dis, locations, start, end):
    while start <= end:
        mid = (start+end) // 2
        if x+dis < locations[mid]:
            end = mid-1
        elif x-dis > locations[mid]:
            start = mid + 1
        else:
            return True
    return False


shoot(targets, shooters)
print(count)
