# 블랙잭 - 완전탐색

import sys
import itertools

N, M = map(int, sys.stdin.readline().split())
cards = list(itertools.combinations(
    list(map(int, sys.stdin.readline().split())), 3))

answer = []  # M에 가장 가까운 카드
diff = 1000000  # M과의 차
for combi in cards:
    if sum(combi) <= M and abs(sum(combi) - M) < diff:
        diff = abs(M - sum(combi))
        answer = combi

print(sum(answer))
