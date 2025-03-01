# 백준 1916. 최소비용 구하기
# https://www.acmicpc.net/problem/1916
import sys
from collections import defaultdict
from heapq import *

def dijkstra(graph, start, end):
    costs = {}
    pq = []
    heappush(pq, (0, start))
    
    while pq:
        cur_cost, cur_v = heappop(pq)
        
        if cur_v not in costs:
            costs[cur_v] = cur_cost
            for cost, next_v in graph[cur_v]:
                next_cost = cur_cost + cost
                heappush(pq, (next_cost, next_v))
    return costs[end]

def main():
    N = int(sys.stdin.readline().strip())
    M = int(sys.stdin.readline().strip())
    graph = defaultdict(list)
    
    for _ in range(M):
        a, b, c = map(int, sys.stdin.readline().split())
        graph[a].append((c, b))
    
    start, end = map(int, sys.stdin.readline().split())
    
    print(dijkstra(graph, start, end))
main()

    