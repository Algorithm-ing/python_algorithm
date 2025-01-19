import sys
from itertools import permutations

N = sys.stdin.readline()
N = int(N)

nums = list(map(int, sys.stdin.readline().rsplit()))

# 절댓값 합 수식을 구현한 함수
def equation(order):
    sumNum = 0
    for i in range(len(order)-1):
        sumNum += abs(order[i]-order[i+1])
    return sumNum

combo = permutations(nums, N)
maxNum = -1
for c in combo:
    answer = equation(c)
    if maxNum < answer:
        maxNum = answer

print(maxNum)
  