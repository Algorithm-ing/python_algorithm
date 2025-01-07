# 백준 2309. 일곱 난쟁이
# https://www.acmicpc.net/problem/2309

####################### 조합 풀이 #######################
import sys
from itertools import combinations
heights = [int(sys.stdin.readline().strip()) for _ in range(9)]
def sol(heights):
    total = sum(heights)
    for comb in combinations(heights, 2):
        if sum(comb) == total - 100:
            result = [height for height in heights if height not in comb]
            break
    return '\n'.join(map(str, sorted(result)))
print(sol(heights=heights))
####################### 조합 풀이 #######################

####################### 반복문 풀이 #######################
import sys
heights = [int(sys.stdin.readline().strip()) for _ in range(9)]
def sol(heights):
    total = sum(heights)
    for i in range(9):
        for j in range(i + 1, 9):
            if heights[i] + heights[j] == total - 100:
                result = [heights[k] for k in range(9) if k  != i and k != j]
                result.sort()
                return '\n'.join(map(str, result))
print(sol(heights=heights))
####################### 반복문 풀이 #######################