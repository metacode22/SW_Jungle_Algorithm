import sys

input = sys.stdin.readline

N, M = map(int, input().strip().split())

treeH = [int(x) for x in input().split()]

# treeH.sort()

# arr 나무들 높이 cut 자를 높이


def cutTree(arr, start, end):
    while start <= end:
        height = 0
        mid = (start+end) // 2
        for tree in treeH:
            if height > M:
                break
            if tree > mid:
                height += (tree-mid)
            else:
                continue
        if height >= M:
            start = mid + 1
        else:
            end = mid - 1
    return end
    # 크거나 같다 높이의 최댓값을 구해야해서 end를 구해야한다 ! ㅅㅃ

    # return cut


print(cutTree(treeH, 1, max(treeH)))
