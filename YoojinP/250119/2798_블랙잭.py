import sys
from itertools import combinations, permutations 

N, M =sys.stdin.readline().rsplit()
N, M = int(N), int(M)

nums = list(map(int, sys.stdin.readline().rsplit()))
combo = combinations(nums,3)

maxNum = -1
answer = []
for c in combo:
    if sum(c)<= M and maxNum < sum(c):
        answer = c
        maxNum = sum(c)
print(sum(answer))

