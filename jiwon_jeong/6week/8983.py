# 백준 8983. 사냥꾼
# https://www.acmicpc.net/problem/8983
import sys
from bisect import bisect_left
# M: 사대의 수, N: 동물의 수, L: 사정거리
M, N, L = map(int, sys.stdin.readline().split())
shootings = list(map(int, sys.stdin.readline().split()))
animals = [tuple(map(int, sys.stdin.readline().split())) for _ in range(N)]

def sol(M, L, shootings, animals): # O(MlogM + NlogM)
    
    shootings.sort() # O(MlogM)
    cnt = 0
    
    for x, y in animals: # O(N)
        
        idx = bisect_left(shootings, x) # O(logM)
        
        if 0 <= idx < M:
            if abs(shootings[idx] - x) + y <= L:
                cnt += 1
                continue
        
        for i in [idx - 1, idx]:
            if 0 <= i < M:
                distance = abs(shootings[i] - x) + y
                
                if distance <= L:
                    cnt += 1
                    break
    return cnt

print(sol(M=M, L=L, shootings=shootings, animals=animals))