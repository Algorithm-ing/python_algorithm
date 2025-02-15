# 백준 2606. 바이러스
# https://www.acmicpc.net/problem/2606
###################### BFS ########################
from collections import deque, defaultdict
import sys
def main():
    n = int(sys.stdin.readline().strip())
    m = int(sys.stdin.readline().strip())
    graph = defaultdict(list)
    for _ in range(m):
        a, b = map(int, sys.stdin.readline().split())
        graph[a].append(b)
        graph[b].append(a)

    def sol(graph, start_v):
        visited = [start_v]
        q = deque()
        q.append(start_v)
        while q:
            cur_v = q.popleft()
            for next_v in graph[cur_v]:
                if next_v not in visited:
                    visited.append(next_v)
                    q.append(next_v)
        return len(visited) - 1
    print(sol(graph=graph, start_v=1))
main()
###################### BFS ########################

###################### DFS ########################
from collections import defaultdict
import sys
def main():
    n = int(sys.stdin.readline().strip())
    m = int(sys.stdin.readline().strip())
    graph = defaultdict(list)
    for _ in range(m):
        a, b = map(int, sys.stdin.readline().split())
        graph[a].append(b)
        graph[b].append(a)
    def sol(graph, start_v, visited):
        visited.append(start_v)
        for next_v in graph[start_v]:
            if next_v not in visited:
                sol(graph, next_v, visited)
        return visited
    print(len(sol(graph=graph, start_v=1, visited=[])) - 1)
main()
###################### DFS ########################