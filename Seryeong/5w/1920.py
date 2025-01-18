# 수 찾기 - 이분탐색

import sys

N = int(sys.stdin.readline())
A = sorted(list(map(int, sys.stdin.readline().split())))
M = int(sys.stdin.readline())
B = list(map(int, sys.stdin.readline().split()))

# 이분탐색


def binarySearch(arr, start, end, target):
    mid = start + ((end - start) // 2)
    if start > end:  # 탈출조건: 시작과 끝이 역전되었을 때
        return 0

    if arr[mid] == target:
        return 1
    elif arr[mid] < target:  # mid 기준으로 오른쪽 탐색
        return binarySearch(arr, mid + 1, end, target)
    else:  # mid 기준으로 왼쪽 탐색
        return binarySearch(arr, start, mid - 1, target)


for num in B:
    print(binarySearch(A, 0, N - 1, num))
