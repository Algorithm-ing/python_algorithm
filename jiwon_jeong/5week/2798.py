# 백준 2798. 블랙잭
# https://www.acmicpc.net/problem/2798
import sys
from itertools import combinations
N, M = map(int, sys.stdin.readline().split())
cards = list(map(int, sys.stdin.readline().split()))
def sol(M, cards):
    max_sum = -1
    for card in combinations(cards, 3):
        if sum(card) <= M:
            max_sum = max(max_sum, sum(card))
    print(max_sum)
sol(M=M, cards=cards)
    