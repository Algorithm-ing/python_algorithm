# 백준 11866. 요푸 문제 O
# https://www.acmicpc.net/problem/11866

################## rotate 풀이: O(N * K)######################
import sys
from collections import deque
N, K = map(int, sys.stdin.readline().split())
def sol(N, K):
    q = deque(range(1, N + 1))
    result = []
    
    while q:
        q.rotate(-(K - 1))
        result.append(q.popleft())
    return "<" + ", ".join(map(str, result)) + ">"
print(sol(N=N, K=K))
################## rotate 풀이 ######################

################## list 풀이: O(N^2)######################
import sys
N, K = map(int, sys.stdin.readline().split())
def sol(N, K):
    q = list(range(1, N + 1))
    result = []
    index = 0
    while q:
        index = (index + (K - 1)) % len(q)
        result.append(q.pop(index))
    return "<" + ", ".join(map(str, result)) + ">"
print(sol(N=N, K=K))
################## list 풀이 #######################