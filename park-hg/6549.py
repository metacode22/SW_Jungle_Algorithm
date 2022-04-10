import sys
sys.setrecursionlimit(10**6)
sys.stdin = open('input.txt')

def find_maxrec(start, mid, end):
    left = right = mid
    s_total = cur_h = hist[mid]

    while start < left or right < end:
        if left == start:
            while right < end:
                right += 1
                cur_h = min(cur_h, hist[right])
                s_total = max(s_total, cur_h*(right-left+1))
        elif right == end:
            while left > start:
                left -= 1
                cur_h = min(cur_h, hist[left])
                s_total = max(s_total, cur_h*(right-left+1))
        else:
            if hist[left-1] > hist[right+1]:
                left -= 1
                cur_h = min(cur_h, hist[left])
            elif hist[left-1] < hist[right+1]:
                right += 1
                cur_h = min(cur_h, hist[right])
            else:
                left -= 1
                right += 1
                cur_h = min(cur_h, hist[left])

        s_total = max(s_total, cur_h*(right-left+1))

    return s_total


def rec(start, end):
    if start == end:
        return hist[start]
    
    mid = (start+end) // 2
    
    s_left = rec(start, mid)
    s_right = rec(mid+1, end)
    s_total = find_maxrec(start, mid, end)
    
    return max(s_left, s_right, s_total)


while True:
    l = list(map(int, sys.stdin.readline().split()))
    if l[0] == 0:
        break
    hist = l[1:]
    print(rec(0, len(hist)-1))
