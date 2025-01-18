# 백준 10971. 외판원 순회 2
# https://www.acmicpc.net/problem/10971
import sys
from itertools import permutations
N = int(sys.stdin.readline().strip())
W = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

def sol(N, W):
    min_cost = 10 **7
    for perm in permutations(range(N)):
        cost = 0
        valid = True
        for i in range(N - 1):
            if W[perm[i]][perm[i + 1]] == 0:
                valid = False
                break
            cost += W[perm[i]][perm[i + 1]]
        
        if valid and W[perm[-1]][perm[0]] != 0:
            cost += W[perm[-1]][perm[0]]
            min_cost = min(min_cost, cost)
    return min_cost
print(sol(N=N, W=W))
            
    
    
    