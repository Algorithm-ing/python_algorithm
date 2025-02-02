import sys
from collections import deque
input = sys.stdin.readline
N, M, V = map(int, input().split())
graph = [[0] * (N + 1) for i in range(N + 1)]
for _ in range(M):
    A, B = map(int, input().split())
    graph[A][B] = 1
    graph[B][A] = 1

visited = [False for _ in range(N + 1)]
def dfs(root):
    visited[root] = True
    print(root, end=" ")
    for node in range(1, N + 1):
        if not visited[node] and graph[root][node] == 1:
            dfs(node)

def bfs(root):
    visited[root] = False
    nodes = deque([root])
    while nodes:
        root = nodes.popleft()
        print(root, end=" ")
        for node in range(1, N + 1):
            if visited[node] and graph[root][node] == 1:
                visited[node] = False
                nodes.append(node)

dfs(V)
print()
bfs(V)