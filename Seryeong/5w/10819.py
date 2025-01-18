# 차이를 최대로 - 완전 탐색
import sys
import itertools

N = int(sys.stdin.readline())
nums = list(itertools.permutations(
    (list(map(int, sys.stdin.readline().split())))))

max = 0
for per in nums:
    sum = 0
    for i in range(0, len(per)-1):
        sum += abs(per[i] - per[i+1])

    if sum > max:
        max = sum

print(max)
