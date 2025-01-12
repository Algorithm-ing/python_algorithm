# 일곱 난쟁이 - 완전 탐색
import sys
from itertools import combinations

height = [int(sys.stdin.readline()) for _ in range(9)]
combi = list(combinations(height, 7))  # 7명의 키 조합
for i in combi:
    if sum(i) == 100:  # 키의 합이 100이면
        for num in sorted(i):
            print(num)
        break
