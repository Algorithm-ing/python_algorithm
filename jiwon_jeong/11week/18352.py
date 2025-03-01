# 백준 18352. 특정 거리의 도시 찾기
# https://www.acmicpc.net/problem/18352
import sys
from collections import defaultdict, deque
def bfs(N, K, X, graph, visited):
    
    queue = deque([X])
    visited[X] = 0
    
    while queue:
        cur_x = queue.popleft()
        
        for next_x in graph[cur_x]:
            if visited[next_x] == -1:
                visited[next_x] = visited[cur_x] + 1
                queue.append(next_x)
    
    result = [i for i in range(1, N + 1) if visited[i] == K]
    
    if result:
        for city in sorted(result):
            print(city)
    else:
        print(-1)
            

def main():
    N, M, K, X = map(int, sys.stdin.readline().split())
    graph = defaultdict(list)
    for _ in range(M):
        a, b = map(int, sys.stdin.readline().split())
        graph[a].append(b)
    
    visited = [-1] * (N + 1)
    
    bfs(N=N, K=K, X=X, graph=graph, visited=visited)
main()    
    