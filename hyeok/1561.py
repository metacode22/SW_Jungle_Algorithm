import sys

sys.stdin = open("input_py.txt")

input = sys.stdin.readline

# N : people
N, M = map(int, input().split())

times = [int(x) for x in input().split()]


def binary():
    if N < M:
        print(N)
    else:
        left, right = 0, (10**10) * 6
        t = None
        while left <= right:
            mid = (left + right) // 2
            cnt = mid
            for time in times:
                cnt += mid//time
            if cnt >= N:
                t = mid
                right = mid - 1
            else:
                left = mid + 1

        # t-1에 탑승한 아이들의 숫자를 계산한다.
        cnt = M
        for time in times:
            cnt += (t-1) // time

        # t에 탑승한 아이를 계산한다.
        for i in range(M):
            if t % times[i] == 0:
                cnt += 1
            if cnt == N:
                print(i+1)
                break

    return


binary()

#  왜이렇게 짜는지도 왜 틀린지도 모르겠음
# 강해져서 돌아오겠음.
