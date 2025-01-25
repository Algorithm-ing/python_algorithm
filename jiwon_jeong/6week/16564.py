# 백준 16564. 히오스 프로게이머
# https://www.acmicpc.net/problem/16564
import sys
N, K = map(int, sys.stdin.readline().split())
levels = [int(sys.stdin.readline().strip()) for _ in range(N)]

def sol(K, levels): # O(NlogN + NlogK)
    levels.sort() # O(NlogN)
    
    low, high = min(levels), min(levels) + K
    result = 0
    
    while low <= high: # O(NlogK)
        mid = (low + high) // 2 # 목표 레벨
        
        cost = 0
        for level in levels:
            if level < mid:
                cost += mid - level
            if cost > K:
                break
            
        if cost <= K:
            result = mid
            low = mid + 1
        else:
            high = mid - 1
    return result

print(sol(K=K, levels=levels))
                