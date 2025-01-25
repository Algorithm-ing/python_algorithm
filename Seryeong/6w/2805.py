# 나무 자르기 - 이분탐색
import sys

N, M = map(int, sys.stdin.readline().split())
trees = list(map(int, sys.stdin.readline().split()))

end = max(trees)
start = 0

mid = end // 2

result = []

while start <= end:
    sum = 0
    mid = (start + end) // 2
    for tree in trees:
        if tree > mid:
            sum += tree - mid

    if sum >= M:
        result.append(mid)
        start = mid + 1
    else:
        end = mid - 1

print(max(result))
