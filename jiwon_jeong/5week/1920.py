# 백준 1920. 수 찾기
# https://www.acmicpc.net/problem/1920
import sys
from bisect import *
N = int(sys.stdin.readline().strip())
A = list(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline().strip())
nums = list(map(int, sys.stdin.readline().split()))
def index(arr, target):
    idx = bisect_left(arr, target)
    if idx != len(arr) and arr[idx] == target:
        return idx
    else:
        return -1

result = []
A.sort()
for num in nums:
    if index(A, num) != -1:
        result.append(1)
    else:
        result.append(0)
print(*result, sep='\n')