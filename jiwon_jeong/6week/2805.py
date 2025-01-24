import sys
N, M = map(int, sys.stdin.readline().split())
heights = list(map(int, sys.stdin.readline().split()))

def sol(M, heights):
    low, high = 1, max(heights)
    result = 0
    while low <= high:
        mid = (low + high) // 2
        cnt = sum(max(0, height - mid) for height in heights)
        
        if cnt >= M:
            result = mid
            low = mid + 1
        else:
            high = mid - 1
    return result
print(sol(M=M, heights=heights))