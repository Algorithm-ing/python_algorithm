# 백준 11279. 최대 힙
# https://www.acmicpc.net/problem/11279
import sys
from heapq import heappop, heappush
N = int(sys.stdin.readline().strip())
def sol(N):
    heap = []
    for _ in range(N):
        x = int(sys.stdin.readline().strip())
        
        
        if x > 0:
            heappush(heap, -x)
        else:
            if not heap:
                print(0)
            else:
                print(-heappop(heap))
sol(N=N)