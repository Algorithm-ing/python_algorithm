import sys
from collections import deque

input = sys.stdin.readline
N, M = map(int, input().split())
graph = [[0] * (N + 1) for _ in range(N + 1)]
for _ in range(M):
    A, B = map(int, input().split())
    graph[A][B] = 1
    graph[B][A] = 1

visited = [False for _ in range(N + 1)]
answer = 0
for root in range(1, N + 1):
    if visited[root]:
        continue
    answer += 1
    visited[root] = True
    nodes = deque([root])
    while nodes:
        root = nodes.popleft()
        for node in range(1, N + 1):
            if not visited[node] and graph[root][node] == 1:
                visited[node] = True
                nodes.append(node)

print(answer)