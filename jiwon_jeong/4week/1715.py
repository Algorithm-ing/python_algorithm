# 백준 1715. 카드 정렬하기
# https://www.acmicpc.net/problem/1715
import sys
from heapq import heappop, heappush
N = int(sys.stdin.readline().strip())
def sol(N):
    heap = []
    for _ in range(N):
        heappush(heap, int(sys.stdin.readline().strip()))
    total_sum = 0
    while len(heap) > 1:
        first = heappop(heap)
        second = heappop(heap)
        
        mid_sum = first + second
        total_sum += mid_sum
        heappush(heap, mid_sum)
    print(total_sum)
sol(N=N)
    